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
    if message.content.startswith("!안녕"):
        await message.channel.send("반갑습니다")


client.run("NjA4NDkzNjcwNjUxMzk2MDk2.XUo98A.wSP0GaWYHBWoGJgSDRmuKDs0Z9g")