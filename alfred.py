#Setup stuff

import asyncio
import json
import discord
from discord.ext import commands
import random
import requests
import hashlib

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

#Pull from config
with open("config.json") as f:
    data = json.load(f)


#Pull from cards.json
with open("cards.json") as f:
    cardData = json.load(f)

#Pull from RockDB
with open("rockDB.json") as f:
    rockDB = json.load(f)


BOT_TOKEN = data["bot-token"]
CHANNEL_ID = data["channel-id"]
PREFIX = data["command-prefix"]

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())
bot.remove_command('help')

#On server join do
@bot.event
async def on_ready():
    print("Alfred online")
    channel = bot.get_channel(CHANNEL_ID)

#Help menu
@bot.command()
async def help(ctx):
    help = discord.Embed(title="Help:")

    help.add_field(name="Command prefix: ~", value="Please put this before the request", inline = False)

    help.add_field(name="Pokedex:", value="poke rand: Returns a random pokemon\npoke (num or name): Returns a specific pokemon", inline=False)

    help.add_field(name="Tarot:", value="tarot (deck) (x): Returns x amount of Tarot cards in selected deck. Decks options are 1 for default and 2 for Abby's cards", inline=False)

    help.add_field(name="Binary:", value="dec2bin: returns decimal value of binary input\nbin2dec: returns base 10 of a binary value")

    help.add_field(name="Hex:", value="dec2hex: returns decimal value of binary input\nhex2dec: returns base 10 of a binary value")

    help.add_field(name="Geoip:", value="geoip (domain or ip): returns geoip info on a target")

    help.add_field(name="Crypto:", value="btc: returns market data \n ltc: returns market data \n xmr: returns market data \n eth: returns market data \n ethc: returns market data \n doge: returns market data \n xrp: returns market data")

    help.add_field(name="Hash:", value="md5 (val), returns md5 hashed input\n sha256 (val) returns sha256 hashed input\n sha512 (val) returns sha512 hashed input")

    help.add_field(name="Define:", value="def: returns dictionary definition of input")

    help.add_field(name="Rocks:", value="rock (val): returns information on a crystal\nrockand: returns information on a random crystal\n rocklist: returns a list of the available crystals")

    help.add_field(name="Goldfish:", value="goldfish")

    help.add_field(name="Robot hash:", value="robohash (val): returns a custom generated robot based on a text input")

    help.add_field(name="Coin flip: ", value="coin (x): flips (x) coins")

    #help.add_field(name="Urban dictionary:", value="udef: returns urban dictionary definition of input")
    #COMING SOON IF I CAN FIND THE API

    await ctx.send(embed=help)

