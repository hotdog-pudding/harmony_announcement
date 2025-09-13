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
                    case "Oona B":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Elliot L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Anna L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Jasper L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Andrew T":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Grace T":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Danny U":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Elyse Y":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Alison Z":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                my_functions.notOnRosterReply(studentName, conn)
                
