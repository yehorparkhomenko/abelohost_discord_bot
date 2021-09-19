from discord import Member
from discord.ext import commands

from bot import bot


class UsersWatcherCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member: Member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Пользователь {0.mention} вошел.'.format(member))
    
    @commands.Cog.listener()
    async def on_member_remove(self, member: Member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Пользователь {0.mention} вышел.'.format(member))
 

bot.add_cog(UsersWatcherCog(bot))
