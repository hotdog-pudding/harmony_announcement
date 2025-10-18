import socket
import my_functions
import roster
import queue
import threading
import playsound

def play_sound_from_queue(sound_queue):
    while True:
        sound_file = sound_queue.get()
        if sound_file is None:
            break
        playsound.playsound(sound_file)
        sound_queue.task_done()

sound_queue = queue.Queue()
sound_thread = threading.Thread(target=play_sound_from_queue, args=(sound_queue,))
sound_thread.start()
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((roster.HOST, roster.PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                studentName = data.decode("utf-8").title()
                my_functions.successReply(studentName, conn)
                sound_queue.put(f"{studentName}.mp3") 
                my_functions.notOnRosterReply(studentName, conn)