import socket
import roster
import my_functions


while True:    
    studentName = input("Student: ").title()
    my_functions.printSeparator()
    studentName = my_functions.typoCheck(studentName)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2.0)
        for key in roster.rosterWithClass:
            if studentName == key:
                try:
                    s.connect((roster.rosterWithClass[studentName], roster.PORT))
                    name_bytes = studentName.encode("utf-8")
                    s.sendall(name_bytes)
                    my_functions.sendMsg(studentName)
                    data = s.recv(1024)
                    received_response = data.decode("utf-8")
                    print(received_response)
                    my_functions.printSeparator()
                except:
                    print(f'{studentName}')
                    print(my_functions.timeOutMsg(studentName))
                    my_functions.printSeparator()
                    continue
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2.0)
        for key in roster.rosterWithClass:
            if studentName == key:
                try:
                    s.connect((roster.classroomIP['Zone1'], roster.PORT))
                    name_bytes = studentName.encode("utf-8")
                    s.sendall(name_bytes)
                    data = s.recv(1024)
                    received_response = data.decode("utf-8")
                except:
                    print(f'{studentName}')
                    print(f'Unable to connect to outside zone')
                    my_functions.printSeparator()