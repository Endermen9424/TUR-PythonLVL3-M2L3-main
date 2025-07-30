# Görev 2 - İhtiyacınız olan her şeyi içe aktarın
import discord
from discord.ext import commands
from discord.ui import Button, View

class Question:
    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    @property
    def text(self):
        return self.__text 

    @property
    def gen_buttons(self):
        # Görev 3 - Dahili klavyeyi oluşturmak için bir metot oluşturun
        buttons = []
        for i, option in enumerate(self.options):
            if i == self.__answer_id:
                buttons.append(Button(label=option, style=discord.ButtonStyle.primary, custom_id=f"correct_{i}"))
            else:
                buttons.append(Button(label=option, style=discord.ButtonStyle.primary, custom_id=f"wrong_{i}"))
        return buttons
    
class MoreAnswerQuestion(Question):
    def __init__(self, text, answer_ids: list, *options):
        self.__text = text
        self.__answer_ids = set(answer_ids)
        self.options = options

    @property
    def gen_buttons(self):
        buttons = []
        for i, option in enumerate(self.options):
            if i in self.__answer_ids:
                buttons.append(Button(label=option, style=discord.ButtonStyle.primary, custom_id=f"correct_{i}"))
            else:
                buttons.append(Button(label=option, style=discord.ButtonStyle.primary, custom_id=f"wrong_{i}"))
        return buttons

# Görev 4 - Listeyi sorularınızla doldurun
quiz_questions = [
   Question("Kediler onları kimse görmediğinde ne yapar?", 1, "Uyurlar", "Espri yazarlar"),
   Question("Kediler sevgilerini nasıl ifade ederler?", 0, "Yüksek sesle mırıldanırlar", "Sevimli fotoğraflar", "Havlar"),
   Question("Kediler hangi kitapları okumayı sever?", 3, "Kişisel gelişim kitapları", "Zaman yönetimi: Günde 18 saat nasıl uyunur","Sahibinizden 5 dakika erken uyumanın 101 yolu", "İnsan yönetimi rehberi"),
   Question("Python'da liste oluşturmak için hangi işaret kullanılır?", 2, "Süslü parantezler", "Köşeli parantezler", "Parantezler", "Tırnak işaretleri"),
   Question("Python'da rastgele sayı üretmek için hangi modül kullanılır?", 1,"math", "random",  "os", "rastgele"),
   Question("Python'da bir fonksiyon nasıl tanımlanır?", 0, "def anahtar kelimesi ile", "function anahtar kelimesi ile", "func anahtar kelimesi ile", "define anahtar kelimesi ile"),
   MoreAnswerQuestion("Aşağıdakilerden hangisi pythonun veri tiplerinden biridir?", [0, 1, 2], "int", "str", "list", "dict", "set", "data", )
]

