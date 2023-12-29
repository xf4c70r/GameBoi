import os
import json

class CodeGeneratorAgent:

    def __init__(self, client, sys_prompt:str) -> None:
        self.client = client
        self.sys_prompt = sys_prompt
    
    def codeGen(self, user_prompt:str) -> dict:
        # Generate Code
        codeResponse = self.client.chat.completions.create(
            model="gpt-4-1106-preview",
            response_format={ "type": "json_object" },  
            messages=[
                {"role": "system", "content": self.sys_prompt},
                {"role": "user", "content": user_prompt},
            ]
        )

        # Extracted code from the response
        formattedCode = codeResponse.choices[0].message.content
        return json.loads(formattedCode)
    
    def createGameFile(self, formattedCodeJSON:dict, parent_dir:str):
        # File path for game.py in the parent directory
        file_path = os.path.join(parent_dir, "game.py")

        # Save the code to game.py in the parent folder
        with open(file_path, "w") as file:
            file.write(formattedCodeJSON['Code'])

        print(f"Code saved to {file_path}")
