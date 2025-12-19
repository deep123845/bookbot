def get_num_words(input_string):
	words = input_string.split()
	return len(words)

def get_char_dict(input_string):
	char_dict = {}
	for char in input_string:
		lowercase_char = char.lower()
		if not lowercase_char in char_dict:
			char_dict[lowercase_char] = 0	
		char_dict[lowercase_char] += 1
	return char_dict	