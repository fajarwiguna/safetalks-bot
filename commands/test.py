from discord.ext import commands
from utils.predict import predict_text

class TestCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("✅ TestCommand Cog loaded")  # Tambahan log

    @commands.command(name="test", help="Test Text Classification")
    async def test_command(self, ctx, *, text: str = None):
        if not text:
            await ctx.send("⚠️ Please provide a message to test.\nUsage: `!test <your text>`")
            return

        print(f"📨 Received test command with text: {text}")  # Tambahan log
        result = predict_text(text)
        await ctx.send(
            f'📊 **Prediction Test**\n'
            f'**Original:** {text}\n'
            f'**Cleaned:** {result["cleaned"]}\n'
            f'**Class:** {result["predicted_class"]} ({result["confidence"]:.2f})\n'
            f'**Scores:**\n'
            f'   • Hate Speech: {result["scores"]["Hate Speech"]:.4f}\n'
            f'   • Offensive: {result["scores"]["Offensive"]:.4f}\n'
            f'   • Neither: {result["scores"]["Neither"]:.4f}'
        )

async def setup(bot):
    await bot.add_cog(TestCommand(bot))
    print("📦 Running setup for TestCommand")  # Tambahan log
