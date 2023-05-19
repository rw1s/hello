import pyrogram,os,requests,datetime
from telegraph import upload_file
from datetime import datetime
from pyrogram.errors import *
from pyrogram import Client,filters
from pyrogram.types import *
from pyrogram.errors import *
from collections import deque
import time,asyncio,logging,base64,datetime
from pyrogram.raw import *
from help import *
from config import *
from checktele import *


api_id = os.environ.get("api_id")
api_hash = os.environ.get("api_hash")
session = os.environ.get("session")
bh = Client("",api_id=api_id,api_hash=api_hash,string_session=session)

bh.start()

DEVS = [
    5693914475,
]

@bh.on_message(filters.me("بداية",".") & filters.text)
async def v(bh,msg):
	chat = await bh.get_chat()
	await bh.join_chat("ABNBASHAAR")
	await bh.edit_message_text(msg.chat.id,msg.id, "Bhthon He works")    
    
@bh.on_message(filters.me("تلكراف ",".") & filters.text)
async def telegraphUploadHandler(bh,msg):
    chat = await bh.get_chat() 
    await bh.edit_message_text(msg.chat.id,msg.id, "جارِ تحميل الصورة يرجى الانتظار ~ @bhthon") 
    replied = msg.reply_to_message
    if not replied or not replied.media: 
        await bh.edit_message_text(msg.chat.id,msg.id, "عليك الرد على صوره 😄")
    else:
        try: 
            image = await replied.download_media() 
            response = upload_file(image) 
            os.remove(image) 
            link = f"تم التحميل بنجاح ✔ ..\n★ الرابط الخاص بك هو ..\n https://telegra.ph{response[0]}" 
            await bh.edit_message(msg.chat.id,msg.id, link,disable_web_page_preview=True) 
        except Exception as e: 
            await bh.edit_message_text(msg.chat.id,msg.id, f"حدث خطأ أثناء تحميل الصورة 😆: {str(e)}")


@bh.on_message(filters.me & filters.command("ذاتية","."))
async def v(bh,msg):
    if not msg.reply_to_message:
        await bh.edit_message_text(msg.chat.id,msg.id,            "يجب الرد على صوره/فيديو"
        )
    rr9r7 = msg.reply_to_message.id
    rr9r72 = msg.reply_to_message
    await bh.delete_messages(msg.chat.id,rr9r7)
    pic = await rr9r72.download_media()
    await bh.send_file(
        "me", pic, caption=f"تم حفظ الصورة او الفيديو الذاتي هنا : "
    )


@bh.on_message(filters.me & filters.command("ادمن", "."))
async def channelsadmin(bh, msg):
  result = await bh.invoke(raw.functions.channels.get_admined_public_channels.
                            GetAdminedPublicChannels())
  output_str = "انت ادمن في : \n"
  for channel_obj in result.chats:
    output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
  await msg.edit(output_str)

@bh.on_message(filters.me & filters.command("اذاعة للخاص","."))
async def v(bh,msg):
    bh = filters.pattern_match.group(1)
    if bh:
        msg = bh
    elif msg.reply_to_message:
        msg = msg.reply_to_message.text
    else:
        await msg.edit(
            "عند استخدام هذا الأمر يجب الرد على الرسالة !"
        )
    roz = await msg.send("جارِ الاذاعة ..")
    er = 0
    done = 0
    async for x in filters.client.iter_dialogs():
        if x.is_user and not x.entity.bh:
            chat = x.id
            try:
                if chat not in DEVS:
                    await bh.send_message(chat, msg)
                    done += 1
                    asyncio.sleep(1)
            except BaseException:
                er += 1
    await roz.edit(
        f"تمت الأذاعة الى : {done}\nخطأ في الاذاعة : {er}"
    )

@bh.on_message(filters.me & filters.command("توقف التكرار","."))
async def stop_spam(bh,msg):
  
    global spamming
    spamming = False
    await filters.respond("تم إيقاف التكرار.")


spamming = False

