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
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Cori H":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Aaron L":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Ari N":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Tyler P":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Jamie S":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Penelope S":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Noah T":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Wren Y":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                my_functions.failReply(studentName, conn)
                
