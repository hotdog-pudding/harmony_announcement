import socket
import my_functions
import roster
    
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
                match studentName:
                    case "Zachary K":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Sadie L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Morgan L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Noemi N":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Gemma O":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Kelly P":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Charlie S":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Uciah T":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Natalia M":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                my_functions.failReply(studentName, conn)
                
