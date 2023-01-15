import telebot
import datetime
from PIL import Image, ImageDraw, ImageFont

bot = telebot.TeleBot('5814428294:AAFeXrDpgm9-y5Fs57bVWO8Gzb4L23sewFs')

fileinfo = open("Stats.csv", "w+")
fileinfo.write("sep=;\n username;date&time\n")
fileinfo.close()

@bot.message_handler(commands=['start'])
def start_message(message):
    img = Image.open('cat.jpg')
    temp = ImageDraw.Draw(img)
    now = datetime.datetime.now()
    temp.text((400, 1075), now.strftime("%d-%m-%Y %H:%M"), font=ImageFont.truetype('cambria.ttc', size=100),
              fill=(0, 0, 0))
    img.save('res.jpg')
    file = open('res.jpg', 'rb')
    bot.send_photo(message.chat.id, file)
    tmpfile = open("Stats.csv", "a+")
    tmpfile.write(message.from_user.username + ';' + now.strftime("%d-%m-%Y %H:%M") + "\n")

    tmpfile.close()


bot.polling()



