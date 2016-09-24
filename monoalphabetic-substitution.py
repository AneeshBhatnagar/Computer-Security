#A simple script which performs monoalphabetic Shift Substitution on a given plaintext

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

f = open('text/message.txt',"r")
lines = f.readlines()
f.close()
space = 0

substitution_key = 9
decrypted = ""

for line in lines:
	for letter in line:
		if letter == '\n' or letter == ' ':
			space = space + 1
		else:
			decrypted = decrypted + alphabets[(alphabets.index(letter) - substitution_key) % 26 ]

print decrypted