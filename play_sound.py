import subprocess
import sys
from pathlib import Path


SOUND_FILE = Path(__file__).resolve().parent / "sounds" / "push.mp3"




def play_sound():
    if not SOUND_FILE.is_file():
        print(f"Sound file not found: {SOUND_FILE}")
        return 1

    sound_path = str(SOUND_FILE).replace("'", "''")

    script = f"""
Add-Type -AssemblyName PresentationCore
$player = New-Object System.Windows.Media.MediaPlayer
$player.Volume = 1
$player.Open([Uri]::new('{sound_path}'))
Start-Sleep -Seconds 2
$player.Play()
Start-Sleep -Seconds 5
$player.Close()
"""

    try:
        result = subprocess.run(
            [
                "powershell.exe",
                "-NoProfile",
                "-NonInteractive",
                "-ExecutionPolicy",
                "Bypass",
                "-Command",
                script,
            ],
            check=False,
        )
        return result.returncode

    except Exception as exc:
        print(f"Could not play sound: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(play_sound())