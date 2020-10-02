import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('message here')
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")

client.run('token here', bot=False)
