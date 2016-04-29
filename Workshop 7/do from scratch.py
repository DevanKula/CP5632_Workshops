
word_string = str(input("Enter the a phrase: ")).split()
counter = 0
words_dicts = {}
for word in word_string:
    counter = word_string.count(word)
    words_dicts = {word:counter}
print(words_dicts)

#print(word_count)

# print(words_lists)
#
#     word_count = word_string.count(words)

#for word in words_lists:
#    print("{} : {}".format(word[0],word[1]))

