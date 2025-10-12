from collections import Counter, defaultdict, OrderedDict

sentence = 'Der Wolf heulte lauf, asl er vom Jäger getroffen wurde !'
# counts each given value
count = Counter(sentence)
print(count)

print('\n')
# Advanced Dictionary with default value if the value doesn't exists
dictionary = defaultdict(
    lambda: 'does not exist',
    {
        'a': 1,
        'b': 2
    }
)
# They key c does not exist ---> get message back
print(dictionary['c'])

dictionary_one = OrderedDict(
    {
        'a': 1,
        'b': 2
    }
)

dictionary_two = OrderedDict(
    {
        'b': 1,
        'a': 2
    }
)
# Checks same values and same order!
print(dictionary_one == dictionary_two)

dictionary_1 = dict()
dictionary_1['a'] = 1
dictionary_1['b'] = 2

dictionary_2 = dict()
dictionary_2['b'] = 2
dictionary_2['a'] = 1

# Checks only are the same values given or not!
print(dictionary_1 == dictionary_2)
