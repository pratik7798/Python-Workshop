k=2
for row in range(1,6):
    for col in range(1,10):
        if row+col==10 or col-row==0:
            print("*",end=" ")
        elif row==1 and col!=k:
            print("*",end=" ")
            k=k+2
        else:
            print(end="  ")
    print()    