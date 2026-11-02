
                  # < "HANGMAN GAME" >


import random
word = random.choice(["python", "java", "code", "sql", "program"])
guess = ["_"]*len(word)
wrong = 0

while wrong < 6:
    print(" ".join(guess))
    inp_word = input("Enter letter: ").lower()

    if inp_word in word:
        for i in range(len(word)):
            if word[i] == inp_word:
                guess[i] = inp_word
        if "_" not in guess:
            print("You win! Word was:", word)
            break
    else:
        wrong += 1
        print("Wrong! Chances left:", 6 - wrong)

if wrong == 6:
    print("Game over! Word was:", word)