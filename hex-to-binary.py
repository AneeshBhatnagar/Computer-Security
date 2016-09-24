import sys
#Program to convert a given message in HEX to Binary

hex_string = "675a69675e5a6b5a"
binary_string = ''
print "This program will convert the message in HEX to Binary"
hex_string = hex_string.upper()
print "The Hex string that we have is: %s" %hex_string

#Code to convert HEX to Binary

for letter in hex_string:
	if letter == '0':
		binary_string = binary_string + '0000'
	elif letter == '1':
		binary_string = binary_string + '0001'
	elif letter == '2':
		binary_string = binary_string + '0010'
	elif letter == '3':
		binary_string = binary_string + '0011'
	elif letter == '4':
		binary_string = binary_string + '0100'
	elif letter == '5':
		binary_string = binary_string + '0101'
	elif letter == '6':
		binary_string = binary_string + '0110'
	elif letter == '7':
		binary_string = binary_string + '0111'
	elif letter == '8':
		binary_string = binary_string + '1000'
	elif letter == '9':
		binary_string = binary_string + '1001'
	elif letter == 'A':
		binary_string = binary_string + '1010'
	elif letter == 'B':
		binary_string = binary_string + '1011'
	elif letter == 'C':
		binary_string = binary_string + '1100'
	elif letter == 'D':
		binary_string = binary_string + '1101'
	elif letter == 'E':
		binary_string = binary_string + '1110'
	elif letter == 'F':
		binary_string = binary_string + '1111'
	else:
		print "The entered string is not HEX in nature!"
		sys.exit(-1)



print "The string in binary is: "
print binary_string