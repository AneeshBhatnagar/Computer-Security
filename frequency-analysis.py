#A script to perform Frequency Analysis on a given text file.

from string import punctuation
print "Hello! Welcome to the Frequency Distribution Counting program"

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_count = [0] * 26

f = open('text/q4b-encrypt.txt',"r")
lines = f.readlines()
f.close()
space = 0

for line in lines:
	line = line.lower()
	for letter in line:
		if letter == '\n' or letter == ' ' or letter in punctuation or letter.isdigit():
			space = space + 1
		else:
			alphabet_count[alphabets.index(letter)]= alphabet_count[alphabets.index(letter)] + 1

for (a,c) in zip(alphabets, alphabet_count):
	print a + ": %s " % c

print "The character that appeared the most common is: ", alphabets[alphabet_count.index(max(alphabet_count))]