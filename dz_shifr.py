def shifr(my_text, my_key): 
    my_text = my_text.split(" ")
    res = []
    x = len(my_text)
    if abs(my_key) > x: 
        my_key = my_key % x 
    else: 
        pass
    if my_key == abs(my_key):
        
        res.append(my_text[x-my_key:])
        res.append(my_text[:x-my_key])
        # for i in range(-1, len(my_text)): 
        #     if i >= len(my_text) - my_key:
        #         my_text[i] = my_text[len(my_text) - i] 
        #     elif i < len(my_text) - my_key:
        #         my_text[i] = my_text[len(my_text) - (i + my_key)]          
    else:
        my_key = abs(my_key)
        my_key = my_key % x
        res.append(my_text[0 + my_key:])
        res.append(my_text[:0 + my_key])
    res2 = []
    res2.append(res[0])
    res2.append(res[1])

    str1 = ""
    for i in res2[0]:
        str1 += str(i)
    for i in res2[1]:
        str1 += str(i)
    return str1
r = input("Enter text: ")
y = int(input("Enter key: "))

print(shifr(r, y))