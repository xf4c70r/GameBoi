import os
import json
import shutil
import requests
from openai import OpenAI

api_key = os.environ.get('OPENAI_API_KEY')

client = OpenAI(api_key= api_key)

# Create a folder for the game
parentFolderName = input("Please enter the name of the game : ")
parentFolderPath = os.path.join(os.getcwd(), parentFolderName)

# Check if the folder alredy exists
if os.path.exists(parentFolderPath):
    shutil.rmtree(parentFolderPath)
else:
    # Create the game folder if it does not exist
    os.makedirs(parentFolderPath)

imageFolderPath = os.path.join(parentFolderPath, 'assets')

# Check if the assets folder exists
if os.path.exists(imageFolderPath):
    shutil.rmtree(imageFolderPath)
    pass
else:
    # Create the assets folder if it does not exist
    os.makedirs(imageFolderPath)

# System prompts is used to set the stage or context for the conversation, and it can influence how the model responds to user inputs.
sys_prompt = "You are my game developer. Help me create good games. We are going to generate 2D games using a python library called PyGame. These will be your task: 1. Identify all the sprites/assets required for the game.  2. Give me a response back in JSON format. The JSON object should have exactly the same amount of keys as the number of sprites identified. The Key-Value pair in the JSON file should be such that the key is the name of the sprite and the value is the description of the sprite/asset such that it would help DALL-E generate images for the required sprites or images. Example of the JSON Object: {\"car\": \"A green colored car\", \"obstacles\": \"Brown boulders\", \"background\": \"A road with yellow colored strips to divide it into two different lanes\"}"

user_prompt1 = "Generate me a racing game where I am a car trying to avoid traffic cones on the road. The car only moves left or right. It automatically keeps moving forward. The Cones can spawn at any place randomly only they should not overlap with the car. "

user_prompt2 = "Generate me a side scroling game with a hero who has a sword and uses magic bullets. He cannot use the magic bullets once his MP runs out and MP is reduced with each magic bullet he fires and he also has an HP which is reduced each time an enemy hits the hero. The enemies are orges."

user_prompt3 = "Generate me a pygame game where I as a spaceship  shoot aliens and asteroids are obstacles that I avoid by moving either left or right the spaceship keeps on moving straight and If the space ship colides with the asteroid it is game over. The score is the number of aliens I succesfully shoot. For shooting use space bar. Give me the whole implimentation. Also see to it that the sprites are sized appropriately"

# Get the description of the sprites to be generated
spriteResponse = client.chat.completions.create(
    model="gpt-4-1106-preview",
    # max_tokens= 100,
    response_format={ "type": "json_object" },  
    messages=[
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt3},
    ]
)

# Extract the required content from the response and convert it to JSON Object
imageDescription = spriteResponse.choices[0].message.content
imageDescriptionJSON = json.loads(imageDescription)

# Iterate over the JSON Object to generate Images according to the description
for key,value in imageDescriptionJSON.items():

    # Generate Image for each key value pair in the JSON Object
    response = client.images.generate(
    model="dall-e-3",
    prompt= value,
    size="1024x1024",
    quality="standard",
    n=1,) 

    # Download the Image and store it in the assets folder
    image_url = response.data[0].url
    response = requests.get(image_url) 
    if response.status_code == 200:
        image_path = os.path.join(imageFolderPath, f'{key}.png')
        with open(image_path, 'wb') as file:
            file.write(response.content)
        print(f"Image {key} downloaded and saved as '{image_path}'")
    else:
        print(f"Failed to download image {key}")
