from time import sleep
import sys
import datetime

string = "Hey there! I'm Miyaki... "

for letter in string:
  sleep(0.05) 
  sys.stdout.write(letter)
  sys.stdout.flush()

sleep(0.5)

string = "\nWho are you?"
print("")

for letter in string:
  sleep(0.05)
  sys.stdout.write(letter)
  sys.stdout.flush()

naam = input("\nName: ")

string = "\nHey there, " + naam

for letter in string:
  sleep(0.05)
  sys.stdout.write(letter)
  sys.stdout.flush()

sleep(0.5)

string = "\nNice to meet you!"

for letter in string:
  sleep(0.05)
  sys.stdout.write(letter)
  sys.stdout.flush()

sleep(0.5)

string = "\nToday's date and time is: "

for letter in string:
  sleep(0.05)
  sys.stdout.write(letter)
  sys.stdout.flush()

x = datetime.datetime.now()
print(x)
