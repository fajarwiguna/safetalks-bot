from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", help="Shows this message")
    async def help_command(self, ctx):
        help_text = "📘 **Help Menu**\n\n"
        for command in self.bot.commands:
            help_text += f"• `!{command.name}` – {command.help}\n"
        await ctx.send(help_text)

async def setup(bot):  # ✅ harus async!
    await bot.add_cog(HelpCommand(bot))  # ✅ harus pakai await
