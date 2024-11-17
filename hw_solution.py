text: str = """
This chocolate cake is rich, moist, and full of delicious chocolate flavor.
To make the cake, you will need chocolate, flour, sugar, eggs, and butter.
After baking the chocolate cake, let the cake cool before adding the chocolate frosting.
"""
# { 'this': 1, 'chocolate': 2}
words: list[str] = (text.lower().replace(".", "").
                    replace(",", "").split())
print(words)
dict_count_words: dict[str: int] = dict()
for word in words:
    # word = [c for c in word if c.isalpha()]
    # shorter
    # dict_count_words[word] = dict_count_words.get(word, 0) + 1
    if word in dict_count_words:
        dict_count_words[word] += 1
    else:
        dict_count_words[word] = 1
print(dict_count_words)

max_value_loop = None
max_value_key = None
for item in dict_count_words.items():
    if max_value_loop is None or item[1] > max_value_loop:
        max_value_loop = item[1]
        max_value_key = item[0]
print(f"max {max_value_key} {max_value_loop}")

max_key = max(dict_count_words, key=lambda key_dict: dict_count_words[key_dict])
max_value = dict_count_words[max_key]
print(f"max {max_key} {max_value}")

print(sorted(dict_count_words.items(), key = lambda item: item[1], reverse=True)[0][0])
print(sorted(dict_count_words.items(), key = lambda item: item[1], reverse=True)[0][1])
print(sorted(dict_count_words.items(), key = lambda item: item[1])[0][0])
print(sorted(dict_count_words.items(), key = lambda item: item[1])[0][1])

dict_count_letters: dict[str: int] = dict()
for lett in text.lower().replace(" ", ""):
    # short
    #dict_count_letters[lett] = dict_count_letters.get(lett, 0) + 1
    if lett in dict_count_letters:
        dict_count_letters[lett] += 1
    else:
        dict_count_letters[lett] = 1
print(dict_count_letters)

print(list(sorted(dict_count_letters.items(), key = lambda item: item[1], reverse=True)))
max_letter = max(dict_count_letters, key=lambda key_item: dict_count_letters[key_item])
print('max', max_letter, dict_count_letters[max_letter])
min_letter = min(dict_count_letters, key=lambda key_item: dict_count_letters[key_item])
print('min', min_letter, dict_count_letters[min_letter])

dict_hezka3: dict[int, int] = dict()
for i in range(0, 20 + 1):
    dict_hezka3[i] = i ** 3
print(dict_hezka3)
print(dict_hezka3[9])
list_power3 = [i**3 for i in range(0, 20 + 1)]
print(list_power3)
print(list_power3[9])

dict_days = {1: 'sunday', 2: 'monday', 3: 'tuesday', 4: 'wednesday', 5: 'thursday', 6:'friday'}
list_days = [None, 'sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday']
print(dict_days[3])
print(list_days[3])

dict_daysw = {'sunday': 1, 'monday': 2, 'tuesday': 3, 'wednesday': 4, 'thursday': 5, 'friday': 6}
print(dict_daysw['monday'])
list_days = [None, 'sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday']
grades = {'danny': 90, 'sharon': 89, 'shlomi': 55}