#Pokedex
@bot.command()
async def poke(ctx,arg):

    pokeLowerList = open("nameLower.txt", "r")
    pokeLowerListDatat = pokeLowerList.read()
    pokeLowerListData = pokeLowerListDatat.split(',')

    pokeList = open("name.txt", "r")
    pokeListDatat = pokeList.read()
    pokeListData = pokeListDatat.split(',')

    pokeTypeList = open("type.txt", "r")
    pokeTypeDatat = pokeTypeList.read()
    pokeTypeData = pokeTypeDatat.split(',')

    uInput = arg


    if uInput.isnumeric():
        pokeNumberData = str(uInput).zfill(3)

        query = (int(pokeNumberData) - 1)

        pokeTypeSplit = pokeTypeData[query].split(' | ')
        firstType = pokeTypeSplit[0]

        if firstType.strip() == "Grass":
            typeColor = 0x007400

        elif firstType.strip() == "Poison":
            typeColor = 0xC000FF

        elif firstType.strip() == "Fire":
            typeColor = 0xFF0000

        elif firstType.strip() == "Flying":
            typeColor = 0x73A7D6

        elif firstType.strip() == "Water":
            typeColor = 0x0071D8

        elif firstType.strip() == "Bug":
            typeColor = 0x579857

        elif firstType.strip() == "Normal":
            typeColor = 0x767676

        elif firstType.strip() == "Electric":
            typeColor = 0xFFFF00

        elif firstType.strip() == "Ground":
            typeColor = 0x675418

        elif firstType.strip() == "Fairy":
            typeColor = 0xFFC0CB

        elif firstType.strip() == "Fighting":
            typeColor = 0x983838

        elif firstType.strip() == "Psychic":
            typeColor = 0xFF3A9C

        elif firstType.strip() == "Rock":
            typeColor = 0xA17950

        elif firstType.strip() == "Steel":
            typeColor = 0xCCCCCC

        elif firstType.strip() == "Ice":
            typeColor = 0x00FFFF

        elif firstType.strip() == "Ghost":
            typeColor = 0x3D47C6

        elif firstType.strip() == "Dragon":
            typeColor = 0x8087E1

        elif firstType.strip() == "Dark":
            typeColor = 0x3E1F00

        image = 'https://www.serebii.net/pokemon/art/' + pokeNumberData + '.png'
        embed = discord.Embed(colour=typeColor)
        embed.add_field(name=pokeListData[query], value="Type: " + pokeTypeData[query] + "\nNumber: " + pokeNumberData)

    elif uInput.lower() == "rand":

        randNum = random.randint(1, 1025)

        pokeNumberData = str(randNum).zfill(3)

        query = (int(pokeNumberData) - 1)

        #embed color by type

        pokeTypeSplit = pokeTypeData[query].split(' | ')
        firstType = pokeTypeSplit[0]

        if firstType.strip() == "Grass":
            typeColor = 0x007400

        elif firstType.strip() == "Poison":
            typeColor = 0xC000FF

        elif firstType.strip() == "Fire":
            typeColor = 0xFF0000

        elif firstType.strip() == "Flying":
            typeColor = 0x73A7D6

        elif firstType.strip() == "Water":
            typeColor = 0x0071D8

        elif firstType.strip() == "Bug":
            typeColor = 0x579857

        elif firstType.strip() == "Normal":
            typeColor = 0x767676

        elif firstType.strip() == "Electric":
            typeColor = 0xFFFF00

        elif firstType.strip() == "Ground":
            typeColor = 0x675418

        elif firstType.strip() == "Fairy":
            typeColor = 0xFFC0CB

        elif firstType.strip() == "Fighting":
            typeColor = 0x983838

        elif firstType.strip() == "Psychic":
            typeColor = 0xFF3A9C

        elif firstType.strip() == "Rock":
            typeColor = 0xA17950

        elif firstType.strip() == "Steel":
            typeColor = 0xCCCCCC

        elif firstType.strip() == "Ice":
            typeColor = 0x00FFFF

        elif firstType.strip() == "Ghost":
            typeColor = 0x3D47C6

        elif firstType.strip() == "Dragon":
            typeColor = 0x8087E1

        elif firstType.strip() == "Dark":
            typeColor = 0x3E1F00


        image = 'https://www.serebii.net/pokemon/art/' + pokeNumberData + '.png'
        embed = discord.Embed(colour=typeColor)
        embed.add_field(name=pokeListData[query], value="Type: " + pokeTypeData[query] + "\nNumber: " + pokeNumberData)

    else:
        inLower = uInput.lower()
        pokeNum = (pokeLowerListData.index(inLower) + 1)
        pokeNumberData = str(pokeNum).zfill(3)

        query = (int(pokeNumberData) - 1)

        #embed color by type

        pokeTypeSplit = pokeTypeData[query].split(' | ')
        firstType = pokeTypeSplit[0]

        if firstType.strip() == "Grass":
            typeColor = 0x007400

        elif firstType.strip() == "Poison":
            typeColor = 0xC000FF

        elif firstType.strip() == "Fire":
            typeColor = 0xFF0000

        elif firstType.strip() == "Flying":
            typeColor = 0x73A7D6

        elif firstType.strip() == "Water":
            typeColor = 0x0071D8

        elif firstType.strip() == "Bug":
            typeColor = 0x579857

        elif firstType.strip() == "Normal":
            typeColor = 0x767676

        elif firstType.strip() == "Electric":
            typeColor = 0xFFFF00

        elif firstType.strip() == "Ground":
            typeColor = 0x675418

        elif firstType.strip() == "Fairy":
            typeColor = 0xFFC0CB

        elif firstType.strip() == "Fighting":
            typeColor = 0x983838

        elif firstType.strip() == "Psychic":
            typeColor = 0xFF3A9C

        elif firstType.strip() == "Rock":
            typeColor = 0xA17950

        elif firstType.strip() == "Steel":
            typeColor = 0xCCCCCC

        elif firstType.strip() == "Ice":
            typeColor = 0x00FFFF

        elif firstType.strip() == "Ghost":
            typeColor = 0x3D47C6

        elif firstType.strip() == "Dragon":
            typeColor = 0x8087E1

        elif firstType.strip() == "Dark":
            typeColor = 0x3E1F00

        image = 'https://www.serebii.net/pokemon/art/' + str(pokeNumberData) + '.png'
        embed = discord.Embed(colour=typeColor)
        embed.add_field(name=pokeListData[query], value="Type: " + pokeTypeData[query] + "\nNumber: " + pokeNumberData)

    embed.set_image(url=image)
    await ctx.send(embed = embed)

