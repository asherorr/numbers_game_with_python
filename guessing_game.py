
import random
import time
import sys

user_selection = []

guesses = []

num_guesses_to_get_right = []

num_guesses = []

random_numbers_generated = []

def welcome_message():
    opening_message = print("""
    -----------------------------------
    WELCOME TO THE NUMBER GUESSING GAME!
    -----------------------------------
    """)

    second_opening_message = "LET'S GET READY TO RUMBLE!!!!"
    moving_message = second_opening_message.split()
    for word in moving_message:
        print(word)
        time.sleep(.5)

def start_game():
    random_num = random.randint(1, 10)
    while True:
        try:
            try:
                user_selection = int(input("Pick any number from {}. ".format("1-10")))
                guesses.append(user_selection)
            except ValueError:
                raise ValueError("Please enter only a number.")
            if user_selection < 1 or user_selection > 10:
                raise ValueError("Please only enter a number within 1 or 10.")
        except ValueError as err:
            print("Oh no! We ran into an issue. {}".format(err))
        else:
            if user_selection != random_num:
                print("\nThat is not the right number! ")
                if user_selection > random_num:
                    print("It's lower. Pick another number")
                elif user_selection < random_num:
                    print("It's higher. Pick another number.")
            if user_selection == random_num:
                num_guesses_to_get_right.append(len(guesses))
                print("\nYou got it! Congratulations! It took you {} guesses to get the right number.".format(len(guesses)))
                guesses.clear()
                option_to_play_again = input("\nWould you like to play again? (Yes/No) ")
                if option_to_play_again.lower() == "yes":
                    print("Current high score: {}.".format(min(num_guesses_to_get_right)))
                    random_numbers_generated.append(random_num)
                    while True:
                        new_random_num = random.randrange(1, 10)
                        if new_random_num not in random_numbers_generated:
                            break
                        else:
                            continue
                    random_num = new_random_num
                    random_numbers_generated.clear()
                    continue
                else:
                    break

def ending_message():
    print("Thanks for playing! The program will close now.")
    sys.exit

welcome_message()
start_game()
ending_message()
