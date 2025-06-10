import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

class SafeTalksBot(commands.Bot):
    async def setup_hook(self):
        await self.load_extension("commands.help")
        await self.load_extension("commands.test")

bot = SafeTalksBot(command_prefix='!', intents=intents, help_command=None)

from utils.predict import predict_text

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

    if predicted_class == "Hate Speech" and confidence >= 0.80:
        await message.delete()
        await message.channel.send(f'🚫 Message from {message.author.mention} was removed due to **Hate Speech**.')
    elif predicted_class == "Offensive" and confidence >= 0.85:
        await message.channel.send(f'⚠️ Warning to {message.author.mention}: your message contains **Offensive Content**.')

    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print(f'❌ Command not found: {ctx.message.content}')
    else:
        print(f'❗ Error: {error}')

bot.run(TOKEN)
