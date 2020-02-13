# -*- coding: utf-8 -*-
#-----MusiBat-----#
from linepy import *
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import ChatRoomAnnouncement
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib3, urllib.parse, html5lib, wikipedia, atexit, timeit, pafy, youtube_dl, traceback
from googletrans import Translator


cl = LINE("email","password")
cl.log("Auth Token : " + str(cl.authToken))

ki = LINE("email","password")
ki.log("Auth Token : " + str(ki.authToken))

kk = LINE("email","password")
kk.log("Auth Token : " + str(kk.authToken))

kc = LINE("email","password")
kc.log("Auth Token : " + str(kc.authToken))

km = LINE("email","password")
km.log("Auth Token : " + str(km.authToken))

kb = LINE("email","password")
kb.log("Auth Token : " + str(kb.authToken))

kd = LINE("email","password")
kd.log("Auth Token : " + str(kd.authToken))

ke = LINE("email","password")
ke.log("Auth Token : " + str(ke.authToken))

kf = LINE("email","password")
kf.log("Auth Token : " + str(kf.authToken))

kg = LINE("email","password")
kg.log("Auth Token : " + str(kg.authToken))

kh = LINE("email","password")
kh.log("Auth Token : " + str(kh.authToken))

sw = LINE("email","password")
sw.log("Auth Token : " + str(sw.authToken))

cl.sendMessage("ubcd98265d4210c2215f3ddb43d79c414", "Hi... I am your bot.")

print ("\n      █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n      █░░║║║╠─║─║─║║║║║╠─░░█\n      █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n")

oepoll = OEPoll(cl)
call = cl

creator = ["ubcd98265d4210c2215f3ddb43d79c414"]
owner = ["ubcd98265d4210c2215f3ddb43d79c414"]
admin = ["ubcd98265d4210c2215f3ddb43d79c414"]
staff = ["ubcd98265d4210c2215f3ddb43d79c414"]

lineProfile = cl.getProfile()
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = km.getProfile().mid
Emid = kb.getProfile().mid
Fmid = kd.getProfile().mid
Gmid = ke.getProfile().mid
Hmid = kf.getProfile().mid
Imid = kg.getProfile().mid
Jmid = kh.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [cl,ki,kk,kc]
ABC = [ki,kk,kc,km,kb,kd,ke,kf,kg,kh]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,Zmid]
Saints = creator + admin + owner + staff
Team = creator + owner + admin + staff + Bots
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

protectcancel = []
welcome = []
targets = []
protectname = []
prohibitedWords = ['nukeall', 'kickall', 'cleanse', 'Kickall', 'fuck', 'Cleanse']
userTemp = {}
userKicked = []
msg_dict = {}
msg_dict1 = {}
temp_flood = {}
groupName = {}
groupImage = {}
list = []
ban_list = []
warmode = []
ghost = []

responsenamea = cl.getProfile().displayName
responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = km.getProfile().displayName
responsename5 = kb.getProfile().displayName
responsename6 = kd.getProfile().displayName
responsename7 = ke.getProfile().displayName
responsename8 = kf.getProfile().displayName
responsename9 = kg.getProfile().displayName
responsename10 = kh.getProfile().displayName


settings = {
    "autoBlock": False,
    "autoRead": False,
    "welcome": False,
    "leave": False,
    "mid": False,
    "replySticker": False,
    "stickerOn": False,
    "checkContact": False,
    "postEndUrl": True,
    "checkPost": False,
    "setKey": False,
    "restartPoint": False,
    "checkSticker": False,
    "userMentioned": False,
    "listSticker": False,
    "messageSticker": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
            },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "changeProfileVideo": False,
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
    "autoJoinTicket":True,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.200.32.99 Safari/537.36"
    ]
}

wait = {
    "limit": 2,
    "owner":{},
    "addowner":False,
    "dellowner":False,
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "dhenza":{},
    "likeOn": True,
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    "invite":False,
    'autoJoin':True,
    'autoAdd':False,
    'autoCancel':{"on":True, "members":1},
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "unsend":False,
    "selfbot":True,
    "mention":"Hey... Join Chat...",
    "Respontag":"Yup!, How Can I Help?",
    "welcome":"Wellcome...",
    "comment":"Auto like By ",
    "comment1":"Auto like By ",
    "message":"[> Thanks For Add Me <]\n\n●> This Is Auto Add Mesage"
}

protect = {
    "pqr":[],
    "pinv":[],
    "proall":[],
    "antijs":[],
    "protect":[]
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)

mulai = time.time()

tz = pytz.timezone("Asia/Dhaka")
timeNow = datetime.now(tz=tz)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def mentionMembers(to, mids=[]):
    parsed_len = len(mids)//20+1
    result = ' [> Mention Members <]\n╭━━•≽ \n'
    mention = '@zeroxyuuki\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*20:(point+1)*20]:
            no += 1
            result += '┣• %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += '╰━━•≽ \n [Total「{}」Mentions]'.format(str(len(mids)))
        if result:
            if result.endswith('\n'): result = result[:-1]
            cl.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''

def logError(text):
    cl.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Dhaka")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Days %02d Hours %02d Mins %02d Secs' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Days %02d Hours %02d Mins %02d Secs' % (days, hours, mins, secs)
    
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            client.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)

def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        cl.sendMessage(tmp, "Bot Activated!")
                    except Exception as error:
                        logError(error)
                        
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = cl.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed Update Profile"
        cl.updateProfilePicture(pict, 'vp')
        return "Success Update Profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))

def changeProfileVideo(to):
    if settings['changeProfileVideo']['picture'] == None:
        return cl.sendMessage(to, "Photo Not Found")
    elif settings['changeProfileVideo']['video'] == None:
        return cl.sendMessage(to, "Video Not Found")
    else:
        path = settings['changeProfileVideo']['video']
        files = {'file': open(path, 'rb')}
        obs_params = cl.genOBSParams({'oid': cl.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return cl.sendMessage(to, "Failed Update Profile")
        path_p = settings['changeProfileVideo']['picture']
        settings['changeProfileVideo']['status'] = False
        cl.updateProfilePicture(path_p, 'vp')

def cloneProfile(mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)

def restoreProfile():
    profile = cl.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        cl.updateProfileAttribute(8, profile.pictureStatus)
        cl.updateProfile(profile)
    else:
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    cl.updateProfileCoverById(coverId)
    
def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)

def backupProfile():
    profile = cl.getContact(mid)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = cl.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)

###

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "[> Mention Members <]\n\n".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1

            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Hello ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "\nHello ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nGroup Name : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2019,4,10)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Dhaka")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"\n●> Time : "+datetime.strftime(timeNow,'%H:%M:%S')+" [GMT +6]\n●> Group : ["+str(len(gid))+"]\n●> Friends : ["+str(len(teman))+"]\n●> Expired : In "+hari+"\n●> Version : TR-1.0.5\n●> Date : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n●> Runtime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain['keyCommand']):
        cmd = pesan.replace(Setmain['keyCommand'],"")
    else:
        cmd = "command"
    return cmd

def helpbot():
    num = 1
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage2 = "╭━━━━━━━━━━━━━━━╮\n"
    helpMessage2 += "║    ♕𝘚𝘶𝘤𝘪𝘥𝘦 𝘚𝘲𝘶𝘢𝘥♕\n"
    helpMessage2 += "║╭══•≽\n"
    helpMessage2 += "║┝•≽Hi \n"
    helpMessage2 += "║┝•≽ %i. " % num + key + "Crot @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Vc @ \n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Mainkan @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Invite \n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Banlist\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Clearban\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Adminexpl:on\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Exladmin:on @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Exladmin:on\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Adminexpl:on @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Owner:on\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Exlstaff:on\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Exlstaff:on @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Staffexpl:on\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Staffexpl:on @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Bot:on\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Bot:on @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Botexpl:on\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Botexpl:on @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Ban:on @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Ban:on\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Unban:on @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Unban:on\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i ." % num + key + "Talkban:on @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Talkban:on\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Untalkban:on @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Untalkban:on\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Talkbanlist\n"
    num = (num+1)    
    helpMessage2 += "║┝•≽ %i. " % num + key + "exl@proall on/off\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Proqr on/off\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Prokick on/off\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Backup on/off\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Proinvite on/off\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Procancel on/off\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Js on/off\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Killban\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Autojoin on/off\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Jointicket on/off\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Play @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Prank\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Admindel @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Admin @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Staffadd @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Staffdel @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Botadd @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Botdel @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Checkpost On/Off\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "CheckSticker On/Off\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Unsend On\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Unsemd Off\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Cowneradd\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Cownerdel\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Cadminadd\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Cadmindel\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Ctaffadd\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Cstaffdel\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Cbotadd\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Cbotdel\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Fresh/Refresh\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Cownerlist\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Cadminlist\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Cstafflist\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Cbotlist\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Antitag On/Off\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Contact On/Off\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "leave on/off\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Respond On/Off\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Autojoin On/Off\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Autoleave On/Off\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Autoadd On /Off\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Sticker On /Off\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Jointicket On/Off\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Talkban @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Talkunban @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Ctalkban\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Ctalkunban\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Ban @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Unban @\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Cban\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Cunban\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Banlist\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Talkbanlist\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Cbanlist\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Clearban\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Set pmreply\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Set respond:\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Set welcome:\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Set sider:\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Check pmreply\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Check welcome\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Check respond\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Check reader\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Checkban\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Checkban\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Checkban\n"
    num = (num+1)
    helpMessage2 += "║┝•≽ %i. " % num + key + "Checkban\n"
    num = (num+1)
    helpMessage2 += "║╰══•≽\n╰━━━━━━━━━━━━━━━╯"
    return helpMessage2

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return

        if op.type == 11:
            if op.param1 in protect["pqr"]:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventJoinByTicket = False
                            cl.updateGroup(X)
                            Ti = cl.reissueGroupTicket(op.param1)
                            ki.acceptGroupInvitationByTicket(op.param1,Ti)
                            ki.sendMessage(op.param1,"wah kiker mainan qr minta di cipok")
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            wait["blacklist"][op.param2] = True
                            X = kj.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            ki.updateGroup(X)
                            ki.leaveGroup(op.param1)
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ki.updateGroup(X)
                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kk.updateGroup(X)
                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kc.updateGroup(X)
                                        cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if kb.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            kb.reissueGroupTicket(op.param1)
                                            X = kb.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            cl.updateGroup(X)
                                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if kd.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                kd.reissueGroupTicket(op.param1)
                                                X = kd.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                kd.updateGroup(X)
                                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        try:
                                            if ke.getGroup(op.param1).preventedJoinByTicket == False:
                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                    ke.reissueGroupTicket(op.param1)
                                                    X = ke.getGroup(op.param1)
                                                    X.preventedJoinByTicket = True
                                                    ke.updateGroup(X)
                                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)            
                                        except:
                                            try:
                                                if kf.getGroup(op.param1).preventedJoinByTicket == False:
                                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                        kf.reissueGroupTicket(op.param1)
                                                        X = kf.getGroup(op.param1)
                                                        X.preventedJoinByTicket = True
                                                        kf.updateGroup(X)
                                                        cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)           
                                            except:
                                                try:
                                                    if kg.getGroup(op.param1).preventedJoinByTicket == False:
                                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                            kg.reissueGroupTicket(op.param1)
                                                            X = kg.getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            kg.updateGroup(X)
                                                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)          
                                                except:
                                                    try:
                                                        if kh.getGroup(op.param1).preventedJoinByTicket == False:
                                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                kh.reissueGroupTicket(op.param1)
                                                                X = kh.getGroup(op.param1)
                                                                X.preventedJoinByTicket = True
                                                                kh.updateGroup(X)
                                                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)             
                                                    except:
                                                        pass
                      
        if op.type == 11:
            if op.param1 in warmode:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            wait["blacklist"][op.param2] = True
                            try:ki.kickoutFromGroup(op.param1,[op.param2])
                            except:
                            	try:kk.kickoutFromGroup(op.param1,[op.param2])
                            	except:
                            	    try:kc.kickoutFromGroup(op.param1,[op.param2])
                            	    except:
                            	        try:sw.kickoutFromGroup(op.param1,[op.param2])
                            	        except:pass
                            warmode.remove(op.param1)
                except:pass


        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                   try:ki.kickoutFromGroup(op.param1,[op.param2])
                   except:
                   	try:kk.kickoutFromGroup(op.param1,[op.param2])
                   	except:
                   	    try:kc.kickoutFromGroup(op.param1,[op.param2])
                   	    except:
                   	        try:cl.reissueGroupTicket(op.param1);X = cl.getGroup(op.param1);X.preventedJoinByTicket = True;Ticket = cl.reissueGroupTicket(op.param1);sw.acceptGroupInvitationByTicket(op.param1,Ticket);sw.kickoutFromGroup(op.param1,[op.param2])
                   	        except:pass
                   cl.reissueGroupTicket(op.param1)
                   X = cl.getGroup(op.param1)
                   X.preventedJoinByTicket = True
                   cl.updateGroup(X)
                   warmode.append(op.param1)
                else:
                   pass

#start...
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Sorry You Are Not In Stafflist...")
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ginfo = cl.getGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ginfo = ki.getGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ginfo = kk.getGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ginfo = kc.getGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ginfo = km.getGroup(op.param1)
                    else:
                        km.acceptGroupInvitation(op.param1)
                        ginfo = km.getGroup(op.param1)
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ginfo = kb.getGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ginfo = kd.getGroup(op.param1)
                    else:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)
            if Gmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ginfo = ke.getGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
            if Hmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ginfo = kf.getGroup(op.param1)
                    else:
                        kf.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1)
            if Imid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ginfo = kg.getGroup(op.param1)
                    else:
                        kg.acceptGroupInvitation(op.param1)
                        ginfo = kg.getGroup(op.param1)
            if Jmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ginfo = kh.getGroup(op.param1)
                    else:
                        kh.acceptGroupInvitation(op.param1)
                        ginfo = kh.getGroup(op.param1)
