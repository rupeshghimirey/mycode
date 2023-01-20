#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import numpy as np

URL= "https://opentdb.com/api.php?amount=5&category=21&difficulty=easy&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    results_array= data.get("results")

    count = 0;
    total = 0;
    for result in results_array:
        total += 1
        # array to hold all the answers so that it can be shuffled later
        answers_array = []
        answers_array.append(result['correct_answer'])
        answers_array.append(result['incorrect_answers'][0])
        answers_array.append(result['incorrect_answers'][1])
        answers_array.append(result['incorrect_answers'][2])

        # shuffle answers_array so that option A is always not correct
        np.random.shuffle(answers_array)

        # answer dictionary so that we can grab user input as a key and match the value of key with correct answer
        answers_dict = {
            'A' : answers_array[0],
            'B' : answers_array[1],
            'C' : answers_array[2],
            'D' : answers_array[3],
        }

        print(f"{result['question']}\nA){answers_array[0]}\nB){answers_array[1]}\nC){answers_array[2]}\nD){answers_array[3]}\n#######################################################################")

        user_input = input("Please choose the correct answer?Choose A or B or C or D \n>").upper()
        
        if(answers_dict[user_input] == result['correct_answer']):
            count += 1
            print(f"Correct Answer! Score: {count}/{total}\n")
        else: 
            print(f"InCorrect Answer! Score: {count}/{total}\n")
        

if __name__ == "__main__":
    main()

