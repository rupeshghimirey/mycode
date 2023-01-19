#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import numpy as np

URL= "https://opentdb.com/api.php?amount=3&category=21&difficulty=easy&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()

    results_array= data.get("results")

    for result in results_array:
        answers_array = []

        answers_array.append(result['correct_answer'])
        answers_array.append(result['incorrect_answers'][0])
        answers_array.append(result['incorrect_answers'][1])
        answers_array.append(result['incorrect_answers'][2])
        
        # to compare the answers with shuffled answers
        print(answers_array)

        np.random.shuffle(answers_array)
        print(f"{result['question']} \nA){answers_array[0]}\nB){answers_array[1]}\nC){answers_array[2]}\nD){answers_array[3]}\n############################################") 

if __name__ == "__main__":
    main()

