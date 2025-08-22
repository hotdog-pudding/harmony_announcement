import my_functions
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                studentName = data.decode("utf-8").title()
                studentName = typoCheck(studentName)
                match studentName:
                    case "Luke B":
                        announcement(studentName)
                    case "Daniel C":
                        announcement(studentName)
                    case "Aeneas S":
                        announcement(studentName)
                    case "Jacob S":
                        announcement(studentName)
                    case "Sophia T":
                        announcement(studentName)
                    case "Nicholas Y":
                        announcement(studentName)
                    case "Noah C":
                        announcement(studentName)
                    case "Violet H":
                        announcement(studentName)
                    case "Jolin H":
                        announcement(studentName)
                    case "Karsten L":
                        announcement(studentName)
                    case "Jacob L":
                        announcement(studentName)
                    case "Oliver L":
                        announcement(studentName)
                    case "Victoria R":
                        announcement(studentName)
                    case "William T":
                        announcement(studentName)
                    case "Abigail C":
                        announcement(studentName)
                    case "Bianca R":
                        announcement(studentName)
                failReply(studentName)
                
