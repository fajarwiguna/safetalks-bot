import discord
from discord.ext import commands
import pandas as pd
import os

LOG_PATH = "logs/violations.csv"

class ClearLogCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clear_log", help="Clear violation logs (admin only)")
    @commands.has_permissions(administrator=True)
    async def clear_log(self, ctx, mode: str = None, arg: str = None):
        if not os.path.exists(LOG_PATH):
            await ctx.send("⚠️ No log file found.")
            return

        try:
            df = pd.read_csv(LOG_PATH)
        except Exception as e:
            await ctx.send(f"❌ Failed to read logs: {e}")
            return

        df = pd.read_csv(LOG_PATH)
        guild_id = str(ctx.guild.id) if ctx.guild else None
        df["GuildID"] = df["GuildID"].astype(str)  # 👈 tambahkan ini
        df_guild = df[df["GuildID"] == guild_id]

        original_count = len(df_guild)

        if mode == "all":
            # Hapus semua log di guild ini
            df = df[df["GuildID"] != guild_id]
            msg = f"🧹 All logs have been cleared for this server. ({original_count} removed)"

        elif mode == "user" and arg:
            # Hapus log user di guild ini
            before_count = len(df)
            df = df[~((df["GuildID"] == guild_id) & (df["Username"] == arg))]
            removed = before_count - len(df)
            msg = f"🧹 Logs for user `{arg}` in this server have been cleared. ({removed} removed)"

        elif mode == "last" and arg and arg.isdigit():
            count = int(arg)
            # Hapus last count log dari guild ini
            df_guild_sorted = df_guild.tail(count)
            indices_to_remove = df_guild_sorted.index
            df = df.drop(indices_to_remove)
            msg = f"🧹 Last {count} log(s) have been removed for this server. ({len(indices_to_remove)} removed)"

        else:
            await ctx.send("⚠️ Invalid command format.\nExamples:\n• `!clear_log all`\n• `!clear_log user <username>`\n• `!clear_log last <count>`")
            return

        try:
            df.to_csv(LOG_PATH, index=False)
            await ctx.send(msg)
        except Exception as e:
            await ctx.send(f"❌ Failed to save updated log file: {e}")

    @clear_log.error
    async def clear_log_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("🚫 You don't have permission to use this command.")
        else:
            await ctx.send(f"❌ Error: {str(error)}")

async def setup(bot):
    await bot.add_cog(ClearLogCommand(bot))