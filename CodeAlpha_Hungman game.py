import random

def Hangman_game():

    words=["apple","orange","mango","pineapple","strawberry","grapse"]

    secret_word=random.choice(words)

    guessed_letter=[]

    chances=6

    print("WELCOME TO HAGMAN_GAME............")

    print("\nGame about: computer select one word\nyou guess one letter at a time\nyou has 6 chances\nif you guess all letter you are win\nelse chances over lose")

    print("\nALL the best")

    print("\nLet's start your Game.......") 

    while chances>0:

        display=" "

        for letter in secret_word:

            if letter in guessed_letter:

                display+=letter+" "

            else:

                display+="_"

        print("\nword",display)
        
        if "_" not in display:

            print("\nyou won the game....perfect:",secret_word)

            break
    
        guess=input("\nenter your guess:").lower()

        if guess in guessed_letter:

            print("\nyour guess is already there........")

        elif guess in secret_word:

            guessed_letter.append(guess)

            print("\nyour guess is correct")

        else:
            guessed_letter.append(guess)

            chances-=1

            print("\nyou guess is wrong,your chances ",chances)

    if chances==0:

        print("\nGame is over......The word is :",secret_word)        
            
Hangman_game()

