import discord
from discord.ext import commands
import random
import time


class Games:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def rps(self):
        """Replies with Rock, Paper or Scissors.
        (You are expected to claim your action after the \"rps\")"""
        await self.bot.say(random.choice(("Rock", "Paper", "Scissors")))
    
    @commands.command()
    async def ping(self):
        """Checks the bot's ping.
        Should reply with "Pong!\"."""
        t = time.time()
        await self.bot.say("Pong!")
        await self.bot.say(str(int((time.time() - t) * 1000)) + "ms ping.")
    
    @commands.command(pass_context=True)
    async def spam(self, ctx, *, msg="This is spam"):
        """Sends some spam.
        You can specify how much spam and what to spam with a number after the >spam command
        eg. >spam 5 Hello There! would sens "Hello There!" 5 times."""
        msg = msg.split()
        try:
            if int(msg[0]) > 50:
                await self.bot.say("That is too much spam. I will only spam 50x")
                msg[0] = "50"
            try:
                for _ in range(int(msg[0])):
                    await self.bot.say(" ".join(msg[1:]))
            except:
                for _ in range(int(msg[0])):
                    await self.bot.say("This is spam.")
        except:
            for _ in range(10):
                await self.bot.say(" ".join(msg))
    
    @commands.command()
    async def echo(self, *, msg):
        """Repeats the message back to you."""
        await self.bot.say(msg)
    
    #@commands.command()
    #async def traffic_light(self):
    #    """Does a traffic light thing with it's status thing.
    #    As requested by Adam for some reason"""
    #    await self.bot.change_presence(status=discord.Status.idle)
    #    time.sleep(2)
    #    await self.bot.change_presence(status=discord.Status.dnd)
    #    time.sleep(2)
    #    await self.bot.change_presence(status=discord.Status.online)
        

    #@commands.command(pass_context=True)
    #async def kys(self, ctx):
    #    """Gets the bot to leave the server."""
    #    print(ctx.message.server)
    #    await self.bot.leave_server(ctx.message.server)


def setup(bot):
    bot.add_cog(Games(bot))
