class FeedbackAgent:
    def __init__(self) -> None:
        self.feedback_response = ''
        self.description = ''

    def feedback(self):
        while True:
            answer = input("Was the game to your expectations? Please answer Yes or No, or type Exit to quit: ").lower()
            
            if answer in ['yes', 'y']:
                print("Thank you for playing! \nDo you want to create a new game?")
                answer = input("Was the game to your expectations? Please answer Yes or No, or type Exit to quit: ").lower()
                if answer in ['yes', 'y']:
                    print("Thank you for playing! \n Do you want to create a new game?")
                    #ToDo: Add method to start the creation of game
                else: 
                    break  # Exit the loop
            
            elif answer in ['no', 'n']:
                while True:

                    try:
                        choice = int(input("What are you unsatisfied with: Type \n 1 for Assets (Images) or \n 2 for Code: "))
                        if choice == 1:
                            self.feedback_response = 'Asset'
                        elif choice == 2:
                            self.feedback_response = 'Code'
                        else:
                            print("Please enter 1 or 2.")
                            continue  # Skips the rest of the current iteration
                        self.description = self._get_description(self.feedback_response.lower())
                        print("Thank you for your feedback")
                        return self.feedback_response, self.description  # Returns and exits function
                    
                    except ValueError:
                        print("Please enter a valid number.")
            
            elif answer == 'exit':
                self.feedback_response = 'Exit'
                print("Exiting feedback collection.")
                break  # Exit the loop
            
            else:
                print("Not a valid choice. Please answer Yes, No, or type Exit to quit.")

    def _get_description(self, feedback_type: str) -> str:
        while True:
            description = input(f"Tell us what problems did you see with the {feedback_type}?").strip()
            if description:
                return description
            else:
                print("Description cannot be empty. Please provide more details.")

# Example usage
feed = FeedbackAgent()
feedback_result = feed.feedback()
print(feedback_result)
