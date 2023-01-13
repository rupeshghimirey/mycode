#!/usr/bin/python3
import pyfiglet

def main():
    # prints the string using figlet format
    header = pyfiglet.figlet_format("     TENNIS TRIVIA")
    print(header)

    # this loop keeps running until the user press D i.e exit
    isRunning = True
    while isRunning:
        print(
            "****Guess the total number of grandslams \nwon by following tennis players****\n")
        print("Choose one of the players below. Enter (A or B or C or D)\n ")
        user_input = input(
            "A) Rafael Nadal\nB) Roger Federer \nC) Novak Djokovic\nD) Exit\n").upper()

        number_of_guess = 0
        # this loop keeps running until user guesses for 4 times / correct answer
        while number_of_guess < 4:
            number_of_guess += 1
            if user_input == 'A':
                answer = input(
                    "\nHow many grandslams have Nadal won? (hint: between 15-25)\n")
                if(answer == "22"):
                    print("\nThat is Correct!!\n")
                    number_of_guess = 5
                elif answer != '22':
                    if number_of_guess == 4:
                        print("Incorrect! The correct answer is 22!")
                    else:
                        print("Please try again!")
            elif user_input == 'B':
                answer = input(
                    "\nHow many grandslams have Federer won? (hint: between 17-25)\n")
                if(answer == "20"):
                    print("\nThat is Correct!!!!\n")
                    number_of_guess = 5
                elif answer != '20':
                    if number_of_guess == 4:
                        print("Incorrect! The correct answer is 20!")
                    else:
                        print("Please try again!")

            elif user_input == 'C':
                answer = input(
                    "\nHow many grandslams have Djokovic won? (hint: between 18-25)\n")
                if(answer == "21"):
                    print("\nThat is Correct\n")
                    number_of_guess = 5
                elif answer != '21':
                    if number_of_guess == 4:
                        print("Incorrect! The correct answer is 21!")
                    else:
                        print("Please try Again!")

            elif user_input == 'D':
                number_of_guess = 5
                isRunning = False

    print("Thank you for participating!")


if __name__ == "__main__":
    main()

