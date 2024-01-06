import os
import json

api = os.environ.get('OPENAI_API_KEY')

class CodeGeneratorAgent:

    def __init__(self, client, assetNames:list) -> None:
        self.client = client
        self.sys_prompt = f"""
    You are my game developer. Help me create good games. We are going to generate 2D games using a python library called PyGame. These will be your task: 

    1. Generate PyGame code for the game described by the user. 
    2. Generate the game in such a way that the window and Image are appropriately sized. 
    3. Give me the output as a JSON Object. 
    4. The sprites are stored in a folder called assests. Give the path approppriately.
    5. All the assets are .png images.  

    Example of the JSON Object: 
    
    {{\"Code\": import pygame\\nimport random\\n\\n# Initialize PyGame\\npygame.init()\\n\ ... "}}"

    These are the names of the image assets: {assetNames}
    """
    
    def run(self, user_prompt:str, parent_dir:str, context:str = " ") -> dict:
        # Generate Code
        codeResponse = self.client.chat.completions.create(
            model="gpt-4-1106-preview",
            response_format={ "type": "json_object" },  
            messages=[
                {"role": "system", "content": self.sys_prompt},
                {"role": "user", "content": user_prompt},
                {"role": "assistant", "content": context}
            ]
        )

        # Extracted code from the response
        formattedCode = codeResponse.choices[0].message.content
        formattedCodeJSON =  json.loads(formattedCode)

        # File path for game.py in the parent directory
        file_path = os.path.join(parent_dir, "game.py")

        # Save the code to game.py in the parent folder
        with open(file_path, "w") as file:
            file.write(formattedCodeJSON['Code'])

        print(f"Code saved to {file_path}")

    
    # def createGameFile(self, formattedCodeJSON:dict, parent_dir:str):
    #     # File path for game.py in the parent directory
    #     file_path = os.path.join(parent_dir, "game.py")

    #     # Save the code to game.py in the parent folder
    #     with open(file_path, "w") as file:
    #         file.write(formattedCodeJSON['Code'])

    #     print(f"Code saved to {file_path}")
