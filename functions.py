def greet():
    print("holaaa")


def square(number):
    return number * number


def greet_person(name="arlenysss"):
    print(f"holaaa, {name}")


def add_numbers(*numbers):
    return sum(numbers)


def print_colors(**colors):
    for name, color in colors.items():
        print(f"{name} es loca con el {color}")


greet()  

number_to_square = 4
result = square(number_to_square) 
print(f"Square of {number_to_square} is {result}")

greet_person()  
greet_person("lynesysarle")

print(add_numbers(1, 2, 3)) 

print_colors(Arle="azulito", lunis="rojito")