import random

f = open('activation_code.txt', 'w')
s = set([])
length = 12
num = 200
a = [0, 0, 0]
while num != 0:
    num -= 1
    str = ''
    for i in range(0, length):
        a[0] = random.randint(48, 57)
        a[1] = random.randint(97, 122)
        a[2] = random.randint(65, 90)
        chose = random.randint(0, 2)
        str += chr(a[chose])
    str += '\n'
    if str in s:
        num += 1
    else:
        s.add(str)
for it in s:
    f.write(it)
f.close()
