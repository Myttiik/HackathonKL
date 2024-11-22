import discord
from discord.ext import commands
import os, random
import requests

#.
def consejo_aleatorio(consejos = "consejos.txt"):
    try:
        with open(consejos, "r", encoding="utf-8") as c_diccionario:
            consejos_e = c_diccionario.readlines()
        return random.choice(consejos_e).strip()
    except FileNotFoundError:
        return "No se pudo accesar a la base de datos de consejos sobre como ayudar a mitigar el cambio climático "

def noticia_aleatoria(noticias= "noticias.txt"):
    try:
        with open(noticias, "r", encoding="utf-8") as n_diccionario:
            noticias_e = n_diccionario.readlines()
        return random.choice(noticias_e).strip()
    except FileNotFoundError:
        return "No se pudo accesar a la base de datos de noticias sobre el cambio climático"

def transporte_aleatorio(transportes= "transportes.txt"):
    try:
        with open(transportes, "r", encoding="utf-8") as t_diccionario:
            transportes_e = t_diccionario.readlines()
        return random.choice(transportes_e).strip()
    except FileNotFoundError:
        return "No se pudo accesar a la base de datos de transportes amigables con el medio ambiente"

def energia_aleatoria(energias= "energias.txt"):
    try:
        with open(energias, "r", encoding="utf-8") as e_diccionario:
            energias_e = e_diccionario.readlines()
        return random.choice(energias_e).strip()
    except FileNotFoundError:
        return "No se pudo accesar a la base de datos de energías sustentables"
    
def img_noticia_aleatoria(imagenes="img_noticias"):
    try:
        imgs_e = [imagen for imagen in os.listdir(imagenes) if imagen.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp", "avif"))]
        if not imgs_e:
            return None
        return os.path.join(imagenes, random.choice(imgs_e))
    except FileNotFoundError:
        return "No se pudo accesar a la base de datos de las imagenes"

def img_energia_aleatoria(energ_img="img_energias"):
    try:
        imgs_e = [imagen for imagen in os.listdir(energ_img) if imagen.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp", "avif"))]
        if not imgs_e:
            return None
        return os.path.join(energ_img, random.choice(imgs_e))
    except FileNotFoundError:
        return "No se pudo accesar a la base de datos de las imagenes"



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'PyTure Bot apareció{bot.user}')

@bot.command()
async def Saludo(ctx):
    await ctx.send(f'Hola! Soy PyTure Bot {bot.user}!')

@bot.command()
async def Consejo(ctx):
    c_comando = consejo_aleatorio()
    await ctx.send(c_comando)

@bot.command()
async def Noticia(ctx):
    n_comando = noticia_aleatoria()
    n_c_img = img_noticia_aleatoria()
    await ctx.send(content=n_comando, file=discord.File(n_c_img))

@bot.command()
async def Energia(ctx):
    e_comando = energia_aleatoria()
    e_c_img = img_energia_aleatoria()
    await ctx.send(content=e_comando, file=discord.File(e_c_img))

@bot.command()
async def Transporte(ctx):
    t_comando = transporte_aleatorio()
    await ctx.send(t_comando)
    

bot.run("Token")