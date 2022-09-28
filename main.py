import discord, time, os, random

class MyClient(discord.Client):

    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))
        channel = client.get_channel(932867446723989524)
        while True:
            for i in range(1,25):
                await channel.send(".bt all @rando#2626")
                print("Sent -> .bt all")
                time.sleep(20)
                await channel.send(".hourly")
                print("Sent -> .hourly ")
                time.sleep(random.randint(2,17))
                for a in range(1,11):
                    await channel.send(".lottery")
                    print("Sent -> .lottery")
                    time.sleep(random.randint(601,700))

                await channel.sent("FINISHED 1 CYCLE")
                print("FINISHED" ,i, "CYCLE")
client = MyClient()
token = os.environ['TOKEN']
print("ACTIVE WORKING NOW")                                                                                        
client.run(token, bot = False)