# euler 1
list35 = []
for i in range(0, 1000):
    if i % 3 == 0:
        list35.append(i)
    elif i % 5 == 0:
        list35.append(i)

print(sum(list35))
