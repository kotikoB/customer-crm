# concatenate.py
def concatenate(**kwargs):
    result = " "
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += f" {arg}"
    return result


    # for arg in kwargs.keys():
    #     result += f" {arg}"
    # return result
print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))


# decorator function
def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def greet_bob(greeter_func):
    return greeter_func("Bob")


print(greet_bob(say_hello))


def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()


parent()
