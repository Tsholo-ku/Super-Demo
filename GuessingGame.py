import random
import click

user_name = input("Enter your name: ")
print("Welcome " + user_name + "!")

lucky_num = random.randint(0, 5)
user_num = click.prompt("Guess the lucky number between 0 and 5: ", type=click.IntRange(0, 5))
print(user_num)

while True:
    counter = 1
    while int(user_num) != lucky_num:
        if int(user_num) < lucky_num:
            print("But it's too low!")
            print("Guess again...")
            user_num = click.prompt("Guess the lucky number between 0 and 5: ", type=click.IntRange(0, 5))
            print(user_num)
            counter += 1

        elif int(user_num) > lucky_num:
            print("But it's too high!")
            print("Guess again...")
            user_num = click.prompt("Guess the lucky number between 0 and 5: ", type=click.IntRange(0, 5))
            print(user_num)
            counter += 1
        else:
            print("Good job, you guessed right!")
            print("You guessed in " + str(counter) + " tries.")
        break

    print("Good job, you guessed right!")
    print("You guessed in " + str(counter) + " tries.")
    answer = input("Do you want to play again? ")

    resp1 = "yes"
    resp2 = "no"

    if answer == resp1:
        print("Yay, Let's play again!")
        user_num = click.prompt("Guess the lucky number between 0 and 5: ", type=click.IntRange(0, 5))
        print(user_num)
        counter += 1
    else:
        print("Sad to see you go :-( ")
        print("Thank you for playing.")
        print("Goodbye "+ user_name+"!")
        break


