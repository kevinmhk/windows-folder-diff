import os
import configparser
from pathlib import Path


def get_all_files(folder_path):
    files = {}
    folder = Path(folder_path)
    if not folder.exists():
        return files
    for root, _, filenames in os.walk(folder):
        for filename in filenames:
            files[filename.lower()] = Path(root) / filename
    return files


def main():
    script_dir = Path(__file__).parent
    config_path = script_dir / "config.ini"

    if not config_path.exists():
        print(f"Config file not found: {config_path}")
        return

    config = configparser.ConfigParser()
    config.read(config_path)

    try:
        folder1 = config.get("folders", "folder1")
        folder2 = config.get("folders", "folder2")
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        print(f"Config error: {e}")
        return

    if not folder1 or not folder2:
        print("Please configure both folder paths in config.ini")
        return

    files1 = get_all_files(folder1)
    files2 = get_all_files(folder2)

    filenames1 = set(files1.keys())
    filenames2 = set(files2.keys())

    only_in_1 = filenames1 - filenames2
    only_in_2 = filenames2 - filenames1
    common = filenames1 & filenames2

    output_path = script_dir / "diff_result.md"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Folder Diff Result\n\n")
        f.write(f"- **Folder 1**: {folder1}\n")
        f.write(f"- **Folder 2**: {folder2}\n\n")
        f.write(f"## Summary\n\n")
        f.write(f"- Total unique files in Folder 1: {len(files1)}\n")
        f.write(f"- Total unique files in Folder 2: {len(files2)}\n")
        f.write(f"- Common files: {len(common)}\n")
        f.write(f"- Files only in Folder 1: {len(only_in_1)}\n")
        f.write(f"- Files only in Folder 2: {len(only_in_2)}\n\n")

        if only_in_1:
            f.write(f"## Files Only in Folder 1\n\n")
            for filename in sorted(only_in_1):
                f.write(f"- {files1[filename].resolve()}\n")
            f.write("\n")

        if only_in_2:
            f.write(f"## Files Only in Folder 2\n\n")
            for filename in sorted(only_in_2):
                f.write(f"- {files2[filename].resolve()}\n")
            f.write("\n")

        # if common:
        #     f.write(f"## Common Files\n\n")
        #     for filename in sorted(common):
        #         f.write(f"- {filename}\n")
        #     f.write("\n")

    print(f"Diff result written to: {output_path}")


if __name__ == "__main__":
    main()
