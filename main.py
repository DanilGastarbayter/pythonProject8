import telebot
import time
bot = telebot.TeleBot('5550078959:AAGAAl1owps1xE3TnKH6S8_8EJYg4Jk7nuU')
CHANNEL_NAME = '@ilikeblackmanbot'
f = open('data/fun.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()
for joke in jokes:
    bot.send_message(CHANNEL_NAME, joke)
    time.sleep(3600)
bot.send_message(CHANNEL_NAME, "Анекдоты закончились :-(")