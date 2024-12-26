import string

def letters_in_file(n):
    with open('output.txt', 'w') as f:
        alphabet = string.ascii_uppercase
        output = [alphabet[i:i+n] + '\n' for i in range(0, len(alphabet), n)]
        f.writelines(output)

letters_in_file(3)
	