from itertools import product

words = [''.join(word) for word in product('ВОЗДУХ', repeat=5)]
k = 0
for word in words:
    temp = word.replace('О', '0').replace('У', '0').replace('В', '1').replace('Х', '1')
    if temp.count('0') == 1 and '01' not in temp and '10' not in temp:
        k += 1
print(k)
