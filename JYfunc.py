import time
import os
import random
import tkinter as tk
from tkinter import messagebox 
class console:
    def TypeLine(msg):
        print(msg)
    def LoadBar():
        print("..........")
        print("0%")
        time.sleep(1.5)
        os.system("clear")
        print("#####.....")
        print("50%")
        time.sleep(1.5)
        os.system("clear")
        print("##########")
        print("100%")
    def error(error):
        print(error)
def getInput(msg):
    input(msg)
def ret(arg):
    return arg
def convertToInt(thing):
    value = int(thing)
def convertToDouble(thing):
    value = float(thing)
class Thread:
    def sleep(time):
        time.sleep(time)
def leng(thing):
    print(len(thing))
class IfElse:
    def If(condition, Condition2,do,elseDo):
        if condition == Condition2:
            console.WriteLine(do)
        else:
            console.WriteLine(elseDo)
    def greater(condition, cond,do,dd):
        if condition > cond:
            print(do)
        else :
            print(dd)
def gameSnip(key1,key2,player):
    playeR = player
    player_x = 0
    while True:
        print(playeR)
        user = input(f"Enter action ({key1}/{key2}): ")
        os.system("clear")
        if user == key1:
            player_x += 1
        elif user == key2:
            player_x -= 1
        else :
            print("invalid action ")
        playeR = " " * abs(player_x) + f"{player}"
class games:
    def game1():
        a = random.randint(1,10)
        b = random.randint(1,10)
        ans = a + b 
        user = int(input(f"what is {a} + {b} ?\n"))
        if user == ans:
            print("Correct!")
        else :
            print("wrong")
    def game2(msg,inpt):
        a = random.randint(0,10)
        print(msg)
        user = int(input(inpt))
        if user == a:
            print("Correct!")
        else:
            print("incorrect!")
class apps:
    def exmplCal(msg1,msg2):
        val1 = int(input(msg1))
        val2 = int(input(msg2))
        return val1 + val2
    def phoneNum():
        n1 = random.randint(0,9)
        n2 = random.randint(0,9)
        n3 = random.randint(0,9)
        n4 = random.randint(0,9)
        n5 = random.randint(0,9)
        n6 = random.randint(0,9)
        n7 = random.randint(0,9)
        n8 = random.randint(0,9)
        n9 = random.randint(0,9)
        n10 = random.randint(0,9)  
        print(f"{n1}{n2}{n3}{n4}{n5}{n6}{n7}{n8}{n9}{n10}")  
    def optimizer():
        user = input("Enter a word or sentence : ")
        print("Length : ",len(user))
        print("character used : ",len(user))
class AI:
    def Chatbot(msg1,msg2,msg3,ans1,ans2,ans3):
        user = input("Ask : ")
        if user == msg1:
            print(ans1)
        elif user == msg2:
            print(ans2)
        elif user == msg3:
            print(ans3)
        else :
            print("Something went wrong...")
def loop(times,thing):
    for i in range (times):
        print(thing)
    