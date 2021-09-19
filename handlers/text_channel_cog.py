from typing import Text
from discord import Message
from discord.ext import commands

from bot import bot
from models.user import User


class TextChannelCog(commands.Cog):
    users_messages_count = dict()
    
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        user_id = message.author.id
        
        try:
            user = User.get(User.user_id == user_id)
        except:
            user = User(user_id = user_id)
            user.save()

        if user_id not in self.users_messages_count.keys():
            self.users_messages_count[user_id] = 1
        else:
            self.users_messages_count[user_id] += 1;

        if self.users_messages_count[user_id] % 20 == 0:
            user.level += 1
            user.save()
            await message.channel.send("Пользователь {0.mention} получил {1} уровень.".format(message.author, user.level))


bot.add_cog(TextChannelCog(bot))