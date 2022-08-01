import csv
from helpers import *
from tkinter import *

def main():
    with open("word_list.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            Word(spelling=row["word"], meaning=row["meaning"])
    print(all_words)
    number_of_question = get_number_of_questions()

    quiz = Quiz()
    quiz.begin(number_of_question)



if __name__ == "__main__":
    main()
