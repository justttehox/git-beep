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

    hooks_dir = git_root / ".git" / "hooks"
    hook_file = hooks_dir / "pre-push"
    backup_file = hooks_dir / "pre-push.backup"

    if hook_file.exists():
        hook_file.unlink()
        print("Git push sound hook removed.")
    else:
        print("Git push sound hook is not installed.")

    if backup_file.exists():
        shutil.copy2(backup_file, hook_file)
        backup_file.unlink()
        print("Original Git hook restored.")

    # Clean up the leftover hook from older, broken installs that used the
    # (non-existent) "post-push" hook name.
    stale_file = hooks_dir / "post-push"
    if stale_file.exists() and "play_sound.py" in stale_file.read_text(encoding="utf-8", errors="ignore"):
        stale_file.unlink()
        print("Removed stale (non-functional) post-push hook.")


if __name__ == "__main__":
    main()