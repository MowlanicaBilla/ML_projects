#

# List of words to be compared


list_of_words = ["also", "although", "and", "as", "because", "before", "but", "for", "if", "nor", "of",
"or", "since", "that", "though", "until", "when", "whenever", "whereas",
"which", "while", "yet", ",", ";", "-", "'"]

count = 0

with open('sample.txt','r') as f:
	for word in f.readlines():
		words = word.lower().split()
		for i in list_of_words:
			if i in words:
				count+=1
		print(str(i),':',count)
