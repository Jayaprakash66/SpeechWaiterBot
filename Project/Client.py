# Module
import gtts as gt
from twilio.rest import Client
import Phonetics as sp
from word2number import w2n
import re
import sqlite3
import pyttsx3
from googletrans import Translator
import pygame
import speech_recognition as sr
import os
import time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
account_sid = 'AC4de50e84b42b6b6869e7a6131e3b871a'
auth_token = '788238f67504438f38b41e9d9d14c687'
twilio_phone_number = '+12707479278'
recipient_phone_number = '+918248829100'
engine = pyttsx3.init()

# Function


def send_sms_notification(order_details):
    client = Client(account_sid, auth_token)

    message_body = order_details

    message = client.messages.create(
        body=message_body,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )
    print(f"SMS notification sent: {message.sid}")


def Word2Num(spoke):
    spoken_text = spoke
    numeric_text = spoken_text
    for word in spoken_text.split():
        if word.isdigit():
            continue
        try:
            numeric_word = str(w2n.word_to_num(word))
            numeric_text = numeric_text.replace(word, numeric_word)
        except ValueError:
            pass
    return numeric_text


def tamil_audio(txt1):
    translated_text = translator.translate(txt1, dest='ta')
    TamilText = translated_text.text
    tts = gt.gTTS(text=TamilText, lang='ta')
    tts.save("Tamil-Audio{}.mp3".format(incr))
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Tamil-Audio{}.mp3".format(incr), 'mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass


engine = pyttsx3.init()


def eng_audio(text):
    engine.setProperty('rate', 130)
    engine.say(text)
    engine.runAndWait()


# Intro
conn1 = sqlite3.connect('Database_Order.db')
translator = Translator()
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 140)
txt = "Welcome To VJ Assistance, If You Want To Continue With English, Say English"
engine.say(txt)
engine.runAndWait()
txt1 = "Vanakam, VJ unavu seyali uingalai anbodu varaverkiradhu tamilil thodara, tamil endru kooravum"
translated_text = translator.translate(txt1, dest='ta')
TamilText = translated_text.text
tts = gt.gTTS(text=TamilText, lang='ta')
tts.save("Tamil-Audio.mp3")
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Tamil-Audio.mp3", 'mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass

# User Input
lang = 2
while lang > 1:
    with sr.Microphone() as source:
        print("-----SPEAK-----")
        audio = r.listen(source)
    spec = ""
    try:
        spec = r.recognize_google(audio, language='en')
    except sr.UnknownValueError:
        print("ERROR")
    except sr.RequestError as e:
        print("Error; {0}".format(e))
    lang = spec
    lang = 0 if (lang == "English") else 1 if (lang == "Tamil") else 2
    if (lang > 1):
        print("-----SPEAK AGAIN-----")

# Menu
incr = 1
x = True
dic = {}
if (x):
    conn = sqlite3.connect('Database_Items.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ITEMS')
    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    print('+------+-----------+---------+')
    print('|  ID  |   ITEMS   |  PRICE  |')
    print('+------+-----------+---------+')
    if (lang == 1):
        tamil_audio("Indraya Unavu Pattiyal")
        incr += 1
        list1 = ""
        for row in rows:
            print("|  {}  |     {}    |    {}   |".format(
                row[0], row[1], row[2]))
            dic[row[1]] = row[2]
            list1 += row[1]
            list1 += str(int(row[2]))
            list1 += ' rubaai'
            list1 += ', '
        print('+------+-----------+---------+')
        tamil_audio(list1)
        incr += 1
        mod = 'Uingaluku virupamana vunavai kooravum'
        tamil_audio(mod)
        incr += 1
    elif (lang == 0):
        eng_audio("Menu List")
        list1 = ""
        for row in rows:
            print("|  {}  |     {}    |    {}   |".format(
                row[0], row[1], row[2]))
            dic[row[1]] = row[2]
            list1 += row[1]
            list1 += str(int(row[2]))
            list1 += ' rupees'
            list1 += ', '
        print('+------+-----------+---------+')
        eng_audio(list1)
        mod = 'What food would you like to have'
        eng_audio(mod)
    cursor.close()
    conn.close()


# Items User Input
try:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("-----SPEAK-----")
        audio = r.listen(source)
    text1 = ""
    engine.setProperty('voice', voices[0 if lang == 0 else 1].id)
    text1 = r.recognize_google(audio, language='en' if lang == 0 else 'ta-IN')

except sr.UnknownValueError:
    print("ERROR")
except sr.RequestError as e:
    print("ERROR; {0}".format(e))
if (lang == 1):
    text1 = translator.translate(text1, dest='en')
    text1 = text1.text
txt1 = Word2Num(text1)
output_list = []

for word in re.findall(r'\d+|\D+', txt1):
    try:
        output_list.append(int(word))
    except ValueError:
        output_list.append(word.strip())
text1 = output_list

# Invoice
print("******************INVOICE******************")
print('+------+-----------+----------------------+')
print('|  ID  |   ITEMS   |  QUANTITY  |  PRICE  |')
print('+------+-----------+----------------------+')
co = 1
format = f"\nVJ ASSITANCE\n******************INVOICE******************\nINVOICE\n"
grand = 0
for i in range(0, len(text1), 2):
    text1[i] = sp.word_change(text1[i])
    print("|   {}   |    {}    |    {}    |    {}    |".format(
        co, text1[i], text1[i + 1], dic[text1[i]] * int(text1[i + 1])))

    grand += dic[text1[i]] * int(text1[i + 1])
    co += 1
    format += "{} - {} - {}\n".format(text1[i],
                                      text1[i + 1], dic[text1[i]] * int(text1[i + 1]))
print('+--------+----------+----------+----------+')
print('                   Grand Total = ' + str(grand))
print('+--------+----------+----------+----------+')
print("*******************************************")
format += "Grand Total : {}".format(grand)
format += "\n*******************************************"
if lang == 0:
    eng_audio("You Have Ordered")
    for i in range(0, len(text1), 2):
        eng_audio("{} {}".format(round(text1[i + 1]), text1[i]))
        # conn1.execute("INSERT INTO INVOICE('Items', 'Quantity') VALUES (?, ?);", (text1[i], text1[i + 1]))
    eng_audio("Total Amount To Be Paid {} rupees".format(round(grand)))
    eng_audio("Thank You For Ordering")

else:
    tamil_audio("Neeingal Aader Seidhadhu")
    incr += 1
    for i in range(0, len(text1), 2):
        tamil_audio("{} {}".format(round(text1[i + 1]), text1[i]))
        # conn1.execute("INSERT INTO INVOICE('Items', 'Quantity') VALUES (?, ?);", (text1[i], text1[i + 1]))
        incr += 1
    tamil_audio(
        "Neeingal Sezhutha Vendiya Motha Thogai {} Rubaai".format(round(grand)))
    incr += 1
    tamil_audio("Order Seidhadhurku Nandri")
    incr += 1

send_sms_notification(format)
# Invoice Database
cursor = conn1.cursor()
cursor.execute("SELECT MAX(ID) FROM INVOICE")
result = cursor.fetchone()
last_id = result[0]
last_id += 1
for i in range(0, len(text1), 2):
    conn1.execute("INSERT INTO INVOICE('ID', 'Items', 'Quantity') VALUES (?, ?, ?);",
                  (last_id, text1[i], text1[i + 1]))
conn1.commit()
conn1.close()
