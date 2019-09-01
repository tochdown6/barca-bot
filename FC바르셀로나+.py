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
    if message.content.startswith("!FC바르셀로나"):
        await message.channel.send("http://blogfiles.naver.net/MjAxNzA3MTBfMjAy/MDAxNDk5NjM3ODg1OTUz.QZkrk4DERMhec_BT79ed8FSTTqnNN3o4kmvRfV6UMwwg.W5RcFkATm1uHCiwoKFaCA16v31NNlon4FBucuZN75owg.JPEG.tripofpassion/FC-Barcelona-16.jpg 스페인의 명문 축구클럽이다.소속 리그는 스페인 라리가 산탄데르 ,현 주장은 리오넬 메시이다.")



client.run("NjA4NDkzNjcwNjUxMzk2MDk2.XU0cJg.dxOMjMHoLJnyXaejjaDSlSWUJmk")