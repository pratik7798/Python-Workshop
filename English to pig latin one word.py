import pandas as pd
print("English to pig latin")
a=list(input(" Enter Single word "))
temp=(a[0])
a=a[1: :]
latin=''.join([str(i) for i in a])
print(latin+temp+'ay')

