from quiz_program import prompt_validation, continue_or_end, ascii_art

def file_finder(file_name):
    import os

    basedir = os.path.dirname(os.path.abspath(__file__))
    categorization_file = os.path.join(basedir, file_name)

    return categorization_file

def start_quiz(file):

    with open(file, "r") as questionnaire:
        list_of_qna = questionnaire.readlines()

        score = 0
        questionnaire = []
        for qna in list_of_qna:
            parts = qna.split(" | ")   

            print(display_questions(parts))

            guess = input("Enter the letter of your answer (a/b/c/d): ")
            point, correct_ans = validate_answer(guess, parts[6])

            parts, score = score_keeper(parts, score, point, correct_ans)
            questionnaire.append(parts)

        ascii_art(f"Your score is: {score}")
        display_answers(questionnaire)

def display_answers(qna_list):
    response = prompt_validation("Do you want to see the answers? (y/n): ")

    if response.lower() == "y":
        for number, qna in enumerate(qna_list):
            display = f"{number+1}. {display_questions(qna)}{qna[7]}\n"
            print(display)    
    elif response == "n":
        continue_or_end()


def display_questions(qna):
    question_str = qna[1] + "\n"

    for i in range(4):
        letter = chr(ord("a") + i)
        question_str += f"{letter}) {qna[i+2]}\n"

    return question_str

def validate_answer(answer, correct_answer):
    correct_answer = correct_answer.split()[0]

    if answer == correct_answer:
        return 1, correct_answer
    else:
        return 0, correct_answer

def score_keeper(qna_list, total_score, value_pt, answer):
    if value_pt == 1:
        total_score += value_pt
        qna_list.append("Correct✅!")
    else:
        answer = f"Incorrect❌! It was {answer}!"
        qna_list.append(answer)

    return qna_list, total_score
    




questionnaire = file_finder("science.txt")
start_quiz(questionnaire)