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
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Faith G":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "James H":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Jace L":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Brandon N":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Wesley N":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "DJ S":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Phoebe T":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Skyler Y":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                my_functions.failReply(studentName)
                
