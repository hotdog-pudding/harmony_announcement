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
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Daniel C":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Aeneas S":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Jacob S":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Sophia T":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Nicholas Y":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Noah C":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Violet H":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Jolin H":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Karsten L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Jacob L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Oliver L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Victoria R":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "William T":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Abigail C":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Bianca R":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
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
                    case "Everett H":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Jasmin H":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Claire H":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "James M":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "James A":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Nora G":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Nathan G":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Hunter H":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Ryan L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Kaylie N":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Zachary K":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Sadie L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Morgan L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Noemi N":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Gemma O":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Kelly P":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Charlie S":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Uciah T":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Natalia M":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Liam C":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Faith G":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "James H":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Jace L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Brandon N":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Wesley N":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Dylan S":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Phoebe T":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Skyler Y":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Iris C":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Cori H":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Aaron L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Ari N":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Tyler P":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Jamie S":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Penny S":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Noah T":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Wren Y":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Silas G":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Mia H":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Ethan L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Lyla M":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Hannah N":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Aaron O":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Courtney S":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Ryan S":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Quinn T":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Addie W":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Oona B":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Elliot L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Anna L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Jasper L":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Andrew T":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Grace T":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Danny U":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Elyse Y":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                    case "Alison Z":
                        my_functions.successReply(studentName, conn)
                        my_functions.play_audio(studentName) 
                my_functions.failReply(studentName, conn)
                
