text = "Python is good language to learn and in same time we like to tell that it is cool experience for us"
my_dict = {letter: text.count(letter) for letter in text if letter.isalpha()}
print(my_dict)