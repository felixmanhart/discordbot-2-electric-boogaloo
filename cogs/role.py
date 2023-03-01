import discord
from discord.ext import commands

client=commands.Bot(command_prefix=commands.when_mentioned_or("$"), intents=discord.Intents.all())

class Role(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

        self.ROLES_CHANNEL = 1043930748664692777
        self.GUILD_ID = 1040220674226139206

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(SelectView())

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def selfroles(self, ctx):
        selfroleembed=discord.Embed(
            title="Ping Roles",
            description="Wähle hier den ping, bei dem du erwähnt werden willst."
        )
        channel = self.bot.get_channel(self.ROLES_CHANNEL)
        await channel.send(embed=selfroleembed, view=SelectView())
        await ctx.send("Sent")

async def setup(bot: commands.Bot):
    await bot.add_cog(
        Role(bot),
        guilds=[discord.Object(id=1040220674226139206)]
    )

ROLES = {
    "RESTOCK PING": 1044351379432538232,
    "GIVEAWAY PING": 1044351422524829729
}

class Select(discord.ui.Select):
    def __init__(self):

        options = [
            discord.SelectOption(label="Giveaway Ping", emoji="🎉", description="Informiert dich über Giveaways!", value="Giveaway Ping"),
            discord.SelectOption(label="Restock Ping", emoji="📢", description="Informiert dich über Stock!", value="Restock Ping"),
            discord.SelectOption(label="Entfernen", emoji="🗑️", description="Löscht deine Ping Roles", value="entfernen")
        ]
        super().__init__(placeholder="Wähle den Ping", max_values=3, min_values=0, options=options, custom_id="select1")


    async def callback(self, interaction: discord.Interaction):
        if "Giveaway Ping" in interaction.data['values']:
            for i in ROLES.values():
                role = interaction.guild.get_role(i)
                if role in interaction.user.roles:
                    await interaction.user.remove_roles(role, atomic=True)

            giveaway_role=interaction.guild.get_role(ROLES["GIVEAWAY PING"])
            await interaction.user.add_roles(giveaway_role, atomic=True, reason="selfrole")

        if "Restock Ping" in interaction.data['values']:
            for i in ROLES.values():
                role = interaction.guild.get_role(i)
                if role in interaction.user.roles:
                    await interaction.user.remove_roles(role, atomic=True)

            giveaway_role=interaction.guild.get_role(ROLES["RESTOCK PING"])
            await interaction.user.add_roles(giveaway_role, atomic=True, reason="selfrole")


        if "entfernen" in interaction.data['values']:
            for i in ROLES.values():
                role = interaction.guild.get_role(i)
                await interaction.user.remove_roles(role, atomic=True)

                embed3=discord.Embed(title="Selfroles entfernt!", colour=discord.Colour.green())
                return await interaction.response.send_message(embed=embed3, ephemeral=True)

        embed1 = discord.Embed(title="Ping hinzugefügt!", colour=discord.Colour.green())
        await interaction.response.send_message(embed=embed1, ephemeral=True)

class SelectView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Select())



