#A script to perform Vigenere Encryption on a given plaintext

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

plaintext = "explanation"
key = "leg"
global i
i=0

# plaintext = "wearediscoveredsaveyourself"
# key = "deceptivewearediscoveredsav"
encrypted = ""

for p in plaintext:
	k = key[i]
	i +=1
	if i>2:
		i=0
	index = (alphabets.index(p) + alphabets.index(k)) % 26
	encrypted = encrypted + alphabets[index]

print encrypted