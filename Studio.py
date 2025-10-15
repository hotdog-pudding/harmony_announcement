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
                    case "Luke B":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Daniel C":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Aeneas S":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Jacob S":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Sophia T":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Nicholas Y":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Noah C":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Violet H":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Jolin H":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Karsten L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Jacob L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Oliver L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Victoria R":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "William T":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Abigail C":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Bianca R":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Leo L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                my_functions.notOnRosterReply(studentName, conn)
                
