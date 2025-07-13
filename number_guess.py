import random

is_playing = True

number = random.randint(0, 100)
attempt = 5

while is_playing:

    ask = input("Please enter the number between 0 and 100: ")
    e_num = int(ask)

    if e_num == number:
        print("Right number")
        break
    elif e_num > number:
        print("Pick Lower!")
        attempt -= 1
        print("There is left only", attempt)
    elif e_num < number:
        print("Pick Higher!")
        attempt -= 1
        print("There is left only", attempt)

    if attempt == 0:
        print("Game is over")
        print(f"The mystic number was {number}")
        break
