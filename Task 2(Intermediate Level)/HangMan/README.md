# Hangman Game

A classic text-based Hangman game implemented in Python. Try to guess the word before the hangman is complete!

## Features

- 🎮 Interactive text-based interface
- 👤 Visual hangman display that updates with each wrong guess
- 📝 Track of used letters
- 🔄 Play again option
- 🧹 Clear screen functionality for better user experience
- ⌨️ Case-insensitive input handling
- ❌ Input validation
- 💭 Predefined word list of computer-related terms

## How to Play

1. Run the game:
   ```bash
   python hangman.py
   ```

2. The game will:
   - Choose a random word
   - Display blank spaces for each letter
   - Show the hangman gallows
   - Show how many lives you have left

3. Gameplay:
   - Guess one letter at a time
   - If correct: the letter appears in the word
   - If wrong: lose a life and hangman grows
   - You can see which letters you've already guessed

4. Win/Lose Conditions:
   - Win: Guess all letters in the word
   - Lose: Run out of lives (6 wrong guesses)

## Requirements

- Python 3.x
- Operating System: Windows/Linux/MacOS

## Installation

1. Clone this repository or download the `hangman.py` file
2. No additional packages needed - uses only built-in Python libraries:
   - `random`
   - `os`

## Game Preview

```
Lives left: 6

You have used these letters: A E I

   --------
   |      |
   |      O
   |     \|/
   |      |
   |     /
   -

Current word: _ _ _ _ _ _ _ _ _ _ _

Guess a letter:
```

## Word List

The game includes words related to computer science and technology:
- python
- programming
- computer
- algorithm
- database
- network
- software
- developer
- keyboard
- monitor

## Contributing

Feel free to fork this project and add your own improvements! Some ideas:
- Add more words to the word list
- Add difficulty levels
- Add hint system
- Add scoring system
- Add sound effects
- Add multiplayer mode

## License

This project is open source and available for anyone to use and modify.
