Class-Responsibility-Collaboration (CRC) cards are a brainstorming tool used in the design of object-oriented software. They help in identifying and organizing information about classes, their responsibilities, and the ways they collaborate with other classes.

### 1. CRC Card for `Game` Class

**Class Name:** Game

**Responsibilities:**
- Maintain the word to be guessed.
- Track the letters that have been guessed.
- Track the number of incorrect guesses.
- Determine if a letter guess is correct.
- Check if the game has been won or lost.
- Determine if the player has remaining guesses.
- Provide the current state of the guessed word (showing guessed letters).

**Collaborators:**
- UserInterface

**Description:**
The `Game` class is responsible for managing the internal state of the Hangman game. It stores the word to be guessed, tracks which letters have been guessed, and keeps a count of incorrect guesses. It provides methods to process guesses, check for game completion, and offer a view of the current state of the word with placeholders for unguessed letters.

---

### 2. CRC Card for `UserInterface` Class

**Class Name:** UserInterface

**Responsibilities:**
- Interact with the user to get guesses.
- Display the current state of the game.
- Show messages (feedback, errors, etc.) to the user.
- Update and manage alerts for the next screen refresh.
- Announce game outcomes (win/loss).

**Collaborators:**
- Game

**Description:**
The `UserInterface` class handles all interactions with the user. It is responsible for collecting user input, displaying the current game state, and communicating messages and game outcomes. It utilizes information from the `Game` class to display the correct state and relies on input from the user to drive the game process.

