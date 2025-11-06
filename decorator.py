def my_decorator(func):
    def wrapper():
        print("Hello i am start")
        result = func()
        print("Hello i am end")
        return result

    return wrapper


def new_decorator(func):
    def wrapper(*args):
        print("Hello this is start of new decorator")
        result = func(*args)
        print("Helo this is new deocorator end")
        return result

    return wrapper


@my_decorator
def greet():
    print("Hello Hassan")


@new_decorator
def sum(a, b):
    print(a + b)


greet()
sum(4, 8)


def required_login(func):
    def wrapper(name):
        if name == "Hassan":
            print("access grandted , welcome to dasbboard")
            return func(name)
        else:
            print("Access denied")

    return wrapper


@required_login
def view_dashboard(name):
    print(f"Welcome to dashboard , {name}")


view_dashboard("Hassan")
view_dashboard("Zain")
