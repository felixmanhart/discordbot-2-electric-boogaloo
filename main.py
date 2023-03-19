import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


class Client(commands.Bot):

    def __init__(self, command_prefix, application_id, exts):
        super().__init__(
            command_prefix=command_prefix,
            application_id=application_id,
            intents=discord.Intents.all()
        )

        self.initial_extensions = exts

    async def setup_hook(self):
        for ext in self.initial_extensions:
            await self.load_extension(ext)
            print("Loaded " + ext + " successfully")

        await bot.tree.sync(guild=discord.Object(id=1073900373577846835))



    async def on_ready(self):
        await bot.change_presence(activity=discord.Game(name="Raion's Shop"))
        print(f"Bot is online")


if __name__ == "__main__":
    initial_extensions = [
        "cogs.utility",
        "cogs.error"
    ]

    bot = Client(command_prefix="$", application_id=1074229915584565338, exts=initial_extensions)
    bot.run(os.getenv("TOKEN"))
    