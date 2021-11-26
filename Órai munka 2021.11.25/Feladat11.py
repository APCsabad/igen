xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
j = 8
for i in range(8):
    print(xs[j])
    j -= 1

for i in range(8):
    print(xs[i] ,pow(xs[i], 2))

osszeg = 0

for i in range(8):
    osszeg += xs[i]

print(osszeg)

for i in range(7):
    for j in range(8):
        print(xs[i] * xs[j])


