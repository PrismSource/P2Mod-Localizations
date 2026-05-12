# Remove lines with "[english]" in them, as Portal 2 translations have them, and deleting them by hand can be annoying
# Usage: python remove_eng.py [path to the txt file] , Or just drag it onto the script

import sys
import os

def read_file_auto_encoding(path):
    for enc in ["utf-8", "utf-16", "utf-16-le", "latin-1"]:
        try:
            with open(path, "r", encoding=enc) as f:
                return f.readlines(), enc
        except UnicodeDecodeError:
            continue

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.readlines(), "utf-8"


def clean_file(path):
    lines, enc = read_file_auto_encoding(path)

    cleaned = [line for line in lines if "[english]" not in line]

    with open(path, "w", encoding=enc, errors="ignore") as f:
        f.writelines(cleaned)
    print(f"Removed {len(lines) - len(cleaned)} lines")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()
        print("")

    for file_path in sys.argv[1:]:
        if os.path.isfile(file_path):
            clean_file(file_path)
        else:
            print(f"Skipping: {file_path}")