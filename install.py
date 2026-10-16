import os
import shutil
import stat
import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
HOOK_NAME = "post-push"


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
        sys.exit(1)

    git_dir = git_root / ".git"

    if not git_dir.is_dir():
        print("Error: .git is not a directory.")
        sys.exit(1)

    hooks_dir = git_dir / "hooks"
    hooks_dir.mkdir(exist_ok=True)

    hook_file = hooks_dir / HOOK_NAME

    python_executable = sys.executable
    play_sound_script = PROJECT_DIR / "play_sound.py"

    if not play_sound_script.exists():
        print(f"Error: {play_sound_script} does not exist.")
        sys.exit(1)



    if os.name == "nt":
        hook_content = f"""#!/bin/sh
"{python_executable}" "{play_sound_script}" &
"""
    else:
        hook_content = f"""#!/bin/sh
"{python_executable}" "{play_sound_script}" &
"""

    if hook_file.exists():
        backup_file = hooks_dir / f"{HOOK_NAME}.backup"

        if not backup_file.exists():
            shutil.copy2(hook_file, backup_file)
            print(f"Existing hook backed up to: {backup_file}")

    hook_file.write_text(hook_content, encoding="utf-8")

    if os.name != "nt":
        current_permissions = hook_file.stat().st_mode
        hook_file.chmod(
            current_permissions
            | stat.S_IXUSR
            | stat.S_IXGRP
            | stat.S_IXOTH
        )

    print()
    print("Git push sound installed successfully!")
    print()
    print(f"Repository: {git_root}")
    print(f"Hook:       {hook_file}")
    print(f"Sound:      {PROJECT_DIR / 'sounds' / 'push.mp3'}")
    print()
    print("Now run:")
    print()
    print("    git push")
    print()
    print("and the sound will play after the push completes.")


if __name__ == "__main__":
    main()