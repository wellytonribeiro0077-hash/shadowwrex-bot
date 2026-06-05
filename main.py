import discord
import os

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Bot Online! Império Shadowwrex ativo! 👑")

@client.event
async def on_member_join(member):
    canal = discord.utils.get(member.guild.text_channels, name="👋・boas-vindas")
    if canal:
        msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 **BEM-VINDO AO IMPÉRIO, {member.mention}!** 🔥
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Você é o membro **#{member.guild.member_count}** da **Tropa Rex**! ⚡

 *Dourado é vida. Tropa Rex no comando!* 👑
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """
        await canal.send(msg)

@client.event
async def on_member_remove(member):
    canal = discord.utils.get(member.guild.text_channels, name="👋・boas-vindas")
    if canal:
        await canal.send(f"💔 **{member.name}** deixou o Império...")

client.run(os.environ["TOKEN"])
