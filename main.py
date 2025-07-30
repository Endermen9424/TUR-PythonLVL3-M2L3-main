import discord
from discord.ext import commands
from logic import quiz_questions
# Görev 7 - defaultdict komutunu içe aktarın
from collections import defaultdict
from config import token

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

user_responses = {}
# Görev 8 - Kullanıcı puanlarını kaydetmek için puan sözlüğünü oluşturun
points = defaultdict(int)

async def send_question(ctx_or_interaction, user_id):
    question = quiz_questions[user_responses[user_id]]
    buttons = question.gen_buttons()
    view = discord.ui.View()
    for button in buttons:
        view.add_item(button)

    if isinstance(ctx_or_interaction, commands.Context):
        await ctx_or_interaction.send(question.text, view=view)
    else:
        await ctx_or_interaction.followup.send(question.text, view=view)


@bot.event
async def on_ready():
    print(f'Yeni giriş: {bot.user}!')


@bot.event
async def on_interaction(interaction):
    user_id = interaction.user.id
    if user_id not in user_responses:
        await interaction.response.send_message("Lütfen !start komutunu yazarak testi başlatın")
        return

    custom_id = interaction.data["custom_id"]
    if custom_id.startswith("correct"):
        await interaction.response.send_message("Doğru cevap!")
        # Görev 9 - Doğru cevap için kullanıcıya puan ekleyin
        points[user_id] += 1
    elif custom_id.startswith("wrong"):
        await interaction.response.send_message("Yanlış cevap!")

    # Görev 5 - soru sayacını ayarlayın
    user_responses[user_id] += 1
    # Görev 6 - kullanıcı tüm soruları yanıtladıysa sınav sonucuyla ilgili bir mesaj gönderin. Aksi takdirde, bir sonraki soruyu gönderin
    if user_responses[user_id] > len(quiz_questions) - 1:
        await interaction.followup.send(f"Sınav bitti!\n\nPuanınız: {points[user_id]}\nTebrikler!")
    else:
        await send_question(interaction, user_id)

@bot.command()
async def start(ctx):
    user_id = ctx.author.id
    if user_id in user_responses:
        user_responses[user_id] = 0
        points[user_id] = 0
        await ctx.send("Test yeniden başlatıldı!")
    else:
        user_responses[user_id] = 0
        points[user_id] = 0
        await ctx.send("Test başlatıldı! Sorulara başlayabilirsiniz.")

    await send_question(ctx, user_id)

bot.run(token)

