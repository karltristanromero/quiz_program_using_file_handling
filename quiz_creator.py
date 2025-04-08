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

    questionnaire_name = input("Enter the file name of the questionnaire: ")

    questionnaire = open(f"{questionnaire_name}", "a")

    while True:
        question = input("Enter a question entry: ")

        choices_list = []
        for i in range(4):
            letter = chr(ord("a") + i)
            choice = input(f"Enter an answer for {letter}: ")
            choices_list.append(choice)

        choices = " | ".join(choices_list)

        while True:
            right_answer = input("Enter the correct letter of the answer: ")

            if right_answer.lower() in ["a", "b", "c", "d"]:
                break

        questionnaire.write(f"{question} | {choices} | {right_answer} \n")

        if continue_or_end() == "n":
            break

def continue_or_end():
    while True:
        response = input("Do you still want to continue? (y/n): ")
        response = response.lower()

        if response in ["y", "n"]:
            break

    return response

        
            



quiz_maker()