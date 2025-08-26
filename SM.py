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
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Apollo B":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Belle E":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Coco H":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Harper L":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Matthew L":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Leighton L":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Mia M":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Mya N":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Nikki T":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Megan U":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                my_functions.failReply(studentName, conn)
                
