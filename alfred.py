#Setup stuff
import asyncio
import json
import discord
from discord.ext import commands
import random
import requests

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

#Pull from config
with open("config.json") as f:
    data = json.load(f)

#Pull from cards.json
with open("cards.json") as f:
    cardData = json.load(f)


BOT_TOKEN = data["bot-token"]
CHANNEL_ID = data["channel-id"]
PREFIX = data["command-prefix"]

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Alfred online")
    channel = bot.get_channel(CHANNEL_ID)

@bot.command()
async def help(ctx):
    help = discord.Embed(title="Help:")

    help.add_field(name="Command prefix: ~", value="Please put this before the request", inline = False)

    help.add_field(name="Pokedex:", value="poke rand: Returns a random pokemon\npoke (num or name): Returns a specific pokemon", inline=False)

    help.add_field(name="Tarot:", value="tarot (deck) (x): Returns x amount of Tarot cards in selected deck. Decks options are 1 for default and 2 for Abby's cards", inline=False)

    help.add_field(name="binary:", value="binary: returns base 10 of a binary value")

    help.add_field(name="Geoip:", value="geoip (domain or ip): returns geoip info on a target")

    help.add_field(name="Crypto", value="btc: returns market data \n ltc: returns market data \n xmr: returns market data \n eth: returns market data \n ethc: returns market data")

    await ctx.send(embed=help)

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

#debug
        print (query)
        print ("Name: " + pokeListData[query])
        print ("Number: " + pokeNumberData)
        print ("Type: " + pokeTypeData[query])
        print("You entered: " + pokeNumberData + " and it was numeric")
#/debug


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

#debug
        print (query)
        print ("Name: " + pokeListData[query])
        print ("Number: " + pokeNumberData)
        print ("Type: " + pokeTypeData[query])
        print("You entered: " + pokeNumberData + " and it was numeric")
#/debug

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

#debug
        print ("Number: " + str(pokeNum))
        print ("Name: " + pokeListData[pokeNum - 1])
        print ("Type: " + pokeTypeData[pokeNum - 1])
#/debug

    embed.set_image(url=image)
    await ctx.send(embed = embed)

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

        print ("http://www.rubberroomwithrats.com/Alfred/Tarot/" + str(deck) + "/" + fileName)

        cardEmbed.set_image(url="http://www.rubberroomwithrats.com/Alfred/Tarot/" + str(deck) + "/" + fileName)

        await ctx.send(embed=cardEmbed)




        #out = discord.Embed(title=cardName, description=position + cardDesc ,colour=0xC000FF)
        #await ctx.send( embed=out)


        #out = discord.Embed(title=cardName, description=position + cardDesc ,colour=0xC000FF)
        #await ctx.send( embed=out)

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

@bot.command()
async def binary(ctx,arg):
    uInput = arg

    apiURL = ("https://networkcalc.com/api/binary/" + uInput + "?from=10&to=2")
    convData = requests.get(apiURL)
    convJson = convData.json()

    binEmb = discord.Embed(title=(uInput + " in binary"))
    binEmb.add_field(name=(convJson["converted"]), value="")

    await ctx.send(embed=binEmb)

bot.run(BOT_TOKEN)