#Tarot
@bot.command()
async def tarot(ctx, deck:int, amount: int):


    for i in range(amount):


        #0-77
        num = random.randint(0,77)

        card = cardData[str(num + 1)]

        pos = random.randint(0,1)
        #print ()
        #print (pos)
        #print(num)
        #print(card)
        cardParts = card.split("|")

        #print("File: " + fileName)

        name = cardParts[1]
        #print("Name:" + name)

        poseDescs = cardParts[2].split(";")

        if pos == 0:
            description = poseDescs[0]
            position = "regular"
            fileName = str(num+1) + ".jpg"
            print(fileName)
        else:
            description = poseDescs[1]
            name = name + " Reversed"
            position = "reversed"
            fileName = "r" + str(num+1) + ".jpg"
            print(fileName)



        print("Title: " + name)
        print("Desc: " + description)
        print("File: " + fileName)


        capitalized_description = description[0].upper() + description[1:]

        cardEmbed = discord.Embed(title=name, description=capitalized_description, colour=0xC000FF)
        
        
        file = discord.File("Tarot/" + str(deck) + "/" + fileName)
        cardEmbed.set_image(url="attachment://" + fileName)
        await ctx.send(file=file, embed=cardEmbed)

        #await ctx.send(embed=cardEmbed)

#Geoip
@bot.command()
async def geoip(ctx, ip):
    apiURL = 'http://ip-api.com/json/' + ip

    ipData = requests.get(apiURL)

    geoipJSON = ipData.json()


    country = (geoipJSON["country"])
    countryCode = (geoipJSON["countryCode"])
    region = (geoipJSON["region"])
    regionName = (geoipJSON["regionName"])
    city = (geoipJSON["city"])
    zipCode = (geoipJSON["zip"])
    latitude = (geoipJSON["lat"])
    longitude = (geoipJSON["lon"])
    timezone = (geoipJSON["timezone"])
    isp = (geoipJSON["isp"])

    geoip = discord.Embed(title="GeoIP information for " + ip + ":")
    geoip.add_field(name="Country: ", value=country)
    geoip.add_field(name="Country Code: ", value=countryCode)
    geoip.add_field(name="Region: ", value=region)
    geoip.add_field(name="Region Name: ", value=regionName)
    geoip.add_field(name="City: ", value=city)
    geoip.add_field(name="Zip Code: ", value=zipCode)
    geoip.add_field(name="Latitude: ", value=latitude)
    geoip.add_field(name="Longitude: ", value=longitude)
    geoip.add_field(name="Timezone: ", value=timezone)
    geoip.add_field(name="ISP: ", value=isp)

    await ctx.send(embed=geoip)

