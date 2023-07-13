def game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("----------------------------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)

        guess = input("ENTER ( A , B or C ) ==>")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("Right !!")
        return 1
    else:
        print("Worng !!")
        return 0

def display_score(correct_guesses, guesses):

    print("--------------------------------")
    print("RESULTS")
    print("---------------------------------")
    print("ANSWER =", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses =", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions)*100))
    print("YOUR SCORE "+str(score)+"%")
def play_again():
    ask = input("DO OU WANT TO PLAY AGAIN? [Y/N] =")
    ask =ask.upper()

    if ask == "Y":
        return True
    else:
        return False
questions ={
    "1) Who sang the title song for the latest Bond film, No Time to Die?": "C",
    "2) Which flies a green, white, and orange (in that order) tricolor flag? ": "C",
    "3) What company makes the Xperia model of smartphone?": "B",
    "4) Which city is home to the Brandenburg Gate?": "C",
    "5) Which of the following is NOT a fruit?": "A",
    "6) Where was the first example of paper money used?":"A",
    "7) Who is generally considered the inventor of the motor car?": "B",
    "8) If you were looking at Iguazu Falls, on what continent would you be?": "C",
    "9) What number was the Apollo mission that successfully put a man on the moon for the first time in human history?": "A",
    "10) Which of the following languages has the longest alphabet?": "B"
}
options = [[
    "A,Adele",
    "B,Sam Smith",
    "C,Billie Eilish", ],
    [
    "A,Ireland",
    "B,Ivory Coast",
    "C,Italy", ],
    [
    "A,Samsung",
    "B,Sony",
    "C,Nokia", ],
    [
    "A,Vienna",
    "B,Zurich",
    "C,Berlin", ],
    [
    "A,Rhubarb",
    "B,Tomatoes",
    "C,Avocados", ],
    [
    "A,China",
    "B,Turkey",
    "C,Greece", ],
    [
    "A,Henry Ford",
    "B,Karl Benz",
    "C,Henry M. Leland", ],
    [
    "A,Asia",
    "B,Africa",
    "C,South America", ],
    [
    "A,Apollo 11",
    "B,Apollo 12",
    "C,Apollo 13", ],
    [
    "A,Greek" ,
    "B,Russian",
    "C,Arabic", ],

    ]

game()
while play_again():
    game()

print("THANKS FOR PLAYING")
