# scripts/check_versions.py
# Implement a repository version consistency checker.
# Usage: python scripts/check_versions.py

def contains_version(filepath, search_string):
    """
    Checks if a text file contains a specific string by reading it line by line.
    More memory-efficient for large files.

    Args:
        filepath (str): The path to the text file.
        search_string (str): The string to search for.

    Returns:
        bool: True if the string is found, False otherwise.
    """
    msg = f"File: {filepath}\nTarget version: {search_string}\n"
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                if search_string in line:
                    return f"{msg}MATCH: {line}"

            return f"{msg}ERROR: Target version not found."

    except FileNotFoundError:
        return f"{msg}ERROR: File not found"
    except Exception as e:
        return f"{msg}ERROR: {e}"


def main():
    print("Version Consistency Checker\n")
    user_input = input("Target package version (e.g. 1.2.3)? ")

    if user_input:
        print('Checking for version consistency...\n')
        file_version_map = {
            '../pyproject.toml': f'version = "v{user_input}"',
            '../docs/source/index.rst': f'**Version**: v{user_input}',
            '../docs/source/conf.py': f"release = f'v{user_input}'",
            '../src/template_library/__init__.py': f'__version__ = "{user_input}"',
        }
        for file_path, version_line in file_version_map.items():
            print(contains_version(file_path, version_line))
    else:
        print("\nNote: You did not enter anything.")


if __name__ == "__main__":
    main()