#CRYPTO COMMANDS:
#Bitcoin
@bot.command()
async def btc(ctx):
    apiURL = 'https://api.coinlore.net/api/ticker/?id=90'
    btcData = requests.get(apiURL)
    btcJson = btcData.json()

    btcEmb = discord.Embed(title=btcJson[0]['name'])
    btcEmb.add_field(name="Ticker: ", value=(btcJson[0]["symbol"]))
    btcEmb.add_field(name="USD Price: ", value=(btcJson[0]["price_usd"]))
    btcEmb.add_field(name="24hr change: ", value=(btcJson[0]["percent_change_24h"]) + "%")
    btcEmb.add_field(name="7d change: ", value=(btcJson[0]["percent_change_7d"]) + "%")

    await ctx.send(embed=btcEmb)

#Monero
@bot.command()
async def xmr(ctx):
    apiURL = 'https://api.coinlore.net/api/ticker/?id=28'
    xmrData = requests.get(apiURL)
    xmrJson = xmrData.json()

    xmrEmb = discord.Embed(title=xmrJson[0]['name'])
    xmrEmb.add_field(name="Ticker: ", value=(xmrJson[0]["symbol"]))
    xmrEmb.add_field(name="USD Price: ", value=(xmrJson[0]["price_usd"]))
    xmrEmb.add_field(name="24hr change: ", value=(xmrJson[0]["percent_change_24h"]) + "%")
    xmrEmb.add_field(name="7d change: ", value=(xmrJson[0]["percent_change_7d"]) + "%")

    await ctx.send(embed=xmrEmb)

#Ethereum
@bot.command()
async def eth(ctx):
    apiURL = 'https://api.coinlore.net/api/ticker/?id=80'
    ethData = requests.get(apiURL)
    ethJson = ethData.json()

    ethEmb = discord.Embed(title=ethJson[0]['name'])
    ethEmb.add_field(name="Ticker: ", value=(ethJson[0]["symbol"]))
    ethEmb.add_field(name="USD Price: ", value=(ethJson[0]["price_usd"]))
    ethEmb.add_field(name="24hr change: ", value=(ethJson[0]["percent_change_24h"]) + "%")
    ethEmb.add_field(name="7d change: ", value=(ethJson[0]["percent_change_7d"]) + "%")

    await ctx.send(embed=ethEmb)

#Ethereum Classic
@bot.command()
async def ethc(ctx):
    apiURL = 'https://api.coinlore.net/api/ticker/?id=118'
    ethcData = requests.get(apiURL)
    ethcJson = ethcData.json()

    ethcEmb = discord.Embed(title=ethcJson[0]['name'])
    ethcEmb.add_field(name="Ticker: ", value=(ethcJson[0]["symbol"]))
    ethcEmb.add_field(name="USD Price: ", value=(ethcJson[0]["price_usd"]))
    ethcEmb.add_field(name="24hr change: ", value=(ethcJson[0]["percent_change_24h"]) + "%")
    ethcEmb.add_field(name="7d change: ", value=(ethcJson[0]["percent_change_7d"]) + "%")

    await ctx.send(embed=ethcEmb)

#LiteCoin
@bot.command()
async def ltc(ctx):
    apiURL = 'https://api.coinlore.net/api/ticker/?id=1'
    ltcData = requests.get(apiURL)
    ltcJson = ltcData.json()

    ltcEmb = discord.Embed(title=ltcJson[0]['name'])
    ltcEmb.add_field(name="Ticker: ", value=(ltcJson[0]["symbol"]))
    ltcEmb.add_field(name="USD Price: ", value=(ltcJson[0]["price_usd"]))
    ltcEmb.add_field(name="24hr change: ", value=(ltcJson[0]["percent_change_24h"]) + "%")
    ltcEmb.add_field(name="7d change: ", value=(ltcJson[0]["percent_change_7d"]) + "%")

    await ctx.send(embed=ltcEmb)

