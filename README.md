# 🎬 What Do I Watch
What Do I Watch is a Discord bot that helps you discover movies randomly, either from all genres or a specific genre, using the TMDB (The Movie Database) API.

---

## Features
- 🎯 Slash commands for easy usage:
  - /ping – Check if the bot is online.
  - /randommovie [genre] – Get a random movie, optionally filtered by genre.
- 🔍 Autocomplete for movie genres.
- 🎨 Rich embed messages with movie title, description, and poster.
- ⚡ Lightweight and fast using discord.py (Pycord).

---

## Requirements
- Python 3.11+
- discord.py (Pycord)
- requests
- python-dotenv

---

## Setup
1. Clone this repository:
```
git clone https://github.com/your-username/your-repo.git
cd your-repo
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Create a ```.env``` file in the project root with your credentials:
```
DISCORD_TOKEN=your_discord_bot_token
TMDB_API_KEY=your_tmdb_api_key
```
4. Run the bot:
```
python bot.py
```

---

## Notes
- Make sure the bot has permission to Send Messages and Embed Links in the server channels.
- ```genres.json``` must contain all the movie genres and their TMDB IDs.

## License
MIT License – feel free to modify and use it.

