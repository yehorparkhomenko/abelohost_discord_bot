from discord import Member, member
from discord.ext import commands

from bot import bot


help_text = '''
.help - помощь
.kick @username - кикнуть пользователя
.ban @username - забанить пользователя
.unban @username - разбанить пользователя
'''


class CommandsCog(commands.Cog):
    users = dict()

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def help(self, ctx):
        await ctx.send(help_text)

    @commands.command()
    async def kick(self, ctx, *, member: Member):
        await member.kick()
        await ctx.send('пользователь {0.mention} кикнут!'.format(member))

    @commands.command()
    async def ban(self, ctx, *, member: Member):
        await member.ban()
        await ctx.send('пользователь {0.mention} забанен!'.format(member))

    @commands.command()
    async def unban(self, ctx, *, username):
        username = username.replace('<', '').replace('>', '')
        if username.startswith('@!'):
            print(1)
            id = username.replace('@!', '')
            print(id)
            for ban in await ctx.guild.bans():
                print(ban)
                if str(ban.user.id) == id:
                    await ctx.guild.unban(ban.user)
                    await ctx.send('пользователь @{0} разбанен!'.format(ban.user.name))
                    return
        else:  
            username = username.replace('@', '')
            member_name = username.split('#')[0]
            for ban in await ctx.guild.bans():
                if ban.user.name == member_name:
                    await ctx.guild.unban(ban.user)
                    await ctx.send('пользователь @{0} разбанен!'.format(ban.user.name))
                    return
        await ctx.send('Пользователь  не найден!')

            
bot.add_cog(CommandsCog(bot))