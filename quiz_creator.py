# Create a program that ask user for a question, it will also ask for 4 
# possible answer (a,b,c,d) and the correct answer. Write the collected data 
# to a text file. Ask another question until the user chose to exit.

# Pseudocode
# - def quiz_maker 
# - append to file that contains the questionnaire
# - while loop
# - ask for input: question, answer options, correct answer
# - append the user inputs to the file
# - close file

# Main Program

import os
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

            choice = input(f"Enter an answer for {letter}: ")
            choices_list.append(choice)

        # Turn choice_list into str with the pipe delimiter for better format
        choices = " | ".join(choices_list)

        # Validate if user inputs the right letter of the correct answer
        while True:
            correct_ans = input("\nEnter the correct letter of the answer: ")

            if correct_ans.lower() in ["a", "b", "c", "d"]:
                break

        # Write into the created/opened file and format
        questionnaire.write(f"{question} | {choices} | {correct_ans} \n")

        # Ask if user still wants to create more questions or not
        if continue_or_end() == "n":
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

def ascii_art(text: str)-> str:
    return print(text2art(text))            

if __name__ == "__main__":
    quiz_maker()
