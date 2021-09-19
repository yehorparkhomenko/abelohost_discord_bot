from discord import Member, VoiceState
from discord.ext import commands

from bot import bot


class VoiceChannelCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: Member, before: VoiceState, after: VoiceState):
        if after.channel and member in after.channel.members:
            channel = member.guild.system_channel
            if channel is not None:
                await channel.send('Пользователь {0.mention} вошел в войсчат.'.format(member))
        else:
            channel = member.guild.system_channel
            if channel is not None:
                await channel.send('Пользователь {0.mention} вышел из войсчата.'.format(member))
 

bot.add_cog(VoiceChannelCog(bot))