#____________________________________________________________________
        if op.type == 13:
            if op.param1 in protect['pinv']:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        cl.reissueGroupTicket(op.param1)
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                wait["blacklist"][op.param2] = True  
                                random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    pass
                        
        if op.type == 19:
            if mid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param3)
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.findAndAddContactsByMid(op.param3)
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param3)
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    km.kickoutFromGroup(op.param1,[op.param2])
                                    km.findAndAddContactsByMid(op.param3)
                                    km.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param3)
                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.findAndAddContactsByMid(op.param3)
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                            cl.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Amid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.findAndAddContactsByMid(op.param3)
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.findAndAddContactsByMid(op.param3)
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                km.kickoutFromGroup(op.param1,[op.param2])
                                km.findAndAddContactsByMid(op.param3)
                                km.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.findAndAddContactsByMid(op.param3)
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    ki.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        cl.findAndAddContactsByMid(op.param3)
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            kk.findAndAddContactsByMid(op.param3)
                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                            ki.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Bmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.findAndAddContactsByMid(op.param3)
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            km.kickoutFromGroup(op.param1,[op.param2])
                            km.findAndAddContactsByMid(op.param3)
                            km.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.findAndAddContactsByMid(op.param3)
                                kb.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    cl.findAndAddContactsByMid(op.param3)
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    kk.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                        kf.findAndAddContactsByMid(op.param3)
                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            kh.kickoutFromGroup(op.param1,[op.param2])
                                            kh.findAndAddContactsByMid(op.param3)
                                            kh.inviteIntoGroup(op.param1,[op.param3])
                                            kk.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Cmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        km.kickoutFromGroup(op.param1,[op.param2])
                        km.findAndAddContactsByMid(op.param3)
                        km.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            ke.findAndAddContactsByMid(op.param3)
                            kc.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.findAndAddContactsByMid(op.param3)
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.findAndAddContactsByMid(op.param3)
                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        kg.kickoutFromGroup(op.param1,[op.param2])
                                        kg.findAndAddContactsByMid(op.param3)
                                        kg.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                            kb.findAndAddContactsByMid(op.param3)
                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Dmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kb.findAndAddContactsByMid(op.param3)
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        km.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            kd.kickoutFromGroup(op.param1,[op.param2])
                            kd.findAndAddContactsByMid(op.param3)
                            kd.inviteIntoGroup(op.param1,[op.param3])
                            km.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.findAndAddContactsByMid(op.param3)
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                km.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.findAndAddContactsByMid(op.param3)
                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                    km.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.findAndAddContactsByMid(op.param3)
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        km.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            kg.kickoutFromGroup(op.param1,[op.param2])
                                            kg.findAndAddContactsByMid(op.param3)
                                            kg.inviteIntoGroup(op.param1,[op.param3])
                                            km.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Emid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        kb.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            kh.kickoutFromGroup(op.param1,[op.param2])
                            kh.findAndAddContactsByMid(op.param3)
                            kh.inviteIntoGroup(op.param1,[op.param3])
                            kb.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param3)
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                kb.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    kb.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        km.kickoutFromGroup(op.param1,[op.param2])
                                        km.findAndAddContactsByMid(op.param3)
                                        km.inviteIntoGroup(op.param1,[op.param3])
                                        kb.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            cl.findAndAddContactsByMid(op.param3)
                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                            kb.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass
                return

            if Fmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                        kf.findAndAddContactsByMid(op.param3)
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        kd.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            kg.kickoutFromGroup(op.param1,[op.param2])
                            kg.findAndAddContactsByMid(op.param3)
                            kg.inviteIntoGroup(op.param1,[op.param3])
                            kd.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                kh.kickoutFromGroup(op.param1,[op.param2])
                                kh.findAndAddContactsByMid(op.param3)
                                kh.inviteIntoGroup(op.param1,[op.param3])
                                kd.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    kd.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        km.kickoutFromGroup(op.param1,[op.param2])
                                        km.findAndAddContactsByMid(op.param3)
                                        km.inviteIntoGroup(op.param1,[op.param3])
                                        kd.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            cl.findAndAddContactsByMid(op.param3)
                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                            kd.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass    
                return

            if Gmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        kd.inviteIntoGroup(op.param1,[op.param3])
                        ke.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            kh.kickoutFromGroup(op.param1,[op.param2])
                            kh.findAndAddContactsByMid(op.param3)
                            kh.inviteIntoGroup(op.param1,[op.param3])
                            ke.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                kf.kickoutFromGroup(op.param1,[op.param2])
                                kf.findAndAddContactsByMid(op.param3)
                                kf.inviteIntoGroup(op.param1,[op.param3])
                                kb.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    kg.kickoutFromGroup(op.param1,[op.param2])
                                    kg.findAndAddContactsByMid(op.param3)
                                    kg.inviteIntoGroup(op.param1,[op.param3])
                                    ke.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        km.kickoutFromGroup(op.param1,[op.param2])
                                        km.findAndAddContactsByMid(op.param3)
                                        km.inviteIntoGroup(op.param1,[op.param3])
                                        kd.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            kh.kickoutFromGroup(op.param1,[op.param2])
                                            kh.findAndAddContactsByMid(op.param3)
                                            kh.inviteIntoGroup(op.param1,[op.param3])
                                            ke.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass 
                return

            if Hmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        kg.kickoutFromGroup(op.param1,[op.param2])
                        kg.findAndAddContactsByMid(op.param3)
                        kg.inviteIntoGroup(op.param1,[op.param3])
                        kf.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            kh.kickoutFromGroup(op.param1,[op.param2])
                            kh.findAndAddContactsByMid(op.param3)
                            kh.inviteIntoGroup(op.param1,[op.param3])
                            kf.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                ke.kickoutFromGroup(op.param1,[op.param2])
                                ke.findAndAddContactsByMid(op.param3)
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                kf.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    kf.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        km.kickoutFromGroup(op.param1,[op.param2])
                                        km.findAndAddContactsByMid(op.param3)
                                        km.inviteIntoGroup(op.param1,[op.param3])
                                        kf.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param3)
                                            kd.inviteIntoGroup(op.param1,[op.param3])
                                            kf.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass 
                return

            if Imid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        kh.kickoutFromGroup(op.param1,[op.param2])
                        kh.findAndAddContactsByMid(op.param3)
                        kh.inviteIntoGroup(op.param1,[op.param3])
                        kg.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param3)
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kg.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param3)
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                kg.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    ke.findAndAddContactsByMid(op.param3)
                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                    kg.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.findAndAddContactsByMid(op.param3)
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        kg.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            kg.kickoutFromGroup(op.param1,[op.param2])
                                            kg.findAndAddContactsByMid(op.param3)
                                            kg.inviteIntoGroup(op.param1,[op.param3])
                                            kg.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass  
                return

            if Jmid in op.param3:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.findAndAddContactsByMid(op.param3)
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        kh.acceptGroupInvitation(op.param1)
                        wait["blacklist"][op.param2] = True
                    except:
                        try:
                            kd.kickoutFromGroup(op.param1,[op.param2])
                            kd.findAndAddContactsByMid(op.param3)
                            kd.inviteIntoGroup(op.param1,[op.param3])
                            kh.acceptGroupInvitation(op.param1)
                            wait["blacklist"][op.param2] = True
                        except:
                            try:
                                kg.kickoutFromGroup(op.param1,[op.param2])
                                kg.findAndAddContactsByMid(op.param3)
                                kg.inviteIntoGroup(op.param1,[op.param3])
                                kh.acceptGroupInvitation(op.param1)
                                wait["blacklist"][op.param2] = True
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    kh.acceptGroupInvitation(op.param1)
                                    wait["blacklist"][op.param2] = True
                                except:
                                    try:
                                        km.kickoutFromGroup(op.param1,[op.param2])
                                        km.findAndAddContactsByMid(op.param3)
                                        km.inviteIntoGroup(op.param1,[op.param3])
                                        kh.acceptGroupInvitation(op.param1)
                                        wait["blacklist"][op.param2] = True
                                    except:
                                        try:
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            cl.findAndAddContactsByMid(op.param3)
                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                            kh.acceptGroupInvitation(op.param1)
                                            wait["blacklist"][op.param2] = True
                                        except:
                                            pass                          
                return
#____________________________________________________________________
        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)
                
        if op.type == 13:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kk.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kc.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    km.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                    	kb.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                    	pass
                                    	    
                return
#__________________________________ 
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    km.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                    	kb.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                    	pass
                                    	    
                return
#____________________________________________________________________               
        if op.type == 19:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    km.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                    	kb.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                    	pass
                                    	    
                return
#____________________________________________________________________
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message"])

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param3 in Bots:
                    if op.param2 not in Bots and op.param2 not in Team:
                        wait["blacklist"][op.param2] = True
                        try:
                            if op.param3 not in wait["blacklist"]:
                                ki.findAndAddContactsByMid(op.param1,[Dmid])
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[Dmid])
                        except:
                            pass


#why
        if op.type == 32:
            if op.param3 in Dmid:
                if op.param2 not in Bots or op.param2 not in owner or op.param2 not in admin or op.param2 not in staff:
                     wait["blacklist"][op.param2] = True
                     try:
                         cl.inviteIntoGroup(op.param1,[op.param3])
                         ki.kickoutFromGroup(op.param1,[op.param2])
                         cl.sendMessage(op.param1, "➲➢Main cancle w cipok⎌༓༓༓▸")
                     except:
                         pass
#___________________________________________________________________
        if op.type == 19:
            if op.param1 in protect["proall"]:
                if op.param2 in Bots:
                    pass
                elif op.param2 in Bots:
                    pass
                elif op.param2 in owner:
                    pass
                elif op.param2 in admin:
                    pass
                elif op.param2 in staff:
                    pass
                else:
                    ki.kickoutFromGroup(op.param1,[op.param2])
                    if op.param3 in wait["blacklist"]:
                        pass
                    else:
                        km.findAndAddContactsByMid(op.param3)
                        km.inviteIntoGroup(op.param1,[op.param3])
                        wait["blacklist"][op.param2] = True

            if op.param1 in protect["protect"]:
                if op.param2 in Bots:
                    pass
                elif op.param2 in owner:
                    pass
                elif op.param2 in admin:
                    pass
                elif op.param2 in staff:
                    pass
                elif op.param2 in Bots:
                    pass
                else:
                    ki.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True

#***
            if op.param1 in protect["antijs"]:
                if op.param3 in mid:
                    if op.param2 in Bots:
                        pass
                    elif op.param2 in Bots:
                        pass
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in staff:
                        pass
                    else:
                        sw.acceptGroupInvitation(op.param1)
                        G = sw.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        sw.updateGroup(G)
                        Ticket = sw.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        km.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = True
                        wait["blacklist"][op.param2] = True

            try:
                if op.param3 in owner:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in admin:
                        pass
                    else:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if op.param3 in admin:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if op.param3 in staff:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in staff:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in staff:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True              
            except:
                pass
#
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        text = command(text)
                        if receiver in temp_flood:
                            if temp_flood[receiver]["expire"] == True:
                                    temp_flood[receiver]["expire"] = False
                                    temp_flood[receiver]["time"] = time.time()

                            elif time.time() - temp_flood[receiver]["time"] <= 2:
                                temp_flood[receiver]["flood"] += 1
                                if temp_flood[receiver]["flood"] >= 15:
                                    temp_flood[receiver]["flood"] = 0
                                    temp_flood[receiver]["expire"] = True
                                    ret_ = "Detect Flood Bot Off For 30 Secs..."
                                    userid = "https://line.me/ti/p/~" + line.profile.userid
                                    cl.sendMessage(msg.to,'[> Spam Detected <]\n\n'+str(ret_), {'AGENT_NAME': '[> Help Settings <]','AGENT_LINK': 'http://line.me/ti/p/7BJuwt8Jiq','AGENT_ICON': 'http://dl.profile.line-cdn.net/0hRa7A93YaDU4KOCA-s_5yGTZ9AyN9FgsGclhELio6UX0gX08cMVZBICc5VX8hWk5KPwsVKikxAHog' })
                                    
                            else:
                                 temp_flood[receiver]["flood"] = 0
                            temp_flood[receiver]["time"] = time.time()
                        else:
                            temp_flood[receiver] = {
    	                        "time": time.time(),
    	                        "flood": 0,
    	                        "expire": False
                            }                    
