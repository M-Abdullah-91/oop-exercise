import random

class FlashCard:
    def __init__(self):
        # Initialize the dictionary of fruits
        self.fruits = {
            "Banana": "yellow",
            "Strawberries": "pink",
            "Apple": "red",
            "Grapes": "purple",
            "Orange": "orange",
            "Lemon": "yellow",
            "Blueberry": "blue",
            "Watermelon": "green"  # Added for demonstration
        }
        
    def get_random_fruit(self):
        # Choose a random fruit from the dictionary
        self.fruit, self.color = random.choice(list(self.fruits.items()))
        
    def ask_question(self):
        # Prompt the user for the color of the randomly chosen fruit
        print(f"What is the color of {self.fruit}?")
        user_answer = input("Your answer: ").strip().lower()
        
        # Check if the user's answer is correct
        if user_answer == self.color.lower():
            print("Correct answer!")
        else:
            print(f"Wrong. The correct color is {self.color}.")

def main():
    print("Welcome to the fruit quiz!")

    flashcard = FlashCard()

    flashcard.get_random_fruit()
    flashcard.ask_question()

    while(True):
        user_input = input("Enter 0 to play again: ")
        if user_input!='0':
            print("Thank You For Playing")
            return False

        main()    

if __name__ == "__main__":
    main()
