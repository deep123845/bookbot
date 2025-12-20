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

def sort_on(items):
	return items["num"]

def sort_char_dict(char_dict):
	char_dict_list = []
	for entry in char_dict:
		entry_dict = {"char": entry, "num": char_dict[entry]}
		char_dict_list.append(entry_dict)
	
	char_dict_list.sort(reverse=True, key=sort_on)
	return char_dict_list