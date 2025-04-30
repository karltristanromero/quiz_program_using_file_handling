def file_finder(file_name):
    import os

    basedir = os.path.dirname(os.path.abspath(__file__))
    categorization_file = os.path.join(basedir, file_name)

    return categorization_file

def start_quiz(file):

    with open(file, "r") as questionnaire:
        list_of_qna = questionnaire.readlines()

        score = 0
        for qna in list_of_qna:
            parts = qna.split(" | ")   

            ask_questions(parts) 
            guess = input("Enter the letter of your answer (a/b/c/d): ")
            point = validate_answer(guess, parts[5])
            score += point

def ask_questions(qna):
    print(qna[0])

    for i in range(4):
        print(f"{chr(97+i)}. {qna[1+i]}")

def validate_answer(answer, correct_answer):
    if answer == correct_answer:
        return 1
    else:
        return 0
    
questionnaire = file_finder("science.txt")
start_quiz(questionnaire)