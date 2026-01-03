# bot.py
import discord
from discord.ext import commands
from config import TOKEN, CHANNEL_AI
from info import INFO

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Penting agar bot bisa baca konten pesan

bot = commands.Bot(command_prefix="!", intents=intents)

# ==============================
# Fungsi AI sederhana Bahasa-lo
# ==============================
def ai_response(message):
    kata = message.lower().split()
    tips = []
    for k in kata:
        if k in INFO:
            tips.append(f"{k}: {INFO[k]}")
    if tips:
        return "💡 Tips Bahasa-lo:\n" + "\n".join(tips)
    return "🤖 Maaf, saya belum tahu tentang itu. Coba gunakan perintah lain dari Bahasa-lo."

# ==============================
# Event on_ready
# ==============================
@bot.event
async def on_ready():
    print(f"✅ Bot siap! Login sebagai {bot.user}")

# ==============================
# Event on_message
# ==============================
@bot.event
async def on_message(message):
    # Jangan respon ke diri sendiri
    if message.author == bot.user:
        return

    # Hanya respon di channel tertentu
    if message.channel.id == CHANNEL_AI:
        response = ai_response(message.content)
        await message.channel.send(response)

    await bot.process_commands(message)

# ==============================
# Jalankan bot
# ==============================
bot.run(TOKEN)
