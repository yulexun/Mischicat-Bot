import os

import discord
from discord.ext import commands


class MischicatBot(commands.Bot):
    def __init__(self):
        prefix = os.getenv("COMMAND_PREFIX", "cat!")
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=prefix, intents=intents)

    async def setup_hook(self):
        await self.load_extension("cogs.music")

    async def on_ready(self):
        print(f"logged in as {self.user}")

    async def on_command_error(self, ctx, error):
        await ctx.send(f"something went wrong: {error}")
