import os
import random
import requests
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
GUILD_ID = os.getenv("GUILD_ID")

TMDB_BASE_URL = "https://api.themoviedb.org/3"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, sync_commands=True)

def get_random_movie(genre_id=None):
    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US",
        "sort_by": "popularity.desc",
        "include_adult": "false",
        "include_video": "false",
        "page": random.randint(1, 50)
    }
    if genre_id:
        params["with_genres"] = genre_id
    url = f"{TMDB_BASE_URL}/discover/movie"
    response = requests.get(url, params=params)
    data = response.json()
    if "results" in data and data["results"]:
        return random.choice(data["results"])
    return None

@bot.event
async def on_ready():
    print(f"🤖 Bot {bot.user} está online!")

async def check_permissions(ctx, embed=False):
    perms = ctx.channel.permissions_for(ctx.guild.me)
    if not perms.send_messages:
        try:
            await ctx.author.send("❌ Eu não tenho permissão para enviar mensagens nesse canal!")
        except:
            pass
        return False
    if embed and not perms.embed_links:
        await ctx.send("❌ Eu não tenho permissão para enviar embeds nesse canal!")
        return False
    return True

@bot.slash_command(name="ping", description="Responde Pong!", guild_ids=[GUILD_ID])
async def ping(ctx):
    if await check_permissions(ctx):
        await ctx.respond("🏓 Pong!")

@bot.slash_command(name="randommovie", description="Sorteia um filme aleatório", guild_ids=[GUILD_ID])
async def randommovie(ctx, genre: str = None):
    if not await check_permissions(ctx, embed=True):
        return

    genre_id = None
    if genre:
        genres_url = f"{TMDB_BASE_URL}/genre/movie/list"
        genres_resp = requests.get(
            genres_url, params={"api_key": TMDB_API_KEY, "language": "en-US"}
        ).json()
        genres = {g["name"].lower(): g["id"] for g in genres_resp["genres"]}
        genre_id = genres.get(genre.lower())
        if not genre_id:
            await ctx.respond(f"❌ Gênero **{genre}** não encontrado!")
            return

    movie = get_random_movie(genre_id)
    if movie:
        title = movie["title"]
        overview = movie.get("overview", "Sem descrição disponível.")
        poster_path = movie.get("poster_path")
        poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None

        embed = discord.Embed(title=title, description=overview, color=discord.Color.blue())
        if poster_url:
            embed.set_image(url=poster_url)

        await ctx.respond(embed=embed)
    else:
        await ctx.respond("❌ Não encontrei nenhum filme. Tente novamente!")

bot.run(DISCORD_TOKEN)