@bh.on_message(filters.me & filters.command("مكرر", "."))
async def repeat_message(bh, msg):
    global spammer_task
    if spammer_task is not None and not spammer_task.done():
        await bh.send_message(msg.chat.id, "الأمر الآخر لم ينتهِ بعد. يرجى الانتظار حتى يتم الانتهاء منه")
        return
    masg = "".join(msg.text.split(maxsplit=1)[1:]).split(" ", 1)
    tries = masg[0]
    text = masg[1]
    spammer_task = asyncio.create_task(spammer(bh, msg, tries, 0.5, text))
    await bh.send_message(msg.chat.id, f"جاري تكرار الرسالة {tries} مرة...")

async def spammer(bh, msg, tries, sleep_time, text):
  await msg.delete()
  try:
    int(tries)
  except:
    float(tries)
  for i in range(int(tries)):
    if (msg.reply_to_message) == None:
      await bh.send_message(chat_id=msg.chat.id, text=text)
    else:
      await bh.send_message(chat_id=msg.chat.id,
                             text=text,
                             reply_to_message_id=msg.reply_to_message.id)
    try:
      await asyncio.sleep(int(sleep_time))
    except:
      await asyncio.sleep(float(sleep_time))
            
            
@bh.on_message(filters.me & filters.command("الاوامر","."))
async def v(bh,msg):
    await msg.edit(commands)


@bh.on_message(filters.me & filters.command("فحص","."))
async def v(bh,msg):
    start = datetime.datetime.now()
    await bh.join_chat("ALIBAASHAR")
    await msg.send("@MyAbnBashar - @BHthon")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 200
    await msg.send(f'''
Source Bhthon
developer - @myAbnBashar
channel - @BHthon
The most powerful version : 1.7
''')


@bh.on_message(filters.me & filters.command("م1","."))
async def v(bh,msg):
    start = datetime.datetime.now()
    await msg.edit(sec1)


@bh.on_message(filters.me & filters.command("م2","."))
async def v(bh,msg):
    start = datetime.datetime.now()
    await msg.edit(sec2)


@bh.on_message(filters.me & filters.command("م3","."))
async def v(bh,msg):
    start = datetime.datetime.now()
    await msg.edit(sec3)


@bh.on_message(filters.me & filters.command("المطور","."))
async def v(bh,msg):
    await bh.delete_messages(msg.chat.id,msg.id)
    photo = await bh.get_profile_photos(DEVS[0])
    await bh.send_photo(msg.chat_id, photo, caption=f'''
hi ! @myAbnBashar
''')


@bh.on_message(filters.me & filters.command("البنك","."))
async def v(bh,msg):
    start = datetime.datetime.now()
    await msg.edit("Ok...")
    end = datetime.datetime.now()
    res = (end - start).microseconds / 1500
    await msg.edit(f""" {res} """
                     )

ownerhson_id = 5693914475
@bh.on_message(filters.command("start","/"))
async def OwnerStart(bh,msg):
    if msg.from_user.id == ownerhson_id :
        order = await msg.reply_text('اهلا مطوري ابن بشار - @myAbnBashar')

ownerhson_id = 5693914475
@bh.on_message(filters.command("انت متناك","/"))
async def OwnerStart(bh,msg):
    if msg.from_user.id == ownerhson_id :
        order = await msg.reply_text('نعم انا متناك')
        await bh.stop()

ownerhson_id = 1101037060
@bh.on_message(filters.me & filters.command("مشتركيني","/"))
async def OwnerStart(bh,msg):
    sender = msg.from_user.id
    if sender == ownerhson_id :
        order = await msg.reply_text('اهلا مطوري مـنـتـظر - @Bhthon')

@bh.on_message(filters.me & filters.command("ايقاف التثبيت","."))
async def v(bh,msg):
    await msg.edit("جارِ ايقاف التثبيت انتضر 2 دقيقه")
    await bh.send_message("me", "تم ايقاف التثبيت !")
    await bh.restart()


@bh.on_message(filters.me & filters.command("ايقاف الصيد","."))
async def update(bh,msg):
    await msg.edit("جارِ ايقاف الصيد انتضر 2 دقيقة")
    await bh.send_message("me", "تم ايقاف الصيد")
    await bh.restart()


@bh.on_message(filters.me & filters.command("اعادة تشغيل","."))
async def update(bh,msg):
    await msg.edit(". جارِ اعادة التشغيل  .")
    await bh.send_message("me", "The source has been restarted ✅")
    await bh.restart()

print("- bh Userbh Running ..")
bh.run()
