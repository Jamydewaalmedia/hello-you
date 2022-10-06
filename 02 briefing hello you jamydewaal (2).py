import datetime
import math
from time import sleep

while True:
    nolist=["no", "n", "stop", "N"]
    yeslist=["yes", "y", "yeah"]
    print("hello you,ik ben jamy. Wie ben jij?")
    username = input("")
    print("hello " + username)
    sleep(2)
    print("in welk jaar ben jij geboren?")
    first_operand = int(input(""))
    datum = datetime.datetime.now()
    sleep(1)
    print("de datum van vandaag is") 
    sleep(2)
    print(datum)
    sleep (2)
    
    second_operand = 2022
    
    output = second_operand - first_operand
    print("het is 2022 jij bent dan" ) 
    print(output)
    sleep(3)
    print("wil je herstarten type y/n")
    core = input("")
    if core in nolist:
        sleep(2)
        break
