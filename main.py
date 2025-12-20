from stats import get_num_words, get_char_dict, sort_char_dict
import sys

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def print_report(book_location, word_count, char_dict_list):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_location}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")

	for char_dict in char_dict_list:
		if not char_dict["char"].isalpha():
			continue
		print(f"{char_dict["char"]}: {char_dict["num"]}")

	print("============= END ===============")

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	
	book_location = sys.argv[1] 
	book_text = get_book_text(book_location)
	num_words = get_num_words(book_text)
	char_dict = get_char_dict(book_text)
	char_dict_list = sort_char_dict(char_dict)
	print_report(book_location, num_words, char_dict_list)

main()