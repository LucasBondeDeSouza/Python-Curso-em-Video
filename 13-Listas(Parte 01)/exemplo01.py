num = [2, 5, 9, 1]
num[2] = 3 # -> [2, 5, 3, 1]

num.append(7) # -> [2, 5, 3, 1, 7]

num.sort() # -> [1, 2, 3, 5, 7]

num.sort(reverse=True) # -> [7, 5, 3, 2, 1]

num.insert(2, 2) # -> [7, 5, 2, 3, 2, 1]

# num.pop() # -> [7, 5, 0, 3, 2]

if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')

print(num)
print(f'Essa lista tem {len(num)} elementos.')