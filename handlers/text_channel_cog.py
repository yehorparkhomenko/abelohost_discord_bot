from typing import Text
from discord import Message
from discord.ext import commands

from bot import bot
from models.member import Member


class TextChannelCog(commands.Cog):
    users_messages_count = dict()
    
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        user_id = message.author.id
        server_id = message.guild.id
        united_id = int(str(user_id) + str(server_id))

        try:
            member = Member.get(Member.user_id == user_id, Member.server_id == server_id)
        except:
            member = Member(user_id=user_id, server_id=server_id)
            member.save()

        if united_id not in self.users_messages_count.keys():
            self.users_messages_count[united_id] = 1
        else:
            self.users_messages_count[united_id] += 1;

        if self.users_messages_count[united_id] % 20 == 0:
            member.level += 1
            member.save()
            await message.channel.send("Пользователь {0.mention} получил {1} уровень.".format(message.author, member.level))


bot.add_cog(TextChannelCog(bot))