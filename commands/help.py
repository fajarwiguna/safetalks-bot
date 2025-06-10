from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", help="Shows this message")
    async def help_command(self, ctx):
        help_text = (
            "📘 **Help Menu**\n\n"
            "• `!help` – Shows this message\n"
            "• `!test <text>` – Test message classification\n"
            "• `!log [count]` – Show recent violation logs (default: 5, max: 20)\n"
            "• `!set_threshold <label> <value>` – Set detection threshold (admin only)\n"
        )
        await ctx.send(help_text)

async def setup(bot):
    await bot.add_cog(HelpCommand(bot))
