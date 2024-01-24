questions = ("How many elements are in the periodic table?: ",
            "Which animal lays the largest eggs?: ",
            "What is the most abundant gas in Earth's atmosphere?: ",
            "How many bones are in the human body?: ",
            "Which planet in the solar system is the hottest?: ")
options = (("A. 116", "B. 117", "C. 118", "D. 119"),
            ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
            ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
            ("A. 206", "B. 207", "C. 208", "D. 209"),
            ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guess = []
def game():
    global guess
    guesses = 0
    for g in range(len(questions)):
        print(questions[guesses])
        f = options[guesses]
        for i in f:
            print(i)
        inp = input("Write A, B, C or D: ").upper()
        if answers[guesses] == inp:
            print("CORRECT")
            guess.append(inp)
        else:
            print("WRONG")
        guesses += 1
        print("___________________________________________")
    score()
    guess.clear()
def score():
    sco = (len(guess) / len(questions)) * 100
    print("you got",sco,"%")
def play_again():
    while True:
        game()
        again = input("Do you wanto to play again? (YES/NO)").upper()
        print(again)
        if again != "YES":
            print("BYEEEE")
            break
    score()


play_again()
