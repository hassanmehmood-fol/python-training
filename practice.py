a = 10
b = 5
print(a > b)

age = 90
if age > 100:
    print("Hello this is not above 100")
else:
    print("This is below 100")

for i in range(5):
    print(i)

fruits = ["Apple", "Mango", "Banana"]
for fruit in fruits:
    print(fruit)

for ch in "Python":
    print(ch)

for i in range(10):
    print(i)
    if i % 2 == 0:
        print("this is even")
    else:
        print("This is not even")

my_list = [1, 2, 3, 4]
sum = 0
dic = {"namee": "Hassan", "agee": 29}

for key, value in dic.items():
    print(key, "->", value)

i = 1
while i <= 5:
    print(i)
    i += 1


x = 0
while x < 5:
    print("This value is lesser than", x, 5)
    x += 1
else:
    print("This value is not lesser than", x)


x = [1, 2, 3]
for item in x:
    if item == 1:
        continue
    print(item)


result = int(input("Enter the number: "))
if result >= 5:
    print("This is greater or equal than 5")
else:
    print("This is not greater or equal than 5, may be less than 5")

names = ["hassan", "zain", "luqman", "hassan"]
filtered = [name for name in names if name == "hassan"]
print(filtered)

names.pop()
print(names)

names.pop()
print(names)
