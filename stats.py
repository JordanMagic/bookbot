def get_book_text(file_path):
    with open(file_path) as f:
        text = f.read()
    return text

def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_num_chars(text):
    words = text.split()

    num_chars = {}
    for word in words:
        for char in word:
            char = char.lower()
            if char not in num_chars:
                num_chars[char] = 1
            else:
                num_chars[char] += 1
    return num_chars

def get_sorted_num_chars(num_chars):
    return dict(sorted(num_chars.items(), key=lambda item: item[1], reverse=True))

def print_report(file_path):
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    sorted_num_chars = get_sorted_num_chars(get_num_chars(text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_num_chars.items():
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")