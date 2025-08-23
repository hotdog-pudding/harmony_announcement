import vlc
import difflib
from datetime import datetime
import roster

def play_audio(studentName):
    instance = vlc.Instance('--no-video')
    media = instance.media_new(f"{studentName}.mp3")
    player = instance.media_player_new()
    player.set_media(media)
    player.play()

def successReply(studentName, conn):
    current_datetime = datetime.now().time().strftime('%I:%M:%S')
    message = f"Server receive: {studentName} at {current_datetime}"
    conn.sendall(message.encode("utf-8"))

def failReply(studentName, conn):
    message = f"{studentName} could not be found in the roster."
    conn.sendall(message.encode("utf-8"))

def announcement(studentName):
    print(studentName)
    play_audio(studentName)

def typoCheck(studentName):
    names = []
    for key in roster.rosterWithClass:
        names.append(key)
    closeMatch = difflib.get_close_matches(studentName, names, n=1, cutoff=0.6)
    if closeMatch:
        return closeMatch[0]
    else:
        print(f'Unable to find {studentName} in roster')
        return studentName