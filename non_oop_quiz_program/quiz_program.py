# Main Program
import os
import time
import random
from art import text2art

def manage_files():

    clear_screen()

    while True:
        ascii_art("Welcome!")
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
                if not start_quiz(file_path):
                    print("Exiting the program...")
                    time.sleep(3)
                    clear_screen()
                    return

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

def prompt_validation(prompt, valid_choices=None):
    while True:
        response = input(prompt).strip().lower()

        if not response:
            print("Your input is invalid!")
            continue

        if valid_choices:
            if response in valid_choices:
                return response
            print(f"Input is invalid! Enter only {','.join(valid_choices)}!")
        
        else:
            return response

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
    prompt_letter = "Enter the letter of the correct answer: "
    letter_choices = ["a", "b", "c", "d"]

    correct_ans = prompt_validation(f"\n{prompt_letter}", letter_choices)

    return correct_ans
    
def display_answers(qna_list):

    valid_response = ["y", "n"]
    prompt_check = "Do you want to see the answers? (y/n): "
    response = prompt_validation(prompt_check, valid_response)

    if response == "y":
        clear_screen()
        ascii_art("Answers\n")

        for number, qna in enumerate(qna_list):
            display = f"{number+1}. {display_questions(qna)}{qna[7]}\n"
            print(display)    
            input("Press any key to continue...\n")
        return

    elif response == "n":
        return
    
def display_questions(qna):
    clear_screen()
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
    valid_response = ["y", "n"]
    prompt_check = "Do you want to continue? (y/n): "
    response = prompt_validation(prompt_check, valid_response)
        
    return response

def clear_screen(): 
    os.system('cls' if os.name == 'nt' else 'clear')       

def ascii_art(text: str):
    print(text2art(text))   

def file_not_exists_warning():
    clear_screen()
    ascii_art("File does not exist.")
    time.sleep(3)
    clear_screen()

def file_empty_warning(file_path):
    try:   
        with open(file_path, "r") as file:
            content = file.read()
            
        if content.strip() == "":
            clear_screen()
            ascii_art("File is empty")
            time.sleep(3)
            clear_screen()
            return True
        
    except FileNotFoundError:
        file_not_exists_warning()
        return True

def rename_file(file_name):
    file_name = file_name.strip().lower()
    file_name = file_name.replace(" ", "_") 

    return file_name

def show_contents(file_path):
    file_path = rename_file(file_path)

    if file_empty_warning(file_path):
        return


    while True:    
        clear_screen()
        try:
            with open(f"{file_path}", "r") as file_qna:
                print(file_qna.read())

                action = input("Press any key to continue/exit: ")

                if action or action == "":
                    clear_screen()
                    return

        except FileNotFoundError:
            file_not_exists_warning()
            return

def create_dir():
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    subdir_name = "questionnaire_inventory"

    dir_path = os.path.join(parent_dir, subdir_name)
    os.makedirs(dir_path, exist_ok=True)
    
    return dir_path

def get_file():
    ask_file = prompt_validation("What is the name of the txt file? ")
    file_name = rename_file(ask_file)

    get_dir = create_dir()
    full_path = os.path.join(get_dir, file_name)

    if not full_path.endswith(".txt"):
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
                return
            
            qna_index += 1

def start_quiz(file_qna):
    if file_empty_warning(file_qna):
        return True
    
    with open(file_qna, "r") as questionnaire:
        list_of_qna = questionnaire.readlines()
        shuffled_list = random.sample(list_of_qna, len(list_of_qna))

        score = 0
        questionnaire = []
        for qna in shuffled_list:
            parts = qna.split(" | ")   

            print(display_questions(parts))

            prompt_guess = "Enter your answer (a/b/c/d): "
            valid_guess = ["a", "b", "c", "d"]

            guess = prompt_validation(prompt_guess, valid_guess)

            point, correct_ans = validate_answer(guess, parts[6])

            parts, score = score_keeper(parts, score, point, correct_ans)
            questionnaire.append(parts)

        clear_screen()
        ascii_art("Quiz Results")
        print(f"Your score is: {score}/{len(shuffled_list)}\n")
        display_answers(questionnaire)

        if continue_or_end() == "y":
            clear_screen()
            return True
        else:
            return False
        
def qna_deleter():
    
    clear_screen()
    ascii_art("QnA Deleter")

    questionnaire_path = get_file()
    if file_empty_warning(questionnaire_path):
        return
    
    with open(questionnaire_path, "r") as file_qna:
        lines = file_qna.readlines()

        ask = f"Want to check the file's contents first (y/n)? "
        valid_response = ["y", "n"]
        action = prompt_validation(ask, valid_response)

        if action == "y":
            show_contents(questionnaire_path)

        while True:
            prompt = "Enter index of QnA for deletion. Type 'q' to exit: "
            req_index = prompt_validation(prompt)

            if req_index.lower() == "q":
                print("Going back to menu...")
                time.sleep(3)
                clear_screen()
                return

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
                    clear_screen()
                    return
            else:
                print("Index given does not exist.")

if __name__ == "__main__":
    manage_files()