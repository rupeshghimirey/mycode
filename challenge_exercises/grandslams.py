# Guessing the total number of grandslams

# choose the players below that you want to guess for
#>Novak Djokovic
#Roger Federer
# Rafael Nadal

isRunning = True;


while isRunning:
    try:
        print("****Guess the total number of grandslams won by tennis player****\n")
        print("Choose one of the players below. Enter (A or B or C)\n ")
        user_input = input("A) Rafael Nadal\nB) Roger Federer \nC) Novak Djokovic\n").upper()

        if user_input == 'A':
            number_of_guess = 0;
            while number_of_guess < 4:
                number_of_guess +=1;
                answer = input("How many grandslams have Nadal won? (hint in between 15-30):");
                if(answer == "21"):
                    print("Correct\n")
                    isRunning = False
                    number_of_guess = 5;
                elif answer != '21':
                    if number_of_guess == 4:
                        print("Incorrect! The correct answer is 23!")
                    else:
                        print("Try Again!")
                    
        elif user_input == 'B':
            answer = input("How many grandslams have Federer won? (hint in between 10-25)");
            if(answer == "20"):
                print("Correct\n")
                isRunning = False
    except Exception as err:
    
        print("We did not anticipate that:", err)

print("Thank you for participating!")