#
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 55:            
            try:
                if op.param1 in read["readPoint"]:
                    if op.param2 in read["readMember"][op.param1]:
                        pass
                    else:
                        read["readMember"][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendImageWithURL(op.param1, image)
                        cl.sendMessage(op.param1, None, contentMetadata={"STKID":"13162615","STKPKGID":"1326453","STKVER":"1"}, contentType=7)

        if op.type == 65:
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Image Below':
                                ginfo = cl.getGroup(at)
                                dhenza = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "Image Detected\nSender : "
                                ret_ = "Group Name : {}".format(str(ginfo.name))
                                ret_ += "\nSent Time : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(dhenza.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':nadyatj.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                dhenza = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "Deleted Msg\n"
                                ret_ += "Sender : {}".format(str(dhenza.displayName))
                                ret_ += "\nGroup Name : {}".format(str(ginfo.name))
                                ret_ += "\nSent Time : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\nMessage : {}".format(str(msg_dict[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                dhenza = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "Deleted Sticker\n"
                                ret_ += "Sender : {}".format(str(dhenza.displayName))
                                ret_ += "\nGroup Name : {}".format(str(ginfo.name))
                                ret_ += "\nSent Time : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          cl.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              ki.kickoutFromGroup(msg.to, [msg._from])
                          except:
                              try:
                                  kk.kickoutFromGroup(msg.to, [msg._from])
                              except:
                                  try:
                                  	kc.kickoutFromGroup(msg.to, [msg._from])
                                  except:
                                      pass
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           saints = cl.getContact(msg._from)
                           sendMention1(msg.to, saints.mid, "", wait["Respontag"])
                           cl.sendMessage(op.param1, None, contentMetadata={"STKID":"13162615","STKPKGID":"1326453","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.mentiontag(msg.to,[msg._from])
                           cl.sendMessage(msg.to, "[> Antitag <]\n\n●> Don't Tag Me When-\n   Antitag Is Activated")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"Sticker ID\n\nSTKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)

#fun
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"Name : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#fun
               if msg.contentType == 7:
                  if msg._from in mid:
                     if settings["AddstickerTag"]["status"] == True:
                         settings["AddstickerTag"]["sid"] = msg.contentMetadata["STKID"]
                         settings["AddstickerTag"]["spkg"] = msg.contentMetadata["STKPKGID"]
                         cl.sendMessage(msg.to, "Sticker Respon Hasbeen Changed")
                         settings["AddstickerTag"]["status"] = False
                         
               if msg.contentType == 1:
                   if msg._from in owner or msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilePicture"]:
                            del settings["ChangeVideoProfilePicture"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','image.jpg')
                            cl.dhenzaPurnama('video.mp4','image.jpg')
                            cl.sendMessage(msg.to,"Change Video Profile Success!!!")
#fun
               if msg.contentType == 1:
                  if msg._from in mid:
                     if settings["Addimage"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         images[settings["Addimage"]["name"]] = str(path)
                         f = codecs.open("image.json","w","utf-8")
                         json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Successfully Added Images {}".format(str(settings["Addimage"]["name"])))
                         settings["Addimage"]["status"] = False
                         settings["Addimage"]["name"] = ""
               if msg.contentType == 2:
                  if msg._from in mid:
                     if settings["Addvideo"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         videos[settings["Addvideo"]["name"]] = str(path)
                         f = codecs.open("video.json","w","utf-8")
                         json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Successfully Added Video {}".format(str(settings["Addvideo"]["name"])))
                         settings["Addvideo"]["status"] = False
                         settings["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                  if msg._from in mid:
                     if settings["Addsticker"]["status"] == True:
                         stickers[settings["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                         f = codecs.open("sticker.json","w","utf-8")
                         json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Successfully Added Sticker {}".format(str(settings["Addsticker"]["name"])))
                         settings["Addsticker"]["status"] = False
                         settings["Addsticker"]["name"] = ""
               if msg.contentType == 3:
                  if msg._from in mid:
                     if settings["Addaudio"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         audios[settings["Addaudio"]["name"]] = str(path)
                         f = codecs.open("audio.json","w","utf-8")
                         json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Successfully Added Mp3 {}".format(str(settings["Addaudio"]["name"])))
                         settings["Addaudio"]["status"] = False
                         settings["Addaudio"]["name"] = ""
               if msg.contentType == 0:
                  if settings["autoRead"] == True:
                      cl.sendChatChecked(msg.to, msg_id)
                      print ("Read")
                  if text is None:
                      return
                  else:
                         for sticker in stickers:
                          if msg._from in mid:
                            if text.lower() == sticker:
                               sid = stickers[text.lower()]["STKID"]
                               spkg = stickers[text.lower()]["STKPKGID"]
                               cl.sendSticker(to, spkg, sid)
                         for image in images:
                          if msg._from in mid:
                            if text.lower() == image:
                               cl.sendImage(msg.to, images[image])
                         for audio in audios:
                          if msg._from in mid:
                            if text.lower() == audio:
                               cl.sendAudio(msg.to, audios[audio])
                         for video in videos:
                          if msg._from in mid:
                            if text.lower() == video:
                               cl.sendVideo(msg.to, videos[video])

#add__bot
               if msg.contentType == 13:
                 if msg._from in owner or msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"Already A Bot...")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"Promoted To Bot...")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Removed From Bot...")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"Not In Botlist...")
#add__owner
                 if msg._from in owner:
                  if wait["addowner"] == True:
                    if msg.contentMetadata["mid"] in owner:
                        cl.sendMessage(msg.to,"Already An Owner...")
                        wait["addowner"] = True
                    else:
                        owner.append(msg.contentMetadata["mid"])
                        wait["addowner"] = True
                        cl.sendMessage(msg.to,"Promoted To Owner...")
                 if wait["dellowner"] == True:
                    if msg.contentMetadata["mid"] in owner:
                        owner.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Removed From Owner...")
                    else:
                        wait["dellowner"] = True
                        cl.sendMessage(msg.to,"Not In Owner...")

#add__staff
                 if msg._from in owner or msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"Already A Staff...")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        cl.sendMessage(msg.to,"Promoted To Staff...")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Removed From Staff...")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        cl.sendMessage(msg.to,"Not In Staff...")
#add__admin
                 if msg._from in owner:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"Already An Admin...")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        cl.sendMessage(msg.to,"Promoted To Admin...")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Removed From Adminlist")
                    else:
                        wait["delladmin"] = True
                        cl.sendMessage(msg.to,"Not In Admin...")
#add__banlist
                 if msg._from in owner:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"Already In Banlist...")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        cl.sendMessage(msg.to,"Added To Banlist...")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Removed From Banlist...")
                    else:
                        wait["dblacklist"] = True
                        cl.sendMessage(msg.to,"Not In Banlist...")
#talkban
                 if msg._from in owner or msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        cl.sendMessage(msg.to,"Already In Talkbanlist...")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        cl.sendMessage(msg.to,"Added To Talkbanlist...")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Removed From Talkbanlist...")
                    else:
                        wait["Talkdblacklist"] = True
                        cl.sendMessage(msg.to,"Not In Talkbanlist...")

#update_photo

               if msg.contentType == 1:
                 if msg._from in owner:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            cl.sendMessage(msg.to, "Successfully Added Picture")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Group Photo Changed...")

#upload__photo__profile

               if msg.contentType == 1:
                   if msg._from in creator or msg._from in owner:
                       if mid in Setmain["SKfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Successfully Chaned Photo...")


               if msg.contentType == 1:
                 if msg._from in creator or msg._from in owner:
                        if Amid in Setmain["SKfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Amid]
                            ki.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Successfully Chaned Photo...")
                        elif mid in Setmain["SKfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Successfully Chaned Photo...")
                        elif Bmid in Setmain["SKfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Bmid]
                            kk.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Successfully Chaned Photo...")
                        elif Cmid in Setmain["SKfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Cmid]
                            kc.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Successfully Chaned Photo...")
                        elif Dmid in Setmain["SKfoto"]:
                            path = km.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Dmid]
                            km.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Successfully Chaned Photo...")
                        elif Emid in Setmain["SKfoto"]:
                            path = kb.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Emid]
                            kb.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Successfully Chaned Photo...")
                        elif Fmid in Setmain["SKfoto"]:
                            path = kd.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Fmid]
                            kd.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Successfully Chaned Photo...")
                        elif Gmid in Setmain["SKfoto"]:
                            path = ke.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Gmid]
                            ke.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Successfully Chaned Photo...")
                        elif Hmid in Setmain["SKfoto"]:
                            path = kf.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Hmid]
                            kf.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Successfully Chaned Photo...")
                        elif Imid in Setmain["SKfoto"]:
                            path = kg.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Imid]
                            kg.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Successfully Chaned Photo...")
                        elif Jmid in Setmain["SKfoto"]:
                            path = kh.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Jmid]
                            kh.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Successfully Chaned Photo...")
                        elif Zmid in Setmain["SKfoto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["SKfoto"][Zmid]
                            sw.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Successfully Chaned Photo...")

#upload__photo__cover

               if msg.contentType == 1:
                 if msg._from in creator or msg._from in owner:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     path4 = km.downloadObjectMsg(msg_id)
                     path5 = kb.downloadObjectMsg(msg_id)
                     path6 = kd.downloadObjectMsg(msg_id)
                     path7 = ke.downloadObjectMsg(msg_id)
                     path8 = kf.downloadObjectMsg(msg_id)
                     path9 = kg.downloadObjectMsg(msg_id)
                     path10 = kh.downloadObjectMsg(msg_id)
                     path11 = sw.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "Successfully Chaned Photo...")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, "Successfully Chaned Photo...")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Successfully Chaned Photo...")
                     km.updateProfilePicture(path4)
                     km.sendMessage(msg.to, "Successfully Chaned Photo...")
                     kb.updateProfilePicture(path5)
                     kb.sendMessage(msg.to, "Successfully Chaned Photo...")
                     kd.updateProfilePicture(path6)
                     kd.sendMessage(msg.to, "Successfully Chaned Photo...")
                     ke.updateProfilePicture(path7)
                     ke.sendMessage(msg.to, "Successfully Chaned Photo...")
                     kf.updateProfilePicture(path8)
                     kf.sendMessage(msg.to, "Successfully Chaned Photo...")
                     kg.updateProfilePicture(path9)
                     kg.sendMessage(msg.to, "Successfully Chaned Photo...")
                     kh.updateProfilePicture(path10)
                     kh.sendMessage(msg.to, "Successfully Chaned Photo...")
                     sw.updateProfilePicture(path11)
                     sw.sendMessage(msg.to, "Successfully Chaned Photo...")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:

                        cmd = command(text)
                        if cmd == "mode on":
                            if msg._from in creator or msg._from in owner:
                                wait["selfbot"] = True
                                cl.sendMessage(msg.to, "Commamd Allowed Now...")
                                
                        elif cmd == "mode  off":
                            if msg._from in creator or msg._from in owner:
                                wait["selfbot"] = False
                                cl.sendMessage(msg.to, "Command Not Allowed Now...")
                                            
                        elif cmd == "help2" or cmd == "H@e#lp":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage2 = helpbot()
                               cl.sendMessage(msg.to, str(helpMessage2))

                        elif cmd == "settings":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                                tz = pytz.timezone("Asia/Dhaka")
                                timeNow = datetime.now(tz=tz)
                                md = ">= Settings <]\n\n"
                                if wait["sticker"] == True: md+="●> Sticker  [>>☑️<<]\n"
                                else: md+="●> Sticker  [>>❎<<]\n"
                                if wait["contact"] == True: md+="●> Contact  [>>☑️<<]\n"
                                else: md+="●> Contact  [>>❎<<]\n"
                                if wait["detectMention"] == True: md+="●> Respond  [>>☑️<<]\n"
                                else: md+="●> Respond  [>>❎<<]\n"
                                if wait["autoJoin"] == True: md+="●> Autojoin  [>>☑️<<]\n"
                                else: md+="●> Autojoin  [>>❎<<]\n"
                                if settings["autoJoinTicket"] == True: md+="●> Jointicket  [>>☑️<<]\n"
                                else: md+="●> Jointicket  [>>❎<<]\n"
                                if wait["autoAdd"] == True: md+="●> Autoadd  [>>☑️<<]\n"
                                else: md+="●> Autoadd  [>>❎<<]\n"
                                if msg.to in welcome: md+="●> Welcome  [>>☑️<<]\n"
                                else: md+="●> Welcome  [>>❎<<]\n"
                                if wait["autoLeave"] == True: md+="●> Autoleave  [>>☑️<<]\n"
                                else: md+="●> Autoleave  [>>❎<<]\n"
                                if msg.to in protect["pqr"]: md+="●> Proqr  [>>☑️<<]\n"
                                else: md+="●> Proqr  [>>❎<<]\n"
                                if msg.to in protect["proall"]: md+="●> Proall  [>>☑️<<]\n"
                                else: md+="●> Proall  [>>❎<<]\n"
                                if msg.to in protect["protect"]: md+="●> Protect  [>>☑️<<]\n"
                                else: md+="●> Protect  [>>❎<<]\n"
                                if msg.to in protect["pinv"]: md+="●> Proinvite  [>>☑️<<]\n"
                                else: md+="●> Proinvite  [>>❎<<]\n"
                                if msg.to in protect["antijs"]: md+="●> Js  [>>☑️<<]\n"
                                else: md+="●> Js  [>>❎<<]\n"
                                if msg.to in protectcancel: md+="●> Procancel  [>>☑️<<]\n"
                                else: md+="●> Procancel  [>>❎<<]\n"
                                cl.sendMessage(msg.to, md+"\n●> Date : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n●> Time : [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ] ")

                        elif cmd == "about" or cmd == 'information':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               sendMention(msg.to, sender, "[> Abouts <]\n\n")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'Me':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': msg._from}, contentType=13)

                        elif cmd == "mymid" or text.lower() == 'Mymid':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               cl.sendMessage(msg.to, msg._from)

                        elif ("getmid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "●> Name : "+str(mi.displayName)+"\n●> MID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Name : "+str(mi.displayName)+"\nMid : " +key1+"\nStatus Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "cbotlist" or text.lower() == 'Cbotlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)
                               msg.contentMetadata = {'mid': Amid}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': Amid}, contentType=13)
                               msg.contentMetadata = {'mid': Bmid}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': Bmid}, contentType=13)
                               msg.contentMetadata = {'mid': Cmid}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': Cmid}, contentType=13)
                               msg.contentMetadata = {'mid': Dmid}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': Dmid}, contentType=13)
                               msg.contentMetadata = {'mid': Emid}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': Emid}, contentType=13)
                               msg.contentMetadata = {'mid': Fmid}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': Fmid}, contentType=13)
                               msg.contentMetadata = {'mid': Gmid}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': Gmid}, contentType=13)
                               msg.contentMetadata = {'mid': Hmid}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': Hmid}, contentType=13)
                               msg.contentMetadata = {'mid': Imid}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': Imid}, contentType=13)
                               msg.contentMetadata = {'mid': Jmid}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': Jmid}, contentType=13)
                               msg.contentMetadata = {'mid': Zmid}
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': Zmid}, contentType=13)
                               
                        elif cmd == "botmid" or text.lower() == 'Botmid':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                              cl.sendMessage(msg.to,mid)
                              ki.sendMessage(msg.to,Amid)
                              kk.sendMessage(msg.to,Bmid)
                              kc.sendMessage(msg.to,Cmid)
                              km.sendMessage(msg.to,Dmid)
                              kb.sendMessage(msg.to,Emid)
                              kd.sendMessage(msg.to,Fmid)
                              ke.sendMessage(msg.to,Gmid)
                              kf.sendMessage(msg.to,Hmid)
                              kg.sendMessage(msg.to,Imid)
                              kh.sendMessage(msg.to,Jmid)
                              cl.sendMessage(msg.to,Zmid)

#group_reject

                        elif cmd == "greject1":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              ginvited = ki.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      ki.rejectGroupInvitation(gid)
                                  ki.sendMessage(to, "Successfully Reject {} ".format(str(len(ginvited))))
                              else:
                                  ki.sendMessage(to, "Group Invitations Rejected")


                        elif cmd == "rejectall":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                      ki.rejectGroupInvitation(gid)
                                      kk.rejectGroupInvitation(gid)
                                      kc.rejectGroupInvitation(gid)
                                      km.rejectGroupInvitation(gid)
                                      kb.rejectGroupInvitation(gid)
                                      kd.rejectGroupInvitation(gid)
                                      ke.rejectGroupInvitation(gid)
                                      kf.rejectGroupInvitation(gid)
                                      kg.rejectGroupInvitation(gid)
                                      kh.rejectGroupInvitation(gid)
                                      sw.rejectGroupInvitation(gid)
                                  cl.sendMessage(to, "Successfully Reject {} ".format(str(len(ginvited))))
                                  ki.sendMessage(to, "Successfully Reject {} ".format(str(len(ginvited))))
                                  kk.sendMessage(to, "Successfully Reject {} ".format(str(len(ginvited))))
                                  kc.sendMessage(to, "Successfully Reject {} ".format(str(len(ginvited))))
                                  km.sendMessage(to, "Successfully Reject {} ".format(str(len(ginvited))))
                                  kb.sendMessage(to, "Successfully Reject {} ".format(str(len(ginvited))))
                                  kd.sendMessage(to, "Successfully Reject {} ".format(str(len(ginvited))))
                                  ke.sendMessage(to, "Successfully Reject {} ".format(str(len(ginvited))))
                                  kf.sendMessage(to, "Successfully Reject {} ".format(str(len(ginvited))))
                                  kg.sendMessage(to, "Successfully Reject {} ".format(str(len(ginvited))))
                                  kh.sendMessage(to, "Successfully Reject {} ".format(str(len(ginvited))))
                                  sw.sendMessage(to, "Successfully Reject {} ".format(str(len(ginvited))))
                              else:
                                  cl.sendMessage(to, "Group Invitations Rejected")
                                  ki.sendMessage(to, "Group Invitations Rejected")
                                  kk.sendMessage(to, "Group Invitations Rejected")
                                  kc.sendMessage(to, "Group Invitations Rejected")
                                  km.sendMessage(to, "Group Invitations Rejected")
                                  kb.sendMessage(to, "Group Invitations Rejected")
                                  kd.sendMessage(to, "Group Invitations Rejected")
                                  ke.sendMessage(to, "Group Invitations Rejected")
                                  kf.sendMessage(to, "Group Invitations Rejected")
                                  kg.sendMessage(to, "Group Invitations Rejected")
                                  kh.sendMessage(to, "Group Invitations Rejected")
                                  sw.sendMessage(to, "Group Invitations Rejected")

                        elif text.lower() == "removechat":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   ki.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   km.removeAllMessages(op.param2)
                                   kb.removeAllMessages(op.param2)
                                   kd.removeAllMessages(op.param2)
                                   ke.removeAllMessages(op.param2)
                                   kf.removeAllMessages(op.param2)
                                   kg.removeAllMessages(op.param2)
                                   kh.removeAllMessages(op.param2)
                                   sw.removeAllMessages(op.param2)
                                   cl.sendMessage(msg.to,"Chat Cleared!")
                                   ki.sendMessage(msg.to,"Chat Cleared!")
                                   kk.sendMessage(msg.to,"Chat Cleared!")
                                   kc.sendMessage(msg.to,"Chat Cleared!")
                                   km.sendMessage(msg.to,"Chat Cleared!")
                                   kb.sendMessage(msg.to,"Chat Cleared!")
                                   kd.sendMessage(msg.to,"Chat Cleared!")
                                   ke.sendMessage(msg.to,"Chat Cleared!")
                                   kf.sendMessage(msg.to,"Chat Cleared!")
                                   kg.sendMessage(msg.to,"Chat Cleared!") 
                                   kh.sendMessage(msg.to,"Chat Cleared!")
                                   sw.sendMessage(msg.to,"Chat Cleared!")
                               except:
                                   pass

                        elif cmd.startswith("broadcast "):
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"[> Broadcast <]\n\n" + str(pesan))

                        elif text.lower() == "help":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                               cl.sendMessage(msg.to, ""
"╭━━━━━━━━━━━•≽\n"
"║  ⓪≽-M E N U-≼⓪\n"
"║╭•≽\n"
"║┝•≽ Me\n"
"║┝•≽ Resp\n"
"║┝•≽ Ding\n"
"║┝•≽ Ping\n"
"║┝•≽ Out\n"
"║┝•≽ Join\n"
"║┝•≽ Help\n"
"║┝•≽ Byeall\n"
"║┝•≽ Speed\n"
"║┝•≽ Settings\n"
"║┝•≽ Mode On/Off\n"
"║┝•≽ Reader On/Off\n"
"║┝•≽ Lineid [ID]\n"
"║┝•≽ About\n"
"║┝•≽ Mymid\n"
"║┝•≽ Getmid\n"
"║┝•≽ Info [Mention]\n"
"║┝•≽ Rejectall\n"
"║┝•≽ Removechat\n"
"║┝•≽ Groupinfo\n"
"║┝•≽ Runtime\n"
"║┝•≽ Groupinfo [Num]\n"
"║┝•≽ Remoteopen [Num]\n"
"║┝•≽ Remoteclose [Num]\n"
"║┝•≽ Friendlist\n"
"║┝•≽ Memberlist\n"
"║┝•≽ Memberlist [Num]\n"
"║┝•≽ Grouplist [Num]\n"
"║┝•≽ Boom [Menrion]\n"
"║┝•≽ Kick [Mention]\n"
"║┝•≽ Vkick [Menrion]\n"
"║┝•≽ Kickall\n"
"║┝•≽ Cleanse\n"
"║┝•≽ Link open\n"
"║┝•≽ Link Close\n"
"║┝•≽ owneradd [Mention]\n"
"║┝•≽ Ownerdel [Mention]\n"
"║┝•≽ Adminadd [Mention]\n"
"║┝•≽ Admindel [Mention]\n"
"║┝•≽ staffadd [Mention]\n"
"║┝•≽ Staffdel [Mention]\n"
"║┝•≽ Cowneradd\n"
"║┝•≽ Cownerdel\n"
"║┝•≽ Cadminadd\n"
"║┝•≽ Cadmindel\n"
"║┝•≽ Cstaffadd\n"
"║┝•≽ Cstaffdel\n"
"║┝•≽ Refresh/Fresh\n"
"║┝•≽ Tagall/Mention/Tag\n"
"║┝•≽ Changename [Text]\n"
"║┝•≽ Changeprofile\n"
"║┝•≽ Banlist\n"
"║┝•≽ Clearban\n"
"║┝•≽ Checkban\n"
"║┝•≽ Botlist\n"
"║┝•≽ Stafflist\n"
"║┝•≽ Protectlist\n"
"║┝•≽ Protect On/Off\n"
"║┝•≽ Welcome On/Off\n"
"║┝•≽ Prolink On/Off\n"
"║┝•≽ Prolick On/Off\n"
"║┝•≽ Backup On/Off\n"
"║┝•≽ Procancel On/Off\n"
"║┝•≽ Proinvite On/Off\n"
"║┝•≽ Protectjs On/Off\n"
"║┝•≽ Reset [Warning]\n"
"║╰•≽\n"
"╰━━━━━━━━━━━•≽")



                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                               cl.sendMessage(msg.to, "[> MyKey <]\n\n" + str(Setmain["keyCommand"]) + " ")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Succes Change Mykey...")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "[> MyKey <]\n\nMykey Set To <{}>".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "Succes Reset Mykey...")

                        elif cmd == "@reset":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               cl.sendMessage(msg.to, "Resetting...")
                               cl.sendMessage(msg.to, "Please Wait...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                               eltime = time.time() - mulai
                               bot = "[> Runtime <]\n\n●> " +waktu(eltime)
                               cl.sendMessage(msg.to,bot)
                            
                        elif cmd == "groupinfo":
                          if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Close"
                                    gTicket = "Not Found"
                                else:
                                    gQr = "Opened"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "[> Group Info <]\n\n●> Group Name : {}".format(G.name)+ "\n●> Group ID : {}".format(G.id)+ "\n●> Creator : {}".format(G.creator.displayName)+ "\n●> Create Time : {}".format(str(timeCreated))+ "\n●> Total Member : {}".format(str(len(G.members)))+ "\n●> Total Pending : {}".format(gPending)+ "\n●> Group Qr : {}".format(gQr)+ "\n●> Group Link : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

#info__group
                        elif cmd.startswith('groupinfo '):
                          if msg._from in creator or msg._from in owner:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Not Found"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Closed"
                                    gTicket = "Not Found"
                                else:
                                    gQr = "Opened"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "[> Remote Ginfo <]\n"
                                ret_ += "\n●> Group Name : {}".format(G.name)
                                ret_ += "\n●> Group ID : {}".format(G.id)
                                ret_ += "\n●> Creator : {}".format(gCreator)
                                ret_ += "\n●> Create Time : {}".format(str(timeCreated))
                                ret_ += "\n●> Total Member : {}".format(str(len(G.members)))
                                ret_ += "\n●> Total Pending : {}".format(gPending)
                                ret_ += "\n●> Group Qr : {}".format(gQr)
                                ret_ += "\n●> Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass

#info__mem
                        elif cmd.startswith("remoteopen "):
                          if msg._from in creator:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                try:
                                    gCreator = G.creator.mid
                                    dia = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '[>Remote Group<]\n\n●> Creator :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    gCreator = "Not Found"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Closed"
                                    gTicket = "Not Found"
                                else:
                                    gQr = "Opened"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))                                
                                ret_ += xpesan+zxc
                                ret_ += "●> Group Name : {}".format(G.name)
                                ret_ += "\n●> Group Qr : {}".format(gQr)
                                ret_ += "\n●> Create Time : {}".format(str(timeCreated))
                                ret_ += "\n●> Total Member : {}".format(str(len(G.members)))
                                ret_ += "\n●> Total Pending : {}".format(gPending)
                                ret_ += "\n●> Group Link : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except:
                                pass

                        elif cmd.startswith("remoteclose "):
                          if msg._from in creator:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                try:
                                    gCreator = G.creator.mid
                                    dia = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '[>Remote Group<]\n\n●> Creator :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    gCreator = "Not Found"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Closed"
                                    gTicket = "Not Found"
                                else:
                                    gQr = "Opened"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += "●> Group Name : {}".format(G.name)
                                ret_ += "\n●> Group Qr : {}".format(gQr)
                                ret_ += "\n●> Create Time : {}".format(str(timeCreated))
                                ret_ += "\n●> Total Member : {}".format(str(len(G.members)))
                                ret_ += "\n●> Total Pending : {}".format(gPending)
                                ret_ += "\n●> Group Link : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except:
                                pass

                        elif cmd.startswith("memberlist "):
                          if msg._from in creator or msg._from in owner:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " ""+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"[> Remote Member <]\n\n●> Member List \n" + ret_ + "\n\n●> Total [%i] Members" % len(G.members))
                            except: 
                                pass

#friendlist
                        elif cmd == "friendlist" or text.lower() == 'friendlist':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"[> Friend Lists <]\n\n"+ma+"\n●> Total ["+str(len(gid))+"] Friends")

#group__list
                        elif cmd == "grouplist0" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"[> Group List <]\n\n"+ma+"\n●> Total ["+str(len(gid))+"] Groups")

                        elif cmd == "grouplist1" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"[> Group List <]\n\n"+ma+"\n●> Total ["+str(len(gid))+"] Groups")

                        elif cmd == "grouplist2" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               ma = ""
                               a = 0
                               gid = kk.getGroupIdsJoined()
                               for i in gid:
                                   G = kk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"[> Group List <]\n\n"+ma+"\n●> Total ["+str(len(gid))+"] Groups")

                        elif cmd == "grouplist3" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"[> Group List <]\n\n"+ma+"\n●> Total ["+str(len(gid))+"] Groups")

                        elif cmd == "grouplist4" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               ma = ""
                               a = 0
                               gid = km.getGroupIdsJoined()
                               for i in gid:
                                   G = km.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"[> Group List <]\n\n"+ma+"\n●> Total ["+str(len(gid))+"] Groups")

                        elif cmd == "grouplist5" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               ma = ""
                               a = 0
                               gid = kb.getGroupIdsJoined()
                               for i in gid:
                                   G = kb.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"[> Group List <]\n\n"+ma+"\n●> Total ["+str(len(gid))+"] Groups")

                        elif cmd == "grouplist6" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               ma = ""
                               a = 0
                               gid = kd.getGroupIdsJoined()
                               for i in gid:
                                   G = kd.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"[> Group List <]\n\n"+ma+"\n●> Total ["+str(len(gid))+"] Groups")

                        elif cmd == "grouplist7" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               ma = ""
                               a = 0
                               gid = ke.getGroupIdsJoined()
                               for i in gid:
                                   G = ke.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               ke.sendMessage(msg.to,"[> Group List <]\n\n"+ma+"\n●> Total ["+str(len(gid))+"] Groups")

                        elif cmd == "grouplist8" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               ma = ""
                               a = 0
                               gid = kf.getGroupIdsJoined()
                               for i in gid:
                                   G = kf.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"[> Group List <]\n\n"+ma+"\n●> Total ["+str(len(gid))+"] Groups")

                        elif cmd == "grouplist9" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               ma = ""
                               a = 0
                               gid = kg.getGroupIdsJoined()
                               for i in gid:
                                   G = kg.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               kg.sendMessage(msg.to,"[> Group List <]\n\n"+ma+"\n●> Total ["+str(len(gid))+"] Groups")

                        elif cmd == "grouplist10" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               ma = ""
                               a = 0
                               gid = kh.getGroupIdsJoined()
                               for i in gid:
                                   G = kh.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"[> Group List <]\n\n"+ma+"\n●> Total ["+str(len(gid))+"] Groups")

                        elif cmd == "grouplist11" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               ma = ""
                               a = 0
                               gid = sw.getGroupIdsJoined()
                               for i in gid:
                                   G = sw.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"[> Group List <]\n\n"+ma+"\n●> Total ["+str(len(gid))+"] Groups")

