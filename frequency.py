def frequency(word):
    a={}

    for i in range(len(word)):
        if a.get(word[i],False) == False:
            a.update({word[i]:1})
        else:
            a[word[i]] +=1

    return a
print(frequency("hello"))