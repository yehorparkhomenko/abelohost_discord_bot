from discord import Member, member
from discord.ext import commands

from bot import bot


help_text = '''
.help - помощь
.kick <username> - кикнуть пользователя
.ban <username> - забанить пользователя
.unban <username> - разбанить пользователя
'''


class CommandsCog(commands.Cog):
    users = dict()

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def help(self, ctx, *, member: Member):
        await ctx.send(help_text)

    @commands.command()
    async def kick(self, ctx, *, member: Member):
        await member.kick()

    @commands.command()
    async def ban(self, ctx, *, member: Member):
        await member.ban()

    @commands.command()
    async def unban(self, ctx, *, username):
        username = username.replace('@', '')
        member_name = username.split('#')[0]
        for ban in await ctx.guild.bans():
            if ban.user.name == member_name:
                await ctx.guild.unban(ban.user)
            

bot.add_cog(CommandsCog(bot))