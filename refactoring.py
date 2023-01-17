#!/usr/bin/env python3

def main():

    rabbit_sign =  [2011, 1999, 1987, 1975, 1963]
    rat_sign = [2020, 2008, 1996, 1984, 1972, 1960]
    tiger_sign = [2010, 1998, 1986, 1974, 1962]
    ox_sign = [2021, 2009, 1997, 1985, 1973, 1961]
    dragon_sign = [2012, 2000, 1988, 1976, 1964]
    snake_sign = [2013, 2001, 1989, 1977, 1965]
    horse_sign = [2014, 2002, 1990, 1978, 1966]
    sheep_sign = [2015, 2003, 1991, 1979, 1967]
    monkey_sign = [2016, 2004, 1992, 1980, 1968]
    rooster_sign = [2017, 2005, 1993, 1981, 1969]
    dog_sign = [2018, 2006, 1994, 1982, 1970]
    pig_sign = [2019, 2007, 1995, 1983, 1971]

    zodiac_dictionary = {
        "rabbit_sign" : "your zodiac sign is Rabbit, you are vigilant, witty, quick-minded, and ingenious.",
        "rat_sign" : "your zodiac sign is Rat, you are artistic, sociable, industrious, charming, and intelligent.",
        "tiger_sign" : "your zodiac sign is Tiger, you are courageous, enthusiastic, confident, charismatic, and a leader.",
        "ox_sign" : "your zodiac sign is Ox, you are strong, thorough, determined, loyal, and reliable.",
        "dragon_sign": "your zodiac sign is Dragon, you are talented, powerful, lucky, and successful.",
        "snake_sign": "your zodiac sign is Snake, you are wise, like to work alone, and determined.",
        "horse_sign" : "your zodiac sign is Horse, you are animated, active, and energetic.",
        "sheep_sign": "your zodiac sign is Sheep, you are creative, resilient, gentle, mild-mannered, and shy.",
        "monkey_sign":"your zodiac sign is Monkey, you are sharp, smart, curious, and mischievous.",
        "rooster_sign":"your zodiac sign is Rooster, you are hardworking, resourceful, courageous, and talented.",
        "dog_sign": "your zodiac sign is Dog, you are loyal, honest, cautious, and kind.",
        "pig_sign":"your zodiac sign is Pig, you are a symbol of wealth, honesty, and practicality."
    }

    usr_name = input("Please enter your name:\n>") 
    usr_name = usr_name.title()
    usr_date = int(input("Please enter your birth year in YYYY format, e.g 2010:\n>"))
            
    if usr_date in rabbit_sign:
        print(f"{usr_name} {zodiac_dictionary['rabbit_sign']}")
    elif usr_date in rat_sign:
        print(f"{usr_name} {zodiac_dictionary['rat_sign']}")
    elif usr_date in tiger_sign:
        print(f"{usr_name} {zodiac_dictionary['tiger_sign']}")
    elif usr_date in ox_sign:
        print(f"{usr_name} {zodiac_dictionary['ox_sign']}")
    elif usr_date in dragon_sign:    
        print(f"{usr_name} {zodiac_dictionary['dragon_sign']}")
    elif usr_date in snake_sign:
        print(f"{usr_name} {zodiac_dictionary['snake_sign']}")
    elif usr_date in horse_sign:
        print(f"{usr_name} {zodiac_dictionary['horse_sign']}")
    elif usr_date in sheep_sign:
        print(f"{usr_name} {zodiac_dictionary['sheep_sign']}")
    elif usr_date in monkey_sign:
        print(f"{usr_name} {zodiac_dictionary['monkey_sign']}")
    elif usr_date in rooster_sign:
        print(f"{usr_name} {zodiac_dictionary['rooster_sign']}")
    elif usr_date in dog_sign:
        print(f"{usr_name} {zodiac_dictionary['dog_sign']}")
    elif usr_date in pig_sign:
        print(f"{usr_name} {zodiac_dictionary['pig_sign']}")

        
        birth_predictor = {


        }


main()

