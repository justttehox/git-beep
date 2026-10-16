# git-beep


A tiny Git hook that plays a custom sound every time you run `git push`.

It installs a `pre-push` hook — the only hook Git actually invokes for a
push — so the sound plays automatically from then on, with no extra steps.

## Features

- Works with Git repositories
- Supports Windows
- Supports macOS
- Supports Linux
- Uses a custom MP3 sound
- No external Python packages required
- Automatically backs up an existing `pre-push` hook

## Project Structure

```text
git-beep/
├── sounds/
│   └── push.mp3
├── install.py
├── play_sound.py
├── uninstall.py
└── README.md
```

## Usage

```text
python install.py      # installs the pre-push hook in the current repo
python uninstall.py     # removes it and restores any backed-up hook
```