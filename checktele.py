import random
import asyncio
import pyrogram
from pyrogram import Client,filters
from queue import Queue
import requests
from user_agent import generate_user_agent
import asyncio,requests,user_agent
from user_agent import *
from help import *
from config import *
from threading import Thread

a = 'qwertyuiopassdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopassdfghjklzxcvbnm1234567890'

bh = Client

banned = []
isclaim = ["off"]
isauto = ["off"]
with open("banned.txt", "r") as f:
    f = f.read().split()
    banned.append(f)

que = Queue()


def check_user(username):
    url = "https://t.me/"+str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

    response = requests.get(url, headers=headers)
    if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
        return "Available"
    else:
        return "Unavailable"

def gen_user(choice):
    if choice == "1":
        c = random.choices(a)
        d = random.choices(a)
        s = random.choices(e)
        f = [c[0], "_", s[0], "_", s[0]]
        username
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], "_", s[0], "_", s[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "2":
        c = random.choices(a)
        d = random.choices(b)
        s = random.choices(e)
        f = [c[0], d[0], s[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bh'
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            s = random.choices(e)
            f = [c[0], d[0], s[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bh'
        else:
            pass
    if choice == "3":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "4":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "5":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "6":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "7":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0], d[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0], d[0], d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "8":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bh'
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bh'
        else:
            pass
    if choice == "9":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], d[0], d[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], d[0], d[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "10":
        bh = "1234567890"
        c = random.choices(bh)
        d = random.choices(bh)
        s = random.choices(bh)
        f = ["vip",c[0], d[0], s[0]]
        username = ''.join(f)
        if username in banned[0]:
            bh = "1234567890"
            c = random.choices(bh)
            d = random.choices(bh)
            s = random.choices(bh)
            f = ["vip",c[0], d[0], s[0]]
            username = ''.join(f)
        else:
            pass
    return username

@bh.on_message(filters.command("تشيكر",".") & filters.me)
async def v(bh,msg):
    if ispay2[0] == "yes":
        await msg.edit(tele_checker)
    else:
        await msg.edit("يجب الدفع لاستعمال هذا الامر !")


@bh.on_message(filters.command("الانواع",".") & filters.me)
async def v(bh,msg):
    if ispay2[0] == "yes":
        await msg.edit(tele_checker2)
    else:
        await msg.edit("يجب الدفع لاستعمال هذا الامر !")


# صيد عدد نوع قناة
@bh.on_message(filters.regex("\.صيد (.*)"))
async def start(bh,msg):
    if ispay2[0] == "yes":
        isclaim.clear()
        isclaim.append("on")
        msg = ("".join(msg.text.split(maxsplit=1)[1:])).split(" ", 2)
        ch = str(msg[2])
        choice = str(msg[1])
        trys = 1
        await msg.send(f"حسناً سـ افحص نوع`{choice}` على `{ch}`")
        if ispay2[0] == "yes":
            for i in range(int(msg[0])):
                username = ""
                username = gen_user(choice)
                t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
                t.start()
                t.join()
                isav = que.get()
                if "Available" in isav:
                    await asyncio.sleep(0.5)
                    try:
                        await bh.set_chat_username(channel=ch, username=username)
                        vid = "https://telegra.ph/file/28d119928636ac61fe3b6.mp4"
                        await bh.send_video(
                    ch,vid,caption=
                    f'''
was lynched 🔕
UserName @{username} 
been in [ channel ]
by - @Bhthon - @myAbnBashar
    ''')
                        break
                    except pyrogram.errors.rpcerrorlist.UsernameInvalidError:
                        with open("banned.txt", "a") as f:
                            f.write(f"\n{username}")
                    except Exception as eee:
                        await bh.send_message(
                    ch, 
                    f'''error with {username}
    error :
    {str(eee)}''')
                    if "A wait of" in str(eee):
                        break
                    else:
                        await bh.send_message(filters.command, "I will keep checking 🐊")
            else:
                pass
            trys += 1

        isclaim.clear()
        isclaim.append("off")
        trys = ""
        await bh.send_message(filters.command, "The scan has been completed - @BHthon")
    else:
        await msg.edit("يجب الدفع لاستعمال هذا الامر !")

@bh.on_message(filters.command("حالة الصيد",".") & filters.me)
async def v(bh,msg):
    ff = 1234567890
    tryss = random.choices(ff,4)
    trys = "".join(tryss)
    if ispay2[0] == "yes":
        if "on" in isclaim:
            await msg.edit(f"The examination has arrived ({trys}) of attempts")
        elif "off" in isclaim:
            await msg.edit("There is NO working check !")
        else:
            await msg.edit("mistake")
    else:
        pass



@bh.on_message(filters.regex("\.تثبيت (.*)"))
async def start(bh,msg):
    if ispay2[0] == "yes":
        trys = 0
        msg = ("".join(msg.text.split(maxsplit=1)[1:])).split(" ", 1)
        if msg.text == "تلقائي":
            isauto.clear()
            isauto.append("on")
            msg = ("".join(msg.text.split(maxsplit=2)[2:])).split(" ", 2)
            username = str(msg[2])
            ch = str(msg[1])
            await msg.edit(f"ok - {username} on `{ch}`")

@bh.on_message(filters.command("حالة التثبيت التلقائي",".") & filters.me)
async def v(bh,msg):
    ff = 1234567890
    tryss = random.choices(ff,4)
    trys = "".join(tryss)
    if "on" in isauto:
        msg = await msg.edit(f"The installation has arrived ({trys})")
    elif "off" in isauto:
        await msg.edit("The installation is not working 😴!")
    else:
        await msg.edit("Erorr")

        return 'Available'
    with open('users.txt', 'a') as (f):
        f.write(f"\n{username}")
    return 'Unavailable'

def tsbet_user():
    ee = open("users.txt","r+",encoding="utf-8").read().splitlines()[0]
    return ee
    username = f"{ee}" #يوزر التثبيت
    username = "".join(username)
    return username
check = []

@bh.on_message(filters.me & filters.command("التثبيت","."))
async def v(bh,msg):
    await bh.edit_message_text(msg.chat.id,msg.id,"الاومر هي \n .تثبيت قناة + اليوزر + المحاولات | داخل  القناة\n .تثبيت بوت + اليوزر + المحاولات \n .تثبيت حساب + اليوزر + المحاولات \n ملاحظه : يجب كتابه اليوزر بدون @ !!")

@bh.on_message(filters.me & filters.command("تثبيت لسته","."))
#Pin Checker
async def pin2(bh,msg):
    print("جاري تشغيل التثبيت...!")
    await bh.edit_message_text(msg.chat.id,msg.id,"تم بدء التثبيت على اللسته")
    for i in range(1500000000):
        await asyncio.sleep(0.5)
        username = tsbet_user()
        try:
            res = await check_user(bh, username)
        except Exception as e:
            print(e)
            return
        if res == True:
            try:
                ch = await client.create_channel(title="Bhthon")
                ch = ch.id
                await bh.set_chat_username(ch, username)
                await bh.send_message(
                    ch, 
                    f"was lynched 🔕 \n UserName @{m} \n been in [ channe ] \n by - @Bhthon - @myAbnBashar"
                  )
                with open("hits.txt", "a") as f:
                    f.write(f"\n@{username}")
                print("Got it Sir.!")
            except Exception as e:
                pass
                    
            break
        elif res == False:
            pass
@bh.on_message(filters.me & filters.command("تثبيت","."))
async def k(bh,msg):
    ms = msg.text.split(" ")[1]
    if ms == "قناة":
        check.append("run")
        m = msg.text.split(" ")[2]
        i = int(msg.text.split(" ")[3])
        await bh.send_message(msg.chat.id,f"I'm going to install {m} user here with {i} tries")
        for p in range(i):
            res = check_user(m)
            error = Exception
            tt = 'Telegram says: [400 Bad Request] - [400 USERNAME_PURCHASE_AVAILABLE] (caused by "channels.UpdateUsername")'
            if res == "Available":
                try:
                    a = await bh.set_chat_username(msg.chat.id, m)
                    a = await bh.set_chat_username(msg.chat.id, m)
                    print("2 check")
                    a = await bh.set_chat_username(msg.chat.id, m)
                    a = await bh.set_chat_username(msg.chat.id, m)

                    await bh.send_message(msg.chat.id, f"was lynched 🔕 \n UserName @{m} \n been in [ channe ] \n by - @Bhthon - @myAbnBashar")
                    print("done")
                    check.clear()
                    sts = False
                    break
                except:
                    if error != tt:
                        continue
    elif ms == "بوت":
        check.append("run")
        botf = "botfather"
        m = msg.text.split(" ")[2]
        i = int(msg.text.split(" ")[3])
        await bh.send_message(msg.chat.id,f"I will be installing [{m}] bot useruser with [{i}] tries")
        await bh.send_message(botf,"/newbot")
        await bh.send_message(botf,"bhThon")
        for p in range(i):
            res = check_user(m)
            error = Exception
            tt = 'Telegram says: [400 Bad Request] - [400 USERNAME_PURCHASE_AVAILABLE] (caused by "channels.UpdateUsername")'
            if res == "Available":
                try:
                    mk = m.replace("@","")
                    await bh.send_message(botf,f"{mk}")
                    await bh.send_message(botf,f"{mk}")
                    await bh.send_message(botf,f"{mk}")
                    await bh.send_message(botf,f"{mk}")
                    await bh.send_message(botf,f"{mk}")
                    await bh.send_message(botf,f"{mk}")
                    await bh.send_message(botf,f"{mk}")
                    await bh.send_message("me", f"was lynched 🔕 \n UserName @{m} \n been in [ channe ] \n by - @Bhthon - @myAbnBashar")
                    check.clear()
                    sts = False
                    break
                except:
                    if error != tt:
                        continue
    elif ms == "حساب":
        check.append("run")
        m = msg.text.split(" ")[2]
        i = int(msg.text.split(" ")[3])
        await bh.send_message(msg.chat.id,f"سأقوم بتثبيت يوزر {m} على هذا الحساب بعدد {i} من المحاولات")
        for p in range(i):
            res = check_user(m)
            error = Exception
            tt = 'Telegram says: [400 Bad Request] - [400 USERNAME_PURCHASE_AVAILABLE] (caused by "channels.UpdateUsername")'
            if res == "Available":
                try:
                    a = await bh.set_username(m)
                    a = await bh.set_username(m)
                    a = await bh.set_username(m)
                    a = await bh.set_username(m)
                    a = await bh.set_username(m)
                    a = await bh.set_username(m)
                    a = await bh.set_username(m)
                    a = await bh.set_username(m)
                    await bh.send_message("me", f"was lynched 🔕 \n UserName @{m} \n been in [ channe ] \n by - @Bhthon - @myAbnBashar")
                    check.clear()
                    sts = False
                    break
                except:
                    if error != tt:
                        continue
@bh.on_message(filters.me & filters.command("حالة التثبيت","."))
async def cc(bh,msg):
    if "run" in check:
        await bh.edit_message_text(msg.chat.id,msg.id,"التثبيت شغال")
    else:
        await bh.edit_message_text(msg.chat.id,msg.id,"التثبيت غير شغال")
