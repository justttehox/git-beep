import platform
import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SOUND_FILE = BASE_DIR / "sounds" / "push.mp3"


def play_sound():
    if not SOUND_FILE.exists():
        print(f"Sound file not found: {SOUND_FILE}")
        return

    system = platform.system()

    try:
        if system == "Windows":
            import winsound

            winsound.PlaySound(
                str(SOUND_FILE),
                winsound.SND_FILENAME | winsound.SND_ASYNC,
            )

        elif system == "Darwin":
            subprocess.Popen(
                ["afplay", str(SOUND_FILE)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

        elif system == "Linux":
            commands = [
                ["paplay", str(SOUND_FILE)],
                ["aplay", str(SOUND_FILE)],
            ]

            for command in commands:
                try:
                    subprocess.Popen(
                        command,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                    )
                    return
                except FileNotFoundError:
                    continue

            print("No supported audio player found.")

        else:
            print(f"Unsupported operating system: {system}")

    except Exception as exc:
        print(f"Could not play sound: {exc}")


if __name__ == "__main__":
    play_sound()