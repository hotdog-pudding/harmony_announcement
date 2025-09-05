import vlc
import difflib
from datetime import datetime
import roster
import time

def play_audio(studentName):
    instance = vlc.Instance('--no-video', '--play-and-exit')
    media = instance.media_new(f"{studentName}.mp3")
    player = instance.media_player_new()
    player.set_media(media)
    player.play()
    time.sleep(5)
    media.release()
    player.release()
    instance.release()

def successReply(studentName, conn):
    print(studentName)
    current_datetime = datetime.now().time().strftime('%I:%M:%S')
    message = f"Classroom announced: {studentName} at {current_datetime}"
    conn.sendall(message.encode("utf-8"))

def failReply(studentName, conn):
    message = f"{studentName} could not be found in the roster."
    conn.sendall(message.encode("utf-8"))

def printSeparator():
    print(f"{'-' * 37}")

def timeOutMsg(studentName):
    return f"Unable to connect to {roster.rosterWithClass[studentName]}"

def sendMsg(studentName):
    print(f"Sending {studentName} to {roster.rosterWithClass[studentName]}")

# Takes input and checks it with the names on the roster and if close enough it will return the name from the roster
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
