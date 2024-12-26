import string

alphabet = string.ascii_uppercase
for i in alphabet:
    files = open("./Output/" + str(i)+".txt","w")