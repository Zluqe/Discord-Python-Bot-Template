import disnake
from disnake.ext import commands


class SayCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('🔩 /say has been loaded')

    @commands.slash_command(name="say", description="Make the bot say something")
    async def say(self, inter, *, content: str):
        try:
            await inter.response.defer()
            await inter.edit_original_message(content=content)
            print(f"🔊 {content}")
        except Exception as e:
            print("An error occured while executing /say command")
            print(e)
            await inter.send(f'```{e}```')

def setup(bot):
    bot.add_cog(SayCommand(bot))