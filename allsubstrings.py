def minion_game(string):
    # your code goes here
    vowel = 'aeiou'
    consonant = 'bcdfghjklmnpqrstvwxyz'
    length = len(string)
    consonantsubstring = []
    vowelsubstring = []
    result = []
    for i in string:
        if i in consonant:
            consonantsubstring = [a[i:j + 1] for i in range(length) for j in range(i, length)]
        else:
            vowelsubstring = [a[i:j + 1] for i in range(length) for j in range(i, length)]
    stuartscore = [[x,consonantsubstring.count(x)] for x in set(consonantsubstring)]
    kevinscore = [[x,vowelsubstring.count(x)] for x in set(vowelsubstring)]

print(stuartscore)