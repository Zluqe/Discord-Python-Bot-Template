import disnake
from disnake.ext import commands
from src.utils.files_loader import load_config
from datetime import datetime

class Starter:
    def __init__(self, bot):
        self.bot = bot
        self.token = load_config()['token']
        self.setup_events()
        self.start()

    def setup_events(self):
        @self.bot.event
        async def on_ready():
            print(f"🔱 Logged in as {self.bot.user} (ID: {self.bot.user.id})")
            print(f"🔱 Prefix: {self.bot.command_prefix}")
            print(f"🔱 {len(self.bot.guilds)} servers")
            print(f"🔱 {len(self.bot.users)} users")
            print(f"🔱 {len(self.bot.commands)} commands")
            print(f"🔱 Latency: {round(self.bot.latency * 1000)}ms")
            print(f"🔱 Connected at {datetime.now().strftime('%H:%M:%S')}")

    def start(self):
        try:
            self.bot.run(self.token)
        except Exception as e:
            print("Failed to start bot")
            print(e)
            exit()