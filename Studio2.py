import my_functions
    
with my_functions.socket.socket(my_functions.socket.AF_INET, my_functions.socket.SOCK_STREAM) as s:
    s.bind((my_functions.HOST, my_functions.PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                studentName = data.decode("utf-8").title()
                studentName = my_functions.typoCheck(studentName)
                match studentName:
                    case "Luke B":
                        my_functions.announcement(studentName)
                    case "Daniel C":
                        my_functions.announcement(studentName)
                    case "Aeneas S":
                        my_functions.announcement(studentName)
                    case "Jacob S":
                        my_functions.announcement(studentName)
                    case "Sophia T":
                        my_functions.announcement(studentName)
                    case "Nicholas Y":
                        my_functions.announcement(studentName)
                    case "Noah C":
                        my_functions.announcement(studentName)
                    case "Violet H":
                        my_functions.announcement(studentName)
                    case "Jolin H":
                        my_functions.announcement(studentName)
                    case "Karsten L":
                        my_functions.announcement(studentName)
                    case "Jacob L":
                        my_functions.announcement(studentName)
                    case "Oliver L":
                        my_functions.announcement(studentName)
                    case "Victoria R":
                        my_functions.announcement(studentName)
                    case "William T":
                        my_functions.announcement(studentName)
                    case "Abigail C":
                        my_functions.announcement(studentName)
                    case "Bianca R":
                        my_functions.announcement(studentName)
                my_functions.failReply(studentName)
                
