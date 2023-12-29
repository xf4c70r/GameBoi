import json

class PromptChecker:

    def __init__(self, client, sys_prompt:str) -> None:
        self.client = client
        self.sys_prompt = sys_prompt
    
    def checkPrompt(self, user_prompt:str) -> str:
        # Check if the prompt given by the user is complete
        descriptionResponse = self.client.chat.completions.create(
        model="gpt-4-1106-preview",
        response_format={ "type": "json_object" },  
        messages=[
            {"role": "system", "content": self.sys_prompt},
            {"role": "user", "content": user_prompt},
        ]
    )
        # Extracted prompt from the response
        finalPrompt = descriptionResponse.choices[0].message.content
        finalPromptJSON = json.loads(finalPrompt)
        return finalPromptJSON['Prompt']