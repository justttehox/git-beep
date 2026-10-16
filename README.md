# git-beep


A tiny Git hook that plays a custom sound every time `git push` completes.

## Features

- Works with Git repositories
- Supports Windows
- Supports macOS
- Supports Linux
- Uses a custom MP3 sound
- No external Python packages required
- Automatically backs up an existing `post-push` hook

## Project Structure

```text
git-push-sound/
├── sounds/
│   └── push.mp3
├── install.py
├── play_sound.py
├── uninstall.py
└── README.md