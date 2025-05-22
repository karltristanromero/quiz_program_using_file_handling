import os
from prompt_functions import FileRetriever

class PathHandler:
    '''This is a code for create_dir(), get_file(), and rename_file()'''
    def __init__(self):
        self.file_name = FileRetriever("Enter a file name: ").get_file_name()

    @staticmethod
    def create_dir():
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        subdir_name = "questionnaire_inventory"

        dir_path = os.path.join(parent_dir, subdir_name)
        os.makedirs(dir_path, exist_ok=True)
        
        return dir_path
    
    def rename_file(self):
        file_name = self.file_name.strip().lower()
        file_name = file_name.replace(" ", "_")
        return file_name

    def get_file_path(self):
        file_path = self.rename_file()
        dir = PathHandler.create_dir()

        full_path = os.path.join(dir, file_path)
        
        if not full_path.endswith(".txt"):
            file_path = f"{full_path}.txt"

        return file_path
    
if __name__ == "__main__":
    file_name = PathHandler()
    print(file_name.get_file_path())