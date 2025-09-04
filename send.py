import socket
import roster
from my_functions import typoCheck


while True:    
    studentName = input("Student: ").title()
    studentName = typoCheck(studentName)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        for key in roster.rosterWithClass:
            if studentName == key:
                s.connect((roster.rosterWithClass[studentName], roster.PORT))
                name_bytes = studentName.encode("utf-8")
                s.sendall(name_bytes)
                print(f"{studentName} at {roster.rosterWithClass[studentName]}")
                data = s.recv(1024)
                received_response = data.decode("utf-8")
                print(received_response)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        for key in roster.rosterWithClass:
            if studentName == key:
                s.connect((roster.classroomIP['Zone1'], roster.PORT))
                name_bytes = studentName.encode("utf-8")
                s.sendall(name_bytes)
                print(f"{studentName} at {roster.rosterWithClass[studentName]}")
                data = s.recv(1024)
                received_response = data.decode("utf-8")
                print(received_response)