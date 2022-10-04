import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='.',intents=discord.Intents.all())

@bot.command()
async def gen(ctx, account = None):
  if account == None:
    embed = discord.Embed(title='Invalid', description='Você não indicou o tipo de conta no comando')
    await ctx.send(embed=embed)

  elif account == "random":
    account = random.choice(open("accounts.txt").readlines())
    embed = discord.Embed(title="Generated!", description="Olhe suas dms (as vezes pode ter contas duplicadas, então caso não funcione regenere sua conta!)")
    em = discord.Embed(title=f"""
    Sua conta foi gerada com sucesso! para copia apenas aperte e segure ou passe o mouse em cima e copie!

    ```{account}```
""")
    await ctx.author.send(embed=em)
    await ctx.send(embed=embed)
    
@bot.command()
async def stock(ctx):
   with open("accounts.txt") as file:
     accounts = len (file.readlines())
     em = discord.Embed(title='Stock', description=f'Stock: **{accounts}** em stock!')
      
     await ctx.send(embed=em)
bot.run('your token here')