#group__link
                        elif cmd == "link close" or text.lower() == 'Link close':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Link Closed...")

                        elif cmd == "link open" or text.lower() == 'Link open':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Link Opened...")
                                   cl.sendMessage(msg.to, "[> Group Link <]\n\n●> Link : http://line.me/R/ti/g/"+gurl)

#mentions-members

                        elif msg.text in ["tagall","Tagall","mention","Mention","Prince","prince","Khokhar","Tayab","Ast","Khan","All"]:
                               if wait["selfbot"] == True:
                                if msg._from in owner or msg._from in admin or msg._from in staff:
                                 group = cl.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//20
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*20 : (a+1)*20]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Zero \n'
                                    cl.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)  
                                    
                        elif msg.text in ["tag","Tag","men","Men","Per","per","Kho","Tyb","th","Karachi","tum"]:
                               if wait["selfbot"] == True:
                                if msg._from in owner or msg._from in admin or msg._from in staff or msg._from in member:
                                 group = ki.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//20
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*20 : (a+1)*20]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Zero \n'
                                    ki.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)  

                        elif msg.text in ["test2","test1","test"]:
                               members = []
                               if msg.toType == 1:
                                   room = cl.getCompactRoom(to)
                                   members = [mem.mid for mem in room.contacts]
                               elif msg.toType == 2:
                                   group = cl.getCompactGroup(to)
                                   members = [mem.mid for mem in group.members]
                               else:
                                   return cl.sendReplyMessage(msg_id, to, 'Only for Groups and Chats')
                               if members:
                                   mentionMembers(to, members)