#DogeCoin
@bot.command()
async def doge(ctx):
    apiURL = 'https://api.coinlore.net/api/ticker/?id=2'
    dogeData = requests.get(apiURL)
    dogeJson = dogeData.json()

    dogeEmb = discord.Embed(title=dogeJson[0]['name'])
    dogeEmb.add_field(name="Ticker: ", value=(dogeJson[0]["symbol"]))
    dogeEmb.add_field(name="USD Price: ", value=(dogeJson[0]["price_usd"]))
    dogeEmb.add_field(name="24hr change: ", value=(dogeJson[0]["percent_change_24h"]) + "%")
    dogeEmb.add_field(name="7d change: ", value=(dogeJson[0]["percent_change_7d"]) + "%")

    await ctx.send(embed=dogeEmb)

#Ripple
@bot.command()
async def xrp(ctx):
    apiURL = 'https://api.coinlore.net/api/ticker/?id=58'
    xrpData = requests.get(apiURL)
    xrpJson = xrpData.json()

    xrpEmb = discord.Embed(title=xrpJson[0]['name'])
    xrpEmb.add_field(name="Ticker: ", value=(xrpJson[0]["symbol"]))
    xrpEmb.add_field(name="USD Price: ", value=(xrpJson[0]["price_usd"]))
    xrpEmb.add_field(name="24hr change: ", value=(xrpJson[0]["percent_change_24h"]) + "%")
    xrpEmb.add_field(name="7d change: ", value=(xrpJson[0]["percent_change_7d"]) + "%")

    await ctx.send(embed=xrpEmb)
#END CRYPTO

#Base conversion
#Binary
#to
@bot.command()
async def dec2bin(ctx,arg):
    uInput = arg

    apiURL = ("https://networkcalc.com/api/binary/" + uInput + "?from=10&to=2")
    convData = requests.get(apiURL)
    convJson = convData.json()

    binEmb = discord.Embed(title=(uInput + " in binary"))
    binEmb.add_field(name=(convJson["converted"]), value="")

    await ctx.send(embed=binEmb)
#from
@bot.command()
async def bin2dec(ctx,arg):
    uInput = arg

    apiURL = ("https://networkcalc.com/api/binary/" + uInput + "?from=2&to=10")
    convData = requests.get(apiURL)
    convJson = convData.json()

    binEmb = discord.Embed(title=(uInput + " in decimal"))
    binEmb.add_field(name=(convJson["converted"]), value="")

    await ctx.send(embed=binEmb)

#Hex
#to
@bot.command()
async def dec2hex(ctx,arg):
    uInput = arg

    apiURL = ("https://networkcalc.com/api/binary/" + uInput + "?from=10&to=16")
    convData = requests.get(apiURL)
    convJson = convData.json()

    binEmb = discord.Embed(title=(uInput + " in hex"))
    binEmb.add_field(name=(convJson["converted"]), value="")

    await ctx.send(embed=binEmb)
#from
@bot.command()
async def hex2dec(ctx,arg):
    uInput = arg

    apiURL = ("https://networkcalc.com/api/binary/" + uInput + "?from=16&to=10")
    convData = requests.get(apiURL)
    convJson = convData.json()

    binEmb = discord.Embed(title=(uInput + " in decimal"))
    binEmb.add_field(name=(convJson["converted"]), value="")

    await ctx.send(embed=binEmb)

#HASHING
#MD5 hash
@bot.command()
async def md5(ctx, *, arg):
    uInput = arg

    md5Emb = discord.Embed(title=("md5 hash of " + uInput))
    md5Emb.add_field(name=hashlib.md5(uInput.encode("utf-8")).hexdigest(), value="")

    await ctx.send(embed=md5Emb)
#sha256 hash
@bot.command()
async def sha256(ctx, *, arg):
    uInput = arg

    sha256Emb = discord.Embed(title=("sha256 hash of " + uInput))
    sha256Emb.add_field(name=hashlib.sha256(uInput.encode("utf-8")).hexdigest(), value="")

    await ctx.send(embed=sha256Emb)
#sha512 hash
@bot.command()
async def sha512(ctx, *, arg):
    uInput = arg

    sha512Emb = discord.Embed(title=("sha512 hash of " + uInput))
    sha512Emb.add_field(name=hashlib.sha512(uInput.encode("utf-8")).hexdigest(), value="")

    await ctx.send(embed=sha512Emb)

