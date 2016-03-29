import stockprice

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = "ccvc"
word = " "
for kind in word_format:
    if kind == "c":
        word += stockprice.choice(CONSONANTS)
    else:
        word += stockprice.choice(VOWELS)
print(word)

