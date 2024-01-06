import os
import json
import shutil
import requests

class SpriteGeneratorAgent:

    def __init__(self, client) -> None:
        self.client = client
        self.sys_prompt = """
        You are my game developer. Help me create good games. We are going to generate 2D games using a python library called PyGame. These will be your task: 

        1. Identify all the images required for the game.  
        2. Give me a response back in JSON format. The JSON object should have exactly the same amount of keys as the number of images identified. 
        3. The Key-Value pair in the JSON file should be such that the key is the name of the image and the value is the description of the images such that it would help DALL-E generate images for the required images. 
        4. Also generate a good name for the game. Do not use any special charecters in the name of the game. The key for the name of the game in the JSON response should strictly be 'name'. 

        Example of the JSON Object: 

        {\"name\": \"Streer Racer\",\"car\": \"A green colored car\", \"obstacles\": \"Brown boulders\", \"background\": \"A road with yellow colored strips to divide it into two different lanes\"}
        """

    def run(self, user_prompt:str, context:str = " ") -> dict:
        spriteResponse = self.client.chat.completions.create(
        model="gpt-4-1106-preview",
        # max_tokens= 100, 
        response_format={ "type": "json_object" },  
        messages=[
            {"role": "system", "content": self.sys_prompt},
            {"role": "user", "content": user_prompt},
            {"role": "assistant", "content": context}
        ]
    )
        # Extract the required content from the response and convert it to JSON Object
        imageDescription = spriteResponse.choices[0].message.content
        imageDescriptionJSON = json.loads(imageDescription)

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


        return parentFolderPath, assetNames
    
    # def createFolder(self, imageDescriptionJSON:dict):
    #     # Create a folder with the name of the game
    #     parentFolderName = imageDescriptionJSON.pop('name')
    #     parentFolderPath = os.path.join(os.getcwd(), parentFolderName)

    #     # Check if the folder alredy exists
    #     if os.path.exists(parentFolderPath):
    #         shutil.rmtree(parentFolderPath)
    #     else:
    #         # Create the game folder if it does not exist
    #         os.makedirs(parentFolderPath)

    #     # Create Assets folder
    #     imageFolderPath = os.path.join(parentFolderPath, 'assets')

    #     # Check if the assets folder exists
    #     if os.path.exists(imageFolderPath):
    #         shutil.rmtree(imageFolderPath)
    #     else:
    #         # Create the assets folder if it does not exist
    #         os.makedirs(imageFolderPath)

    #     # Get the names of the assets
    #     assetNames = list(imageDescriptionJSON.keys())
    #     return parentFolderPath, imageFolderPath, assetNames
    
    # def downloadAssets(self, imageDescriptionJSON:dict, imageFolderPath:str):
    #     # Iterate over the JSON Object to generate Images according to the description
    #     for key,value in imageDescriptionJSON.items():

    #         # Generate Image for each key value pair in the JSON Object
    #         response = self.client.images.generate(
    #         model="dall-e-3",
    #         prompt= value,
    #         size="1024x1024",
    #         quality="standard",
    #         n=1,) 

    #         # Download the Image and store it in the assets folder
    #         image_url = response.data[0].url
    #         response = requests.get(image_url) 
    #         if response.status_code == 200:
    #             image_path = os.path.join(imageFolderPath, f'{key}.png')
    #             with open(image_path, 'wb') as file:
    #                 file.write(response.content)
    #             print(f"Image {key} downloaded and saved as '{image_path}'")
    #         else:
    #             print(f"Failed to download image {key}")
