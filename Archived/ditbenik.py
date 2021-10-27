from time import sleep
import sys

text = "Hey daar! Wat is je naam?\nNaam: "
for letter in text:
  sleep(0.05)
  sys.stdout.write(letter)
  sys.stdout.flush()

naam = input()
print()

text = "Hey, " + naam + "! Stel je zou in Syrië leven tijdens een burgeroorlog. Zou je dan: \na. Vluchten\nb. Blijven\nKeuze: "
for letter in text:
  sleep(0.05)
  sys.stdout.write(letter)
  sys.stdout.flush()

choice1 = input()
print()
if choice1 == "a":
    text = "Dat was inderdaad waarschijnlijk de beste keuze."
    for letter in text:
        sleep(0.05)
        sys.stdout.write(letter)
        sys.stdout.flush()

elif choice1 == "b":
    text = "Wat nou als je zou weten dat je het niet zou overleven als je zou blijven, zou je dan wel gaan vluchten?\na. Ja\nb. Nee\nKeuze: "
    for letter in text:
        sleep(0.05)
        sys.stdout.write(letter)
        sys.stdout.flush()

    choice1_2 = input()

    if choice1_2 == "b":
        text = "\nJe bent helaas overleden :("
        for letter in text:
            sleep(0.05)
            sys.stdout.write(letter)
            sys.stdout.flush()
        sys.exit()

    elif choice1_2 == "a":
        text = "Dat is waarschijnlijk de beste keuze."
        for letter in text:
            sleep(0.05)
            sys.stdout.write(letter)
            sys.stdout.flush()
    
    else:
        text = "Dat was geen optie :("
        for letter in text:
            sleep(0.05)
            sys.stdout.write(letter)
            sys.stdout.flush()
        sys.exit()


else:
    text = "Dat was geen optie :("
    for letter in text:
        sleep(0.05)
        sys.stdout.write(letter)
        sys.stdout.flush()
    sys.exit()


choice2 = input()
