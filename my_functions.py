import difflib
from datetime import datetime
import roster
import playsound
import threading

def play_audio_in_background(audio_file_path):
    playsound.playsound(audio_file_path, True)

def play_audio(studentName):
    audio_file = f"/home/pudding/Desktop/Announcement/{studentName}.mp3"
    audio_thread = threading.Thread(target=play_audio_in_background, args=(audio_file,))
    audio_thread.start()

def successReply(studentName, conn):
    print(studentName)
    current_datetime = datetime.now().time().strftime('%I:%M:%S')
    message = f"Classroom announced: {studentName} at {current_datetime}"
    conn.sendall(message.encode("utf-8"))

def notOnRosterReply(studentName, conn):
    message = f"{studentName} could not be found in the roster."
    conn.sendall(message.encode("utf-8"))

def printSeparator():
    print(f"{'-' * 57}")

def timeOutMsg(studentName):
    return f"Unable to connect to classroom ({roster.rosterWithClass[studentName]})"

def sendMsg(studentName):
    print(f"Student found : {studentName}")

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
