import random  # Imports the random library for random number generation.
import os  # Imports the os library to interact with the operating system.

def clear_screen():
    """Clears the console screen based on the operating system."""
    if os.environ.get('TERM'):  # Checks if the 'TERM' environment variable is set.
        os.system('cls' if os.name == 'nt' else 'clear')  # Clears screen for Windows (nt) or Unix.

class Game:
    """Defines the game logic for Hangman."""
    MAX_MOVES = 7  # Class variable that defines the maximum number of incorrect guesses.
    WORD_BANK = ("microwave", "tesla", "computer", "pineapple", "garage",
                 "python", "bottle", "processor", "australia", "continent", "dictionary")  # Possible words.

    def __init__(self):
        """Initializes a new game instance with a random word and reset counters."""
        self.word = random.choice(Game.WORD_BANK)  # Randomly selects a word from the WORD_BANK.
        self.guessed_letters = set()  # Initializes an empty set to store guessed letters.
        self.number_of_moves = 0  # Initializes the number of moves (incorrect guesses) to zero.

    def guess_letter(self, letter):
        """Processes a single letter guess and updates the game state."""
        if letter in self.guessed_letters:  # Checks if the letter has already been guessed.
            return False, 'already guessed'
        self.guessed_letters.add(letter)  # Adds the new letter to the set of guessed letters.
        if letter in self.word:  # Checks if the guessed letter is in the word.
            return True, None
        else:
            self.number_of_moves += 1  # Increments the move counter if the guess is incorrect.
            return False, None

    def is_solved(self):
        """Checks if the entire word has been correctly guessed."""
        return all(letter in self.guessed_letters for letter in self.word)

    def has_guesses_left(self):
        """Determines if the player has remaining guesses."""
        return self.number_of_moves < Game.MAX_MOVES

    def get_masked_word(self):
        """Returns the current state of the word with unguessed letters masked."""
        return ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])

    def get_remaining_moves(self):
        """Returns the number of remaining moves allowed."""
        return Game.MAX_MOVES - self.number_of_moves

class UserInterface:
    """Handles all user interactions."""
    def __init__(self, game):
        """Initializes the user interface with a game instance."""
        self.game = game  # Stores the game instance.
        self.next_alert = ''  # Temporary storage for messages to display.

    def display_game_state(self):
        """Displays the current game state and clears the previous content."""
        clear_screen()
        if self.next_alert:  # Checks if there is a message to display.
            print(self.next_alert)
            self.next_alert = ''  # Clears the message after displaying.
        print(self.game.get_masked_word())  # Shows the masked word.
        print(f"Guessed Letters: {', '.join(sorted(self.game.guessed_letters)) if self.game.guessed_letters else 'None'}")
        print(f"Moves left: {self.game.get_remaining_moves()}")  # Shows remaining moves.

    def update_alert(self, message):
        """Updates the message to be displayed on the next screen refresh."""
        self.next_alert = message

    def get_user_input(self):
        """Prompts the user for a letter or a word guess."""
        return input("Enter a letter or 'guess' to guess the whole word: ").strip().lower()

    def show_message(self, message):
        """Displays a message to the user."""
        if message:
            print(message)

    def user_won(self):
        """Displays a winning message."""
        print("Congratulations! You solved the puzzle!")

    def user_lost(self):
        """Displays a losing message with the correct word."""
        print(f"Sorry, you didn't guess the word. It was '{self.game.word}'. Better luck next time!")

def main():
    """Main function to control the flow of the game."""
    game = Game()  # Creates a new game instance.
    ui = UserInterface(game)  # Creates a new user interface instance linked to the game.

    while game.has_guesses_left() and not game.is_solved():  # Continues until all guesses are used or the word is solved.
        ui.display_game_state()  # Displays the current state of the game.
        choice = ui.get_user_input()  # Gets user input.

        if choice == 'guess':  # If the user wants to guess the entire word.
            word_guess = input("Guess the whole word: ").strip().lower()
            if word_guess == game.word:  # Checks if the word guess is correct.
                ui.user_won()
                return
            else:
                ui.update_alert("Wrong guess!")  # Updates the alert for incorrect word guess.
                continue
        elif len(choice) == 1 and choice.isalpha():  # Checks if the input is a single letter.
            correct, message = game.guess_letter(choice)  # Processes the letter guess.
            if not correct:
                alert_msg = "You already guessed that letter." if message == 'already guessed' else f"{choice} is not in the word."
                ui.update_alert(alert_msg)  # Updates the alert based on the outcome.
        else:
            ui.update_alert("Invalid input. Please enter a single letter.")  # Sets the alert for invalid input.

    if not game.is_solved():  # If the game ends without solving the word.
        ui.user_lost()  # Displays the losing message.

if __name__ == "__main__":
    main()  # Calls the main function to start the game.
