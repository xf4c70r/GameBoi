import os
import subprocess
from openai import OpenAI
from sympy import im
from PromptChecker import PromptChecker
from SpriteGeneratorAgent import SpriteGeneratorAgent
from CodeGneratorAgent import CodeGeneratorAgent

def run_game_script(formattedPath):
    os.chdir(formattedPath)
    game_script_path = os.path.join(formattedPath, "game.py")
    process = subprocess.run(["python", game_script_path], text=True, stderr=subprocess.PIPE)
    return process.returncode, process.stderr

def main(client, user_prompt):

    # Check the prompt entered by the user
    prompt_check = PromptChecker(client)
    user_prompt = prompt_check.run(user_prompt)

    # Generate the assets
    asset_generator = SpriteGeneratorAgent(client)
    parentFolderPath, assetNames = asset_generator.run(user_prompt)
    formattedPath = parentFolderPath.replace("\\", "\\\\")

    # Generate Code
    code_generator = CodeGeneratorAgent(client, assetNames)

    while True:
        returncode, stderr = run_game_script(formattedPath)
        if returncode != 0:
            print(f"An error occurred:\n{stderr}") 
            code_generator.run(user_prompt, formattedPath, stderr) 
        else:
            print(f"Code running Succesfully") 
            break
if __name__ == "__main__":

    api = os.environ.get('OPENAI_API_KEY')
    client = OpenAI(api_key = api)

    user_prompt = input("Enter the description for the game you want to generate: \n")

    main(client, user_prompt)