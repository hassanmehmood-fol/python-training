# fruits = ["apple", "banana", "cherry"]
# print(fruits[-1]);


from ntpath import samefile


student={
    "name": "John",
    "age": 20,
    "city": "New York"
}

# print(student);

# print(student.items());


for key, value in student.items():
    print(key, "=>", value)



x=[1,2,3,4,5]
print(type(x));

y=("apple", "banana", "cherry");
print(type(y));

name ="Hassan";
print(type(name));
print(name);

print(name[0]);
print(name[0:4]);
print(name[0:5]);
print(name[0:4]);

print(name.upper());
print(name.lower());
print(name.replace("H", "J"));
print(name.split(" "));
print(name.split("s"));
print(name.split("a"));
print(len(name));

name = "Ali"
age = 21

print(f"My name is {name} and I am {age} years old.")

print(name[1]); 

sample_text = "Hello, World!"

print(sample_text[-8]);

print(sample_text[::-1]);


name1="assan";
'p'+name1;
print(name1);

name2="Hassan Mehmood";
print("my name is {}".format(name2));




mylist=[1,2,3,4,5,6];
print(mylist);

  
data = [1, 2, [3, 4, 5], 6]
print(data)


student ={
    "name": ["John", "Hassan" , "Zain"],
    "age": 20,
    "city": "New York"
}

mylist =student['name'];

print(student["name"]);

print(mylist);

tuple = (1,2,3,4,5,6);

num={1,2,3,4,5,5,6,11,23,23,23,};  
print(num);


sett={1,2,3,4,5,6,7,8,9,10};
sett.add(11);
print(set);

name="Hassan";
if name is "Hassan":
    print("name is Hassan");
else:
    print("name is not Hassan");


print(type(True));

if 1 > 2:
    print(True)
else:
    print(False)

print(set([1,2,2,1,2]))



# print(tuple);

try:
    import pandas as pd;  # pyright: ignore[reportMissingImports]
except ModuleNotFoundError:
    print("Missing dependency 'pandas'. Install with: pip install pandas openpyxl")
    pd = None

if pd is not None:
    try:
        df = pd.read_excel(r"C:\Users\Admin\Desktop\Book1.xlsx")
        print(df)
    except FileNotFoundError:
        print("Excel file not found at the specified path: C:\\Users\\Admin\\Desktop\\Book1.xlsx")
    except Exception as e:
        print(f"Failed to read Excel file: {e}")

