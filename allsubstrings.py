def stringstartingconsonant(a):
    vowel = 'aeiou'
    consonant = 'bcdfghjklmnpqrstvwxyz'
    length = len(a)
    result = []
    "below comments shows how to do this with a list comprehension, faster and cleaner"
    if a[0] in consonant:
        result = [a[i:j + 1] for i in range(length) for j in range(i, length)]
    return result

    if a[0] in consonant:
        for i in range(length):
            for j in range(i,length):
                result.append(a[i:j+1])
    else:
        for i in range(length):
            for j in range(i,length):
                result.append(a[i:j+1])

    return result

print(stringstartingconsonant('banana'))