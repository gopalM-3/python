import discord
import os
import requests
import json
import random
from replit import db
from keepAlive import keepAlive

client = discord.Client()

if "responding" not in db.keys():
  db["responding"] = True

hi = ["hi", "Hi", "Hello", "hello", "hey", "Hey"]

sadWords = ["sad", "unhappy", "angry", "waste", "not good", "not happy", "im sad", "bad", "depressed", "depressing", "defrsan"]
encWords = [
  "Cheer up bud!", "Hey, I can talk to you...", "It's not bad to feel sad sometimes :)", "Why so serious? (Joker ref dude, cheer up!)", "Buckle up fam!", "Brooo! Cheer up!", "Dude, Cheer up!", "You're a great person to talk to, cheer up!"
]

bestWords = ["best", "great"]
bestReply = ["I know that I'm the best, thank you. Credit to my creator."]

grayWords = ["gray", "jans"]
grayReply = ["Gray is the best!", "Gray goes cray cray..."]

abbuWords = ["abbu", "geck"]
abbuReply = ["Abbu the Geck!", "Hacker!"]

proWords = ["pro", "progamer", "pranav"]
proReply = ["Progamer the best!", "Pranav lesgooo!", "Topper!"]

jeevWords = ["jeev"]
jeevReply = ["Jeeb niceuuu"]

lalaWords = ["lala", "luli"]
lalaReply = ["Luli cutu", "Luli!"]

spamWord = ["anthey le", "anthe le"]
spamReply = ["Buddy!", "Enough buddy...", "Bruh"]

def getQuote():
  resp = requests.get("https://zenquotes.io/api/random")
  jsonData = json.loads(resp.text)
  quote = jsonData[0]['q'] + " - " + jsonData[0]['a']
  return (quote)

@client.event
async def on_ready():
  print("{0.user} is good to go!".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("@f"):
    await message.channel.send("A soldier has fallen, F in the chat please...")
  
  if message.content.startswith("@inspireme"):
    quote = getQuote()
    await message.channel.send(quote)
    
  if any(word in message.content for word in hi):
    await message.channel.send("Hello there!")

  if db["responding"]:
    if any(word in message.content for word in sadWords):
      await message.channel.send(random.choice(encWords))
  
  if any(word in message.content for word in spamWord):
    await message.channel.send(random.choice(spamReply))
  
  if any(word in message.content for word in bestWords):
    await message.channel.send(random.choice(bestReply))
  
  if any(word in message.content for word in grayWords):
    await message.channel.send(random.choice(grayReply))
  
  if any(word in message.content for word in abbuWords):
    await message.channel.send(random.choice(abbuReply))
  
  if any(word in message.content for word in proWords):
    await message.channel.send(random.choice(proReply))
  
  if any(word in message.content for word in jeevWords):
    await message.channel.send(random.choice(jeevReply))
  
  if any(word in message.content for word in lalaWords):
    await message.channel.send(random.choice(lalaReply))
  
  if message.content.startswith("@best"):
    await message.channel.send("My creator - Zer0 sama, is the best!")

  if message.content.startswith("@responding"):
    value = message.content.split("@responding ", 1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Ofcourse I'll respond to you :)")
    else:
      db["responding"] = False
      await message.channel.send("Ok, I won't be interrupting you again :(")

keepAlive()
client.run(os.getenv("noice"))
