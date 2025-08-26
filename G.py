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
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Elliot L":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Anna L":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Jasper L":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Andrew T":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Grace T":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Danny U":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Elyse Y":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Alison Z":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                my_functions.failReply(studentName, conn)
                
