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

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file. You need to add your OpenAI api key. 

`OPENAI_API_KEY`




##  Steps For Adding 'openai_api_key' To Your Environment Variables

1. Open the Start Menu.

2. Search for “Environment Variables” and click on “Edit the system environment variables.”

3. Click the “Environment Variables” button.

4. Under “User variables,” click “New” and enter the variable name and value.
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
  pip install pygame
```
```bash
  pip install openai
```

Run the main file

```bash
  python3 main.py
```

## Demo

Insert gif or link to demo

## License

Copyright (c) 2023 Arvind Sudarshan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.