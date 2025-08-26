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
                    case "Zachary K":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Sadie L":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Morgan L":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Noemi N":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Gemma O":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Kelly P":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Charlie S":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Uciah T":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Natalia M":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                my_functions.failReply(studentName, conn)
                
