import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("FC바르셀로나")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("크리스티아누 호날두"):
        await message.channel.send("http://imgnews.naver.net/image/5129/2019/07/26/261475908_20190726192028480.jpg 포르투갈의 축구스타이다. 현재는 내한 결장으로 인하여 사람들에게 날강두 라고 불리고 있다.")


client.run("NjA4NDkzNjcwNjUxMzk2MDk2.XUo98A.wSP0GaWYHBWoGJgSDRmuKDs0Z9g")