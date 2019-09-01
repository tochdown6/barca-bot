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
    if message.content.startswith("리오넬 메시"):
        await message.channel.send("http://imgnews.naver.net/image/5002/2019/02/24/0001156798_004_20190224082000867.jpg FC바르셀로나의 현 주장이다. 빠른스피드와 건장한 체격으로 사람들에게 인기를 받고 있다.")


client.run("NjA4NDkzNjcwNjUxMzk2MDk2.XUo98A.wSP0GaWYHBWoGJgSDRmuKDs0Z9g")