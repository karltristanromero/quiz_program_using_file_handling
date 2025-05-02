# Main Program

import os
import time
from art import text2art

def manage_files():

    clear_screen()
    ascii_art("Welcome!")

    while True:
        print("""a. Create/Add QnA to a file
b. Start a quiz
c. Show contents of file
d. Delete a specific QnA in a file
e. Exit program\n""")
        
        action = input("What do you want to do? (a/b/c/d/e): ")
        action = action.lower()

        if action == "a":
            quiz_maker()

        elif action == "b":
            file_path = get_file()

            try:
                start_quiz(file_path)
            except FileNotFoundError:
                file_not_exists_warning()
                continue

        elif action == "c":
            file_path = get_file()
            show_contents(file_path)

        elif action == "d":
            qna_deleter()

        elif action == "e":
            break

        else:
            print("Your input is invalid!")
            time.sleep(1.25)

def prompt_validation(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Your input is not valid!")

def prompt_question():
    question = prompt_validation("Enter a question entry: ")
    print("") 
    return question

def prompt_choices():
    choices_list = []
    for i in range(4):
        letter = chr(ord("a") + i)
        choice = prompt_validation(f"Enter an answer for {letter}: ")
        choices_list.append(choice)
    
    choices_list = " | ".join(choices_list)

    return choices_list

def prompt_correct_answer():
    while True:
        letter = "Enter the letter of the correct answer: "
        correct_ans = prompt_validation(f"\n{letter}")
        correct_ans = correct_ans.lower()

        if correct_ans in ["a", "b", "c", "d"]:
            return correct_ans
        
def display_answers(qna_list):


    while True:
        response = prompt_validation("Do you want to see the answers? (y/n): ")
        response = response.lower()

        if response in ["y", "n"]:
            break
        else:
            print("Your input is invalid!")

    if response == "y":
        clear_screen()
        ascii_art("Answers\n")

        for number, qna in enumerate(qna_list):
            display = f"{number+1}. {display_questions(qna)}{qna[7]}\n"
            print(display)    
            input("Press any key to continue...")
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
        qna_list.append(f"Correct✅! The answer is: {qna_list[6]}")
    else:
        answer = f"Incorrect❌! It was {answer}!"
        qna_list.append(answer)

    return qna_list, total_score

def continue_or_end():
    while True:
        response = prompt_validation("\nDo you want to continue? (y/n): ")
        response = response.lower()

        if response in ["y", "n"]:
            break
        else:
            print("Your input is invalid!")
        
    return response

def clear_screen(): 
    os.system('cls' if os.name == 'nt' else 'clear')       

def ascii_art(text: str):
    print(text2art(text))   

def file_not_exists_warning():
    ascii_art("File does not exist.")
    time.sleep(3)
    clear_screen()

def file_empty_warning(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        
    if content.strip() == "":
        clear_screen()
        ascii_art("File is empty")
        time.sleep(3)
        return

def rename_file(file_name):
    file_name = file_name.strip().lower()
    file_name = file_name.replace(" ", "_") 

    return file_name

def show_contents(ask_file):
    ask_file = rename_file(ask_file)

    while True:    
        clear_screen()
        try:
            with open(f"{ask_file}", "r") as file:
                print(file.read())

                action = input("Press any key to continue/exit: ")

                if action or action == "":
                    break

        except FileNotFoundError:
            file_not_exists_warning()
            break

def create_dir():
    directory = os.getcwd()
    subdir_name = "questionnaire_inventory"

    dir_path = os.path.join(directory, subdir_name)
    os.makedirs(dir_path, exist_ok=True)
    
    return dir_path

def get_file():
    ask_file = prompt_validation("What is the name of the txt file? ")
    file_name = rename_file(ask_file)

    get_dir = create_dir()
    full_path = os.path.join(get_dir, file_name)
    file_path = f"{full_path}.txt"

    return file_path

def quiz_maker():

    clear_screen()
    ascii_art("Quiz Maker")

    full_path = get_file()

    with open(full_path, "a+") as questionnaire:
        questionnaire.seek(0)

        lines = questionnaire.readlines()

        if not lines:
            qna_index = 1  

        else:
            last_line = lines[-1]
            index_part = last_line.split(".")[0]

            qna_index = int(index_part) + 1

        while True:
            clear_screen()
            ascii_art("Creation Camp")

            # Create the questionnaire
            question = prompt_question()
            choices = prompt_choices()
            correct_ans = prompt_correct_answer()

            # Write into the created/opened file and format
            entry = f"{qna_index}. | {question} | {choices} | {correct_ans}"
            questionnaire.write(entry + "\n")

            # Ask if user still wants to create more questions or not
            if continue_or_end() == "n":
                print("Exiting the program...")
                clear_screen()
                break
            
            qna_index += 1

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

        continue_or_end()

def qna_deleter():
    
    clear_screen()
    ascii_art("QnA Deleter")

    questionnaire_path = get_file()
    file_empty_warning(questionnaire_path)
        
    try:
        file = open(questionnaire_path, "r")
        file.close()
    except FileNotFoundError:
        clear_screen()
        file_not_exists_warning()
        return
    
    with open(questionnaire_path, "r") as file:
        lines = file.readlines()

        ask = f"Want to check the file'sd contents first (y/n)? "
        action = prompt_validation(ask)
        action = action.lower()

        if action == "y":
            show_contents(questionnaire_path)

        while True:
            req_index = prompt_validation("Enter index of QnA for deletion: ")

            updated_lines = []
            found = False

            for line in lines:
                parts = line.split(".")[0]

                if parts.strip() == req_index.strip():
                    found = True
                else:
                    updated_lines.append(line)

            if found:
                with open(questionnaire_path, "w") as updated_file:
                    updated_file.writelines(updated_lines)
                    print("The line has now been deleted.")
                    time.sleep(3)
                    break
            else:
                print("Index given does not exist.")

if __name__ == "__main__":
    manage_files()