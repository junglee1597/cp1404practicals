number = int(input("number: "))
for i in range(0, number):
    i = "*" * i
    print(i)

for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
