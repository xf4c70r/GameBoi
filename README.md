# GameBoi

Gameboi leverages ChatGPT and PyGame to create customized 2D games based on user input. It is designed to streamline the game development process by automating various stages, from generating game sprits and assets to writing PyGame code. 

Features:

1. Prompt Enhancement: The Game Generator begins by enhancing the prompt entered by the user. This step ensures that the game concept is well-defined and rich in detail, setting a strong foundation for the game development.

2. Image Asset Generation and Organization: One of the standout features is its ability to identify and generate the necessary image assets for the game. These assets are automatically downloaded and organized into an 'asset' subfolder within the main game folder, ensuring easy access and management.

3. Pygame Code Generation: The tool generates the initial Pygame code required to bring the game to life. This code serves as a starting point for further development and customization.

4. Error Resolution Loop: In the event of any errors during gameplay, the Game Generator enters a loop where it identifies the issues, solves them, and regenerates the necessary code. This feature significantly reduces debugging time and enhances the overall development process.

System Requirements:

1. Python 3.x
2. Pygame Library
3. ChatGPT API Access

## Demo

https://github.com/xf4c70r/GameBoi/assets/57385228/975c3747-860d-4541-bc77-795d2f2fa997


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file. You need to add your OpenAI api key. 

`OPENAI_API_KEY`




##  Steps For Adding 'openai_api_key' To Your Environment Variables

Windows: 

1. Open the Start Menu.

2. Search for “Environment Variables” and click on “Edit the system environment variables.”

3. Click the “Environment Variables” button.

4. Under “User variables,” click “New” and enter the variable name and value.

macOS:

1. Open your Terminal app. You can find it in Applications › Utilities › Terminal

2. Type nano ~/.shre if you're using Zsh (default on newer macOS), or nano ~/. bash profile for Bash.

3. In the file that opens, add export OPENAI API KEY="your api key here" at the end.

4. Save changes by pressing Ctrl + 0, then Enter. Exit by pressing ctrl + X

5. Type source ~/.zshre Or source ~/. bash profile to reload the profile.

6.  Verify the setup by typing echo $OPENAI_API_KEY in the terminal. It should display your API key.


## Run Locally

Clone the project

```bash
  git clone https://github.com/xf4c70r/GameBoi.git
```

Go to the project directory

```bash
  cd GameBoi
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run the main file

```bash
  python3 main.py
```

<!-- ## Demo

https://github.com/xf4c70r/GameBoi/assets/57385228/975c3747-860d-4541-bc77-795d2f2fa997 -->
