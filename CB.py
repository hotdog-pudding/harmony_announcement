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
                    case "Everett H":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Jasmin H":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Claire H":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "James M":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "James A":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Nora G":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Nathan G":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Hunter H":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Ryan L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Kaylie N":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                my_functions.notOnRosterReply(studentName, conn)
                