#invite__bots

                        elif cmd == "invitebots":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid]
                                    G = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    ki.acceptGroupInvitation(msg.to)
                                    kk.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    km.acceptGroupInvitation(msg.to)
                                    kb.acceptGroupInvitation(msg.to)
                                    kd.acceptGroupInvitation(msg.to)
                                    ke.acceptGroupInvitation(msg.to)
                                    kf.acceptGroupInvitation(msg.to)
                                    kg.acceptGroupInvitation(msg.to)
                                    kh.acceptGroupInvitation(msg.to)
                                except:
                                    pass


                        elif cmd == "reinvite":
                            if msg._from in creator or msg._from in owner:
                                G = cl.getGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                km.leaveGroup(msg.to)
                                kb.leaveGroup(msg.to)
                                kd.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                kf.leaveGroup(msg.to)
                                kg.leaveGroup(msg.to)
                                kh.leaveGroup(msg.to)
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                km.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)

#bot-name
                        elif cmd.startswith("changename0 "):
                          if msg._from in creator or msg._from in owner:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Name Change To... [ " + string + " ]")

                        elif cmd.startswith("changename1 "):
                          if msg._from in creator or msg._from in owner:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                cl.sendMessage(msg.to,"Name Change To... [ " + string + " ]")

                        elif cmd.startswith("changename2 "):
                          if msg._from in creator or msg._from in owner:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                cl.sendMessage(msg.to,"Name Change To... [ " + string + " ]")

                        elif cmd.startswith("changename3 "):
                          if msg._from in creator or msg._from in owner:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                cl.sendMessage(msg.to,"Name Change To... [ " + string + " ]")
                                
                        elif cmd.startswith("changename4 "):
                          if msg._from in creator or msg._from in owner:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = km.getProfile()
                                profile.displayName = string
                                km.updateProfile(profile)
                                cl.sendMessage(msg.to,"Name Change To... [ " + string + " ]")    

                        elif cmd.startswith("changename5 "):
                          if msg._from in creator or msg._from in owner:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kb.getProfile()
                                profile.displayName = string
                                kb.updateProfile(profile)
                                cl.sendMessage(msg.to,"Name Change To... [ " + string + " ]")    
   
                        elif cmd.startswith("changename6 "):
                          if msg._from in creator or msg._from in owner:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kd.getProfile()
                                profile.displayName = string
                                kd.updateProfile(profile)
                                cl.sendMessage(msg.to,"Name Change To... [ " + string + " ]")

                        elif cmd.startswith("changename7 "):
                          if msg._from in creator or msg._from in owner:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ke.getProfile()
                                profile.displayName = string
                                ke.updateProfile(profile)
                                cl.sendMessage(msg.to,"Name Change To... [ " + string + " ]")

                        elif cmd.startswith("changename8 "):
                          if msg._from in creator or msg._from in owner:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kf.getProfile()
                                profile.displayName = string
                                kf.updateProfile(profile)
                                cl.sendMessage(msg.to,"Name Change To... [ " + string + " ]")

                        elif cmd.startswith("changename9 "):
                          if msg._from in creator or msg._from in owner:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kg.getProfile()
                                profile.displayName = string
                                kg.updateProfile(profile)
                                cl.sendMessage(msg.to,"Name Change To... [ " + string + " ]")
                                
                        elif cmd.startswith("changename10 "):
                          if msg._from in creator or msg._from in owner:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kh.getProfile()
                                profile.displayName = string
                                kh.updateProfile(profile)
                                cl.sendMessage(msg.to,"Name Change To... [ " + string + " ]")       

                        elif cmd.startswith("changename11 "):
                          if msg._from in creator or msg._from in owner:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                cl.sendMessage(msg.to,"Name Change To... [ " + string + " ]")

#bot__profile__left
                        elif cmd == "changegroup":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendMessage(msg.to,"Send your images.....")

                        elif cmd == "cpp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ARfoto"][mid] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "changeprofile1":
                            if msg._from in creator or msg._from in owner:
                                Setmain["SKfoto"][Amid] = True
                                cl.sendMessage(msg.to,"Send your images.....")

                        elif cmd == "changeprofile2":
                            if msg._from in creator or msg._from in owner:
                                Setmain["SKfoto"][Bmid] = True
                                cl.sendMessage(msg.to,"Send your images.....")

                        elif cmd == "changeprofile3":
                            if msg._from in creator or msg._from in owner:
                                Setmain["SKfoto"][Cmid] = True
                                cl.sendMessage(msg.to,"Send your images.....")

                        elif cmd == "changeprofile4":
                            if msg._from in creator or msg._from in owner:
                                Setmain["SKfoto"][Dmid] = True
                                cl.sendMessage(msg.to,"Send your images.....")

                        elif cmd == "changeprofile5":
                            if msg._from in creator or msg._from in owner:
                                Setmain["SKfoto"][Emid] = True
                                cl.sendMessage(msg.to,"Send your images.....")

                        elif cmd == "changeprofile6":
                            if msg._from in creator or msg._from in owner:
                                Setmain["SKfoto"][Fmid] = True
                                cl.sendMessage(msg.to,"Send your images.....")

                        elif cmd == "changeprofile7":
                            if msg._from in creator or msg._from in owner:
                                Setmain["SKfoto"][Gmid] = True
                                cl.sendMessage(msg.to,"Send your images.....")

                        elif cmd == "changeprofile8":
                            if msg._from in creator or msg._from in owner:
                                Setmain["SKfoto"][Hmid] = True
                                cl.sendMessage(msg.to,"Send your images.....")

                        elif cmd == "changeprofile9":
                            if msg._from in creator or msg._from in owner:
                                Setmain["SKfoto"][Imid] = True
                                cl.sendMessage(msg.to,"Send your images.....")

                        elif cmd == "changeprofile10":
                            if msg._from in creator or msg._from in owner:
                                Setmain["SKfoto"][Jmid] = True
                                cl.sendMessage(msg.to,"Send your images.....")

                        elif cmd == "changeprofile11":
                            if msg._from in creator or msg._from in owner:
                                Setmain["SKfoto"][Zmid] = True
                                cl.sendMessage(msg.to,"Send your images.....")

