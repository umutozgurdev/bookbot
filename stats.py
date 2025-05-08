def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def num_words(text):
    wordswordswords = text.split()
    wordcounter = 0
    for words in wordswordswords:
        wordcounter += 1
    return wordcounter

def sort_on(item):
    return item[1]

def dic_char(text):
    chars = {}
    text = text.lower()
    
    for char in text:
        if char in chars:
            chars[char] += 1
        else: 
            chars[char] = 1
    return chars
