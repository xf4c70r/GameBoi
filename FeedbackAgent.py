class FeedbackAgent:
    def __init__(self) -> None:
        self.feedback_response = ''
        self.description = ''

    def run(self) -> tuple:
        while True:
            print("Was the game to your expectations? Please answer Yes or No (or type 'exit' to end): ")
            answer = input().lower()

            if answer in ['yes', 'y']:
                print("Thank you for your feedback!")
                print("Do ypu want to play the game again? Answer Again to play again or Stop to stop")
                answer = input().lower()
                if answer =='again':
                    self.feedback_response = 'again'
                else:
                    break

            elif answer in ['no', 'n']:
                valid_choice = False
                while not valid_choice:
                    print("What are you unsatisfied with: Type \n 1 for Assets (Images) or \n 2 for Code")
                    try:
                        choice = int(input())
                        if choice == 1:
                            self.feedback_response = 'Asset'
                            self.description = self._get_description("assets")
                            valid_choice = True
                        elif choice == 2:
                            self.feedback_response = 'Code'
                            self.description = self._get_description("code")
                            valid_choice = True
                        else:
                            print("Not a valid choice")
                    except ValueError:
                        print("Please enter a number.")
                break

            elif answer == 'exit':
                self.feedback_response = 'Exit'
                break
            else:
                print("Not a valid choice")

        return self.feedback_response, self.description

    def _get_description(self, feedback_type: str) -> str:
        description = ""
        while not description.strip():
            print(f"Tell us what problems did you see with the {feedback_type}?")
            description = input()
            if not description.strip():
                print("Description cannot be empty. Please provide more details.")
        return description
