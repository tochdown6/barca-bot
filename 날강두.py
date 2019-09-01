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
    if message.content.startswith("일정표"):
        await message.channel.send("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjA5&query=FC%20%EB%B0%94%EB%A5%B4%EC%85%80%EB%A1%9C%EB%82%98%20%EA%B2%BD%EA%B8%B0%EC%9D%BC%EC%A0%95")


client.run("NjA4NDkzNjcwNjUxMzk2MDk2.XUo98A.wSP0GaWYHBWoGJgSDRmuKDs0Z9g")