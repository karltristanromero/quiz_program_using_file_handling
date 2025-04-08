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

def quiz_maker():
    questionnaire = open("questionnaire.txt", "a")

    while True:
        question = input("Enter a question entry: ")

        choices_list = []
        for i in range(4):
            letter = chr(ord("a") + i)
            choice = input(f"Enter an answer for {letter}: ")
            choices_list.append(choice)

        choices = " | ".join(choices_list)

        right_answer = input("Enter the correct letter of the answer: ")

        questionnaire.write(f"{question} | {choices} | {right_answer} \n")

quiz_maker()