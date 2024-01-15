import string
def long_word(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    word = text.lower().split()
    word = [word.strip(string.punctuation) for word in word]
    word = [word for word in word if word]
    max_len = max(len(word) for word in word)
    longest_word = [word for word in word if len(word) == max_len]
    print("Слово (слова) с макимальной длиной:", longest_word)
long_word("article.txt")