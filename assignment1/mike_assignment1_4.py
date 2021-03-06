from matplotlib import pyplot as plt    #importing pyplot library to use the functions to generate the graph
import math                             #importing math library to be able later to use the functions sin() and cosin()
import random                           #importing the library random, to use the function randomint to generate random numbers in a specific range

x = 0                                   #declaring integer variable to use it as a counter later in a loop
sin = []                                #declaring array sin
cosin = []                              #declaring array sin
while (x < 10):                         #while loop that circels 10 times
    y = random.randint(0, 90)           #declaring y variable that has the value of the result of the function randit() which generates random value in the range of 0-90
    s = math.sin(y)                     #declaring s variable that holds the result of the function sinus() of the previous randomly generated number
    c = math.cos(y)                     #declaring c variable that holds the result of the function cosine() of the previous randomly generated number
    sin.insert(x, s)                    #using the function insert() in order to put the value s in the array sin[] in position x (in the first loop x=0)
    cosin.insert(x, c)                  #using the function insert() in order to put the value c in the array cosin[] in position x (in the first loop x=0)
    x += 1                              #increasing the value of the counter by 1
plt.plot(sin, color="red")              #creating the first line in the graph out of the values stored in the array sin[], which is the first argument of the funtion plot. And the second argument is for defining the color of the line.
plt.plot(cosin, color="blue")           #creating the first line in the graph out of the values stored in the array cosin[], which is the first argument of the funtion plot. And the second argument is for defining the color of the line.
plt.show()                              #showing the above created graph


# Team name: mike
#Team memebers: Anish Girijashivaraj, Shohel Ahamad, Slobodan Kocevski
