# Graham the Text Interpreter

# Libraries
import time


# Functions
def wordCounter(text):
    print(" + Has " + str(len(text.split())) + " words.")


def charCounter(text):
    print(" + Has " + str(len(list(text))) + " characters.")


def lineCounter(dir):
    with open(dir, "r") as fp:
        num_lines = sum(1 for line in fp)
        print(" + Has", num_lines, "lines.")


def analysis(text):
    wordCounter(text)
    charCounter(text)


# Welcome and Menu
def welcome():
    print(
        """
                      ____________________________________________________________________      
         /\_/\       | Hello there! I am Graham! I love reading texts and analyzing them. |
        ((@v@))     <  What would you like me to do?                                      |
        ():::()      |____________________________________________________________________|
    _____VV_VV__/__
                \\
"""
    )


def menu():
    print(
        """
        #1 - Listen to my story.
        #2 - Read my story.
        #3 - Tell me about yourself.
        #4 - How to use?
        #0 - Exit.
        """
    )


def prompt():
    select = input("@v@?   ")

    if select == "1":
        story = input("Alright, let's hear it! \n")
        print("\n--- Wow, such a story! Your story...")
        analysis(story)
        print("\n--- What else would you like me to do? \n")

    elif select == "2":
        print("\nOkay. Where is your text file?\n")
        dir = input("@v@?   ")
        with open(dir) as file:
            contents = file.read()
        print("\n--- Wow, such a story! Your story...")

        analysis(contents)
        lineCounter(dir)

        print("\n--- What else would you like me to do? \n")

    elif select == "3":
        print(
            """
             ____________________________________________________________________________________________
            <  Of course!                                                                                |
            |  I am Graham the Text Interpreter. Developed by Pouya. I'm currently at version 1.0.       |
            |  I take ".txt" files and analize them for you; or you can copy and paste the text here.    |
            |____________________________________________________________________________________________|
            """
        )
        print("\n--- What else would you like me to do? \n")
        menu()
        prompt()

    elif select == "4":
        print(
            """
        
        """
        )
    elif select == "0":
        print(
            """
             ___________________________
            < See you later, adventurer.|
            |___________________________|
            """
        )
        time.sleep(3)
        quit()

    else:
        print(
            """
             _____________________________
            < Sorry, I did not catch that.|
            |_____________________________|
            """
        )


# Main program struct

welcome()

while True:
    menu()
    prompt()
