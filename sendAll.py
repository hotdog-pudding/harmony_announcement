import socket
import roster
import my_functions

while True:
    studentName = input("Student: ").title()
    my_functions.printSeparator()
    studentName = my_functions.typoCheck(studentName)
    for key in roster.rosterWithClass:
        if studentName == key:
            for value in roster.fridayClassroomIP.values():
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(2.0)
                    try:
                        s.connect((value, roster.PORT))
                        name_bytes = studentName.encode("utf-8")
                        s.sendall(name_bytes)
                        print(f'Sending {studentName} to {value}')
                        data = s.recv(1024)
                        received_response = data.decode("utf-8")
                        #print(received_response)
                    except:
                        print(f'Unable to connect to {value}')
                        #print(value)
                        continue
            my_functions.printSeparator()