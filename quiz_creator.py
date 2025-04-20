# Main Program

import os
from art import text2art

def quiz_maker():

    clear_screen()
    ascii_art("Quiz Maker")
    questionnaire_name = input("Enter the file name of the questionnaire: ")

    # Create or open file to be appended
    with open(f"{questionnaire_name}.txt", "a") as questionnaire:

        while True:
            clear_screen()
            ascii_art("Creation Camp")

            question = prompt_validation("Enter a question entry: ")
            print("")

            choices_list = []
            # Loop through letter a to d for the list of choices from user
            for i in range(4):
                letter = chr(ord("a") + i)

                # Validation if the input is empty
                choice = prompt_validation(f"Enter an answer for {letter}: ")
                choices_list.append(choice)


            # Turn choice_list into str with the pipe delimiter for better format
            choices = " | ".join(choices_list)

            # Validate if user inputs the right letter of the correct answer
            while True:
                letter = "Enter the letter of the correct answer: "
                correct_ans = prompt_validation(f"\n{letter}")
                correct_ans = correct_ans.lower()

                if correct_ans in ["a", "b", "c", "d"]:
                    break

            # Write into the created/opened file and format
            entry = f"{question} | {choices} | {correct_ans}"
            questionnaire.write(entry + "\n")

            # Ask if user still wants to create more questions or not
            if continue_or_end() == "n":
                print("Exiting the program...")
                clear_screen()
                break


def continue_or_end():
    # Use while loop to validate that user inputs correctly
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

def prompt_validation(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Your input is not valid!")
        
if __name__ == "__main__":
    quiz_maker()