import os
from openai import OpenAI
from SpriteGeneratorAgent import SpriteGeneratorAgent
from CodeGneratorAgent import CodeGeneratorAgent


def main():
    api = os.environ.get('OPENAI_API_KEY')
    client = OpenAI(api_key = api)

    user_prompt1 = "Generate me a racing game where I am a car trying to avoid traffic cones on the road. The car only moves left or right. It automatically keeps moving forward. The Cones can spawn at any place randomly only they should not overlap with the car. "

    user_prompt2 = "Generate me a side scroling game with a hero who has a sword and uses magic bullets. He cannot use the magic bullets once his MP runs out and MP is reduced with each magic bullet he fires and he also has an HP which is reduced each time an enemy hits the hero. The enemies are orges."

    user_prompt3 = "Generate me a pygame game where I as a spaceship  shoot aliens and asteroids are obstacles that I avoid by moving either left or right the spaceship keeps on moving straight and If the space ship colides with the asteroid it is game over. Also if the spaceship collides with the alien its game over. The score is the number of aliens I succesfully shoot. For shooting use space bar. Give me the whole implimentation. Also see to it that the sprites are sized appropriately"

    # System prompts is used to set the stage or context for the conversation, and it can influence how the model responds to user inputs.
    sys_prompt_sprite_gen = """
    You are my game developer. Help me create good games. We are going to generate 2D games using a python library called PyGame. These will be your task: 
    1. Identify all the sprites/assets required for the game.  
    2. Give me a response back in JSON format. The JSON object should have exactly the same amount of keys as the number of sprites identified. 
    3. The Key-Value pair in the JSON file should be such that the key is the name of the sprite and the value is the description of the sprite/asset such that it would help DALL-E generate images for the required sprites or images. 
    4. Also generate a good name for the game. Do not use any special charecters in the name of the game. The key for the name of the game in the JSON response should strictly be 'name'. 
    Example of the JSON Object: {\"name\": \"Streer Racer\",\"car\": \"A green colored car\", \"obstacles\": \"Brown boulders\", \"background\": \"A road with yellow colored strips to divide it into two different lanes\"}
    """

    asset_generator = SpriteGeneratorAgent(client, sys_prompt_sprite_gen)

    imageDescriptionJSON = asset_generator.spriteDescGen(user_prompt3)

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
    Example of the JSON Object: {{\"Code\": import pygame\\nimport random\\n\\n# Initialize PyGame\\npygame.init()\\n\ ... "}}"
    These are the names of the image assets: {assetNames}
    """

    formattedPath = parentFolderPath.replace("\\", "\\\\")

    code_generator = CodeGeneratorAgent(client, sys_prompt_code_gen)

    formattedCodeJSON = code_generator.codeGen(user_prompt3)

    code_generator.createGameFile(formattedCodeJSON, formattedPath)

if __name__ == "__main__":
    main()