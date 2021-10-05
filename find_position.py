import re
def alphabet_position(text):
    new = list(text)
    find = []
    for i in new:
        find.append(ord(i))
    #print(find)
    alpha = 64
    capital_letter = []
    for i in range(0,26):
        alpha = alpha +1
        capital_letter.append(alpha)
    #print(capital_letter)
    beta = 96
    small_letter = []
    for i in range(0,26):
        beta = beta +1
        small_letter.append(beta)
    #print(small_letter)
    final = []
    for i in find:
        for j in small_letter:
            if i == j:
                final.append(small_letter.index(j)+1)
        for k in capital_letter:
            if i == k:
                final.append(capital_letter.index(k)+1)
    ans = str(final)
    a = ans.replace('[',"")
    b = a.replace(']',"")
    c = b.replace(",","")
    return c