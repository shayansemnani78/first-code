import random
secret_number = random.randint(1, 100)

while True:
    x = int(input("pls enter your number"))
    if x > secret_number:
       print("bigger")

    elif x < secret_number :
        print("lower")
    elif x == secret_number:
        print("correct answer")
        break