#Dictionaries
#Dictionary api
#https://api.dictionaryapi.dev/api/v2/entries/en/WORD

@bot.command()
async def define(ctx, arg):
    uInput = arg
    apiURL = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + arg
    dictData = requests.get(apiURL)
    dictJson = dictData.json()

    dictEmb = discord.Embed(title=dictJson[0]['word'] + " " + dictJson[0]['phonetic'])

    dictEmb.add_field(name="Definition:", value=(dictJson[0]['meanings'][0]['definitions'][0]['definition']))

    await ctx.send(embed=dictEmb)


#Pull from RockDB and key
#with open("rockDB.json") as f:
#    rockDB = json.load(f)
#with open("rockDBKey.json") as f:
#    rockDBKey = json.load(f)

@bot.command()
async def rock(ctx, *, arg):
    uInput = arg.lower()

    RockEmb = discord.Embed(title=uInput.capitalize(), colour=0xC000FF)
    RockEmb.add_field(name="Metaphysical properties:", value=(rockDB[uInput]["metaphysical"]))
    fileName = uInput.replace(' ', '') + ".jpg"

    file = discord.File("Rocks/" + fileName)

    RockEmb.set_image(url="attachment://" + fileName)
    await ctx.send(file=file, embed = RockEmb)

@bot.command()
async def rockand(ctx):
    #num = random.randint(1,59)
    num = random.randint(1,59)

    if num == 1:
        uInput = "agate"
    elif num == 2:
        uInput = "amber"
    elif num == 3:
        uInput = "amethyst"
    elif num == 4:
        uInput = "aventurine"
    elif num == 5:
        uInput = "aquamarine"
    elif num == 6:
        uInput = "azurite"
    elif num == 7:
        uInput = "amazonite"
    elif num == 8:
        uInput = "calcite"
    elif num == 9:
        uInput = "celestite"
    elif num == 10:
        uInput = "chrysocolla"
    elif num == 11:
        uInput = "chrysoprase"
    elif num == 12:
        uInput = "citrine"
    elif num == 13:
        uInput = "cobaltian calcite"
    elif num == 14:
        uInput = "copal"
    elif num == 15:
        uInput = "danburite"
    elif num == 16:
        uInput = "emerald"
    elif num == 17:
        uInput = "epidote"
    elif num == 18:
        uInput = "fairy stone"
    elif num == 19:
        uInput = "fire agate"
    elif num == 20:
        uInput = "fluorite"
    elif num == 21:
        uInput = "fuchsite"
    elif num == 22:
        uInput = "garnet"
    elif num == 23:
        uInput = "hematite"
    elif num == 24:
        uInput = "herkimer diamond"
    elif num == 25:
        uInput = "howlite"
    elif num == 26:
        uInput = "kunzite"
    elif num == 27:
        uInput = "kyanite"
    elif num == 28:
        uInput = "labradorite"
    elif num == 29:
        uInput = "lapis lazuli"
    elif num == 30:
        uInput = "lepidolite"
    elif num == 31:
        uInput = "lingam stone"
    elif num == 32:
        uInput = "malachite"
    elif num == 33:
        uInput = "moldavite"
    elif num == 34:
        uInput = "moonstone"
    elif num == 35:
        uInput = "obsidian"
    elif num == 36:
        uInput = "onyx"
    elif num == 37:
        uInput = "opal"
    elif num == 38:
        uInput = "peridot"
    elif num == 39:
        uInput = "petrified wood"
    elif num == 40:
        uInput = "prehnite"
    elif num == 41:
        uInput = "pyrite"
    elif num == 42:
        uInput = "quartz crystal"
    elif num == 43:
        uInput = "rhodochrosite"
    elif num == 44:
        uInput = "ruby"
    elif num == 45:
        uInput = "rutilated quartz"
    elif num == 46:
        uInput = "sapphire"
    elif num == 47:
        uInput = "selenite"
    elif num == 48:
        uInput = "silver"
    elif num == 49:
        uInput = "smoky quartz"
    elif num == 50:
        uInput = "sodalite"
    elif num == 51:
        uInput = "staurolite"
    elif num == 52:
        uInput = "stromatolite"
    elif num == 53:
        uInput = "tanzanite"
    elif num == 54:
        uInput = "tigereye"
    elif num == 55:
        uInput = "topaz"
    elif num == 56:
        uInput = "tourmaline"
    elif num == 57:
        uInput = "tourmalinated quartz"
    elif num == 58:
        uInput = "vanadinite"
    elif num == 59:
        uInput = "zircon"

    RockEmb = discord.Embed(title=uInput.capitalize(), colour=0xC000FF)
    RockEmb.add_field(name="Metaphysical properties:", value=(rockDB[uInput]["metaphysical"]))

    fileName = uInput.replace(' ', '') + ".jpg"

    file = discord.File("Rocks/" + fileName)

    RockEmb.set_image(url="attachment://" + fileName)
    await ctx.send(file=file, embed = RockEmb)

