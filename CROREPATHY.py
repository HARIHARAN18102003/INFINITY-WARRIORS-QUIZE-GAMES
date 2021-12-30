
print("WELCOME TO THE KCG COLLEGE CROREPATHY GAME...")
print("YOU HAVE TEN QUESTIONS.. ANSWER THE TEN QUESTIONS AND GET THE MONEY....")
input("TYPE (OK) TO CONTINUE....   ")

name = input("What is your name? : ")
print("Good Luck ! ", name)
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*10000000)
    print(name, "YOUR WINNING AMOUNT iS: "+str(score)+" RUPPESS  OUT OF 10000000 "" CONGRATULATIONS  ENJOY")

def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
    
questions = {
 "Who Is The Faculty for B10 PYTHON PROGRAMMING COURSE ?: ": "C",
 "What year was KCG COLLEGE STARTED ?: ": "A",
 "Who is The Founder Of THE KCG COLLEGE OF TECHNOLOGY ?: ": "C",
 "Who is The BOY Representative For B10 Department ?: ": "B",
 "Who is The HOD of The SCINECE AND HUMANITY DEPARTMENT ?: ": "A",
 "How Many Students Are in the B10 ?: ": "B",
 "What is the Full Form For AI and DS ?:": "D",
 "Who is the Girl REPRESENTATIVE for B10 Department ?: ": "C",
 "Who is the Handsome Male Faculty For B10 Department ?: ": "A",
 "Who is Our CURRENT PRINCIPAL ? " :"D"
}

options = [["A. KAMALA HASAN SIR", "B. VIJAYAKANTH SIR", "C. PALANIAPPAN SIR", "D. RAJINIKANTH SIR"],
          ["A. 1998", "B. 1999","C. 2000", "D. 2016"],
          ["A. KCG GOKUL ", "B. KCG SRIRAM", "C. KCG VERGHESE", "D. KCG SRIRAM"],
          ["A. DIKESH ","B. KUMARAN", "C. DINAKARAN", "D. ANAND"],
           ["A. BINDHU MAM", "B. JANANI MAM", "C. RAJALAKSHMI MAM", "D. LINU MAM"],
           ["A. 78","B. 63","C. 64","D. 71"],
           ["A. Articulture and developing ","B. Artificial Developements","C. Artical Writting","D. Artificial Intelegence And Data Science"],
           ["A. DHAKSHA SING  ","B. APPARNA SING","C. NEHA SING","D. ANJANA SING"],
           ["A. SHANKAR SIR ","B. AR MUGUGADASS SIR ","C. PALANIAPPAN SIR","D. ATLEE SIR"],
           ['A.GOKUL','B.GOUSHIK SAM','C.SASHREEK','D.P.DEIVA SUNDARI']]



new_game()

while play_again():
    new_game()

print("THANK YOU!")
