import math                             #importing math library to be able later to use the functions sin() and cosin()
import random                           #importing the library random, to use the function randomint to generate random numbers in a specific range

x = 0                                   #declaring integer variable to use it as a counter later in a loop
while (x < 10):                         #while loop that circels 10 times
    y = random.randint(0, 99)           #declaring y variable that has the value of the result of the function randit() which generates random value in the range of 0-99
    s = math.sin(y)                     #declaring s variable that holds the result of the function sinus() of the previous randomly generated number
    c = math.cos(y)                     #declaring c variable that holds the result of the function cosine() of the previous randomly generated number
    print("Number %d has \t sin:%f \t  and cosine:%f" % (y, s, c))  #command print to show the randoly generated number and its sinus in cosinus
    x += 1                              #increasing the value of the counter by 1


# Team name: mike
#Team memebers: Anish Girijashivaraj, Shohel Ahamad, Slobodan Kocevski
