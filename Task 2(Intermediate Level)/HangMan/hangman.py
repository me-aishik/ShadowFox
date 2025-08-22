import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]

def get_word():
    words = ['python', 'programming', 'computer', 'algorithm', 'database', 
             'network', 'software', 'developer', 'keyboard', 'monitor']
    return random.choice(words).upper()

def play_hangman():
    word = get_word()
    word_letters = set(word)  # letters in the word
    alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    used_letters = set()  # letters guessed by the user

    lives = 6  # number of tries before game over

    # Game loop
    while len(word_letters) > 0 and lives > 0:
        clear_screen()
        print('Lives left:', lives)
        print('\nYou have used these letters:', ' '.join(sorted(used_letters)))

        # Show the word with guessed letters
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(display_hangman(lives))
        print('Current word:', ' '.join(word_list))

        # Get user input
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('Good guess!')
            else:
                lives = lives - 1
                print('Wrong guess!')
        
        elif user_letter in used_letters:
            print('You have already used that letter. Try again!')
        
        else:
            print('Invalid character. Please enter a letter!')

    # Game ended
    clear_screen()
    if lives == 0:
        print(display_hangman(lives))
        print('Sorry, you died! The word was', word)
    else:
        print('Congratulations! You guessed the word', word, '!!')

def main():
    while True:
        play_hangman()
        play_again = input("Would you like to play again? (Y/N): ").upper()
        if play_again != 'Y':
            break
    print("Thanks for playing Hangman!")

if __name__ == "__main__":
    main()
