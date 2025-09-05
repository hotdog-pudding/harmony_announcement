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
                    case "Raelyn A":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Apollo B":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Belle E":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Coco H":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Harper L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Matthew L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Leighton L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Mia M":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Mya N":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Nikki T":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Megan U":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                my_functions.failReply(studentName, conn)
                
