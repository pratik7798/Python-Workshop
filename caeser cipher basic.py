#For encryption
word=input("Enter word to encrypt ") #Input word from user
k=int(input("Enter the encrypt value ")) #k value for encryption
alphabet_values=[] #list to store alphabets
number_alphabet=[] #list to store numbers
for i in word:
    alphabet_values.append(ord(i)) #for loop for conversion of alphabet to its number
alphabet_values=[int(i) for i in alphabet_values]
# print(alphabet_values) #to print ascii values
result=[x+k for x in alphabet_values]
# print((result)) #to print ascii values
for i in result:
    number_alphabet.append(chr(i)) #for loopn for conversion of number to alphabet
number_alphabet="".join([str(i) for i in number_alphabet])
print(number_alphabet)

# For Decryption
decrypt=input("Enter word to decrypt ")
j=int(input("Enter the decrypt value "))
alphabet_values1=[] #list to store alphabets
number_alphabet1=[] #list to store numbers
for i in decrypt:
    alphabet_values1.append(ord(i)) #for loop for conversion of alphabet to its number
alphabet_values1=[int(i) for i in alphabet_values1]
# print(alphabet_values) #to print ascii values
result1=[x-k for x in alphabet_values1]
# print((result1)) #to print ascii values
for i in result1:
    number_alphabet1.append(chr(i)) #for loopn for conversion of number to alphabet
number_alphabet1="".join([str(i) for i in number_alphabet1])
print(number_alphabet1)

 