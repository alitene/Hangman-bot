import os
from dotenv import load_dotenv
import asyncio
from Hangman import Hangman as hm
import discord
from discord.ext import commands
intents = discord.Intents.all()
intents.members = True
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f"{bot.user} is online!")
@bot.command()
async def hangman(ctx):
    user = await bot.fetch_user(ctx.author.id)
    await user.send("What is your phrase?")
    msg = await bot.wait_for('message', check=lambda message: message.author == user)
    phrase = msg.content.title()
    a = hm(phrase)

    def check(m):
        return m.channel == ctx.channel
    try:
        while a.placeholder.count("_") != 0:
            b = a.placeholder
            await ctx.send(f"{b.replace('_', '-')}\nGuess the letter or the phrase")
            guess = await bot.wait_for("message",check=check,timeout=60)
            message = str(guess.content)
            result = a.check_guess(message)
            if result == True:
                a.place_guess(message)
            elif result == "Guessed".upper():
                await ctx.send(f"You already guessed {message.upper()}\n ")
            elif result == "SOLVED":
                await ctx.send(f"You guessed correctly the phrase was: '{phrase}'\n ")
                return
            elif result == False:
                counter = len(a.wrong_guesses)
                if counter < 7:
                    await ctx.send(f"Sorry, there are no {message.upper()} in the phrase\n ")
                elif counter >= 7:
                    await ctx.send(f'Sorry, you guessed wrong too many time the phrase was: "{phrase}"\n ')
                    return
            elif result == "Too Many Letters".upper():
                await ctx.send(f"Sorry, too many letters and not enough or too many letters to be the phrase\n ")
        if "result" not in locals().copy() or (eval("result") != "SOLVED" and eval("result") != False):
            await ctx.send(f'you solved the phrase it was: "{phrase}"')
    except asyncio.TimeoutError:
        await ctx.send("Hangman has Timed Out")
    except Exception as e:
        await ctx.send("An error has occurred")
        print(f"Unexpected error: {e}")
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
bot.run(token)