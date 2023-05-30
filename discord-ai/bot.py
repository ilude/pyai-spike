import discord
import responses
from dotenv import dotenv_values, find_dotenv

config = dotenv_values(find_dotenv())

async def send_message(message, user_message, is_private):
  try:
    response = responses.get_response(user_message)
    await message.author.send(response) if is_private else await message.channel.send(response)
    
  except Exception as e:
    print(e)
    
def run_discord_bot():
  intents = discord.Intents.default()
  intents.message_content = True
  client = discord.Client(intents=intents)

  @client.event
  async def on_ready():
    print(f'{client.user} is now running!')
    text_channel_list = []
    for server in client.guilds:
      for channel in server.channels:
        
        if str(channel.type) == 'text' and 'general' in  channel.name:
          print(channel)
          #text_channel_list.append(channel)
          filename = str(channel.name)
          with open(f"{filename}.txt", "w") as fp:
            async for msg in channel.history(limit=None, oldest_first=True):
              try:
                towrite = f"[{msg.author.name}] @ [{msg.created_at}] said: {msg.clean_content} \n"
              except:
                towrite = "message unreadable. likely an image?"
              fp.write(towrite)
          print("completed export")

    
  @client.event
  async def on_message(message):
    if message.author == client.user:
      return
    
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    
    print(f'{username} said: "{user_message}" ({channel})')
    
    if user_message[0] == '?':
      user_message = user_message[1:]
      await send_message(message, user_message, is_private=(True))
    else:
      await send_message(message, user_message, is_private=(False))

  client.run(config['DISCORD_BOT_TOKEN'])  