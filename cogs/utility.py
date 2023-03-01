import discord
import interactions
from discord.ext import commands
from discord import app_commands
from discord.ui import View
from lib.buttons import BotButton, ServerButton
import time

class Utility(commands.Cog):
    def __int__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 60 * 60 * 48, commands.BucketType.user)
    @commands.has_role("ping")
    async def ping(self, ctx):
        await ctx.send(ctx.guild.default_role)
        await ctx.message_delete

    @app_commands.command(name="embed", description="creates custom embed")
    @app_commands.default_permissions(manage_channels=True)
    async def embed(self, interaction, title: str, description: str):
        customembed = discord.Embed(
            title=title,
            description=description,
            colour=discord.Colour.red()
        )
        await interaction.response.send_message(embed=customembed)

    @app_commands.command(name="create", description="creates text channel")
    @app_commands.default_permissions(manage_channels=True)
    async def create(self,ctx, name: str, category: str):
        guild = ctx.guild
        category = discord.utils.get(ctx.guild.categories, name=category)
        await guild.create_text_channel(name=name, category=category)
        successembed= discord.Embed(
            title="Success",
            description="Your channel has been created.",
            colour=discord.Colour.green()
        )
        await ctx.response.send_message(embed=successembed)




    @commands.command("rule0")
    async def rule0(self, ctx: commands.Context):
        await ctx.send("https://tenor.com/view/goku-rule-rule0-dragon-ball-gif-23837411")
        await ctx.message.delete()

    @app_commands.command(name="help", description="Information über den Bot/ über den Server.")
    async def help(self, interation: interactions.Interaction):
        helpembed = discord.Embed(title="Informationen!",
                                  description=f"**Um eine Information zu sehen, musst du einen der unteren Knöpfe drücken!**\nWenn du Kontakt zum Team brauchst, dann öffne ein Ticket!",
                                  colour=discord.Colour.red())
        view = View()
        view.add_item(BotButton())
        view.add_item(ServerButton())

        await interation.response.send_message(embed=helpembed, view=view, ephemeral=True)

    @app_commands.command(name="nuke", description="Säubert den Channel.")
    @app_commands.default_permissions(manage_channels=True)
    async def nuke(self, ctx: interactions.CommandContext):
        await ctx.channel.purge()
        await ctx.response.send_message(f"Nuked by `{ctx.user}`!")

    @app_commands.command(name="hello", description="Grüß doch mal!")
    async def hello(self, interation: interactions.Interaction):
        await interation.response.send_message(f"Salam {interation.user.mention}, ich hoffe dir geht es gut!")


async def setup(bot: commands.Bot):
    await bot.add_cog(
        Utility(bot),
        guilds=[discord.Object(id=1073900373577846835)]
    )
