from enum import Enum
from functions import TranslateWord

class Languages(Enum):
    HE = 1
    EN = 2
    ES = 3
    FR = 4

def print_languages():
    for language in Languages:
        print(f"{language.name} - {language.value}")

def start_program():
    while True:
        print_languages()
        try:
            language = Languages(int(input("Choose your language: ")))
            word = input("Word To Translate: ")
            TranslateWord(word,str(language.name.lower()))
        except Exception as e:
            print(f"ERROR: {str(e)}")
		

if __name__ == "__main__":
    start_program()