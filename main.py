import random
import sys
import time
#This function allows text to be typed out when you print it 
def type(text):
  words = text
  for char in words:
    time.sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
#this function allows a random choice to be picked from a list
def oppdr(list):
  return random.choice(list)
#this functions allows for everything before this function in the console to be wiped out
def clearConsole():
    print("\033[H\033[J", end="")
#this function returns a random number between 1 and 10
def curv():
 return random.randint(1,10)
# this function allows you to pick an element of a list using an int
def listpicker(list, num):
  return list[num -1]
cards = ["one","two" ,"three","four" ,"five" , "six" , "seven","eight","nine","ten"]
type("totally not shady dude: hey kid welcome to blackja- I MEAN whitemike!!! please bet the amount of money ")
monez = int(input("(Enter the amount of money you want to bet "))
