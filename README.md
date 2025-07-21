# Idea Logger Bot

A simple Discord bot that lets users save and list their ideas using slash commands. Ideas are stored in a text file and can be viewed with `/listideas`. Built with Python and discord.py.

## Features

- `/idea <your idea>`: Save a new idea.
- `/listideas`: List the last 10 saved ideas.

## Setup

1. **Clone the repository:**
   ```
   git clone https://github.com/mintcodec/idea-logger
   cd idea-logger-bot
   ```

2. **Install dependencies:**
   ```
   pip install discord.py python-dotenv
   ```

3. **Create a `.env` file in the project folder:**
   ```
   DISCORD_TOKEN=your_token_here
   ```
   Replace `your_token_here` with your Discord bot token.

4. **(Optional) Create an empty `ideas.txt` file:**  
   The bot will create this automatically if it doesn't exist.

5. **Run the bot:**
   ```
   python bot.py
   ```

## Notes

- Do **not** share your `.env` file or bot token publicly.
- Make sure `.env` and `ideas.txt` are listed in your `.gitignore` file.

## License

MIT
