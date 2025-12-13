import os

CONTENT_DIR = "content"

HEADER = """---
tags: [public]
---

# {title}

## 📂 Subfolders
"""

NOTES_HEADER = """

## 📄 Notes
"""

def title_from_path(path):
    name = os.path.basename(path)
    name = name.replace("-", " ")
    name = name.replace("_", " ")
    return name.title()

def is_md_file(filename):
    return filename.endswith(".md") and filename != "index.md"

def md_name(filename):
    return filename[:-3]  # strip .md

def write_index(path, folders, files):
    index_path = os.path.join(path, "index.md")

    if os.path.exists(index_path):
        return  # do not overwrite

    f = open(index_path, "w", encoding="utf-8")

    f.write(HEADER.format(title=title_from_path(path)))

    if folders:
        for d in folders:
            f.write(f"- [[{d}]]\n")
    else:
        f.write("_None_\n")

    f.write(NOTES_HEADER)

    if files:
        for f_md in files:
            f.write(f"- [[{md_name(f_md)}]]\n")
    else:
        f.write("_None_\n")

    f.close()
    print("Created", index_path)

# ===== main =====
for root, dirs, files in os.walk(CONTENT_DIR):
    if root == CONTENT_DIR:
        continue

    folders = []
    md_files = []

    for d in dirs:
        folders.append(d)

    for f in files:
        if is_md_file(f):
            md_files.append(f)

    if not folders and not md_files:
        continue

    write_index(root, folders, md_files)
