#librería discord
import discord
from discord.ext import commands
from discord import app_commands
from token_1 import token

#archivo
import os

def create_file(nombre_Archivo):
    try:
        with open(nombre_Archivo, 'w') as f:
            f.write('-Nº VECES-')
            f.close()
        print("Archivo: `" + nombre_Archivo + "` creado.")
    except IOError:
        print("Error: no se puede crear `" + nombre_Archivo + "`.")

def append_file(nombre_Archivo, text):
    try:
        with open(nombre_Archivo, 'a') as f:
            f.write(text)
        print("Texto añadido al archivo: `" + nombre_Archivo + "`.")
    except IOError:
        print("Error: no se pudo añadir texto a `" + nombre_Archivo + "`.")

#create_file("gnight.txt")

#tiempo actual
from datetime import datetime
now = datetime.now()
current_now = now.strftime("%D: %H:%M:%S")

bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} is ready")
    await bot.tree.sync(guild=discord.Object(id = 771108283783970836))
async def on_command_error(self, ctx, error):
    await ctx.reply(error, ephemeral= True)

@bot.hybrid_command(name="gnight", with_app_command = True, description="zzz")
@app_commands.guilds(discord.Object(id = 771108283783970836))
async def votar(ctx:commands.Context):
    mensajito = f'\n-> {ctx.author} ha usado goodnight, con un ID de {ctx.author.id} : [{current_now}]'
    print(mensajito)
    append_file('gnight.txt', mensajito)
    await ctx.defer(ephemeral = False)
    await ctx.reply("buenas noches precioso")

bot.run(token)