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

            display_questions(parts)

            guess = input("Enter the letter of your answer (a/b/c/d): ")
            point, correct_ans = validate_answer(guess, parts[6])

            parts, score = score_keeper(parts, score, point, correct_ans)
            questionnaire.append(parts)

        print(f"Your score is: {score}")

        for number, qna in enumerate(questionnaire):
            display = f" {number+1}. {display_questions(qna)} {qna[7]}"
            print(display)


def display_questions(qna):
    print(qna[1])

    for i in range(4):
        print(f"{chr(97+i)}. {qna[2+i]}")

def validate_answer(answer, correct_answer):
    correct_answer = correct_answer.split()[0]

    if answer == correct_answer:
        return 1, correct_answer
    else:
        return 0, correct_answer

def score_keeper(qna_list, total_score, value_pt, answer):
    if value_pt == 1:
        total_score += value_pt
        qna_list.append(" | Correct✅!")
    else:
        answer = f" | Incorrect❌! It was {answer}!"
        qna_list.append(answer)

    return qna_list, total_score
    

def display_answers():
    pass



questionnaire = file_finder("science.txt")
start_quiz(questionnaire)