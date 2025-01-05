import disnake
import disnake.ext
from disnake.ext import commands
from src.modules.creator import Creator
from src.modules.loader import Loader
from src.modules.starter import Starter
from src.utils.files_loader import load_config

prefix = load_config()['prefix']

bot = commands.Bot(
    command_prefix=prefix,
    intents=disnake.Intents.all(),
    case_insensitive=True
)

class main:
    def __init__(self):
        Creator()
        Loader(bot)
        Starter(bot)

if __name__ == "__main__":
    main()