#botlist
                        elif cmd == "botlist" or text.lower() == 'Botlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"[> Botlists <]\n\n"+ma+"\n●> Total [%s] Bots" %(str(len(Bots))))

                        elif cmd == "js on" or text.lower() == 'Js on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    random.choice(ABC).inviteIntoGroup(msg.to, [Zmid])
                                    cl.sendMessage(msg.to,"Ready To Backup...")
                                except:
                                    pass

                        elif cmd == "stafflist" or text.lower() == 'Stafflist':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"[> Staff-List <]\n\n\n☣️[>OWNERS<]☣️\n"+ma+"\n\n☣️[>ADMINS<]☣️\n"+mb+"\n\n☣️[>STAFFS<]☣️\n"+mc+"\n●> Total [%s] Staffs" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "protectlist" or text.lower() == 'Protectlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                mg = ""
                                mf = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                g = 0
                                f = 0
                                gid = protect["pqr"]
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["protect"]
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["proall"]
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["pinv"]
                                for group in gid:
                                    f = f + 1
                                    end = '\n'
                                    mf += str(f) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["antijs"]
                                for group in gid:
                                    g = g + 1
                                    end = '\n'
                                    mg += str(g) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendMessage(msg.to,"[> Pro Settings <]\n\n\n🛡[>PRO-JS<]🛡\n"+mg+"\n🛡[>PRO-LINK<]🛡\n"+ma+"\n🛡[>BACK-UP<]🛡\n"+mb+"\n🛡[>PRO-KICK<]🛡\n"+md+"\n🛡[>PRO-INVITE<]🛡\n"+mf+"\n🛡[>PRO-CANCEL<]🛡\n"+mc+"\n●> Total [%s] In List" %(str(len(protect["pqr"])+len(protect["protect"])+len(protect["antijs"])+len(protect["proall"])+len(protectcancel)+len(protect["pinv"]))))

                        elif cmd == "resp" or text.lower() == 'Resp':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                cl.sendMessage(msg.to,responsenamea)
                                ki.sendMessage(msg.to,responsename1)
                                kk.sendMessage(msg.to,responsename2)
                                kc.sendMessage(msg.to,responsename3)
                                km.sendMessage(msg.to,responsename4)
                                kb.sendMessage(msg.to,responsename5)
                                kd.sendMessage(msg.to,responsename6)
                                ke.sendMessage(msg.to,responsename7)
                                kf.sendMessage(msg.to,responsename8)
                                kg.sendMessage(msg.to,responsename9)
                                kh.sendMessage(msg.to,responsename10)
                                
                                
                        elif cmd == "join":
                         if msg._from in owner or msg._from in admin:
                           if msg.toType == 2:
                               group = cl.getGroup(to)
                               group.preventedJoinByTicket = False
                               cl.updateGroup(group)
                               invsend = 0
                               ticket = cl.reissueGroupTicket(to)
                               ki.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.001)
                               kk.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.001)
                               kc.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.001)
                               km.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.001)
                               kb.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.001)
                               kd.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.001)
                               ke.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.001)
                               kf.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.001) 
                               kg.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.001)
                               kh.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.001)
                               group.preventedJoinByTicket = True
                               cl.updateGroup(group)

                        elif cmd == "ding":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                               cl.sendMessage(msg.to, "Dong...")
                               ki.sendMessage(msg.to, "Dong...")
                               kk.sendMessage(msg.to, "Dong...")
                               kc.sendMessage(msg.to, "Dong...")
                               km.sendMessage(msg.to, "Dong...")
                               kb.sendMessage(msg.to, "Dong...")
                               kd.sendMessage(msg.to, "Dong...")
                               ke.sendMessage(msg.to, "Dong...")
                               kf.sendMessage(msg.to, "Dong...")
                               kg.sendMessage(msg.to, "Dong...")
                               kh.sendMessage(msg.to, "Dong...")
  
                        elif cmd == "ping":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                               cl.sendMessage(msg.to, "Pong...")
                               ki.sendMessage(msg.to, "Pong...")
                               kk.sendMessage(msg.to, "Pong...")
                               kc.sendMessage(msg.to, "Pong...")
                               km.sendMessage(msg.to, "Pong...")
                               kb.sendMessage(msg.to, "Pong...")
                               kd.sendMessage(msg.to, "Pong...")
                               ke.sendMessage(msg.to, "Pong...")
                               kf.sendMessage(msg.to, "Pong...")
                               kg.sendMessage(msg.to, "Pong...")
                               kh.sendMessage(msg.to, "Pong...")

                        elif cmd == "bye0":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to, "Good-Bye...")
                                cl.leaveGroup(msg.to)
               
                        elif cmd == "bye1":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.sendMessage(msg.to, "Good-Bye...")
                                ki.leaveGroup(msg.to)
                                
                        elif cmd == "bye2":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin:
                                G = cl.getGroup(msg.to)
                                kk.sendMessage(msg.to, "Good-Bye...")
                                kk.leaveGroup(msg.to)
                                
                        elif cmd == "bye3":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin:
                                G = cl.getGroup(msg.to)
                                kc.sendMessage(msg.to, "Good-Bye...")
                                kc.leaveGroup(msg.to)
                                
                        elif cmd == "bye4":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin:
                                G = cl.getGroup(msg.to)
                                km.sendMessage(msg.to, "Good-Bye...")
                                km.leaveGroup(msg.to)

                        elif cmd == "bye5":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin:
                                G = cl.getGroup(msg.to)
                                kb.sendMessage(msg.to, "Good-Bye...")
                                kb.leaveGroup(msg.to)

                        elif cmd == "bye6":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin:
                                G = cl.getGroup(msg.to)
                                kd.sendMessage(msg.to, "Good-Bye...")
                                kd.leaveGroup(msg.to)

                        elif cmd == "bye7":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ke.sendMessage(msg.to, "Good-Bye...")
                                ke.leaveGroup(msg.to)

                        elif cmd == "bye8":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin:
                                G = cl.getGroup(msg.to)
                                kf.sendMessage(msg.to, "Good-Bye...")
                                kf.leaveGroup(msg.to)

                        elif cmd == "bye9":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin:
                                G = cl.getGroup(msg.to)
                                kg.sendMessage(msg.to, "Good-Bye...")
                                kg.leaveGroup(msg.to)

                        elif cmd == "bye10":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin:
                                G = cl.getGroup(msg.to)
                                kh.sendMessage(msg.to, "Good-Bye...")
                                kh.leaveGroup(msg.to)

                        elif cmd == "byeall":
                           if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               cl.sendMessage(msg.to, "Good-Bye...")
                               cl.leaveGroup(msg.to)
                               ki.sendMessage(msg.to, "Good-Bye...")
                               ki.leaveGroup(msg.to)
                               kk.sendMessage(msg.to, "Good-Bye...")
                               kk.leaveGroup(msg.to)
                               kc.sendMessage(msg.to, "Good-Bye...")
                               kc.leaveGroup(msg.to)
                               km.sendMessage(msg.to, "Good-Bye...")
                               km.leaveGroup(msg.to)
                               kb.sendMessage(msg.to, "Good-Bye...")
                               kb.leaveGroup(msg.to)
                               kd.sendMessage(msg.to, "Good-Bye...")
                               kd.leaveGroup(msg.to)
                               ke.sendMessage(msg.to, "Good-Bye...")
                               ke.leaveGroup(msg.to)
                               kf.sendMessage(msg.to, "Good-Bye...")
                               kf.leaveGroup(msg.to)
                               kg.sendMessage(msg.to, "Good-Bye...")
                               kg.leaveGroup(msg.to)
                               kh.sendMessage(msg.to, "Good-Bye...")
                               kh.leaveGroup(msg.to)
                               sw.sendMessage(msg.to, "Good-Bye...")
                               sw.leaveGroup(msg.to)

                        elif cmd == "ghost out":
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sw.sendMessage(msg.to, "Good-Bye...")
                                sw.leaveGroup(msg.to)
                                


                        elif cmd == "ghost join":
                          if msg._from in creator or msg._from in owner or msg._from in admin:
                           if msg.toType == 2:
                               group = cl.getGroup(to)
                               group.preventedJoinByTicket = False
                               cl.updateGroup(group)
                               invsend = 0
                               ticket = cl.reissueGroupTicket(to)
                               sw.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.001)
                               sw.sendMessage(msg.to, "I Am Here...")
                               group.preventedJoinByTicket = True
                               cl.updateGroup(group)


                        elif cmd == "out":
                           if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin:
                               ki.leaveGroup(msg.to)
                               kk.leaveGroup(msg.to)
                               kc.leaveGroup(msg.to)
                               km.leaveGroup(msg.to)
                               kb.leaveGroup(msg.to)
                               kd.leaveGroup(msg.to)
                               ke.leaveGroup(msg.to)
                               kf.leaveGroup(msg.to)
                               kg.leaveGroup(msg.to)
                               kh.leaveGroup(msg.to)
                               sw.leaveGroup(msg.to)

#remoteleave                               
                        elif cmd.startswith("groupleave0 "):
                            if msg._from in creator:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        cl.sendMessage(i, "Please Invite Owner...")
                                        cl.leaveGroup(i)
                                        ki.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        km.leaveGroup(i)
                                        kb.leaveGroup(i)
                                        kd.leaveGroup(i)
                                        ke.leaveGroup(i)
                                        kf.leaveGroup(i)
                                        kg.leaveGroup(i)
                                        kh.leaveGroup(i)
                                        sw.leaveGroup(i)
                                        cl.sendMessage(to,"[> Remote Leave <]\n\n●> Successfully Leave\n●> Group Name : " +h)

                        elif cmd.startswith("groupleave1 "):
                            if msg._from in creator:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        ki.sendMessage(i, "Please Invite Owner...")
                                        ki.leaveGroup(i)
                                        cl.sendMessage(to,"[> Remote Leave <]\n\n●> Successfully Leave\n●> Group Name : " +h)

                        elif cmd.startswith("groupleave2 "):
                            if msg._from in creator:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        kk.leaveGroup(i)
                                        cl.sendMessage(to,"[> Remote Leave <]\n\n●> Successfully Leave\n●> Group Name : " +h)

                        elif cmd.startswith("groupleave3 "):
                            if msg._from in creator:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        kc.sendMessage(i, "Please Invite Owner...")
                                        kc.leaveGroup(i)
                                        cl.sendMessage(to,"[> Remote Leave <]\n\n●> Successfully Leave\n●> Group Name : " +h)

                        elif cmd.startswith("groupleave4 "):
                            if msg._from in creator:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        km.sendMessage(i, "Please Invite Owner...")
                                        km.leaveGroup(i)
                                        cl.sendMessage(to,"[> Remote Leave <]\n\n●> Successfully Leave\n●> Group Name : " +h)

                        elif cmd.startswith("groupleave5 "):
                            if msg._from in creator:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        kb.sendMessage(i, "Please Invite Owner...")
                                        kb.leaveGroup(i)
                                        cl.sendMessage(to,"[> Remote Leave <]\n\n●> Successfully Leave\n●> Group Name : " +h)

                        elif cmd.startswith("groupleave6 "):
                            if msg._from in creator:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        kd.sendMessage(i, "Please Invite Owner...")
                                        kd.leaveGroup(i)
                                        cl.sendMessage(to,"[> Remote Leave <]\n\n●> Successfully Leave\n●> Group Name : " +h)

                        elif cmd.startswith("groupleave7 "):
                            if msg._from in creator:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        ke.sendMessage(i, "Please Invite Owner...")
                                        ke.leaveGroup(i)
                                        cl.sendMessage(to,"[> Remote Leave <]\n\n●> Successfully Leave\n●> Group Name : " +h)

                        elif cmd.startswith("groupleave8 "):
                            if msg._from in creator:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        kf.sendMessage(i, "Please Invite Owner...")
                                        kf.leaveGroup(i)
                                        cl.sendMessage(to,"[> Remote Leave <]\n\n●> Successfully Leave\n●> Group Name : " +h)

                        elif cmd.startswith("groupleave9 "):
                            if msg._from in creator:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        kg.sendMessage(i, "Please Invite Owner...")
                                        kg.leaveGroup(i)
                                        cl.sendMessage(to,"[> Remote Leave <]\n\n●> Successfully Leave\n●> Group Name : " +h)

                        elif cmd.startswith("groupleave10 "):
                            if msg._from in creator:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        kh.sendMessage(i, "Please Invite Owner...")
                                        kh.leaveGroup(i)
                                        cl.sendMessage(to,"[> Remote Leave <]\n\n●> Successfully Leave\n●> Group Name : " +h)

                        elif cmd.startswith("groupleave11 "):
                            if msg._from in creator:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        sw.sendMessage(i, "Please Invite Owner...")
                                        sw.leaveGroup(i)
                                        cl.sendMessage(to,"[> Remote Leave <]\n\n●> Successfully Leave\n●> Group Name : " +h)

                        elif cmd == "rspeed":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "[> Respond Speed <]\n\n●> Get Profile\n   %.10f\n●> Get Contact\n   %.10f\n●> Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               start = time.time()                               
                               cl.sendMessage(msg.to, "Calculating...")                               
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "{} secs".format(str(elapsed_time)))

                        elif cmd == "reader on":
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in crearor or msg._from in admin or msg._from in staff:
                              try:
                                  tz = pytz.timezone("Asia/Dhaka")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "[> Sider Activated <]\n\n●> Date : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n●> Time : "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "reader off":
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Dhaka")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "[> Sider Deactivated <]\n\n ●> Date : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n●> Time : "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                              else:
                                  cl.sendMessage(msg.to, "Inactive...")

