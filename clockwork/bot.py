import asyncio
from config import discord_token
import discord
from discord.ext import commands
from pprint import PrettyPrinter
import random
pp = PrettyPrinter(indent=4)


class DiscordBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        """
        Daily Briefing: return webull top active + gainers
        """
        @self.command(name='brief', help='')
        async def dd(ctx):
            r = {'lol': 'haha'}
            await ctx.send(r)

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
