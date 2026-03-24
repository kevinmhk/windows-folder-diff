# Windows Folder Diff

Compare files between two Windows folder trees using filename as the only comparison criteria.

## Overview

This script recursively scans two folders and their subfolders, then generates a markdown report showing the differences based solely on filenames.

## Requirements

- Python 3.7+

## Installation

No external dependencies required. Uses only Python standard library.

## Configuration

Edit `config.ini` and set the two folder paths:

```ini
[folders]
folder1 = C:\Path\To\Folder1
folder2 = C:\Path\To\Folder2
```

## Usage

```bash
python windows-folder-diff.py
```

## Output

The script generates `diff_result.md` with:

- Summary statistics
- Files only in Folder 1
- Files only in Folder 2
- Common files

All filename comparisons are case-insensitive.
