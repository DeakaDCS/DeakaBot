import discord

bot = discord.Bot()
token = "MTE1NzkxNzQ0ODA2Mjg5ODIyNw.GBF50O.edidnTFMjqZwQU-iHHzH2g6-vQwhHU42kWNb6s"

@bot.event
async def on_ready():
    print("Bot activated. {time.hour}")

@bot.slash_command(description="Check the ping of the bot.")
async def ping(ctx):
    embed = discord.Embed(title="Deaka Bot Ping", description=f"Delay: {bot.latency} seconds", color=0x3498db)
    embed.set_footer(text="Deaka Bot CMD")
    await ctx.respond(embed=embed)

bot.run(token)