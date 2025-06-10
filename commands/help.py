from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", help="Shows this message")
    async def help_command(self, ctx):
        help_text = (
            "📘 **Help Menu**\n\n"
            "• `!help` – Show this help message\n"
            "• `!test <text>` – Classify any text and see its prediction and confidence\n"
            "• `!log [count]` – Show recent violation logs (default: 5, max: 20)\n"
            "• `!clear_log <mode>` – Clear logs: `all`, `user <name>`, or `last <count>` (admin only)\n"
            "• `!set_threshold <label> <value>` – Change detection threshold for 'Hate Speech' or 'Offensive' (admin only)\n\n"
            "💡 *SafeTalks automatically warns or deletes toxic messages based on detection confidence.*"
            

        )
        await ctx.send(help_text)

async def setup(bot):
    await bot.add_cog(HelpCommand(bot))
