def numbers_to_letters(s):
    alphabet = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    swords = s.split('+')
    chars = []
    ans = ''
    for i in swords:
        chars.append(i.split())
    # return chars
    for i in range(len(chars)):
        for j in chars[i]:
            ans += chr(97-int(j))
    return ans

print(numbers_to_letters('20 5 19 20+4 15 13 5'))  #should return 'TEST DOME'


def numbers_to_letters(s):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = dict()
    for idx, c in enumerate(alphabet):
        d[idx + 1] = c
    print(d)

    swords = s.split('+')
    chars = []
    ans: str = ''
    print(swords)
    for i in swords:
        chars.append(i.split())

    print(chars)
    # return chars
    for i in range(len(chars)):
        for j in chars[i]:
            ans += d[int(j)]
            print(ans)
        ans += " "
    return ans


print(numbers_to_letters('20 5 19 20+4 15 13 5'))  # should return 'TEST DOME'