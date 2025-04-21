# Main Program

import os
import time
from art import text2art

def manage_files():

    while True:
        clear_screen()
        ascii_art("Welcome!")

        print("""a. Create/Add QnA to a file
b. Show contents of file
c. Delete a specific QnA in a file
d. Exit program\n""")
        
        action = input("What do you want to do? (a/b/c/d): ")
        action = action.lower()

        if action == "a":
            quiz_maker()

        elif action == "b":
            ask_file = prompt_validation("What is the name of the txt file? ")
            ask_file = f"{ask_file}.txt"
            show_contents(ask_file)

        elif action == "c":
            qna_deleter()

        elif action == "d":
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

def continue_or_end():
    while True:
        response = input("\nDo you still want to continue? (y/n): ")
        response = response.lower()

        if response in ["y", "n"]:
            break
        
    return response

def clear_screen(): 
    os.system('cls' if os.name == 'nt' else 'clear')       

def ascii_art(text: str):
    print(text2art(text))   

def show_contents(ask_file):
    while True:    
        clear_screen()
        try:
            with open(f"{ask_file}", "r") as file:
                print(file.read())

                action = input("Press any key to exit: ")

                if action or action == "":
                    break

        except FileNotFoundError:
            return print("File does not exist.")
        
            
def quiz_maker():

    clear_screen()
    ascii_art("Quiz Maker")
    questionnaire_name = prompt_validation("Enter the file name: ")

    # Create or open file to be appended
    with open(f"{questionnaire_name}.txt", "a") as questionnaire:
        qna_index = 1

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

def qna_deleter():
    
    clear_screen()
    ascii_art("QnA Deleter")

    questionnaire_name = prompt_validation("Enter the file name: ")
    questionnaire_name = f"{questionnaire_name}.txt"

    try:
        file = open(questionnaire_name, "r")
        file.close()
    except FileNotFoundError:
        clear_screen()
        print("File does not exist.")
        return

    ask = f"Want to check {questionnaire_name}.txt's contents first (y/n)? "
    ask = ask.lower()

    action = prompt_validation(ask)

    if action == "y":
        show_contents(questionnaire_name)

    request_index = prompt_validation("Enter number of QnA for deletion: ")

    with open(questionnaire_name, "r") as file:
        lines = file.readlines()

    updated_lines = []
    found = False

    for line in lines:
        parts = line.split(".")[0]

        if parts.strip() == request_index.strip():
            found = True
        else:
            updated_lines.append(line)

    if found:
        with open(questionnaire_name, "w") as updated_file:
            updated_file.writelines(updated_lines)
            print("The line has now been deleted.")
    else:
        print("Index given does not exist.")
    
if __name__ == "__main__":
    manage_files()