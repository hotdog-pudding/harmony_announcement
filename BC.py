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
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Mia H":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Ethan L":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Lyla M":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Hannah N":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Aaron O":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Courtney S":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Ryan S":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Quinn T":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Addie W":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                my_functions.failReply(studentName, conn)
