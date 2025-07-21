import discord
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

IDEA_FILE = "ideas.txt"

if not os.path.exists(IDEA_FILE):
    with open(IDEA_FILE, "w") as f:
        f.write("")

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")
    await tree.sync()  

@tree.command(name="idea", description="Save a new idea")
async def save_idea(interaction: discord.Interaction, idea: str):
    user = interaction.user.name
    with open(IDEA_FILE, "a") as f:
        f.write(f"{user}: {idea}\n")
    await interaction.response.send_message(f"🧠 Idea saved: “{idea}”")

@tree.command(name="listideas", description="List the last 10 saved ideas")
async def list_ideas(interaction: discord.Interaction):
    with open(IDEA_FILE, "r") as f:
        ideas = f.readlines()
    if not ideas:
        await interaction.response.send_message("🗒 No ideas saved yet.")
        return
    response = "📋 **Saved Ideas:**\n" + "\n".join(f"- {line.strip()}" for line in ideas[-10:])
    await interaction.response.send_message(response)

client.run(TOKEN)
