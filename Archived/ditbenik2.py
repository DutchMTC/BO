import sys

def v1():
    print("Je komt thuis van school en je hoort bommen, wat ga je doen?\nA. Verstoppen in een bunker\nB. Vluchten")

def v2():
    print("\nJe bent geraakt door een bom, wat ga je doen?\nA. Ambulance bellen\nB. Familie bellen\nC. Wachten op hulp")

def v3():
    print("\nJe bent naar het ziekenhuis gebracht en je bent weer hersteld, wat ga je doen?\nA. Verder met vluchten\nB. Naar huis")

def v3v2():
    print("\nHet is weer veilig buiten dus je gaat vluchten. Wat ga je doen?\nA. Naar de grens toe\nB. Naar het vliegveld toe")

def v4():
    print("\nJe bent aangekomen bij de grens, wat ga je doen?\nA. Een smokkelaar betalen om je te helpen\nB. Doorlopen")

def v5():
    print("\nJe hebt het vliegtuig gepakt en bent beland in Nederland. Wat ga je doen?\nA. Mensen vragen om hulp\nB. Naar de politie")

def v6():
    print("\nDe smokkelaar heeft je over de grens gebracht en je bent nu in Turkije. Wat ga je doen?\nA. Doorvluchten\nB. Zoeken voor verblijf in Turkije")

def v7():
    print("\nJe vraagt iemand om hulp en je wordt verteld om terug naar je eigen land te gaan. Wat ga je doen?\nA. Andere mensen vragen om hulp\nB. Terug gaan naar je eigen land")

def v8():
    print("\nJe wordt verteld om naar de politie te gaan omdat die je zullen helpen. Wat ga je doen?\nA. Naar de politie gaan\nB. Doorzoeken naar hulp")

def start():
    v1()
    a1 = input()
    if a1 == "b" or a1 == "B":
        v2()
        a2 = input()
        if a2 == "a" or a2 == "A":
            v3()
            a3 = input()
            if a3 == "b" or a3 == "B":
                print("\nJe bent overleden omdat het niet veilig was thuis.\n")
                start()
        elif a2 == "b" or a2 == "B":
            v3()
            a3 = input() 
            if a3 == "b" or a3 == "B":
                print("\nJe bent overleden omdat het niet veilig was thuis.\n")
                start()
        elif a2 == "c" or a2 == "C":
            print("\nNiemand kwam je helpen en je bent overleden.\n")      
            start()
    v3v2()
    a3v2 = input()
    if a3v2 == "a" or a3v2 == "A":
        v4()
        a4 = input()
        if a4 == "a" or a4 == "A":
            v6()
            a6 = input()
            if a6 == "a" or a6 == "A":
                print("TBC")

    v5()

start()