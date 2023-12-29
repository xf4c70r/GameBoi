import os
from openai import OpenAI
from PromptChecker import PromptChecker
from SpriteGeneratorAgent import SpriteGeneratorAgent
from CodeGneratorAgent import CodeGeneratorAgent

def main(client, sys_prompt_check, sys_prompt_sprite_gen, user_prompt):

    prompt_check = PromptChecker(client, sys_prompt_check)

    user_prompt = prompt_check.checkPrompt(user_prompt)

    asset_generator = SpriteGeneratorAgent(client, sys_prompt_sprite_gen)

    imageDescriptionJSON = asset_generator.spriteDescGen(user_prompt)

    parentFolderPath, imageFolderPath, assetNames = asset_generator.createFolder(imageDescriptionJSON)

    asset_generator.downloadAssets(imageDescriptionJSON, imageFolderPath)

    # System prompts is used to set the stage or context for the conversation, and it can influence how the model responds to user inputs.

    sys_prompt_code_gen = f"""
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

    formattedPath = parentFolderPath.replace("\\", "\\\\")
    code_generator = CodeGeneratorAgent(client, sys_prompt_code_gen)
    formattedCodeJSON = code_generator.codeGen(user_prompt)
    code_generator.createGameFile(formattedCodeJSON, formattedPath)

if __name__ == "__main__":

    api = os.environ.get('OPENAI_API_KEY')
    client = OpenAI(api_key = api)

    user_prompt = input("Enter the description for the game you want to generate: \n")

    # System prompts is used to set the stage or context for the conversation, and it can influence how the model responds to user inputs.

    sys_prompt_check = """
    You are my game developer. Help me create good games. We are going to generate 2D games using a python library called PyGame. These will be your task: 

    1. Check if the user prompt is well formed
    2. Check if it has the objective
    3. Check if it has the condition for scoring
    4. Check if it mentions the scenarios for when game ends
    5. If the prompts are not well written, write a good prompt for generating the game which has the following: Objective, scoring condition and conditions for when the game ends. Also check if the controls are mentioned if not then also add that to the querry
    6. If the prompt is well formed then return the prompt entered by the user as is
    7. Check if the this line is present in the prompt. If it is not present add these exact same lines without altering them to the end of the querry. The line is: "Give me the whole implimentation. Also see to it that the window and the sprites are sized appropriately"

    Note: The output should be in JSON format only

    Example of a well written prompt: 

    Generate me a pygame game where I as a spaceship  shoot aliens and asteroids are obstacles that I avoid by moving either left or right the spaceship keeps on moving straight and If the space ship colides with the asteroid it is game over. Also if the spaceship collides with the alien its game over. The score is the number of aliens I succesfully shoot. For shooting use space bar. Give me the whole implimentation. Also see to it that the sprites are sized appropriately

    Example of the JSON Object: 

    {\"Prompt\": Generate me a pygame game where I as a spaceship  shoot aliens and asteroids are obstacles that I avoid by moving either left or right the spaceship keeps on moving straight and If the space ship colides with the asteroid it is game over. Also if the spaceship collides with the alien its game over. The score is the number of aliens I succesfully shoot. For shooting use space bar. Give me the whole implimentation. Also see to it that the sprites are sized appropriately\\"}
    """

    sys_prompt_sprite_gen = """
    You are my game developer. Help me create good games. We are going to generate 2D games using a python library called PyGame. These will be your task: 

    1. Identify all the sprites/assets required for the game.  
    2. Give me a response back in JSON format. The JSON object should have exactly the same amount of keys as the number of sprites identified. 
    3. The Key-Value pair in the JSON file should be such that the key is the name of the sprite and the value is the description of the sprite/asset such that it would help DALL-E generate images for the required sprites or images. 
    4. Also generate a good name for the game. Do not use any special charecters in the name of the game. The key for the name of the game in the JSON response should strictly be 'name'. 

    Example of the JSON Object: 
    
    {\"name\": \"Streer Racer\",\"car\": \"A green colored car\", \"obstacles\": \"Brown boulders\", \"background\": \"A road with yellow colored strips to divide it into two different lanes\"}
    """

    main(client, sys_prompt_check, sys_prompt_sprite_gen, user_prompt)