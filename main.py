from stats import get_num_words, get_char_dict

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def main():
	book_text = get_book_text("books/frankenstein.txt")
	num_words = get_num_words(book_text)
	print(f"Found {num_words} total words")
	char_dict = get_char_dict(book_text)
	print(char_dict)

main()