import subprocess
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TRCK, TYER, error

def convert_video_to_audio(input_file: str, output_file: str, quality: str, codec: str, effect: str) -> tuple[bool, str]:
    command = [
        'ffmpeg', '-i', input_file,
        '-vn', '-ar', '44100', '-ac', '2', '-ab', quality,
        '-codec:a', codec
    ]
    
    if effect:
        command.extend(['-af', effect])
        
    command.append(output_file)
    
    try:
        subprocess.run(command, check=True)
        return True, ""
    except subprocess.CalledProcessError as e:
        return False, str(e)

def set_id3_tags(file_path: str, title: str, artist: str, album: str, track: str, year: str) -> None:
    try:
        audio = ID3(file_path)
    except error:
        audio = ID3()

    audio["TIT2"] = TIT2(encoding=3, text=title)
    audio["TPE1"] = TPE1(encoding=3, text=artist)
    audio["TALB"] = TALB(encoding=3, text=album)
    audio["TRCK"] = TRCK(encoding=3, text=track)
    audio["TYER"] = TYER(encoding=3, text=year)
    
    audio.save(file_path)
