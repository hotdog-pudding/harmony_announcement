import socket
import subprocess
import vlc
import difflib
import time
from datetime import datetime
    
HOST = ''  # Listen on all available interfaces
ICP = '192.168.1.xxx'
CP = '192.168.1.xxx'
HMC = '192.168.1.xxx'
G = '192.168.1.xxx'
BC = '192.168.1.xxx'
CB = '192.168.1.xxx'
SM = '192.168.0.189'
S = '192.168.0.189'
PORT = 2360

rosterWithClass = {
    "Raelyn A" : SM, "Apollo B" : SM, "Belle E" : SM, "Coco H" : SM,
    "Harper L" : SM, "Matthew L" : SM, "Leighton L" : SM, "Mia M" : SM,
    "Mya N" : SM, "Nikki T" : SM, "Megan U" : SM,
    "Luke B" : S, "Daniel C" : S, "Aeneas S" : S, "Jacob S" : S,
    "Sophia T" : S, "Nicholas Y" : S, "Noah C" : S, "Violet H" : S,
    "Jolin H" : S, "Karsten L" : S, "Jacob L" : S, "Oliver L" : S,
    "Victoria R" : S, "William T" : S, "Abigail C" : S, "Bianca R" : S,
    "Everett H" : CB, "Jasmin H" : CB, "Claire H" : CB, "James M" : CB,
    "James A" : CB, "Nora G" : CB, "Nathan G" : CB, "Hunter H" : CB,
    "Ryan L" : CB, "Kaylie N" : CB,
    "Oona B" : G, "Elliot L" : G, "Anna L" : G, "Jasper L" : G,
    "Andrew T" : G, "Grace T" : G, "Danny U" : G, "Elyse Y" : G,
    "Alison Z" : G,
    "Silas G" : BC, "Mia H" : BC, "Ethan L" : BC, "Lyla M" : BC,
    "Hannah N" : BC, "Aaron O" : BC, "Courtney S" : BC, "Ryan S" : BC,
    "Quinn T" : BC, "Adelyn W" : BC,
    "Iris C" : HMC, "Cori H" : HMC, "Aaron L" : HMC, "Ari N" : HMC,
    "Tyler P" : HMC, "Jamie S" : HMC, "Penny S" : HMC, "Noah T" : HMC,
    "Wren Y" : HMC,
    "Liam C" : CP, "Faith G" : CP, "James H" : CP, "Jace L" : CP,
    "Brandon N" : CP, "Wesley N" : CP, "Dylan S" : CP, "Phoebe T" : CP,
    "Skyler Y" : CP,
    "Zachary K" : ICP, "Sadie L" : ICP, "Morgan L" : ICP, "Noemi N" : ICP,
    "Gemma O" : ICP, "Kelly P" : ICP, "Charlie S" : ICP, "Uciah T" : ICP,
    "Natalia M" : ICP,
}

def play_audio(studentName):
    instance = vlc.Instance('--no-video')
    media = instance.media_new(f"{studentName}.mp3")
    player = instance.media_player_new()
    player.set_media(media)
    player.play()

def successReply(studentName):
    current_datetime = datetime.now().time().strftime('%I:%M:%S')
    message = f"Server receive: {studentName} at {current_datetime}"
    conn.sendall(message.encode("utf-8"))

def failReply(studentName):
    message = f"{studentName} is not in this class"
    conn.sendall(message.encode("utf-8"))

def announcement(studentName):
    print(studentName)
    play_audio(studentName)
    time.sleep(3)
    play_audio(studentName)
    successReply(studentName)

def typoCheck(studentName):
    names = []
    for key in rosterWithClass:
        names.append(key)
    closeMatch = difflib.get_close_matches(studentName, names, n=1, cutoff=0.6)
    if closeMatch:
        return closeMatch[0]
    else:
        return studentName
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                studentName = data.decode("utf-8").title()
                studentName = typoCheck(studentName)
                match studentName:
                    case "Raelyn A":
                        announcement(studentName)
                    case "Apollo B":
                        announcement(studentName)
                    case "Belle E":
                        announcement(studentName)
                    case "Coco H":
                        announcement(studentName)
                    case "Harper L":
                        announcement(studentName)
                    case "Matthew L":
                        announcement(studentName)
                    case "Leighton L":
                        announcement(studentName)
                    case "Mia M":
                        announcement(studentName)
                    case "Mya N":
                        announcement(studentName)
                    case "Nikki T":
                        announcement(studentName)
                    case "Megan U":
                        announcement(studentName)
                failReply(studentName)
                
