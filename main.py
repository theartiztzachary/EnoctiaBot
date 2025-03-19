import os
import discord

def main():
    intents = discord.Intents.default()
    intents.message_content = True

    client = Client(intents=intents)
    client.run(os.environ['ACCESSTOKEN'])

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

if __name__ == '__main__':
    main()