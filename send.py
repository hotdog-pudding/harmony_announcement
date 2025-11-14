import socket
import roster
import my_functions
import threading
import os

def connect_to_server(host, port, studentName):
        try:
            with socket.create_connection((host,port), timeout=10) as s:
                s.sendall(bytes(studentName, encoding='utf-8'))
        except Exception as e:
            print(f"Error: {e}")
            print(f"{studentName} - Unable to connect to {host}")

def find_classroom_ip(studentName):
     for key in roster.rosterWithClass:
          if studentName == key:
               return roster.rosterWithClass[studentName]
          
def clear_screen():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")
          
same_first_names = ["James", "Aaron", "Tyler", "Mia", "Ryan"]
                  
while True:
    my_functions.printSeparator()
    print("Enter 1 or 2 to select mode")
    print("1 - Send to individual classroooms")
    print("2 - Send to Zone 1, CP, HMC, and Studio (Friday)")
    my_functions.printSeparator()
    mode = input()

    if mode == "1":
        clear_screen()
        while True:
            print("\033[32mMode 1 - Sent to all classrooms\033[0m")
            studentName = input("Student Name('exit' to select mode) : ").title()
            my_functions.printSeparator()
            if studentName == "Exit": 
                clear_screen()
                break
            if studentName in same_first_names:
                print("\033[41m\033[97mPlease also enter last name inital\033[0m")
                continue
            original_student_name = studentName
            studentName = my_functions.typoCheck(studentName)
            if studentName == "Error":
                print(f'Unable to find {original_student_name} in roster')
                continue

            servers = [("192.168.1.18", 2360)]
            servers.append((find_classroom_ip(studentName), 2360))
            threads = []
            for host, port in servers:
                t = threading.Thread(target=connect_to_server, args=(host, port, studentName))
                t.start()
                threads.append(t)

    elif mode == "2":
         clear_screen()
         while True:
            print("\033[32mMode 2 - Sent to Zone 1, CP, HMC, and Studio\033[0m")
            studentName = input("Student Name('exit' to select mode) : ").title()
            my_functions.printSeparator()
            if studentName == "Exit":
                 clear_screen()
                 break
            if studentName in same_first_names:
                print("\033[41m\033[97mPlease also enter last name inital\033[0m")
                continue
            studentName = my_functions.typoCheck(studentName)
            original_student_name = studentName
            studentName = my_functions.typoCheck(studentName)
            if studentName == "Error":
                print(f'Unable to find {original_student_name} in roster')
                continue

            servers = [("192.168.1.18", 2360), ("192.168.1.15", 2360), ("192.168.1.13", 2360), ("192.168.1.11", 2360)]
            threads = []
            for host, port in servers:
                t = threading.Thread(target=connect_to_server, args=(host, port, studentName))
                t.start()
                threads.append(t)
    else:
        my_functions.printSeparator() 
        print("Invalid selection")
          
'''
while True:    
    studentName = input("Student: ").title()
    my_functions.printSeparator()
    studentName = my_functions.typoCheck(studentName)
    
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
        s.settimeout(0.5)
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

    servers = [("192.168.1.18", 2360)]
    servers.append((find_classroom_ip(studentName), 2360))
    threads = []
    for host, port in servers:
         t = threading.Thread(target=connect_to_server, args=(host, port, studentName))
         t.start()
         threads.append(t)
'''
