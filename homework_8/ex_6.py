text = """Любіть Україну, як сонце, любіть,
як вітер, і трави, і води…
В годину щасливу і в радості мить,
любіть у годину негоди.
Любіть Україну у сні й наяву,
вишневу свою Україну,
красу її, вічно живу і нову,
і мову її солов’їну.
Між братніх народів, мов садом рясним,
сіяє вона над віками…
Любіть Україну всім серцем своїм
і всіми своїми ділами.
Для нас вона в світі єдина, одна
в просторів солодкому чарі…
Вона у зірках, і у вербах вона,
і в кожному серця ударі,
у квітці, в пташині, в електровогнях,
у пісні у кожній, у думі,
в дитячий усмішці, в дівочих очах
і в стягів багряному шумі…"""

words = text.split()

my_new_dict = {}
for i in words:
    i = i.strip('.,!?"\'')
    i = i.lower()
    if i in my_new_dict:
        my_new_dict[i] += 1
    else:
        my_new_dict[i] = 1

most_common_word = max(my_new_dict, key=my_new_dict.get)
less_common_word = min(my_new_dict, key=my_new_dict.get)
most_common_count = my_new_dict[most_common_word]
less_common_count = my_new_dict[less_common_word]

print(f"Слово, яке зустрічається найчастіше: '{most_common_word}' ({most_common_count})")
print(f"Слово, яке зустрічається найменше: '{less_common_word}' ({less_common_count})")