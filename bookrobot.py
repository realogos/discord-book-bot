import discord
import random
import requests

TOKEN = 'MTM4NTQ4ODUxMDMwMzM0MjY2Mw.Gf0F9m.jL1hKb4UxGpHxH3Xs7Wrvt7lUx1_LuBBdRXccE'
GIST_RAW_URL = ' https://gist.githubusercontent.com/realogos/15cf6185178ead6ee7fa637b1a5f9a1b/raw/5e6c28e23ee16c584e62221598cdc8a0af6cb8e9/The%2520Tower%2520of%2520Babel_texts.txt'

# 获取文本块
def fetch_text_blocks():
    response = requests.get(GIST_RAW_URL)
    if response.status_code == 200:
        return [block.strip() for block in response.text.split('---') if block.strip()]
    return []

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'布克机器人 已上线：{client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.strip()

    if content == '!book':
        blocks = fetch_text_blocks()
        if blocks:
            await message.channel.send(random.choice(blocks))
        else:
            await message.channel.send("此书架为空，请等待更新。")

client.run(TOKEN)
