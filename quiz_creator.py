# Main Program

import os
import time
from art import text2art

def quiz_maker():

    clear_screen()

    # Print ASCII Art
    ascii_art("Quiz Maker")

    # Create or open file to be appended
    questionnaire_name = input("Enter the file name of the questionnaire: ")
    questionnaire = open(f"{questionnaire_name}.txt", "a")

    while True:
        clear_screen()

        ascii_art("Creation Camp")

        question = input("Enter a question entry: ")
        print("")

        choices_list = []

        # Loop through letter a to d for the list of choices from user input
        for i in range(4):
            letter = chr(ord("a") + i)

            # Validation if the input is empty
            while True:

                choice = input(f"Enter an answer for {letter}: ")
                if choice.strip():
                    choices_list.append(choice)
                    break
                else:
                    print("Please input an answer")

        # Turn choice_list into str with the pipe delimiter for better format
        choices = " | ".join(choices_list)

        # Validate if user inputs the right letter of the correct answer
        while True:
            correct_ans = input("\nEnter the correct letter of the answer: ")
            correct_ans = correct_ans.lower()

            if correct_ans in ["a", "b", "c", "d"]:
                break

        # Validates if there are no empty strings in user input
        if question and correct_ans and len(choices_list) == 4:
            # Write into the created/opened file and format
            entry = f"{question} | {choices} | {correct_ans}"
            questionnaire.write(entry + "\n")

        else:
            print("Couldn't add the entry due to missing inputs. Try again.")

        # Ask if user still wants to create more questions or not
        if continue_or_end() == "n":
            print("Exiting the program...")

            time.sleep(3)
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

if __name__ == "__main__":
    quiz_maker()