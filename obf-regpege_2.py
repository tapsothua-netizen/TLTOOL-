from pystyle import Colors, Colorate
from rich.console import Console
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
import requests,os, random
from time import sleep
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
trang = "\033[1;37m"
tim = "\033[1;35m"
xanh = "\033[1;36m"
list_clone = []
list_img = []
dem = 0
stt = 0
stt2 = 0
SUCCESS = "THÀNH CÔNG"
# =========================== [ CLASS + FUNCTION TOOL ] ===========================
class API_PRO5_TLTOOL:
    
    def banner(self):
        os.system("cls" if os.name == "nt" else "clear")
        RESET = "[0m"
        BOLD  = "[1m"

        C1 = "[38;5;51m"
        C2 = "[38;5;75m"
        C3 = "[38;5;99m"
        C4 = "[38;5;129m"
        C5 = "[38;5;196m"

        logo = f"""{BOLD}
{C1}████████╗██╗          ████████╗ ██████╗  ██████╗ ██╗
{C2}╚══██╔══╝██║          ╚══██╔══╝██╔═══██╗██╔═══██╗██║
{C3}   ██║   ██║             ██║   ██║   ██║██║   ██║██║
{C4}   ██║   ██║             ██║   ██║   ██║██║   ██║██║
{C5}   ██║   ███████╗        ██║   ╚██████╔╝╚██████╔╝███████╗
{C5}   ╚═╝   ╚══════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
{RESET}
"""
        print(logo)
        print("─" * 65)
        print("[</>] LƯU Ý : MỖI ACC 1 NGÀY REG MÃ LÀ 3 PAGE DELAY ĐỂ LÀ 1500 THÌ XÁC SUẤT REG DC LÀ 90% VÀ ACC CHÍNH KHÓ DIE")
        print("[</>] BOX ZALO : https://zalo.me/g/buxmoo796")
        print("[</>] ZALO CÁ NHÂN : 0352816362")
        print("[</>] WEBSITE FB CỔ SCAN : https://betammo.site/client/home")
        print("─" * 65)
    def vttool_delay_tool(self, p):
       
        while(p>1):
            p=p-1
            print(fr'\033[1;31m [TLTOOL]  \033[1;91m[|] [CHƠ......] \033[1;91m[\033[1;37m{p}\033[1;91m]\033[1;37m','     ',end='\r');sleep(1/6)
            print(fr'\033[1;32m [TLTOOL]  \033[1;37m[/] [CHỜ_ĐI.....] \033[1;91m[\033[1;37m{p}\033[1;91m]\033[1;37m','     ',end='\r');sleep(1/6)
            print(fr'\033[1;33m [TLTOOL]  \033[1;91m[-] [CHỜ_ĐI_EM....] \033[1;91m[\033[1;37m{p}\033[1;91m]\033[1;37m','     ',end='\r');sleep(1/6)
            print(fr'\033[1;34m [TLTOOL]  \033[1;37m[+] [CHƠ_ĐI_EM_YÊU...] \033[1;91m[\033[1;37m{p}\033[1;91m]\033[1;37m','     ',end='\r');sleep(1/6)
            print(fr'\033[1;35m [TLTOOL]  \033[1;91m[\] [CHỜ_ĐI_EM_YÊU_LẮM..] \033[1;91m[\033[1;37m{p}\033[1;91m]\033[1;37m','     ',end='\r');sleep(1/6)
            print(fr'\033[1;36m [TLTOOL]  \033[1;37m[|] [😜_CHƯA_ĐƯƠC_MÔ_😂] \033[1;91m[\033[1;37m{p}\033[1;91m]\033[1;37m','     ',end='\r');sleep(1/6)
    def getthongtinfacebook(self, cookie: str):
        
        headers_get = {'authority': 'www.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36','viewport-width': '1184','cookie': cookie}
        try:
            print(f'\033[1;95mĐang Tiến Hành Check Live Nhé', end="\r")
            url_profile = requests.get('https://www.facebook.com/me', headers = headers_get).url
            get_dulieu_profile = requests.get(url = url_profile, headers = headers_get).text
        except:
            return False
        try:
            uid_get = cookie.split('c_user=')[1].split(';')[0]
            fb_dtsg_get = get_dulieu_profile.split('{"name":"fb_dtsg","value":"')[1].split('"},')[0]
            jazoest_get = get_dulieu_profile.split('{"name":"jazoest","value":"')[1].split('"},')[0]
            name_get = get_dulieu_profile.split('<title>')[1].split('</title>')[0]
            return name_get,uid_get,fb_dtsg_get,jazoest_get
        except:
            try:
                uid_get = cookie.split('c_user=')[1].split(';')[0]
                fb_dtsg_get = get_dulieu_profile.split(',"f":"')[1].split('","l":null}')[0]
                jazoest_get = get_dulieu_profile.split('&jazoest=')[1].split('","e":"')[0]
                name_get = get_dulieu_profile.split('<title>')[1].split('</title>')[0]
                return name_get,uid_get,fb_dtsg_get,jazoest_get
            except:
                return False    
    def RegPage(self, cookie, name, uid, fb_dtsg, jazoest):
        
        namepage = requests.get('https://www.webkey.x10.mx/listname.php?count=2').json()['data'][0]['name']
        global de
        headers_reg = {'authority': 'www.facebook.com','accept': '*/*','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','origin': 'https://www.facebook.com','referer': 'https://www.facebook.com/pages/creation?ref_type=launch_point','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','viewport-width': '979','x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation','x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY','cookie': cookie}
        data_reg = {'av': uid,'__user': uid,'__a': '1','__dyn': '7AzHxq1mxu1syUbFuC0BVU98nwgU29zEdEc8co5S3O2S7o11Ue8hw6vwb-q7oc81xoswIwuo886C11xmfz81sbzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzE8FU5e7oqBwJK2W5olwuEjUlDw-wUws9ovUaU3qxWm2Sq2-azo2NwkQ0z8c84K2e3u362-2B0oobo','__csr': 'gP4ZAN2d-hbbRmLObkZO8LvRcXWVvth9d9GGXKSiLCqqr9qEzGTozAXiCgyBhbHrRG8VkQm8GFAfy94bJ7xeufz8jK8yGVVEgx-7oiwxypqCwgF88rzKV8y2O4ocUak4UpDxu3x1K4opAUrwGx63J0Lw-wa90eG18wkE7y14w4hw6Bw2-o069W00CSE0PW06aU02Z3wjU6i0btw3TE1wE5u','__req': 't','__hs': '19296.HYP:comet_pkg.2.1.0.2.1','dpr': '1','__ccg': 'EXCELLENT','__rev': '1006496476','__s': '1gapab:y4xv3f:2hb4os','__hsi': '7160573037096492689','__comet_req': '15','fb_dtsg': fb_dtsg,'jazoest': jazoest,'lsd': 'ZM7FAk6cuRcUp3imwqvHTY','__aaid': '800444344545377','__spin_r': '1006496476','__spin_b': 'trunk','__spin_t': '1667200829','fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation','variables': '{"input":{"bio":"TLTOOL TÔI MUA TOOL BẠN DÙNG","categories":["181475575221097"],"creation_source":"comet","name":"'+namepage+'","page_referrer":"launch_point","actor_id":"'+uid+'","client_mutation_id":"1"}}','server_timestamps': 'true','doc_id': '5903223909690825',}
        try:
            idpage = requests.post('https://www.facebook.com/api/graphql/', headers=headers_reg, data=data_reg, timeout=20).json()['data']['additional_profile_plus_create']['additional_profile']['id']
            dem+=1
            part1 = Colorate.Horizontal(Colors.red_to_yellow, f"| {dem} |")
            part2 = Colorate.Horizontal(Colors.green_to_white, f" {SUCCESS} |")
            part3 = Colorate.Horizontal(Colors.red_to_green, f" NAME FB: {name} |")
            part4 = Colorate.Horizontal(Colors.purple_to_red, f" UID PRO5: {idpage} |")
            part5 = Colorate.Horizontal(Colors.red_to_green, f" NAME PRO5: {namepage} |")
            print(part1 + part2 + part3 + part4 + part5)
            return idpage
        except:
            print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;31mReg Thất Bại Có Vẻ Acc Của Bạn Đã Bị Block!!')
            return False