@bot.command()
async def rocklist(ctx):
    RockListEmb = discord.Embed(colour=0xC000FF)
    RockListEmb.add_field(name="Rock List:", value="Agate, Amber, Amethyst, Aventurine, Aquamarine, Azurite, Amazonite, Calcite, Celestite, Chrysocolla, Chrysoprase, Citrine, Cobaltian Calcite, Copal, Danburite, Emerald, Epidote, Fairy Stone, Fire Agate, Fluorite, Fuchsite, Garnet, Hematite, Herkimer Diamond, Howlite, Kunzite, Kyanite, Labradorite, Lapis Lazuli, Lepidolite, Lingam Stone, Malachite, Moldavite, Moonstone, Obsidian, Onyx, Opal, Peridot, Petrified Wood, Prehnite, Pyrite, Quartz Crystal, Rhodochrosite, Ruby, Rutilated Quartz, Sapphire, Selenite, Silver, Smoky Quartz, Sodalite, Staurolite, Stromatolite, Tanzanite, Tigereye, Topaz, Tourmaline, Tourmalinated Quartz, Vanadinite, Zircon")
    await ctx.send(embed = RockListEmb)

@bot.command()
async def goldfish(ctx):
    await ctx.send("https://i.kym-cdn.com/photos/images/newsfeed/002/486/154/c06.gif")

@bot.command()
async def abby(ctx):
    await ctx.send("gail")
@bot.command()
async def Abby(ctx):
    await ctx.send("gail")

@bot.command()
async def robohash(ctx, *, arg):
    uInput = arg.replace(" ","%20")

    link = "https://robohash.org/" + uInput

    RobotEmb = discord.Embed(title=("Robot hash of " + arg))

    RobotEmb.set_image(url=link)

    await ctx.send(embed = RobotEmb)

@bot.command()
async def coin(ctx):
    num = random.randint(0,1)
    if num == 0:
        cFlip = "heads"
        print(cFlip)
    else:
        cFlip = "tails"
        print(cFlip)

    fileName = "Coins/" + cFlip +  ".png"
    print(fileName)
    CoinEmb = discord.Embed(title=cFlip.capitalize(), colour=0xC000FF)
    #CoinEmb.add_field(name="Metaphysical properties:", value=(rockDB[uInput]["metaphysical"]))
    #file = discord.File(fileName)
    #print(file)
    file = discord.File(fileName)
    CoinEmb.set_image(url="attachment://" + fileName)
    await ctx.send(file=file, embed = CoinEmb)

@bot.command()
async def eight(ctx):
    num = random.randint(1,11)
    
    fileName = "8ball/" + str(num) + ".png" 
    
    BallEmb = discord.Embed(title="~Your Fortune~", colour = 0xC000FF)
    file = discord.File(fileName)
    
    BallEmb.set_image(url="attachment://" + fileName)
    await ctx.send(file=file, embed = BallEmb)


#@bot.command()
#async def cowsay(ctx, *, arg):


    

bot.run(BOT_TOKEN)
