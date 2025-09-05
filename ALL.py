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
                    case "Luke B":
                        my_functions.announcement(studentName, conn)
                        #my_functions.successReply(studentName, conn)
                    case "Daniel C":
                        my_functions.announcement(studentName, conn)
                        #my_functions.successReply(studentName, conn)
                    case "Aeneas S":
                        my_functions.announcement(studentName, conn)
                        #my_functions.successReply(studentName, conn)
                    case "Jacob S":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Sophia T":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Nicholas Y":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Noah C":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Violet H":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Jolin H":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Karsten L":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Jacob L":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Oliver L":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Victoria R":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "William T":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Abigail C":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Bianca R":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
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
                    case "Everett H":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Jasmin H":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Claire H":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "James M":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "James A":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Nora G":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Nathan G":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Hunter H":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Ryan L":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Kaylie N":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
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
                    case "Dylan S":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Phoebe T":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Skyler Y":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
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
                    case "Penny S":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Noah T":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
                    case "Wren Y":
                        my_functions.announcement(studentName)
                        my_functions.successReply(studentName, conn)
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
                
