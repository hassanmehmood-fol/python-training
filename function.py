def greet():
    print("Hello how are you?")


greet()


def greeting(name):
    print("Hello", name)


greeting("Hassan")


def add(num1, num2):
    return num1 + num2


print(add(2, 3))


def even_check(number):
    result = number % 2 == 0
    return result


print(even_check(31))


def addn_num(*arg):
    print(arg)


addn_num(1, 2, 3, 4)


def info(**kwargs):
    print(kwargs)


info(name="Hassan", age=22, city="Lahore")


def create_user(**data):
    print(f"User created: {data}")


create_user(name="Hassan", email="a@b.com", role="admin")


def add_two(a, b):
    return a + b


print(add_two(3, 3))
