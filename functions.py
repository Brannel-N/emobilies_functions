def myfunction():
    print("Hello World, this is my first code")

    # function with parameters
    def students(name, age, gender):
        print(f"{name} is {age} years old and gender is {gender}")

    students("Gessy", "18", "F")
    students("Bran", "25", "M")

    # function with return values
    def add_numbers(a, b):
        return a + b

    result = add_numbers(10, 35)
    print(result)

# call the main function
myfunction()
