print "This is a simple cypher. Call 'shift_coder' and input a string and\
 either 'code' or 'decode'."

SHIFT = 1

def shift_coder(str, method):

	if method == "code":
	## Takes a string and codes it
		characters = list(str)
		coded_characters = []
		
		for dummy_char in characters:
			ascii_int = ord(dummy_char)
			if ascii_int in range(32) + range(32, 65) + range(91, 97) + \
			range(123, 128):
				new_char = chr(ascii_int)
			elif ascii_int in range(65, 91):
				new_char = chr(((ord(dummy_char) + SHIFT - 65) % 26) + 65)
			elif ascii_int in range(97, 123):
				new_char = chr(((ord(dummy_char) + SHIFT - 97) % 26) + 97)
				
			coded_characters.append(new_char)
			
		coded_str = "".join(coded_characters)
		return coded_str

	elif method == "decode":
	## Takes a coded string and decodes it into the original message
		characters = list(str)
		coded_characters = []
		
		for dummy_char in characters:
			ascii_int = ord(dummy_char)
			
			if ascii_int in range(32) + range(32, 65) + range(91, 97) + \
			range(123, 128):
				new_char = chr(ascii_int)
			elif ascii_int in range(65, 91):
				new_char = chr(((ord(dummy_char) - SHIFT - 65) % 26) + 65)
			elif ascii_int in range(97, 123):
				new_char = chr(((ord(dummy_char) - SHIFT - 97) % 26) + 97)
				
			coded_characters.append(new_char)
			
		coded_str = "".join(coded_characters)
		return coded_str
	
	else:
		return "Method not recognized. Input 'code' or 'decode'."
