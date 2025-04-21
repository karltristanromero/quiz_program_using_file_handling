# Main Program

import os
from art import text2art

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
            break

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

def quiz_maker():

    clear_screen()
    ascii_art("Quiz Maker")
    questionnaire_name = input("Enter the file name of the questionnaire: ")

    # Create or open file to be appended
    with open(f"{questionnaire_name}.txt", "a") as questionnaire:

        while True:
            clear_screen()
            ascii_art("Creation Camp")

            # Create the questionnaire
            question = prompt_question()
            choices = prompt_choices()
            correct_ans = prompt_correct_answer()

            # Write into the created/opened file and format
            entry = f"{question} | {choices} | {correct_ans}"
            questionnaire.write(entry + "\n")

            # Ask if user still wants to create more questions or not
            if continue_or_end() == "n":
                print("Exiting the program...")
                clear_screen()
                break

if __name__ == "__main__":
    quiz_maker()