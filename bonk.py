import sys
from art import *

def v1():
    tprint("VLUCHTELING")
    print("Je komt thuis van school en je hoort bommen, wat ga je doen?\nA. Verstoppen in een bunker\nB. Vluchten")
    q1 = input()
    if q1 == "a" or q1 == "A":
        v4()
    elif q1 == "b" or q1 == "B":
        v2()
    else:
        print("\nDat was geen keuze\n")
        v1()

def v2():
    print("\nJe bent geraakt door een bom, wat ga je doen?\nA. Ambulance bellen\nB. Familie bellen\nC. Wachten op hulp")
    q2 = input()
    if q2 == "a" or q2 == "A":
        v3()
    elif q2 == "b" or q2 == "B":
        v3()
    elif q2 == "c" or q2 == "C":
        print("\nNiemand kwam je helpen en bent overleden!\n")
        tprint("YOU DIED")
        v1()
    else:
        print("\nDat was geen keuze\n")
        v3()

def v3():
    print("\nJe bent naar het ziekenhuis gebracht en je bent weer hersteld, wat ga je doen?\nA. Verder met vluchten\nB. Naar huis")
    q3 = input()
    if q3 == "a" or q3 == "A":
        v4()
    elif q3 == "b" or q3 == "B":
        print("\nHet was niet veilig thuis en je bent overleden\n")
        tprint("YOU DIED")
        v1()
    else:
        print("\nDat was geen keuze\n")
        v3()

def v4():
    print("\nHet is weer veilig buiten dus je gaat vluchten. Wat ga je doen?\nA. Naar de grens toe\nB. Naar het vliegveld toe")
    q4 = input()
    if q4 == "a" or q4 == "A":
        v5()
    elif q4 == "b" or q4 == "B":
        v6()
    else:
        print("\nDat was geen keuze\n")
        v4()

def v5():
    print("\nJe bent aangekomen bij de grens, wat ga je doen?\nA. Een smokkelaar betalen om je te helpen\nB. Doorlopen")
    q5 = input()
    if q5 == "a" or q5 == "A":
        v7()
    elif q5 == "b" or q5 == "B":
        print("\nJe hebt zo lang gelopen en had geen eten en je bent verhongerd.\n")
        tprint("YOU DIED")
        v1()

def v6():
    print("\nJe hebt het vliegtuig gepakt en bent beland in Nederland. Wat ga je doen?\nA. Mensen vragen om hulp\nB. Naar de politie")
    q6 = input()
    if q6 == "a" or q6 == "A":
        v8()


def v7():
    print("\nDe smokkelaar heeft je over de grens gebracht en je bent nu in Turkije. Wat ga je doen?\nA. Doorvluchten\nB. Zoeken voor verblijf in Turkije")

def v8():
    print("\nJe vraagt iemand om hulp en je wordt verteld om terug naar je eigen land te gaan. Wat ga je doen?\nA. Andere mensen vragen om hulp\nB. Terug gaan naar je eigen land")

def v9():
    print("\nJe wordt verteld om naar de politie te gaan omdat die je zullen helpen. Wat ga je doen?\nA. Naar de politie gaan\nB. Doorzoeken naar hulp")

def v10():
    print("\nJe vind een politieagent en vraagt om hulp")

v1()