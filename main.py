def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    created_dict = get_count_characters(text)
    print(created_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_count_characters(text):
    lower_text = text.lower()
    count_dict = {}

    for letter in lower_text:
        if(letter in count_dict):
            count_dict[letter] +=1
        else:
            count_dict[letter] = 1
    #for key, value in count_dict.items():
    return count_dict


main()
