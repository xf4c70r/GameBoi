import os
import json
import shutil
import requests
from openai import OpenAI

api_key = os.environ.get('OPENAI_API_KEY')

client = OpenAI(api_key= api_key)

# System prompts is used to set the stage or context for the conversation, and it can influence how the model responds to user inputs.
sys_prompt = """
You are my game developer. Help me create good games. We are going to generate 2D games using a python library called PyGame. These will be your task: 
1. Generate PyGame code for the game described by the user. 
2. Generate the game in such a way that the window and Image are appropriately sized. 
3. Give me the output as a JSON Object. 4. The sprites are stored in a folder called assests. Give the path approppriately. 
Example of the JSON Object: {\"Code\": import pygame\\nimport random\\n\\n# Initialize PyGame\\npygame.init()\\n\ ... "}"
These are the names of the image assets: ['spaceship', 'alien', 'asteroid', 'laser_beam', 'background', 'explosion', 'game_over_text', 'score_text']
"""

user_prompt1 = "Generate me a racing game where I am a car trying to avoid traffic cones on the road. The car only moves left or right. It automatically keeps moving forward. The Cones can spawn at any place randomly only they should not overlap with the car. "

user_prompt2 = "Generate me a side scroling game with a hero who has a sword and uses magic bullets. He cannot use the magic bullets once his MP runs out and MP is reduced with each magic bullet he fires and he also has an HP which is reduced each time an enemy hits the hero. The enemies are orges."

user_prompt3 = "Generate me a pygame game where I as a spaceship  shoot aliens and asteroids are obstacles that I avoid by moving either left or right the spaceship keeps on moving straight and If the space ship colides with the asteroid it is game over. The score is the number of aliens I succesfully shoot. For shooting use space bar. Give me the whole implimentation. Also see to it that the sprites are sized appropriately"

# Get the description of the sprites to be generated
codeResponse = client.chat.completions.create(
    model="gpt-4-1106-preview",
    # max_tokens= 100,
    response_format={ "type": "json_object" },  
    messages=[
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt3},
    ]
)

# print(codeResponse)

# Extracted code from the response
formattedCode = codeResponse.choices[0].message.content

print("Content\n", formattedCode)

formattedCodeJSON = json.loads(formattedCode)

print("JSON\n", formattedCodeJSON['Code'])

# Finding the start of the actual code after '{"Code": "'

start = formattedCode.find('{"Code": "') + len('{"Code": "')

# Removing the prefix and the trailing '"'
formattedCode = formattedCode[start+1:-1-1]

# Removing the extra backslashes for newline characters
formattedCode = formattedCode.replace("\\n", "\n")

# Print the formatted code
# print(formattedCode)

# Save the code to a file
with open("game.py", "w") as file:
    file.write(formattedCodeJSON['Code'])

print("Code saved to game.py")