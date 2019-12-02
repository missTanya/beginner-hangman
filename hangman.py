
import random
import sys

class game_methods():
    """
    This will list all the methods used in the main file.
    This class contains triple loops divided into multiple functions to break out of nested loops.
    """

#This will ask the user to guess a letter
    def guess_letter(generated_rand_num, attempts, list_tracker):

        if attempts>0:
            guess = input("Guess a letter that could be in the mystery word: ")
            if (generated_rand_num.find(guess.lower())) > 0:
                list_tracker.append(guess)
                print("Congrats! Your letter is in the word!\nHere is a list of correctly guessed answer: ", sep= '\t')
                print(list_tracker)
                attempts -= 1
                return attempts, list_tracker
            else:
                print("Sorry, that is not in the mystery word.\n")
                attempts -= 1
                return attempts, list_tracker
        else:
            return game_methods.go_exit()

#This will exit program when user ran out of attempts
    def go_exit(generated_rand_num):
        print("Sorry, you have ran out of attempts :(\nThe mystery word is {}".format(str(generated_rand_num).title()))
        sys.exit(1)

#This will ask the user if he/she wants to guess the word
    def guess_word(generated_rand_num, name, attempts):
        mystery_word = input("What is the mystery word? ")
        if (generated_rand_num == mystery_word.lower()):
            return game_methods.say_goodbye(name)
        else:
            return game_methods.guess_letter(generated_rand_num, attempts)

#This will execute a method to end the game
    def say_goodbye(name):
        print("\n\nCongrats {}! You have guessed the mystery word! ".format(name.upper()))
        sys.exit(1)

#This will run the game
    def run_hangman(list, name):
        attempts = 6
        rand_num = random.choice(list)
       # print(rand_num)
        list_tracker = []
        print("Hint:\tThe mystery word has {} letters".format(len(rand_num)))
        print('\n')
        print(game_methods.run_loop(attempts,rand_num, name,list_tracker))

    def run_loop(num_of_attempts, generated_rand_num, name, list_tracker):
        while num_of_attempts>0:

            if (num_of_attempts<6):
                answer = input("Would you like to guess the word? [Y/N]")
                if answer.upper() == "Y":
                    print(game_methods.guess_word(generated_rand_num, name, num_of_attempts))
                else:
                    num_of_attempts, list_tracker = game_methods.guess_letter(generated_rand_num, num_of_attempts, list_tracker)

            else:
                num_of_attempts, list_tracker  = game_methods.guess_letter(generated_rand_num, num_of_attempts, list_tracker)

        else:
            game_methods.go_exit(generated_rand_num)


class main():
    """
    This program will simulate a HANGMAN GAME.

    The user will be given six (6) attempts to guess a letter in a randomly generated word.
    The user program will exit if the user successfully guessed the word before reaching the max attempts or if
    the user reached its maximum attempts.
    """
    name = input("Hello! Let's play HANGMAN ^_^\nBefore starting, please input your name: ")
    choice = input("Hello {}! You will be given six(6) attempts to guess the random word\nChoose theme\n(a) color\n(b) country\n".format(name.title()))
    color = [
        'red', 'blue', 'green', 'yellow', 'black', 'gray', 'pink', 'violet', 'white'
    ]

    country = [
        'Philippines', 'Australia', 'Japan', 'China', 'Singapore', 'Poland', 'Ireland', 'Romania', 'Russia', 'Indonesia',
        'Thailand', 'Neatherlands', 'America', 'Spain'
    ]

    game_choices = []
    if (choice == "A".lower()):
        game_choices = color.copy()
    else:
        game_choices = country.copy()

    print(game_methods.run_hangman(game_choices, name))




if __name__ == "__main__":
    main()