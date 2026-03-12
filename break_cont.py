i = 0
while i <= 20:
    if i % 2 == 0:
        i += 1
        continue
    if i == 17:
        break
    print(i)
    i += 1