# =========================== [ START TOOL ] ===========================
TLTOOL = API_PRO5_TLTOOL()
TLTOOL.banner()
print('[ENTER - ĐỂ DỪNG NHẬP]')
while True:
    stt+=1
    cookie_fb = input(f'\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mVUI LÒNG NHẬP COOKIE THỨ \033[1;31m[\033[1;33m{stt}\033[1;31m]\033[1;33m: ')
    if cookie_fb == '':
        break
    checklive = TLTOOL.getthongtinfacebook(cookie_fb)
    if checklive != False:
        print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mName Facebook \033[1;33m: '+checklive[0])
        list_clone.append(f'{cookie_fb}|{checklive[0]}|{checklive[1]}|{checklive[2]}|{checklive[3]}')
        print('─'*50)
    else:
        stt-1
        print('\033[1;31mCookie '+cookie_fb.split('c_user=')[1].split(';')[0]+', Die Or Out Vui Lòng Kiểm Tra Lại!!')
# Tiến Hành Nhập Setting Reg Page
print('─'*50)
slpage = int(input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mBẠN MUỐN TẠO BAO NHIÊU PAGE THÌ DỪNG TOOL\033[1;33m: '))
print('─'*50)
delay = int(input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mVUI LÒNG NHẬP DELAY REG PAGE\033[1;33m: '))
print('─'*50)
# Tiến Hành Chạy Tool
TLTOOL.banner()
while True:
    for dulieuclone in list_clone:
        idpage = TLTOOL.RegPage(str(dulieuclone).split('|')[0], str(dulieuclone).split('|')[1], str(dulieuclone).split('|')[2], str(dulieuclone).split('|')[3], str(dulieuclone).split('|')[4])        
        TLTOOL.vttool_delay_tool(delay)
        if dem == slpage:
            input(f'\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mDone \033[1;33m{dem}, \033[1;32mPage </> \033[1;95mENTER ĐỂ EXIT')
            exit()