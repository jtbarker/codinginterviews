
def perm(n, i):
    "a general purpose reusable function for generating all permutations of an array n recursively"
    if i == len(n) - 1:
        print(n)
    else:
        for j in range(i,len(n)):
            n[i], n[j] = n[j], n[i]
            perm(n,i + 1)
            n[i], n[j] = n[j], n[i]
print(perm([1,2,3],0))