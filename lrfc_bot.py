import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random

lines = [
    "New **LRFC** alert! Looks like someone spilled another LRFC into the server! 🎉 Check out {0}.",
    "Look out! A wild **LRFC** has appeared and it's bringing groundbreaking changes! 🚀✨ See it at {0}.",
    "Beep boop! Detected a fresh **LRFC** with a 100% chance of innovation ahead! 🚀 Tune in at {0}.",
    "Alert! The Lyra-awesome-meter is hitting new highs with this **LRFC**! 📈 Discover more at {0}.",
    "Breaking News: A game-changing **LRFC** has landed. Fasten your seatbelts for awesome improvements! 🎢❤️ Details at {0}.",
    "Just so you know, I might be a bit biased towards this latest **LRFC**! 🤖❤️ See why at {0}.",
    "Galactic Update: The latest **LRFC** might be our coolest discovery yet! 🌌 Explore it at {0}.",
    "Eureka! A groundbreaking **LRFC** is here. Time to gear up for innovation! 🛠️🌟 Dive in at {0}.",
    "Hey innovators, a fresh **LRFC** is shaking things up! 💡🌪️ Catch the wave at {0}.",
    "Lyra pioneers, assemble! A new **LRFC** is rewriting the rules! 📜✨ Details at {0}.",
    "Guess what? A new **LRFC** has just made its entry, launching us into an era of innovation! 🚀🌌 See at {0}.",
    "Alert: New **LRFC** on the horizon. Probability of major improvements: sky-high! 🎯🔥 Check it out at {0}.",
    "A wild **LRFC** is here and it's super effective at sparking change! ⚡🌈 Discover how at {0}.",
    "New **LRFC** incoming! Time to brainstorm some brilliant ideas. 🧠💭 Join in at {0}.",
    "Prepare for impact! A revolutionary **LRFC** is here to shake up Lyra! 🌪️💫 Check it at {0}.",
    "All aboard the innovation train! Next stop: this amazing **LRFC**! 🚂🛤️ See more at {0}.",
    "Dive into creativity with the new **LRFC**! 🌊🔮 Uncover the wisdom at {0}."
]
# Load environment variables from .env file
load_dotenv()
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
DISCORD_GUILD_ID = int(os.getenv("DISCORD_GUILD_ID"))
DISCORD_GENERAL_CHANNEL_ID = int(os.getenv("DISCORD_GENERAL_CHANNEL_ID"))

# Define intents
intents = discord.Intents.default()

# Initialize the bot with the defined intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_guild_channel_create(channel):
    # Check if the channel is in the specific guild and follows the naming pattern
    if channel.guild.id == DISCORD_GUILD_ID and channel.name.lower().startswith('lrfc-'):
        general_channel = bot.get_channel(DISCORD_GENERAL_CHANNEL_ID)
        if general_channel:
            random_line = random.choice(lines)
            message_template = "🚨 @everyone 📢 " + random_line
            message = await general_channel.send(message_template.format(channel.mention))
            # Add reactions
            try:
                custom_emoji = discord.utils.get(channel.guild.emojis, name='heart')  # Replace 'heart' with your emoji's name
                if custom_emoji:
                    await message.add_reaction(custom_emoji)
                await message.add_reaction("🔥")  # Add fire emoji
                custom_emoji = discord.utils.get(channel.guild.emojis, name='Lyra')  # Replace 'Lyra' with your emoji's name
                if custom_emoji:
                    await message.add_reaction(custom_emoji)
            except Exception as e:
                print(f"Error adding reactions: {e}")

# Run the bot with the token from the .env file
bot.run(DISCORD_BOT_TOKEN)
