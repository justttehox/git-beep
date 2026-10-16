import shutil
from pathlib import Path


def find_git_root():
    current = Path.cwd()

    while current != current.parent:
        if (current / ".git").exists():
            return current

        current = current.parent

    return None


def main():
    git_root = find_git_root()

    if git_root is None:
        print("Error: This script must be run inside a Git repository.")
        return

    hook_file = git_root / ".git" / "hooks" / "post-push"
    backup_file = git_root / ".git" / "hooks" / "post-push.backup"

    if hook_file.exists():
        hook_file.unlink()
        print("Git push sound hook removed.")
    else:
        print("Git push sound hook is not installed.")

    if backup_file.exists():
        shutil.copy2(backup_file, hook_file)
        backup_file.unlink()
        print("Original Git hook restored.")


if __name__ == "__main__":
    main()