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
                    case "Iris C":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Cori H":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Aaron L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Ari N":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Tyler P":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Jamie S":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Penny S":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Noah T":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Wren Y":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                my_functions.failReply(studentName, conn)
                
