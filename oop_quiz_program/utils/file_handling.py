import time
from utils.miscellaneous_functions import UICleaner

class FileHandler:

    def __init__(self, file_path):
        self.file_path = file_path

    @staticmethod
    def file_not_exists_warning():
        UICleaner.clear_screen()
        UICleaner.ascii_art("File does not exist.")
        time.sleep(3)
        UICleaner.clear_screen()    

    def file_empty_warning(self):
        try:   
            with open(self.file_path, "r") as file:
                content = file.read()

            if content.strip() == "":
                UICleaner.clear_screen()
                UICleaner.ascii_art("File is empty")
                time.sleep(3)
                UICleaner.clear_screen()
                return True

        except FileNotFoundError:
            FileHandler.file_not_exists_warning()
            return True
