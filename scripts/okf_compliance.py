import os
import re
from pathlib import Path
from datetime import datetime, timezone

# OKF Strict Valid Types
VALID_TYPES = [
    "Assembly Module", 
    "Game Asset", 
    "Game Mechanic", 
    "Memory Map", 
    "Build System", 
    "Reference"
]
RESOURCE_REQUIRED_TYPES = ["Assembly Module", "Game Asset", "Build System"]

def parse_frontmatter(content):
    """Extracts frontmatter and body from markdown content."""
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    
    frontmatter_str = parts[1]
    body = parts[2]
    
    metadata = {}
    for line in frontmatter_str.strip().split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            metadata[key.strip()] = val.strip().strip('"').strip("'")
            
    return metadata, body

def build_frontmatter_string(metadata):
    """Reconstructs YAML frontmatter enforcing OKF field order."""
    lines = ["---"]
    # Enforce order: type, title, description, resource, tags, timestamp
    ordered_keys = ["type", "title", "description", "resource", "tags", "timestamp"]
    
    for key in ordered_keys:
        if key in metadata:
            val = metadata[key]
            # Quote titles if they have special characters
            if key == "title" and any(c in ":{}[]&*#?|<>=!%@`" for c in val):
                lines.append(f'{key}: "{val}"')
            else:
                lines.append(f"{key}: {val}")
                
    # Add any leftover keys that aren't in the standard OKF order
    for key, val in metadata.items():
        if key not in ordered_keys:
            lines.append(f"{key}: {val}")
            
    lines.append("---")
    return "\n".join(lines) + "\n"

def enforce_okf_standards(kb_root):
    """Enforces OKF frontmatter and body conventions on all concepts."""
    print("Enforcing OKF specification standards...")
    project_root = Path.cwd()
    abs_kb_root = (project_root / kb_root).resolve()

    for root, dirs, files in os.walk(abs_kb_root):
        for file in files:
            # Skip indexes and logs
            if not file.endswith(".md") or file in ["index.md", "log.md"]:
                continue

            path = Path(root) / file
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            metadata, body = parse_frontmatter(content)
            modified = False

            # --- 1. Enforce Frontmatter Fields ---
            if "type" not in metadata or metadata["type"] not in VALID_TYPES:
                metadata["type"] = "Game Mechanic" # Default fallback
                modified = True
                
            if "title" not in metadata:
                metadata["title"] = path.stem.replace('_', ' ').title()
                modified = True
                
            if "description" not in metadata:
                metadata["description"] = "TODO: Add one-sentence summary per OKF spec."
                modified = True
                
            if metadata["type"] in RESOURCE_REQUIRED_TYPES and "resource" not in metadata:
                metadata["resource"] = "TODO: sources/path/to/file"
                modified = True
                
            if "timestamp" not in metadata:
                metadata["timestamp"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                modified = True

            # --- 2. Enforce Body Conventions ---
            original_body = body
            
            if metadata["type"] == "Assembly Module" and "# Implementation" not in body:
                body = "\n# Implementation\n" + body.lstrip()
                
            if metadata["type"] == "Game Asset" and "# Asset Details" not in body:
                body = "\n# Asset Details\n" + body.lstrip()
                
            if body != original_body:
                modified = True

            if modified:
                print(f"Applied OKF standards to: {path}")
                new_content = build_frontmatter_string(metadata) + body
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)

def get_concept_map(kb_root):
    """Builds a map of Concept Title -> OKF Absolute Path (/folder/file.md)."""
    concept_map = {}
    project_root = Path.cwd()
    abs_kb_root = (project_root / kb_root).resolve()

    for root, dirs, files in os.walk(abs_kb_root):
        for file in files:
            if file.endswith(".md") and file not in ["index.md", "log.md"]:
                path = Path(root) / file
                with open(path, "r", encoding="utf-8") as f:
                    metadata, _ = parse_frontmatter(f.read())
                    if "title" in metadata:
                        # Create OKF absolute path relative to KB root (e.g., /logic/game.md)
                        rel_path = path.relative_to(abs_kb_root).as_posix()
                        concept_map[metadata["title"]] = f"/{rel_path}"
    return concept_map

def apply_okf_cross_links(kb_root, concept_map):
    """Applies mandatory cross-linking using absolute OKF paths."""
    print("Applying OKF absolute cross-links to document bodies...")
    project_root = Path.cwd()
    abs_kb_root = (project_root / kb_root).resolve()

    for root, dirs, files in os.walk(abs_kb_root):
        for file in files:
            if not file.endswith(".md"):
                continue

            path = Path(root) / file
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            metadata, body = parse_frontmatter(content)
            original_body = body

            # Sort by length descending to prevent partial word matches
            sorted_titles = sorted(concept_map.keys(), key=len, reverse=True)
            
            for title in sorted_titles:
                # Prevent a document from linking to itself
                if metadata.get("title") == title:
                    continue
                    
                target_abs_path = concept_map[title]
                # Regex: Find title not already wrapped in brackets
                pattern = re.compile(rf'(?<!\[)({re.escape(title)})(?!\])')
                body = pattern.sub(rf'[\1]({target_abs_path})', body)

            if body != original_body:
                print(f"Updated cross-links in: {path}")
                new_content = build_frontmatter_string(metadata) + body
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)

