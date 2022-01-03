import aiohttp
import asyncio
from bot import DiscordBot
from config import discord_token


class Clockwork:

    def __init__(self, loop=None) -> None:
        self.ws = None
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.discord = DiscordBot(command_prefix='>')

    async def print_message(self, data):
        print(await data)

    async def listen_discord(self):
        while True:
            await self.discord.start(discord_token)

    def tick(self):
        self.loop.create_task(self.listen_discord())
        self.loop.run_forever()


if __name__ == '__main__':
    cw = Clockwork()
    cw.tick()
