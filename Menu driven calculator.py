import numpy as np
import pandas as pd
loop=True
print("\n***CACULATOR***\n")
while loop:

    a=int(input("\nEnter your choice:\n1.ADD\n2.Subtract\n3.Multiplication\n4.Division\n5.Exit  "))
    if(a==1):
        m=int(input("Enter 1st number "))
        n=int(input("Enter 2nd number "))
        print("ANSWER:", m+n)
    elif(a==2):
        m=int(input("Enter 1st number "))
        n=int(input("Enter 2nd number "))
        print("ANSWER:" ,m-n)
    elif(a==3):
        m=int(input("Enter 1st number "))
        n=int(input("Enter 2nd number "))
        print("ANSWER:" ,m*n)
    elif(a==4):
        m=int(input("Enter 1st number "))
        n=int(input("Enter 2nd number "))
        print("ANSWER:" ,m/n)
    elif(a==5):
        loop=False
    else:    
        print("Invalid choice")

    
