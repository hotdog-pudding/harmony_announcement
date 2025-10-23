import socket
import roster
import my_functions
import threading


def connect_to_server(host, port, studentName):
        try:
            with socket.create_connection((host,port), timeout=10) as s:
                s.sendall(bytes(studentName, encoding='utf-8'))
        except Exception as e:
            print(f"{studentName} Unable to connect to {host}")

def find_classroom_ip(studentName):
     for key in roster.rosterWithClass:
          if studentName == key:
               return roster.rosterWithClass[studentName]

while True:    
    studentName = input("Student: ").title()
    my_functions.printSeparator()
    studentName = my_functions.typoCheck(studentName)
    '''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #s.settimeout(0.5)
        for key in roster.rosterWithClass:
            if studentName == key:
                try:
                    s.connect((roster.rosterWithClass[studentName], roster.PORT))
                    name_bytes = studentName.encode("utf-8")
                    s.sendall(name_bytes)
                    my_functions.studentFoundReply(studentName)
                    #data = s.recv(1024)
                    #received_response = data.decode("utf-8")
                    #print(received_response)
                except:
                    print(f'{studentName}')
                    print(my_functions.timeOutMsg(studentName))
                    continue
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
<<<<<<< HEAD
        #s.settimeout(2.0)
=======
        s.settimeout(0.5)
>>>>>>> 11fbb119a84a56acd1938f9a81f9c94e42e5fa66
        for key in roster.rosterWithClass:
            if studentName == key:
                try:
                    s.connect((roster.classroomIP['Zone1'], roster.PORT))
                    name_bytes = studentName.encode("utf-8")
                    s.sendall(name_bytes)
                    #data = s.recv(1024)
                    #received_response = data.decode("utf-8")
                except:
                    print(f'Unable to connect to Zone 1 (192.168.1.18)')
    my_functions.printSeparator()
    '''

    servers = [("192.168.1.18", 2360)]
    servers.append((find_classroom_ip(studentName), 2360))
    threads = []
    for host, port in servers:
         t = threading.Thread(target=connect_to_server, args=(host, port, studentName))
         t.start()
         threads.append(t)
