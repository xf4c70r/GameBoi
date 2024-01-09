import json

class PromptChecker:

    def __init__(self, client) -> None:
        self.client = client
        self.sys_prompt = """
        You are my game developer. Help me create good games. We are going to generate 2D games using a python library called PyGame. I will give you a prompt and these will be your task: 

        1. Check if the user prompt is well formed
        2. Check if it has the objective
        3. Check if it has the condition for scoring
        4. Check if it mentions the scenarios for when game ends
        5. If the prompts are not well written, write a good prompt for generating the game which has the following: Objective, scoring condition and conditions for when the game ends. Also check if the controls are mentioned if not then also add that to the query
        6. If the prompt is well formed then return the prompt entered by the user as is

        Note: The output should be in JSON format only

        Example of a poorly written prompt:

        Generate me a 2D racing game using pygame

        Example of a well written prompt: 

        Generate me a 2D racing game using pygame where the objective is to race against other cars and finish the track in the shortest time. Scoring is based on the position in which the player finishes and the time taken to complete the race. The game ends when the player crosses the finish line or if the player's car is too damaged to continue. Use arrow keys for steering, acceleration, and braking. Give me the whole implementation. Also see to it that the window and the sprites are sized appropriately

        Example of the JSON Object: 

        {\"Prompt\": Generate me a 2D racing game using pygame where the objective is to race against other cars and finish the track in the shortest time. Scoring is based on the position in which the player finishes and the time taken to complete the race. The game ends when the player crosses the finish line or if the player's car is too damaged to continue. Use arrow keys for steering, acceleration, and braking. Give me the whole implementation. Also see to it that the images are sized appropriately\\"}
        """
    
    def run(self, user_prompt:str) -> str:
        # Check if the prompt given by the user is complete
        descriptionResponse = self.client.chat.completions.create(
        model="gpt-4-1106-preview",
        response_format={ "type": "json_object" },  
        messages=[
            {"role": "system", "content": self.sys_prompt},
            {"role": "user", "content": user_prompt},
        ]
    )
        # Extracted prompt from the response
        finalPrompt = descriptionResponse.choices[0].message.content
        finalPromptJSON = json.loads(finalPrompt)
        print("\n Enriched Prompt: \n", finalPromptJSON['Prompt'], "\n")
        return finalPromptJSON['Prompt']