ans = input("select a game. \n a) Addition b) Multiplication\n")
ans = str(ans)
from MathGame import *
if ans=="a":
    addition()
if ans=="b":
    multiplication()
