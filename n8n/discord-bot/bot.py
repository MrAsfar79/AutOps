import discord
import requests
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = "YOUR_DISCORD_BOT_TOKEN"  # replace with your bot token
N8N_WEBHOOK = "https://your-n8n-instance.com/webhook/your-webhook-id"  # replace with your n8n webhook URL
CHANNEL_ID = YOUR_CHANNEL_ID  # your channel ID as integer

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logging.info(f"Bot connected as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.channel.id != CHANNEL_ID:
        return
    
    logging.info(f"Forwarding message from {message.author}: {message.content}")
    
    try:
        r = requests.post(N8N_WEBHOOK, json={
            "content": message.content,
            "author": message.author.name,
            "channel_id": str(message.channel.id),
	    "sessionId": str(message.channel.id)
        }, timeout=10)
        logging.info(f"n8n responded: {response.status_code}")
    except Exception as e:
        logging.error(f"Failed to forward to n8n: {e}")

client.run(TOKEN)
