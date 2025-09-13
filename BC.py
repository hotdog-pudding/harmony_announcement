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
                    case "Silas G":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Mia H":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Ethan L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Lyla M":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Hannah N":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Aaron O":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Courtney S":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Ryan S":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Quinn T":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Addie W":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                my_functions.notOnRosterReply(studentName, conn)
