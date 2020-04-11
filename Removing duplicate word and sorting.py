import pandas as pd
Input=input("Enter text ")
Word_Dictionary=Input.split()
List=[]
for i in Word_Dictionary:
    if i not in List:
        List.append(i)
    else:
        continue 
List.sort()        
print((' ').join(List))