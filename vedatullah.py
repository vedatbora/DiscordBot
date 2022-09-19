from xml.dom.pulldom import CHARACTERS
import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands
import string
import random

TOKEN = ('MTAxODE2ODc3NTIzMDYyMzg0NQ.GALrIR.r-vh6BLT3rEfnyBIAnwjFs3EUtkUKeteV6lKFo')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)

def compose(username):
    URL = 'https://www.leagueofgraphs.com/summoner/tr/' + username

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

    page = requests.get(URL, headers=headers)

    content = BeautifulSoup(page.content,'html.parser')

    summonerName = content.find('div', attrs={'class':'pageBanner'})


    for element in summonerName.find('h2'):
        summonerName = element.text
        
    summonerPoints = content.find('div', attrs={'class':'league-points'}).text

    summonerRank = content.find('div', attrs={'class':'leagueTier'}).text
    
    return [summonerRank + "\n" + summonerPoints, summonerName, URL]


length = 12

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,length)

password = "".join(temp)

@bot.command()
async def sifre(ctx, *args):
    await ctx.send(password)



@bot.command(pass_context=True)
async def volkan(ctx):
    channel= bot.get_channel(1018213804074602566)
    await channel.send('VIZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ')


#@bot.command()
#async def gosu(ctx, *args):
#   await ctx.send(" ".join(args))
#   print(args[0])

@bot.command()
async def gosu(ctx, *args):
    args = "+".join(args)
    userData = compose(args)
    embed=discord.Embed(title=userData[1], url=userData[2], description=userData[0],  color=discord.Color.green())
    await ctx.send(embed=embed)
        
    
@bot.command()
async def hamza(ctx):
    await ctx.send("Arkadaşlar ejder ejder ejdeeeeeeeeeeeeeeeeeeeer!!!!!!!!!!!!")
    

    

    
bot.run(TOKEN)
