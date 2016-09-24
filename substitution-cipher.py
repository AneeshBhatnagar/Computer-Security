#Program to perform a monoalphabetic substituion based on a substitution function

from string import punctuation
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
file = open("q4b.txt")
lines = file.readlines()
file.close()
spaces = 0
encrypted = ''


#Encrypt the entire text using one fucntion
for line in lines:
	line = line.lower()
	for letter in line:
		if letter == '\n' or letter == ' ' or letter in punctuation or letter.isdigit():
			spaces +=1
		else:
			index = 3 * (alphabets.index(letter)) % 26
			encrypted = encrypted + alphabets[index]

print encrypted

'''
#Encrypting Odd and Even position characters differently
count = 1
encrypted = ''
for line in lines:
	line = line.lower()
	for letter in line:
		if letter == '\n' or letter == ' ' or letter in punctuation or letter.isdigit():
			spaces+=1
		else:
			if count % 2 == 1:
				#Function for odd positions
				index = 3 * (alphabets.index(letter)) % 26
			else:
				#Function for even positions
				index = ((5 * (alphabets.index(letter)))+13) % 26
			encrypted = encrypted + alphabets[index]
			count +=1			
print encrypted
'''