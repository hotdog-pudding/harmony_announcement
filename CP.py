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
                    case "Liam C":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Faith G":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "James H":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Jace L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Brandon N":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Wesley N":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Dylan S":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Phoebe T":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                my_functions.notOnRosterReply(studentName, conn)
                
