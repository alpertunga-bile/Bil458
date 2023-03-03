import random

if __name__ == "__main__":
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)

    while number1 == number2:
        number2 = random.randint(0, 100)

    print(f"Number1 : {number1} | Number2 : {number2}")

    print("Swapping ...")

    temp = number1
    number1 = number2
    number2 = temp

    print(f"Number1 : {number1} | Number2 : {number2}")