#youtube

                        elif cmd.startswith("youtube "):
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "[> Media Result <]\n\n●> Tittle [ " + vid.title + " ]"
                                    author = '\n\n●> Author : ' + str(vid.author)
                                    durasi = '\n●> Duration : ' + str(vid.duration)
                                    suka = '\n●> Likes : ' + str(vid.likes)
                                    rating = '\n●> Rating : ' + str(vid.rating)
                                    deskripsi = '\n●> Description : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))

                        elif 'lineid ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in creator or msg._from in owner or msg._from in admin:
                              msgs = msg.text.replace('lineid ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "[> Username <]\n\n●> ID : http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)
#====='=======#
                        elif 'welcome ' in msg.text:
                           if msg._from in creator or msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "●> Already Activated"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "●> Welome-msg\n●> Successfully Activated"
                                  cl.sendMessage(msg.to, "[> Welcome <]\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "●> Welome-msg\n●> Successfully Deactivated"
                                    else:
                                         msgs = "●> Already Deactivated"
                                    cl.sendMessage(msg.to, "[> Welcome <]\n\n" + msgs)

                        elif 'prolink ' in msg.text:
                           if msg._from in creator or msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('prolink ','')
                              if spl == 'on':
                                  if msg.to in protect["pqr"]:
                                       msgs = "●> Already Activated"
                                  else:
                                       protect["pqr"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "●> Link-pro\n●> Successfully Activate"
                                  cl.sendMessage(msg.to, "[> Pro Link <]\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["pqr"]:
                                         protect["pqr"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "●> Link-pro\n●>Successfully Deactivated"
                                    else:
                                         msgs = "●> Already Deactivated"
                                    cl.sendMessage(msg.to, "[> Pro Link <]\n\n" + msgs)

                        elif 'prokick ' in msg.text:
                           if msg._from in creator or msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('prokick ','')
                              if spl == 'on':
                                  if msg.to in protect["protect"]:
                                       msgs = "●> Already Activated"
                                  else:
                                       protect["protect"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "●> Pro-Kick\n●> Successfully Activate"
                                  cl.sendMessage(msg.to, "[> Pro Kick <]\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["protect"]:
                                         protect["protect"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "●> Pro-kick\n●> Successfully Deactivate"
                                    else:
                                         msgs = "●> Already Deactivated"
                                    cl.sendMessage(msg.to, "[> Pro Kick <]\n\n" + msgs)

                        elif 'backup ' in msg.text:
                           if msg._from in creator or msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('backup ','')
                              if spl == 'on':
                                  if msg.to in protect["proall"]:
                                       msgs = "●> Already Activated"
                                  else:
                                       protect["proall"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "●> Backup Member\n●> Successfully Activate"
                                  cl.sendMessage(msg.to, "[> Backups <] \n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["proall"]:
                                         protect["proall"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "●>Backup member\n●> Successfully Deactivate"
                                    else:
                                         msgs = "●> Already Deactivated"
                                    cl.sendMessage(msg.to, "[> Backups <]\n\n" + msgs)

                        elif 'procancel ' in msg.text:
                           if msg._from in creator or msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('procancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "●> Already Ativated"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "●> Pro-cancel\n●> Successfully Activate"
                                  cl.sendMessage(msg.to, "[> Pro Cancel <]\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "●>Pro-cancel\n●> Successfully Deactivate"
                                    else:
                                         msgs = "●> Already Deactivate"
                                    cl.sendMessage(msg.to, "[> Pro Cancel <]\n\n" + msgs)

                        elif 'proinvite ' in msg.text:
                           if msg._from in creator or msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('proinv ','')
                              if spl == 'on':
                                  if msg.to in protect["pinv"]:
                                       msgs = "●> Already Activated"
                                  else:
                                       protect["pinv"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "●> Invite Protect\n●> Successfully Activate"
                                  cl.sendMessage(msg.to, "[> Pro Invite <] \n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["pinv"]:
                                         protect["pinv"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "●> Invite Protect\n●> Successfully Deactivate"
                                    else:
                                         msgs = "●> Already Deactivated"
                                    cl.sendMessage(msg.to, "[> Pro Invite <]\n\n" + msgs)

                        elif 'protectjs ' in msg.text:
                           if msg._from in creator or msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('protectjs ','')
                              if spl == 'on':
                                  if msg.to in protect["antijs"]:
                                       msgs = "●> Already Activated"
                                  else:
                                       protect["antijs"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "●> Protect Js\n●> Successfully Activate"
                                  cl.sendMessage(msg.to, "[> Pro-JS <]\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["antijs"]:
                                         protect["antijs"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "●> Protect Js\n●> Successfully Deactivate"
                                    else:
                                         msgs = "●> Already Deactivated"
                                    cl.sendMessage(msg.to, "[> Anti Js <]\n\n" + msgs)
#ghost                                 
                        elif 'ghost ' in msg.text:
                           if msg._from in creator or msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('ghost ','')
                              if spl == 'on':
                                  if msg.to in ghost["ghost"]:
                                       msgs = "Ghost Ready..."
                                  else:
                                       ghost["ghost"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Ghost \n\naktif di group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "active\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost["ghost"]:
                                         ghost["ghost"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Ghost off\ndi group : " +str(ginfo.name)
                                    else:
                                         msgs = "Ghost off "
                                    cl.sendMessage(msg.to, "nonactive\n" + msgs)            

                        elif 'protect ' in msg.text:
                           if msg._from in creator or msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('protect ','')
                              if spl == 'on':
                                  if msg.to in protect["pqr"]:
                                       msgs = ""
                                  else:
                                       protect["pqr"].append(msg.to)
                                  if msg.to in protect["protect"]:
                                      msgs = ""
                                  else:
                                      protect["protect"].append(msg.to)
                                  if msg.to in protect["pinv"]:
                                      msgs = ""
                                  else:
                                      protect["pinv"].append(msg.to)
                                  if msg.to in protect["antijs"]:
                                      msgs = ""
                                  else:
                                      protect["antijs"].append(msg.to)
                                  if msg.to in protect["proall"]:
                                      msgs = ""
                                  else:
                                      protect["proall"].append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "●> Already Activated"
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "●> Successfully Activate"
                                  cl.sendMessage(msg.to, "[> Full Pro <]\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["pqr"]:
                                         protect["pqr"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["protect"]:
                                         protect["protect"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["pinv"]:
                                         protect["pinv"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["antijs"]:
                                         protect["antijs"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["proall"]:
                                         protect["proall"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "●> Succesfully Deactivate"
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "●> Already Deactivated"
                                    cl.sendMessage(msg.to, "[> Full Pro <]\n\n" + msgs)

#Kick__members
                        elif ("boom " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("kick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("vkick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                           random.choice(ABC).inviteIntoGroup(msg.to, [target])
                                           random.choice(ABC).cancelGroupInvitation(msg.to, [target])
                                       except:
                                           pass


#vkick__members
                        elif ("fuck " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                      if target not in owner:
                                         if target not in creator:
                                            try:
                                                random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                                random.choice(ABC).inviteIntoGroup(msg.to, [target])
                                                random.choice(ABC).cancelGroupInvitation(msg.to, [target])
                                            except:
                                                pass

#kickall__members
                        elif ("kissall" in msg.text):
                            if msg._from in owner or msg._from in creator:
                             if msg.toType == 2:
                                 print ("[ 19 ] KICK ALL MEMBER")
                                 _name = msg.text.replace("kissall","")
                                 gs = cl.getGroup(msg.to)
                                 gs = ki.getGroup(msg.to)
                                 gs = kk.getGroup(msg.to)
                                 gs = kc.getGroup(msg.to)
                                 gs = km.getGroup(msg.to)
                                 gs = kb.getGroup(msg.to)
                                 cl.sendMessage(msg.to,"Making Plan...")
                                 cl.sendMessage(msg.to,"Getting Targets...")
                                 targets = []
                                 for g in gs.members:
                                     if _name in g.displayName:
                                         targets.append(g.mid)
                                 if targets == []:
                                     cl.sendMessage(msg.to,"Empty List...")
                                 else:
                                     for target in targets:
                                       if not target in Bots:
                                          if not target in owner:
                                             if not target in creator:
                                               try:
                                                      random.choice(ABC).kickoutFromGroup(msg.to,[target])
                                                      G = cl.getGroup(msg.to)
                                                      G.preventedJoinByTicket = True
                                                      cl.updateGroup(G)
                                                      G.preventedJoinByTicket(G)
                                                      cl.updateGroup(G)
                                               except:
                                                   pass

                        elif text.lower() == "cleanse":
                           if msg._from in owner:
                           	if msg.toType == 2:
                                  ginfo = cl.getGroup(msg.to)
                                  cl.sendMessage(msg.to, "Start Nuking...")
                                  cl.sendMessage(msg.to, "Good-Bye All...")
                                  G = cl.getGroup(msg.to)
                                  G.preventedJoinByTicket = False
                                  cl.updateGroup(G)
                                  Ticket = cl.reissueGroupTicket(msg.to)
                                  ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  km.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  _name = text.lower().replace("cleanse",'')
                                  gs = ki.getGroup(msg.to)
                                  gs = kk.getGroup(msg.to)
                                  gs = kc.getGroup(msg.to)
                                  gs = km.getGroup(msg.to)
                                  gs = kb.getGroup(msg.to)
                                  gs = kd.getGroup(msg.to)
                                  gs = ke.getGroup(msg.to)
                                  gs = kf.getGroup(msg.to)
                                  gs = kg.getGroup(msg.to)
                                  gs = kh.getGroup(msg.to)
                                  targets = []
                                  for g in gs.members:
                                  	if _name in g.displayName:
                                  	   targets.append(g.mid)
                                  if targets == []:
                                  	cl.sendMessage(msg.to, "Empty List...")
                                  else:
                                       for target in targets:
                                        if not target in Bots:
                                           if not target in owner:
                                              if not target in creator:
                                                 try:
                                                      random.choice(ABC).kickoutFromGroup(msg.to,[target])
                                                      G = cl.getGroup(msg.to)
                                                      G.preventedJoinByTicket = True
                                                      cl.updateGroup(G)
                                                      G.preventedJoinByTicket(G)
                                                      cl.updateGroup(G)
                                                 except:
                                                      pass
                                                      
                        elif text.lower() == 'killban':
                           if msg._from in owner:
                              gid = cl.getGroupIdsJoined()
                              group = cl.getGroup(to)
                              gMembMids = [contact.mid for contact in group.members]
                              ban_list = []
                              for tag in wait["blacklist"]:
                                    ban_list += filter(lambda str: str == tag, gMembMids)
                              if ban_list == []:
                                    cl.sendMessage(to, "Empty List...")
                                    return
                              else:
                                    for i in gid:
                                    	for jj in ban_list:
                                         if jj in admin:
                                                pass
                                         elif jj in staff:
                                                pass
                                         elif jj in Bots:
                                                pass
                                         else:
                                                random.choice(ABC).kickoutFromGroup(i, [jj])
                                                cl.sendMessage(msg.to, "Removed All...")

                        elif "play " in msg.text:
                           if msg._from in creator or msg._from in owner:
                              key = eval(msg.contentMetadata["MENTION"])
                              key["MENTIONEES"][0]["M"]                                                                                                                                
                              targets = []
                              for x in key["MENTIONEES"]:
                                  targets.append(x["M"])
                              for target in targets:                                                                                                                                       
                                  try:
                                      ki.kickoutFromGroup(msg.to,[target])
                                      ki.findAndAddContactsByMid(target)
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                  except:
                                      pass
                                      
                        elif "invite " in msg.text:
                            if msg._from in owner or msg._from in admin:                                                                                                                                       
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]                                                                                                                                
                               targets = []
                               for x in key["MENTIONEES"]:                                                                                                                                  
                                   targets.append(x["M"])
                               for target in targets:                                                                                                                                       
                                   try:
                                      cl.kickoutFromGroup(msg.to,[target])
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(msg.to,[target])
                                   except:
                                       pass 
                                       
                        elif cmd == "prank":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               cl.sendMessage(msg.to, "Mu-Ha-Ha-Ha...")
                               cl.sendContact(to, mid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)                          
                               cl.sendMessage(to, None, contentMetadata={"STKID":"406","STKPKGID":"1","STKVER":"100"}, contentType=7)

#staffadd
                        elif ("owneradd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           owner.append(target)
                                           cl.sendMessage(msg.to,"Promoted To Owner...")
                                       except:
                                           pass

                        elif ("ownerdel " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           owner.remove(target)
                                           cl.sendMessage(msg.to,"Removed From Owner...")
                                       except:
                                           pass

                        elif ("adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           admin.append(target)
                                           cl.sendMessage(msg.to,"Promoted To Admin...")
                                       except:
                                           pass

                        elif ("admindel " in msg.text):
                            if msg._from in creator or msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"Removed From Admin...")
                                       except:
                                           pass

                        elif ("staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.append(target)
                                           cl.sendMessage(msg.to,"Promoted To Staff...")
                                       except:
                                           pass

                        elif ("staffdel " in msg.text):
                            if msg._from in creator or msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"Removed From Staff...")
                                       except:
                                           pass

                        elif ("botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.append(target)
                                           cl.sendMessage(msg.to,"Promoted To Bot...")
                                       except:
                                           pass

                        elif ("botdel " in msg.text):
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"Removed From Bots...")
                                       except:
                                           pass

#settings
                        elif cmd == "antitag on" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                wait["Mentionkick"] = True
                                cl.sendMessage(msg.to,"Antitag Activated...")

                        elif cmd == "antitag off" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                wait["MentionKick"] = False
                                cl.sendMessage(msg.to,"Antitag Deactivated...")

                        elif cmd == "contact on" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                wait["contact"] = True
                                cl.sendMessage(msg.to,"Check Contact Activated...")

                        elif cmd == "contact off" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                wait["contact"] = False
                                cl.sendMessage(msg.to,"Check Contact Deactivated...")

                        elif cmd == "respond on" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                wait["detectMention"] = True
                                cl.sendMessage(msg.to,"Autorespond Activated...")

                        elif cmd == "respond off" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                wait["detectMention"] = False
                                cl.sendMessage(msg.to,"Autorespond Deactivated...")

                        elif cmd == "autojoin on" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                wait["autoJoin"] = True
                                cl.sendMessage(msg.to,"Autojoin Activated...")

                        elif cmd == "autojoin off" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                wait["autoJoin"] = False
                                cl.sendMessage(msg.to,"Autojoin Deactivated...")

                        elif cmd == "autoleave on" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                wait["autoLeave"] = True
                                cl.sendMessage(msg.to,"Autoleave Activated...")

                        elif cmd == "autoleave off" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                wait["autoLeave"] = False
                                cl.sendMessage(msg.to,"Autoleave Deactivated...")

                        elif cmd == "autoadd on" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                wait["autoAdd"] = True
                                cl.sendMessage(msg.to,"Autoadd Activated...")

                        elif cmd == "autoadd off" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                wait["autoAdd"] = False
                                cl.sendMessage(msg.to,"Autoadd Deactivated...")

                        elif cmd == "sticker on" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                wait["sticker"] = True
                                cl.sendMessage(msg.to,"Sticker Details Activaged...")

                        elif cmd == "sticker off" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                wait["sticker"] = False
                                cl.sendMessage(msg.to,"Sticker Details Deactivated...")

                        elif cmd == "jointicket on" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                settings["autoJoinTicket"] = True
                                cl.sendMessage(msg.to,"Jointicket Activated...")

                        elif cmd == "jointicket off" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                settings["autoJoinTicket"] = False
                                cl.sendMessage(msg.to,"Jointicket Deactivated...")

                        elif cmd == "@autojoin on":
                            if msg._from in creator or msg._from in owner:
                                settings["autoJoin"] = True
                                cl.sendMessage(to, "Jointicket Activated...")
                                
                        elif cmd == "@autojoin off":
                            if msg._from in creator or msg._from in owner:
                                settings["autoJoin"] = False
                                cl.sendMessage(to, "Jointicket Disabled...")
                                
                        elif cmd == "@autoleave on":
                            if msg._from in creator or msg._from in owner:
                                settings["autoLeave"] = True
                                cl.sendMessage(to, "Autoleave Activated...")
                                
                        elif cmd == "@autoleave off":
                            if msg._from in creator or msg._from in owner:
                                settings["autoLeave"] = False
                                cl.sendMessage(to, "Autoleave Deactivated...")

                        elif cmd == "checkpost on":
                           if msg._from in creator or msg._from in owner:
                                 settings["checkPost"] = True
                                 cl.sendMessage(to, "Check Post Activated...")
                                 
                        elif cmd == "checkpost off":
                           if msg._from in creator or msg._from in owner:
                                settings["checkPost"] = False
                                cl.sendMessage(to, "Check Post Deactivated...")
                                
                        elif cmd == "checksticker on":
                        	if msg._from in creator or msg._from in owner:
                                 settings["checkSticker"] = True
                                 cl.sendMessage(to, "Check Sticker Activated...")
                                 
                        elif cmd == "checksticker off":
                            if msg._from in creator or msg._from in owner:
                                 settings["checkSticker"] = False
                                 cl.sendMessage(to, "Check Sticker Deactivated...")
                                 
                        elif cmd == "unsend on":
                       	 if msg._from in creator or msg._from in owner:
                                 settings["unsendMessage"] = True
                                 cl.sendMessage(to, "Unsend Detect Activated...")
                                 
                        elif cmd == "unsend off":
                            if msg._from in creator or msg._from in owner:
                                 settings["unsendMessage"] = False
                                 cl.sendMessage(to, "Unsend Detect Deactivated...")
                                 
#staffadd
                        elif cmd == "Cowneradd" or text.lower() == 'cowneradd':
                            if msg._from in creator:
                                wait["addowner"] = True
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif cmd == "Cownerdel" or text.lower() == 'cownerdel':
                            if msg._from in creator:
                                wait["dellowner"] = True
                                cl.sendMessage(msg.to,"Send contact...")

                        elif cmd == "Cadminadd" or text.lower() == 'cadminadd':
                            if msg._from in creator or msg._from in owner:
                                wait["addadmin"] = True
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif cmd == "Cadmindel" or text.lower() == 'cadmindel':
                            if msg._from in creator or msg._from in owner:
                                wait["delladmin"] = True
                                cl.sendMessage(msg.to,"Send contact...")

                        elif cmd == "Cstaffadd" or text.lower() == 'cstaffadd':
                            if msg._from in creator or msg._from in owner or msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendMessage(msg.to,"Send contact...")

                        elif cmd == "Cstaffdel" or text.lower() == 'cstaffdel':
                            if msg._from in creator or msg._from in owner or msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendMessage(msg.to,"Send contact...")

                        elif cmd == "Cbotadd" or text.lower() == 'cbotadd':
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["addbots"] = True
                                cl.sendMessage(msg.to,"Send contact...")

                        elif cmd == "Cbotdel" or text.lower() == 'cbotdel':
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["dellbots"] = True
                                cl.sendMessage(msg.to,"Send Contact...")

#refresh
                        elif cmd == "fresh" or text.lower() == 'refresh':
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["addowner"] = False
                                wait["dellowner"] = False
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendMessage(msg.to,"Refresh Done...")

                        elif cmd == "reboot" or text.lower() == 'restart':
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["addowner"] = False
                                wait["dellowner"] = False
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendMessage(msg.to,"Done...")
                                ki.sendMessage(msg.to,"Done...")
                                kk.sendMessage(msg.to,"Done...")
                                kc.sendMessage(msg.to,"Done...")
                                km.sendMessage(msg.to,"Done...")
                                kb.sendMessage(msg.to,"Done...")
                                kd.sendMessage(msg.to,"Done...")
                                ke.sendMessage(msg.to,"Done...")
                                kf.sendMessage(msg.to,"Done...")
                                kg.sendMessage(msg.to,"Done...")
                                kh.sendMessage(msg.to,"Done...")
#cstaffadd
                        elif cmd == "Cownerlist" or text.lower() == 'cownerlist':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in owner:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "Cadminlist" or text.lower() == 'cadminlist':
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "Cstafflist" or text.lower() == 'cstafflist':
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "Cbotlist" or text.lower() == 'cbotlist':
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#banlist
                        elif text.lower() == "BANALL":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendMessage(msg.to,"Not Found...")
                                else:
                                    for target in targets:
                                         if target not in wait["selfbot"] or target not in Bots:
                                            try:
                                                wait["blacklist"][target] = True
                                                cl.sendMessage(msg.to,"You Got Marked...")
                                            except:
                                                pass
                        elif text.lower() == "UNBANALL":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    cl.sendMessage(msg.to,"Not Found...")
                                else:
                                    for target in targets:
                                            try:
                                                del wait["blacklist"][target]
                                                cl.sendMessage(msg.to,"You Got Free...")
                                            except:
                                                pass

                        elif ("talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Added To Talkbanlist...")
                                       except:
                                           pass

                        elif ("talkunban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"Removed From Talkbanlist...")
                                       except:
                                           pass

                        elif cmd == "ctalkban" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                wait["Talkwblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact...")

                        elif cmd == "ctalkunban" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                wait["Talkdblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact...")

                        elif ("banadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"Added To Banlist...")
                                       except:
                                           pass

                        elif ("removeban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"Removed From Banlist...")
                                       except:
                                           pass

                        elif cmd == "cban" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                wait["wblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact...")

                        elif cmd == "cunban" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                                wait["dblacklist"] = True
                                cl.sendMessage(msg.to,"Send contact...")

                        elif cmd == "banlist" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"Empty Banlist...")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"[> Banlist <]\n\n"+ma+"\n●> Total [%s] User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"Empty Talkbanlist...")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"[> Talkbanlist <]\n\n"+ma+"\n●> Total [%s] User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "cbanlist" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"Empty Blacklist...")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == '':
                          if wait["selfbot"] == True:
                            if msg._from in creator or msg._from in owner:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "%i" % len(ragets)
                              cl.sendMessage(msg.to,"Blacklist Cleared...")                        
#===========COMMAND SET============#
                        elif 'set pmreply: ' in msg.text:
                           if msg._from in creator or msg._from in owner:
                              spl = msg.text.replace('set pmreply: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Failed Replace Pmreply Msg...")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "[> Pm Reply...\n\n●> Pmreply Msg Set To :\n「{}」".format(str(spl)))

                        elif 'set welcome: ' in msg.text:
                           if msg._from in creator or msg._from in owner:
                              spl = msg.text.replace('set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Failed Replace Welcome Msg...")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "[> Welcome Msg <]\n\n●> Welcome Msg Set To :\n「{}」".format(str(spl)))

                        elif 'set respond: ' in msg.text:
                           if msg._from in creator or msg._from in owner:
                              spl = msg.text.replace('set respond: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Failed Replace Respond Msg...")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "[> Respond Tag <]\n\n●> Respond Msg Set To :\n「{}」".format(str(spl)))

                        elif 'set reader: ' in msg.text:
                           if msg._from in creator or msg._from in owner:
                              spl = msg.text.replace('set reader: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Failed Replace Reader Msg...")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "[> Reply Reader <]\n\n●> Reply Msg Set To :\n「{}」".format(str(spl)))

                        elif text.lower() == "check pmreply":
                            if msg._from in creator or msg._from in owner:
                               cl.sendMessage(msg.to, "[> Pm Reply <]\n\n●> Reply Msg :\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "check welcome":
                            if msg._from in owner or msg._from in admin:
                               cl.sendMessage(msg.to, "[> Welcome <]\n\n●> Welcome Msg :\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "check respond":
                            if msg._from in creator or msg._from in owner:
                               cl.sendMessage(msg.to, "[> Respond Tag <]\n\n●> Respond Msg :\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "check reader":
                            if msg._from in creator or msg._from in owner:
                               cl.sendMessage(msg.to, "[> Reply Reader <]\n\n●> Reply Msg :\n「 " + str(wait["mention"]) + " 」")
                               
                        elif cmd == "checkban":
                            if msg._from in creator or msg._from in owner or msg._from in admin or msg._from in staff:
                               try:cl.inviteIntoGroup(to, ["u45882d0ead1703855dbc60d40e37bec7"]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, ["u45882d0ead1703855dbc60d40e37bec7"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = ": [>>☑️<<]"
                               else:sil = ": [>>❎<<]"
                               if has1 == "OK":sil1 = ": [>>☑️<<]"
                               else:sil1 = ": [>>❎<<]"
                               cl.sendMessage(to, "●> Kick {} \n●> Invite {}".format(sil1,sil))
                               try:ki.inviteIntoGroup(to, ["u2bf37dc8bb9ac850615395a9e15850f9"]);has = "OK"
                               except:has = "NOT"
                               try:ki.kickoutFromGroup(to, ["u2bf37dc8bb9ac850615395a9e15850f9"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = ": [>>☑️<<]"
                               else:sil = ": [>>❎<<]"
                               if has1 == "OK":sil1 = ": [>>☑️<<]"
                               else:sil1 = ": [>>❎<<]"
                               ki.sendMessage(to, "●> Kick {} \n●> Invite {}".format(sil1,sil))                               
                               try:kk.inviteIntoGroup(to, ["u0a5ee8d796e3677a56b84ff03b6564ec"]);has = "OK"
                               except:has = "NOT"
                               try:kk.kickoutFromGroup(to, ["u0a5ee8d796e3677a56b84ff03b6564ec"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = ": [>>☑️<<]"
                               else:sil = ": [>>❎<<]"
                               if has1 == "OK":sil1 = ": [>>☑️<<]"
                               else:sil1 = ": [>>❎<<]"
                               kk.sendMessage(to, "●> Kick {} \n●> Invite {}".format(sil1,sil))
                               try:kc.inviteIntoGroup(to, ["u29b16f0e99cfdf0e7d7b8170f7cdc1a7"]);has = "OK"
                               except:has = "NOT"
                               try:kc.kickoutFromGroup(to, ["u29b16f0e99cfdf0e7d7b8170f7cdc1a7"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = ": [>>☑️<<]"
                               else:sil = ": [>>❎<<]"
                               if has1 == "OK":sil1 = ": [>>☑️<<]"
                               else:sil1 = ": [>>❎<<]"
                               kc.sendMessage(to, "●> Kick {} \n●> Invite {}".format(sil1,sil))                               
                               try:km.inviteIntoGroup(to, ["udfad8056476f3e76903575513cc8aebe"]);has = "OK"
                               except:has = "NOT"
                               try:km.kickoutFromGroup(to, ["udfad8056476f3e76903575513cc8aebe"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = ": [>>☑️<<]"
                               else:sil = ": [>>❎<<]"
                               if has1 == "OK":sil1 = ": [>>☑️<<]"
                               else:sil1 = ": [>>❎<<]"
                               km.sendMessage(to, "●> Kick {} \n●> Invite {}".format(sil1,sil))                              
                               try:kb.inviteIntoGroup(to, ["uea5fe04e39713e6768cf5687bc5ac7aa"]);has = "OK"
                               except:has = "NOT"
                               try:kb.kickoutFromGroup(to, ["uea5fe04e39713e6768cf5687bc5ac7aa"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = ": [>>☑️<<]"
                               else:sil = ": [>>❎<<]"
                               if has1 == "OK":sil1 = ": [>>☑️<<]"
                               else:sil1 = ": [>>❎<<]"
                               kb.sendMessage(to, "●> Kick {} \n●> Invite {}".format(sil1,sil))
                               try:kd.inviteIntoGroup(to, ["uea5fe04e39713e6768cf5687bc5ac7aa"]);has = "OK"
                               except:has = "NOT"
                               try:kd.kickoutFromGroup(to, ["uea5fe04e39713e6768cf5687bc5ac7aa"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = ": [>>☑️<<]"
                               else:sil = ": [>>❎<<]"
                               if has1 == "OK":sil1 = ": [>>☑️<<]"
                               else:sil1 = ": [>>❎<<]"
                               kd.sendMessage(to, "●> Kick {} \n●> Invite {}".format(sil1,sil))
                               try:ke.inviteIntoGroup(to, ["uea5fe04e39713e6768cf5687bc5ac7aa"]);has = "OK"
                               except:has = "NOT"
                               try:ke.kickoutFromGroup(to, ["uea5fe04e39713e6768cf5687bc5ac7aa"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = ": [>>☑️<<]"
                               else:sil = ": [>>❎<<]"
                               if has1 == "OK":sil1 = ": [>>☑️<<]"
                               else:sil1 = ": [>>❎<<]"
                               ke.sendMessage(to, "●> Kick {} \n●> Invite {}".format(sil1,sil))
                               try:kf.inviteIntoGroup(to, ["uea5fe04e39713e6768cf5687bc5ac7aa"]);has = "OK"
                               except:has = "NOT"
                               try:kf.kickoutFromGroup(to, ["uea5fe04e39713e6768cf5687bc5ac7aa"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = ": [>>☑️<<]"
                               else:sil = ": [>>❎<<]"
                               if has1 == "OK":sil1 = ": [>>☑️<<]"
                               else:sil1 = ": [>>❎<<]"
                               kf.sendMessage(to, "●> Kick {} \n●> Invite {}".format(sil1,sil))
                               try:kg.inviteIntoGroup(to, ["uea5fe04e39713e6768cf5687bc5ac7aa"]);has = "OK"
                               except:has = "NOT"
                               try:kg.kickoutFromGroup(to, ["uea5fe04e39713e6768cf5687bc5ac7aa"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = ": [>>☑️<<]"
                               else:sil = ": [>>❎<<]"
                               if has1 == "OK":sil1 = ": [>>☑️<<]"
                               else:sil1 = ": [>>❎<<]"
                               kg.sendMessage(to, "●> Kick {} \n●> Invite {}".format(sil1,sil))
                               try:kh.inviteIntoGroup(to, ["uea5fe04e39713e6768cf5687bc5ac7aa"]);has = "OK"
                               except:has = "NOT"
                               try:kh.kickoutFromGroup(to, ["uea5fe04e39713e6768cf5687bc5ac7aa"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = ": [>>☑️<<]"
                               else:sil = ": [>>❎<<]"
                               if has1 == "OK":sil1 = ": [>>☑️<<]"
                               else:sil1 = ": [>>❎<<]"
                               kh.sendMessage(to, "●> Kick {} \n●> Invite {}".format(sil1,sil))
                               
#jointicket
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     group2 = kk.findGroupByTicket(ticket_id)
                                     kk.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     group3 = kc.findGroupByTicket(ticket_id)
                                     kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     group4 = km.findGroupByTicket(ticket_id)
                                     km.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     group5 = kb.findGroupByTicket(ticket_id)
                                     kb.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     group6 = kd.findGroupByTicket(ticket_id)
                                     kd.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     group7 = ke.findGroupByTicket(ticket_id)
                                     ke.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     group8 = kf.findGroupByTicket(ticket_id)
                                     kf.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     group9 = kg.findGroupByTicket(ticket_id)
                                     kg.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     group10 = kh.findGroupByTicket(ticket_id)
                                     kh.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     group11 = sw.findGroupByTicket(ticket_id)
                                     sw.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     cl.sendMessage(msg.to, "[> Jointicket <]\n\n●>Successfully Joined\n●> Group Name : %s" % str(group.name))


    except Exception as error:
        print (error)


while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                # Don't remove this line, if you wan't get error soon!
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
