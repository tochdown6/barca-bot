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
    if message.content.startswith("네이마르"):
        await message.channel.send("http://imgnews.naver.net/image/477/2019/07/01/0000192721_001_20190701113528510.jpg 전에 바르샤에 있던 선수이다 현재는 PSG에 있다.")


client.run("NjA4NDkzNjcwNjUxMzk2MDk2.XUo98A.wSP0GaWYHBWoGJgSDRmuKDs0Z9g")