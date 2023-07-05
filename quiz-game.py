from bcolors import bcolors

def run_quiz(question):
    score = 0
    total_questions = len(question)

    for question, answer in question.items():
        user_answer = input(bcolors.OKCYAN + question + bcolors.ENDC + " ")

        if user_answer.lower() == answer.lower():
            print(bcolors.OKGREEN + "Correct! Great job!" + bcolors.ENDC)
            score += 1
        else:
            print(bcolors.FAIL + "Incorrect, the answer is: ",
                  answer + bcolors.ENDC)
        print()

    print("End of quiz!")
    print("Score {}/{}".format(score, total_questions))

def main():
    quiz_questions = {
        "What is the capital of Python?": "interpreter",
        "Which keyword is used to define a function?": "def",
        "What is the result of 2 + 2?": "4",
        "What symbol is used for single-line comments in Python?": "#",
        "Which built-in function is used to get the length of a string?": "len",
        "What is the file extension for Python files?": "py",
        "What is the output of 'Hello' + 'World'?": "HelloWorld",
        "What is the output of 'Python' * 3?": "PythonPythonPython",
        "Which data type is used to store a sequence of characters?": "string",
        "What does the 'print' function do?": "display"
    }

    print(bcolors.HEADER + """Basic Python Quiz
    Enter 'start' to begin, or 'quit' to end""" + bcolors.ENDC)

    while True:
        user_input = input("> ")
        if user_input.lower() == "start":
            run_quiz(quiz_questions)
        elif user_input.lower() == "quit":
            print(bcolors.WARNING + "Good-bye!" + bcolors.ENDC)
            break
        else:
            print(bcolors.WARNING +
                  "Invalid input, type 'start' or 'quit'" + bcolors.ENDC)

if __name__ == "__main__":
    main()
