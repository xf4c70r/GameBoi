import os
import shutil
import subprocess
from openai import OpenAI
from dotenv import load_dotenv
from FeedbackAgent import FeedbackAgent
from PromptChecker import PromptChecker
from SpriteGeneratorAgent import SpriteGeneratorAgent
from CodeGneratorAgent import CodeGeneratorAgent

def run_game_script(formattedPath):
    python_executable = "python3" if shutil.which("python3") else "python"
    os.chdir(formattedPath)
    game_script_path = os.path.join(formattedPath, "game.py")
    process = subprocess.run([python_executable, game_script_path], text=True, stderr=subprocess.PIPE)
    return process.returncode, process.stderr

# Enrich the prompt entered by the user
def promptEnricher(client, user_prompt) -> str:
    print("\nChecking Prompt.......\n")
    prompt_check = PromptChecker(client)
    return prompt_check.run(user_prompt)

# Generate assets
def assetGenerator(client, user_prompt, feedback = "") -> str:
    print("\nGenerating Assets.......\n")
    asset_generator = SpriteGeneratorAgent(client)
    parentFolderPath, assetNames = asset_generator.run(user_prompt, feedback)
    formattedPath = parentFolderPath.replace("\\", "\\\\")
    return assetNames, formattedPath

# Generate code
def codeGenerator(client, user_prompt, assetNames, formattedPath, formattedCodeJSON = {}, feedback = "") -> dict:
    print("\nGenerating Code.......\n")
    code_generator = CodeGeneratorAgent(client, assetNames)

    if feedback:
        formattedCodeJSON = code_generator.run(formattedCodeJSON['Code'], formattedPath, feedback) 
    else:
        formattedCodeJSON = code_generator.run(user_prompt, formattedPath) 

    while True:
        returncode, stderr = run_game_script(formattedPath)
        if returncode != 0:
            print(f"An error occurred:\n{stderr}\nRegenerating Code\n") 
            formattedCodeJSON = code_generator.run(formattedCodeJSON['Code'], formattedPath, stderr) 
        else:
            print(f"Code running Succesfully") 
            return formattedCodeJSON

def main(client, user_prompt):

    # Enrich the prompt
    user_prompt = promptEnricher(client, user_prompt)
    # Initial asset generation
    assetNames, formattedPath = assetGenerator(client, user_prompt)
    # Initial code generation
    formattedCodeJSON = codeGenerator(client, user_prompt, assetNames, formattedPath)

    # Feedback loop
    while True:  
        feed = FeedbackAgent()
        feedback_type, feedback_description = feed.feedback()
        
        if feedback_type == 'Asset':
            print("Regenerating assets based on feedback...")
            assetNames, formattedPath = assetGenerator(client, user_prompt, feedback_description)
            formattedCodeJSON = codeGenerator(client, user_prompt, assetNames, formattedPath)
        
        elif feedback_type == 'Code':
            print("Regenerating code based on feedback...")
            formattedCodeJSON = codeGenerator(client, user_prompt, assetNames, formattedPath, formattedCodeJSON, feedback_description)
        
        elif feedback_type == 'Exit':
            print("Quitting...")
            break  # Exit the loop

if __name__ == "__main__":
    load_dotenv()
    api = os.environ.get('OPENAI_API_KEY')
    client = OpenAI(api_key=api)
    user_prompt = input("Enter the description for the game you want to generate: \n")
    main(client, user_prompt)