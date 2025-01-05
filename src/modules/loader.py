import os

from src.data.var import folders


class Loader():
    def __init__(self, bot):
        self.bot = bot
        self.load_cogs()

    def load_cogs(self):
        for element in os.listdir(folders['cogs']):
            try:
                elementDir = f"{folders['cogs']}{element}"
                if os.path.isdir(elementDir):
                    for filename in os.listdir(elementDir):
                        if filename.endswith(".py"):
                            cogName = filename[:-3]
                            try:
                                self.bot.load_extension(f"src.addons.{element}.{cogName}")
                                print(f"Load {filename}")
                            except Exception as e:
                                print(f"Failed to load {filename}")
                                print(e)
                                exit()
            except Exception as e:
                print(f"Failed to load {element}")
                print(e)
                exit()