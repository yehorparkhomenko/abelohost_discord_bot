import os 

from bot import bot
from handlers import *


bot.run(os.environ['TOKEN'])
