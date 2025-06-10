import csv
import os
from discord.ext import commands

LOG_FILE = "logs/violations.csv"

class LogCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="log", help="Show recent violation logs (default: 5). Usage: !log [amount]")
    async def log_command(self, ctx, count: int = 5):
        if not os.path.exists(LOG_FILE):
            await ctx.send("📂 No logs available yet.")
            return

        with open(LOG_FILE, mode="r", encoding="utf-8") as file:
            reader = list(csv.reader(file))
            logs = reader[1:]  # Skip header row

        if not logs:
            await ctx.send("📂 No logs available yet.")
            return

        count = max(1, min(count, 20))  # Clamp count between 1 and 20
        last_logs = logs[-count:]

        message = "📄 **Recent Violations**\n\n"
        for log in reversed(last_logs):
            timestamp, username, userid, msg, predicted, confidence, action = log
            message += (
                f"• **{username}** ({predicted}, {confidence}) – {action}\n"
                f"   _\"{msg[:80]}\"_ \n"
            )

        await ctx.send(message)

async def setup(bot):
    await bot.add_cog(LogCommand(bot))
