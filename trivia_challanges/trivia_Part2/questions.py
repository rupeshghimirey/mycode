#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import numpy as np

URL= "https://opentdb.com/api.php?amount=1&category=21&difficulty=easy&type=multiple"

def question_and_answer():

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

        answers_dict = {
            
        }

        # shuffle answers_array so that option A is always not correct
        np.random.shuffle(answers_array)

        question_answer = {
            "question" : f"{result['question']}",
            'A' : answers_array[0],
            'B' : answers_array[1],
            'C' : answers_array[2],
            'D' : answers_array[3],
            "answer" : f"{result['correct_answer']}"
        }

        return question_answer