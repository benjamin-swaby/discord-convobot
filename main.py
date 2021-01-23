import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='#')

created_conv = []


@bot.command()
async def new(ctx, topic):
    name = 'talks'
    category = discord.utils.get(ctx.guild.categories, name=name)
    created_conv.append(topic)

    channel = await ctx.guild.create_text_channel(topic, category=category)
    await ctx.send(f"created new topic: {topic}")

@bot.command()
async def close(ctx):
    name = ctx.channel.name
    if name in created_conv:
        await ctx.channel.delete()
    else:
        await ctx.send("i cannot delete this channel.")
        return
    
    




if __name__ == "__main__":
    with open("token.txt") as file:
        token = file.read()

    bot.run(token)




