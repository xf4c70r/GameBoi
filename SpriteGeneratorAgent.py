import os
import json
import shutil
import requests

class SpriteGeneratorAgent:

    def __init__(self, client, sys_prompt:str) -> None:
        self.client = client
        self.sys_prompt = sys_prompt

    def spriteDescGen(self, user_prompt:str) -> dict:
        spriteResponse = self.client.chat.completions.create(
        model="gpt-4-1106-preview",
        # max_tokens= 100, 
        response_format={ "type": "json_object" },  
        messages=[
            {"role": "system", "content": self.sys_prompt},
            {"role": "user", "content": user_prompt},
        ]
    )
        # Extract the required content from the response and convert it to JSON Object
        imageDescription = spriteResponse.choices[0].message.content
        return json.loads(imageDescription)
    
    def createFolder(self, imageDescriptionJSON:dict):
        # Create a folder with the name of the game
        parentFolderName = imageDescriptionJSON.pop('name')
        parentFolderPath = os.path.join(os.getcwd(), parentFolderName)

        # Check if the folder alredy exists
        if os.path.exists(parentFolderPath):
            shutil.rmtree(parentFolderPath)
        else:
            # Create the game folder if it does not exist
            os.makedirs(parentFolderPath)

        # Create Assets folder
        imageFolderPath = os.path.join(parentFolderPath, 'assets')

        # Check if the assets folder exists
        if os.path.exists(imageFolderPath):
            shutil.rmtree(imageFolderPath)
        else:
            # Create the assets folder if it does not exist
            os.makedirs(imageFolderPath)

        # Get the names of the assets
        assetNames = list(imageDescriptionJSON.keys())
        return parentFolderPath, imageFolderPath, assetNames
    
    def downloadAssets(self, imageDescriptionJSON:dict, imageFolderPath:str):
        # Iterate over the JSON Object to generate Images according to the description
        for key,value in imageDescriptionJSON.items():

            # Generate Image for each key value pair in the JSON Object
            response = self.client.images.generate(
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
