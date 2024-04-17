class FeedbackAgent:
    def __init__(self):
        self.feedback_response = ''
        self.description = ''

    def feedback(self):
        answer = input("Was the game to your expectations? Please answer Yes, No, or type Exit to quit: ").lower()
        if answer in ['yes', 'y']:
            print("Thank you for playing! If you want to create a new game, please restart the application.")
            return ('Exit', '')  # Direct exit after a positive response

        elif answer in ['no', 'n']:
            return self.handle_negative_feedback()

        elif answer == 'exit':
            print("Exiting feedback collection.")
            return ('Exit', '')  # Exit feedback

        else:
            print("Not a valid choice. Please answer Yes, No, or type Exit to quit.")
            return self.feedback()  # Recursive call for invalid input

    def handle_negative_feedback(self):
        choice = input("What are you unsatisfied with: Type \n 1 for Assets (Images) or \n 2 for Code: \n")
        if choice == '1':
            self.feedback_response = 'Asset'
        elif choice == '2':
            self.feedback_response = 'Code'
        else:
            print("Please enter 1 or 2.")
            return self.handle_negative_feedback()  # Recursive call for invalid input

        self.description = self._get_description(self.feedback_response.lower())
        return self.feedback_response, self.description

    def _get_description(self, feedback_type):
        description = input(f"Tell us what problems did you see with the {feedback_type}? ").strip()
        if description:
            return description
        else:
            print("Description cannot be empty. Please provide more details.")
            return self._get_description(feedback_type)  # Recursive call for empty description