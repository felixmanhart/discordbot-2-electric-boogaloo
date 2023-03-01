import discord
from main import Client
from discord.ext.commands import Cog, MissingRole, CommandOnCooldown
import time



class ErrorHandler(Cog):

    def __init__(self, bot: Client):
        self.bot = bot

    @Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRole):
            embed1 = discord.Embed(title="Error", description="Missing Permission!", colour=discord.Colour.red())
            await ctx.send(embed=embed1)

        if isinstance(error, CommandOnCooldown):
            embed = discord.Embed(title="Error", description='Can\'t ping. Try again in <t:{}:R>'.format(int(time.time() + error.retry_after)),
                                  colour=discord.Colour.red())
            await ctx.send(embed=embed, delete_after=60)


async def setup(bot: Client):
    await bot.add_cog(
        ErrorHandler(bot),
        guilds=[discord.Object(id=1040220674226139206)]
    )
