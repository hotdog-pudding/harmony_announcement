import socket
import difflib

ICP = '192.168.1.153'
CP = '192.168.1.xxx'
HMC = '192.168.1.xxx'
G = '192.168.1.xxx'
BC = '192.168.1.112'
CB = '192.168.1.101'
SM = '192.168.1.228'
S = '192.168.1.126'
PORT = 2360

rosterWithClass = {
    "Raelyn A" : SM, "Apollo B" : SM, "Belle E" : SM, "Coco H" : SM,
    "Harper L" : SM, "Matthew L" : SM, "Leighton L" : SM, "Mia M" : SM,
    "Mya N" : SM, "Nikki T" : SM, "Megan U" : SM,
    "Luke B" : S, "Daniel C" : S, "Aeneas S" : S, "Jacob S" : S,
    "Sophia T" : S, "Nicholas Y" : S, "Noah C" : S, "Violet H" : S,
    "Jolin H" : S, "Karsten L" : S, "Jacob L" : S, "Oliver L" : S,
    "Victoria R" : S, "William T" : S, "Abigail C" : S, "Bianca R" : S,
    "Everett H" : CB, "Jasmin H" : CB, "Claire H" : CB, "James M" : CB,
    "James A" : CB, "Nora G" : CB, "Nathan G" : CB, "Hunter H" : CB,
    "Ryan L" : CB, "Kaylie N" : CB,
    "Oona B" : G, "Elliot L" : G, "Anna L" : G, "Jasper L" : G,
    "Andrew T" : G, "Grace T" : G, "Danny U" : G, "Elyse Y" : G,
    "Alison Z" : G,
    "Silas G" : BC, "Mia H" : BC, "Ethan L" : BC, "Lyla M" : BC,
    "Hannah N" : BC, "Aaron O" : BC, "Courtney S" : BC, "Ryan S" : BC,
    "Quinn T" : BC, "Adelyn W" : BC,
    "Iris C" : HMC, "Cori H" : HMC, "Aaron L" : HMC, "Ari N" : HMC,
    "Tyler P" : HMC, "Jamie S" : HMC, "Penny S" : HMC, "Noah T" : HMC,
    "Wren Y" : HMC,
    "Liam C" : CP, "Faith G" : CP, "James H" : CP, "Jace L" : CP,
    "Brandon N" : CP, "Wesley N" : CP, "Dylan S" : CP, "Phoebe T" : CP,
    "Skyler Y" : CP,
    "Zachary K" : ICP, "Sadie L" : ICP, "Morgan L" : ICP, "Noemi N" : ICP,
    "Gemma O" : ICP, "Kelly P" : ICP, "Charlie S" : ICP, "Uciah T" : ICP,
    "Natalia M" : ICP,
}

def typoCheck(studentName):
    names = []
    for key in rosterWithClass:
        names.append(key)
    closeMatch = difflib.get_close_matches(studentName, names, n=1, cutoff=0.6)
    if closeMatch:
        return closeMatch[0]
    else:
        return studentName

while True:    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        studentName = input("").title()
        studentName = typoCheck(studentName)
        print(f"Calling {studentName}")
        for key in rosterWithClass:
            if studentName == key:
                s.connect((rosterWithClass[studentName], PORT))
                name_bytes = studentName.encode("utf-8")
                s.sendall(name_bytes)
                print(f"{studentName} at {rosterWithClass[studentName]}")
                data = s.recv(1024)
                received_response = data.decode("utf-8")
                print(received_response)
