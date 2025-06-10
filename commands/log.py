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
            logs = reader[1:]  # skip header

        if not logs:
            await ctx.send("📂 No logs available yet.")
            return

        guild_id = str(ctx.guild.id) if ctx.guild else "DM"

        # Filter hanya logs yang sesuai guild_id saat ini
        logs_guild = [log for log in logs if log[1] == guild_id]

        if not logs_guild:
            await ctx.send("📂 No logs found for this server.")
            return

        count = max(1, min(count, 20))  # clamp count
        last_logs = logs_guild[-count:]

        message = "📄 **Recent Violations**\n\n"
        for log in reversed(last_logs):
            timestamp, guild, username, userid, msg, predicted, confidence, action = log
            confidence = float(confidence)
            action_clean = action.strip().lower()
            msg_snippet = msg[:80].replace("`", "'")

            if action_clean == "deleted":
                action_display = "**Deleted**"
                message += (
                    f"• **{username}** ({predicted}, {confidence:.4f}) – {action_display}\n"
                    f"   `\"{msg_snippet}\"`\n"
                )
            elif action_clean == "warned":
                action_display = "Warned"
                message += (
                    f"• **{username}** ({predicted}, {confidence:.4f}) – {action_display}\n"
                    f"   _\"{msg_snippet}\"_\n"
                )
            else:
                message += (
                    f"• **{username}** ({predicted}, {confidence:.4f}) – {action}\n"
                    f"   _\"{msg_snippet}\"_\n"
                )

        await ctx.send(message)

async def setup(bot):
    await bot.add_cog(LogCommand(bot))
