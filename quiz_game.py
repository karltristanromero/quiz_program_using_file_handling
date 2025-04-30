def file_finder(file_name):
    import os

    basedir = os.path.dirname(os.path.abspath(__file__))
    categorization_file = os.path.join(basedir, file_name)

    return categorization_file

def start_quiz(file):

    with open(file, "r") as questionnaire:
        questions = questionnaire.readlines()
        print(questions)

        for question in questions:
            parts = question.split()

questionnaire = file_finder("science.txt")
start_quiz(questionnaire)