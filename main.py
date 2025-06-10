import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

# Thresholds (mutable global state)
thresh_hate = 0.80
thresh_offensive = 0.85

class SafeTalksBot(commands.Bot):
    async def setup_hook(self):
        await self.load_extension("commands.help")
        await self.load_extension("commands.test")
        await self.load_extension("commands.log")
        await self.load_extension("commands.threshold")

bot = SafeTalksBot(command_prefix='!', intents=intents, help_command=None)

from utils.predict import predict_text
from utils.logger import log_violation

@bot.event
async def on_ready():
    print(f'✅ Bot logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith(bot.command_prefix):
        await bot.process_commands(message)
        return

    content = message.content
    result = predict_text(content)
    predicted_class = result["predicted_class"]
    confidence = result["confidence"]

    if predicted_class == "Hate Speech" and confidence >= bot.thresholds["hate"]:
        await message.delete()
        await message.channel.send(f'🚫 Message from {message.author.mention} was removed due to **Hate Speech**.')
        log_violation(message.author, message, result, "Deleted")
    elif predicted_class == "Offensive" and confidence >= bot.thresholds["offensive"]:
        await message.channel.send(f'⚠️ Warning to {message.author.mention}: your message contains **Offensive Content**.')
        log_violation(message.author, message, result, "Warned")


    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print(f'❌ Command not found: {ctx.message.content}')
    else:
        print(f'❗ Error: {error}')

bot.run(TOKEN)
