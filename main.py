# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random


def main():
    categories = ["Actors", "Countries", "Movies", "TV Shows", "Board Games", "Breakfast Foods", "Jobs",
                  "Things you find in the kitchen", "Things with Wheels", "Musical Instruments", "Sea Creatures",
                  "Books",
                  "Languages", "Things in an office", "Things made of wood",
                  "Animals", "Types of Candy", "Clothing", "Beverages", "Things to take to the beach",
                  "Something at a picnic", "Athlete", "School Supplies", "Things you save up to buy",
                  "Things that are cold"]

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "w"]

    def random_category_generator():
        random_category = random.randint(0, len(categories) - 1)
        print(categories[random_category])

    def random_letter_generator():
        random_letter = random.randint(0, len(letters) - 1)
        print("Your Letter is", letters[random_letter])
        return str(letters[random_letter])

    print("Welcome to Scattergories! This game will generate a random letter and multiple categories. Provide an \n"
          "answer to each of the categories with a word starting with your given letter. If you do, you will earn a \n"
          "point. If you cannot come up with a word, enter \"x,\" and you will not earn any points.After each round,\n"
          " the program will print how many points you earned that round followed by your total score.\n"
          "Have fun!")
    random_letter = random_letter_generator()

    global score
    score = 0

    def round_one():
        def question():
            random_category_generator()
            print("your answer:")

        def user_list():
            question()
            user_ask = input().lower()
            return list(user_ask)

        def check_word(overall_list, random_letter,):
            global score
            first_element = overall_list[0]
            if first_element == random_letter:
                print("1 Point")
                score += 1
                print(score)
                return score

            else:
                print("0 Points")
                score += 0
                print(score)
                return score

        overall_list = user_list()
        check_word(overall_list, random_letter,)

    round_one()
    round_one()
    round_one()
    round_one()
    round_one()


main()


