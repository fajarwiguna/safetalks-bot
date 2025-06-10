from discord.ext import commands

class ThresholdCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.thresholds = {
            "hate": 0.80,
            "offensive": 0.85
        }

    @commands.command(name="set_threshold", help="Set confidence threshold (Admin only)")
    async def set_threshold(self, ctx, category: str, value: float):
        if not ctx.author.guild_permissions.administrator:
            await ctx.send("🚫 You don't have permission to use this command.")
            return

        category = category.lower()
        if category in self.bot.thresholds:
            self.bot.thresholds[category] = value
            await ctx.send(f"✅ Threshold for **{category}** set to **{value:.2f}**")
        else:
            await ctx.send("❌ Invalid category. Use `hate` or `offensive`.")
            
async def setup(bot):
    await bot.add_cog(ThresholdCommand(bot))