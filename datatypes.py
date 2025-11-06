fruits = ["apple", "banana", "cherry"]
print(fruits[-1])


student = {"name": "John", "age": 20, "city": "New York"}

print(student)
print(student.items())
for key, value in student.items():
    print(key, "=>", value)


x = [1, 2, 3, 4, 5]
print(type(x))
y = ("apple", "banana", "cherry")
print(type(y))
name = "Hassan"
print(type(name))
print(name)
print(name[0])
print(name[0:4])
print(name[0:5])
print(name[0:4])
print(name.upper())
print(name.lower())
print(name.replace("H", "J"))
print(name.split(" "))
print(name.split("s"))
print(name.split("a"))
print(len(name))
name = "Ali"
age = 21

print(f"My name is {name} and I am {age} years old.")

print(name[1])
sample_text = "Hello, World!"

print(sample_text[-8])
print(sample_text[::-1])
name1 = "assan"
"p" + name1
print(name1)
name2 = "Hassan Mehmood"
print("my name is {}".format(name2))
mylist = [1, 2, 3, 4, 5, 6]
print(mylist)
data = [1, 2, [3, 4, 5], 6]
print(data)


student = {"name": ["John", "Hassan", "Zain"], "age": 20, "city": "New York"}

mylist = student["name"]
print(student["name"])
print(mylist)
my_tuple = (1, 2, 3, 4, 5, 6)
num = {
    1,
    2,
    3,
    4,
    5,
    5,
    6,
    11,
    23,
    23,
    23,
}
print(num)
sett = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
sett.add(11)
print(sett)
if name == "Hassan":
    print("name is Hassan")
else:
    print("name is not Hassan")


print(type(True))
if 1 > 2:
    print(True)
else:
    print(False)

print(set([1, 2, 2, 1, 2]))


print(my_tuple)
try:
    import pandas as pd  # pyright: ignore[reportMissingImports]
except ModuleNotFoundError:
    print("Missing dependency 'pandas'. Install with: pip install pandas openpyxl")
    pd = None

file_path = r"C:\Users\Admin\Desktop\Book1.xlsx"

if pd is not None:
    try:
        df = pd.read_excel(file_path)
        print("Old Data:")
        print(df)

        new_row = {"Name": "Ali", "Age": 25, "City": "Lahore"}

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        df.to_excel(file_path, index=False)
        print("\n✅ Row added successfully!")

        print("\nUpdated Data:")
        print(df)

    except FileNotFoundError:
        print(f"❌ Excel file not found at: {file_path}")
    except Exception as e:
        print(f"❌ Failed to read/write Excel file: {e}")

file_name = "notes.txt"

try:
    file = open(file_name, "w")
    if not file.closed:
        print("✅ File opened successfully in write mode!")
    file.write("Hello! This is first line.\n")
    file.write("Learning Python file handling.\n")
    file.close()
    print("✅ Data written & file closed!")
except Exception as e:
    print("❌ Error opening file in write mode:", e)


try:
    file = open(file_name, "a")
    if not file.closed:
        print("\n✅ File opened successfully in append mode!")
    file.write("This line is appended.\n")
    file.close()
    print("✅ Append complete & file closed!")
except Exception as e:
    print("❌ Error in append mode:", e)


try:
    print("\n📖 Reading file...")
    with open(file_name, "r") as file:
        if not file.closed:
            print("✅ File opened successfully in read mode!")
        content = file.read()
        print("\n----- FILE CONTENT -----")
        print(content)
        print("------------------------")
except FileNotFoundError:
    print("❌ File not found!")
except Exception as e:
    print("❌ Error reading file:", e)
