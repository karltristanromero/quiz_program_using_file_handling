
class PromptValidator:
    def __init__(self, prompt, valid_response=None):
        self.prompt = prompt
        self.valid_response = valid_response

    def get_input(self):
        while True:

            response = input(self.prompt).strip().lower()

            if not response: 
                print("Your input is invalid!")
                continue

            if self.valid_response:
                if response in self.valid_response:
                    return response
                print(f"Input is invalid! Enter only {','.join(self.valid_response)}!")
            else:
                return response
            
question_validator = PromptValidator("Enter a question entry: ")
print(question_validator.get_input())

