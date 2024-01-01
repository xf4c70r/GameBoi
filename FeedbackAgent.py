class FeedbackAgent:
    def __init__(self) -> None:
        self.feedback_response = ''
        self.description = ''

    def feedback(self) -> str:
        while True:
            print("Was the game to your expectations? Please answer Yes or No (or type 'exit' to end): ")
            answer = input().lower()

            if answer in ['yes', 'y']:
                print("Thank you! Would you like to generate one more game? (Yes/No)")
                continue_game = input().lower()
                if continue_game not in ['yes', 'y']:
                    break
                elif continue_game in ['yes', 'y']:
                    self.feedback_response = 'New'
                else:
                    print("Not a valid choice")

            elif answer in ['no', 'n']:
                while True:
                    print("What are you unsatisfied with: \n 1. Assets (Images) \n 2. Code")
                    try:
                        choice = int(input())
                        if choice == 1:
                            self.feedback_response = 'Asset'
                            print("Tell us what problems did you see with the assets? \n")
                            self.description = input()
                            break
                        elif choice == 2:
                            self.feedback_response = 'Code'
                            print("Tell us what problems did you see with the code? \n")
                            self.description = input()
                            break
                        else:
                            print("Not a valid choice")
                    except ValueError:
                        print("Please enter a number.")

            elif answer == 'exit':
                break
            else:
                print("Not a valid choice")

        return self.feedback_response, self.description