def generate_okf_indexes(kb_root):
    """Generates frontmatter-less index.md files, grouping concepts by type and listing subdirectories."""
    print("Generating OKF compliant index.md files...")
    project_root = Path.cwd()
    abs_kb_root = (project_root / kb_root).resolve()
    
    for root, dirs, files in os.walk(abs_kb_root):
        index_path = Path(root) / "index.md"
        
        md_files = [f for f in files if f.endswith(".md") and f not in ["index.md", "log.md"]]
        valid_dirs = [d for d in dirs if not d.startswith(".")] # Skip hidden folders
        
        # Group concepts by OKF Type
        grouped_concepts = {}
        for mf in sorted(md_files):
            file_path = Path(root) / mf
            with open(file_path, "r", encoding="utf-8") as f:
                metadata, _ = parse_frontmatter(f.read())
                
                c_type = metadata.get("type", "Uncategorized Concepts")
                title = metadata.get("title", mf.replace(".md", "").title())
                desc = metadata.get("description", "No description provided.")
                
                if c_type not in grouped_concepts:
                    grouped_concepts[c_type] = []
                    
                # Format: * [Title 1](relative-url-1) - short description
                grouped_concepts[c_type].append(f"* [{title}]({mf}) - {desc}")
        
        content = ""
        
        # 1. Write Concepts Grouped by Heading
        for c_type in sorted(grouped_concepts.keys()):
            # Pluralize the heading (e.g., "Assembly Modules")
            heading = f"{c_type}s" if not c_type.endswith('s') else c_type
            content += f"# {heading}\n"
            for item in grouped_concepts[c_type]:
                content += f"{item}\n"
            content += "\n"
            
        # 2. Write Subdirectories Section
        if valid_dirs:
            content += "# Subdirectories\n"
            for d in sorted(valid_dirs):
                dir_title = d.replace('_', ' ').title()
                content += f"* [{dir_title}]({d}/) - Browse {dir_title} contents\n"
            content += "\n"
            
        # 3. Write to file (No frontmatter, just the body)
        if content.strip():
            with open(index_path, "w", encoding="utf-8") as f:
                f.write(content.strip() + "\n")
        else:
            # Fallback for completely empty directories
            with open(index_path, "w", encoding="utf-8") as f:
                f.write("# Empty Directory\n* No OKF concepts found here yet.\n")
                
def auto_generate_project_log(kb_root):
    """Auto-generates a global log.md by extracting OKF timestamps from all concepts."""
    print("Auto-generating project log from timestamps...")
    project_root = Path.cwd()
    abs_kb_root = (project_root / kb_root).resolve()
    
    logs_by_date = {}

    # 1. Sweep the KB for all valid concepts and extract their timestamps
    for root, dirs, files in os.walk(abs_kb_root):
        for file in files:
            if file.endswith(".md") and file not in ["index.md", "log.md"]:
                path = Path(root) / file
                with open(path, "r", encoding="utf-8") as f:
                    metadata, _ = parse_frontmatter(f.read())
                
                # Ensure the file has OKF compliant data
                if "timestamp" in metadata and "title" in metadata:
                    raw_time = metadata["timestamp"]
                    try:
                        # Extract strict YYYY-MM-DD from ISO 8601 (e.g. 2026-07-08T17:51:30Z)
                        date_str = raw_time.split("T")[0]
                        
                        # Validate it matches OKF date format
                        if re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
                            if date_str not in logs_by_date:
                                logs_by_date[date_str] = []
                            
                            # Generate absolute OKF link
                            rel_path = "/" + path.relative_to(abs_kb_root).as_posix()
                            title = metadata["title"]
                            c_type = metadata.get("type", "Concept")
                            
                            logs_by_date[date_str].append({
                                "title": title,
                                "path": rel_path,
                                "type": c_type
                            })
                    except Exception as e:
                        print(f"Warning: Could not parse timestamp '{raw_time}' in {file}")

    if not logs_by_date:
        print("No valid timestamps found to generate logs.")
        return

    # 2. Reconstruct the OKF compliant log.md (No frontmatter, newest first)
    content = "# Project Update Log\n\n"
    content += "This log is auto-generated from concept frontmatter timestamps.\n\n"
    
    # Sort dates descending (Newest first)
    for date_key in sorted(logs_by_date.keys(), reverse=True):
        content += f"## {date_key}\n"
        
        # Sort entries within a date alphabetically by title
        entries = sorted(logs_by_date[date_key], key=lambda x: x["title"])
        
        for entry in entries:
            content += f"* **Update**: Processed {entry['type']} - [{entry['title']}]({entry['path']})\n"
        
        content += "\n"

    # 3. Write to the root knowledge base directory
    log_path = abs_kb_root / "log.md"
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"✅ Generated global OKF log at: {log_path.relative_to(project_root)}")

    # 4. Cleanup: Remove the old manual logs folder if it exists
    old_logs_dir = abs_kb_root / "logs"
    if old_logs_dir.exists() and old_logs_dir.is_dir():
        import shutil
        shutil.rmtree(old_logs_dir)
        print("Removed deprecated manual 'logs' directory.")

def main():
    kb_root = "knowledge_base"
    if not os.path.exists(kb_root):
        print(f"Directory '{kb_root}' not found. Please run this script from the repository root.")
        return

    # 1. Enforce OKF fields (including injecting missing timestamps)
    enforce_okf_standards(kb_root)

    # 2. Build map of all valid concepts to their absolute paths
    concept_map = get_concept_map(kb_root)

    # 3. Apply absolute cross-links universally
    apply_okf_cross_links(kb_root, concept_map)

    # 4. Generate Indexes using semantic groupings and no frontmatter
    generate_okf_indexes(kb_root)
    
    # 5. Auto-generate the global log based on updated timestamps
    auto_generate_project_log(kb_root)
    
    print("\n✅ Knowledge Base is now fully OKF v0.1 compliant and synced.")

if __name__ == "__main__":
    main()
