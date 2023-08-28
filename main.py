import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
from pyromod import listen
from pyrogram.types import Message
import tgcrypto
import pyrogram
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
from pyrogram.errors import FloodWait
import time
from pyrogram.types import User, Message
from p_bar import progress_bar
import subprocess
from subprocess import getstatusoutput
import logging
import os
import sys
from get_video_info import get_video_attributes, get_video_thumb
import re
from pyrogram import Client as bot

from dotenv import load_dotenv
load_dotenv()
os.makedirs("./downloads", exist_ok=True)
API_ID = 952608
API_HASH = "8d8d0ad8e3d4bcd54420190f57da78ad"
BOT_TOKEN = "6615719407:AAEiTUDx9wZEu61Cf3c7kr_iW0BGDy347PA"

AUTH_USERS = 818269274
sudo_users = [818269274]
bot = Client(
    "bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)
async def exec(cmd):
  proc = await asyncio.create_subprocess_exec(*cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
  stdout, stderr = await proc.communicate()
  print(stdout.decode())
  return proc.returncode,stderr.decode()
  
  
  
  
@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
 editable = await m.reply_text("**HI Send /down or /cpd or /dhurina or /vision**")


          

@bot.on_message(filters.command(["cancel"]))
async def cancel(_, m):
    editable = await m.reply_text("Canceling All process Plz wait")
    global cancel
    cancel = True
    await editable.edit("cancled")
    return
@bot.on_message(filters.command("restart"))
async def restart_handler(_, m):
    await m.reply_text("Restarted!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)
    
    
    
    
    
    
@bot.on_message(filters.command(["cpd"]))
async def account_login(bot: Client, m: Message):
    
    editable = await m.reply_text("Send Classplus Links Text File")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/"

    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(
        f"Total **{len(links)}** Founded 🤷‍♂️\n\n Download Start From Which Link?.(Enter Line Number) \n\n If You Need To Download From First Then Enter Number 👉 **0**"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0

    editable = await m.reply_text("**Enter Tittle For Batch** 🥎")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text

    await m.reply_text("**Enter Resolution Quality**🥊\n\n Eg:- 720 or 480 or 360...without P")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    raw_text6 = "no"
    thumb = "no"
    res = "NA"
   
    
  
    if raw_text2 == '1280' or (raw_text2.isdigit() and 1200 <= int(raw_text2) <= 1300):
       format_filter = 'bestvideo[height>=1200][height<=1300]+bestaudio/best[height>=1200][height<=1300],854,720,480,360,best'
    elif raw_text2 == '854' or (raw_text2.isdigit() and 800 <= int(raw_text2) <= 900):
       format_filter = 'bestvideo[height>=800][height<=900]+bestaudio/best[height>=800][height<=900],720,480,360,1280,best'
    elif raw_text2 == '720' or (raw_text2.isdigit() and 700 <= int(raw_text2) <= 800):
       format_filter = 'bestvideo[height>=700][height<=800]+bestaudio/best[height>=700][height<=800],854,480,360,1280,best'
    elif raw_text2 == '480' or (raw_text2.isdigit() and 400 <= int(raw_text2) <= 500):
       format_filter = 'bestvideo[height>=400][height<=500]+bestaudio/best[height>=400][height<=500],720,854,1280,best'
    elif raw_text2 == '360' or (raw_text2.isdigit() and 300 <= int(raw_text2) <= 400):
       format_filter = 'bestvideo[height>=300][height<=400]+bestaudio/best[height>=300][height<=400],480,720,854,1280,best'
    elif raw_text2 == '240' or (raw_text2.isdigit() and 200 <= int(raw_text2) <= 300):
       format_filter = 'bestvideo[height>=200][height<=300]+bestaudio/best[height>=200][height<=300],360,480,720,854,1280,best'
    elif raw_text2 == '180' or (raw_text2.isdigit() and 100 <= int(raw_text2) <= 200):
       format_filter = 'bestvideo[height>=100][height<=200]+bestaudio/best[height>=100][height<=200],240,360,480,720,854,1280,best'
    else:
       format_filter = 'best'



    if raw_text == '0':
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(arg, len(links)):

            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/","").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*","").replace("download",".pdf").replace(".","").strip()
            name = f'{str(count).zfill(3)}) {name1}'    

            if "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'
            elif "youtu" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={int(raw_text2)}]+bestaudio" --no-keep-video --remux-video mkv "{url}"'
            elif "classplus" in url:
            	headers = {'Host': 'api.classplusapp.com', 'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6ODg5NjE4NDMsIm9yZ0lkIjoyNTUxLCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTY2NjMzMzY2NjU1OCIsIm5hbWUiOiJGZmZmZmZmIiwiZW1haWwiOiJsYWtlZm94NzA1QGxpZWJvZS5jb20iLCJpc0ZpcnN0TG9naW4iOnRydWUsImRlZmF1bHRMYW5ndWFnZSI6IkVOIiwiY291bnRyeUNvZGUiOiJJTiIsImlzSW50ZXJuYXRpb25hbCI6MCwiaXNEaXkiOmZhbHNlLCJsb2dpblZpYSI6Ik90cCIsImZpbmdlcnByaW50SWQiOiJiNjY3M2Y1YjQ2NmNiODZmZGFhZmJlZGZjNzRjZWYzNSIsImlhdCI6MTY4MTIzMjExNywiZXhwIjoxNjgxODM2OTE3fQ.r0klWJjEaA2jqpij_aSGXA7Mth2rd6LEsfRUhZT8a0byvsJd811FUiyH3TnIfTev', 'user-agent': 'Mobile-Android', 'app-version': '1.4.37.1', 'api-version': '18', 'device-id': '5d0d17ac8fhb3c9f51', 'device-details': '2848b866799971ca_2848b8667a33216c_SDK-30', 'accept-encoding': 'gzip'}
            	params = (('url', f'{url}'),)
            	response = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)
            	url = response.json()['url']
            	cmd = f'yt-dlp -o "{name}.%(ext)s" -f "{format_filter}" --no-keep-video --no-check-certificate --remux-video mkv "{url}"'
            	#cmd = f'yt-dlp -o "{name}.%(ext)s" --no-keep-video --remux-video mkv "{url}"'
            elif "player.vimeo" in url:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif "m3u8" or "livestream" in url:
                if "classplus" in url:
                    cmd = f'yt-dlp --no-keep-video --no-check-certificate --remux-video mkv "{url}" -o "{name}.%(ext)s"'
                else:
                    cmd = f'yt-dlp -f "{ytf}" --no-check-certificate --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif ytf == "0" or "unknown" in out:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif ".pdf" or "download" in url:
                cmd = "pdf"
            else:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --no-check-certificate --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            print(cmd)
            output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
            eta=0
            percentage_10_reached = False
            percentage_20_reached = False
            percentage_30_reached = False
            percentage_40_reached = False
            percentage_50_reached = False
            percentage_60_reached = False
            percentage_70_reached = False
            percentage_80_reached = False
            percentage_90_reached = False
            percentage_100_reached = False
            boom1 = "Downloading..."
            

            
            try:
                Show = f"**Downloading:-**\n\n**Name:** `{name}`\n**Quality:** **{raw_text2}p** (If It's Not Available, Automatically Download Best Quality)\n**URL:** `{url}`"
                prog = await m.reply_text(Show)
                cc = f'{str(count).zfill(3)}**.** {name1} {res}\n**Batch :-** {raw_text0}'
                cc1 = f'{str(count).zfill(3)}**.** {name1} {res}.pdf\n**Batch :-** {raw_text0}'
                # Read the output line by line
                #editable1 = await m.reply_text("Downloading **0%**")
                #editable2 = await m.reply_text("Downloading **0%**")


                for line in output.stdout:
                    if 'ETA' in line:
                       # Extract the ETA value from the output
                       eta = line.split('ETA')[1].strip()
                       
                       
                       #eta = "28:42 (frag 0/324)"

                       # Extract the frag values from the eta string
                       frag_start = eta.find("frag ") + len("frag ")
                       frag_end = eta.find("/", frag_start)
                       frag_current_str = eta[frag_start:frag_end]
                       frag_total_str = eta[frag_end + 1:]
                       #print(f"Extracted frag values: frag_current_str={frag_current_str}, frag_total_str={frag_total_str}")
                       frag_current_str = ''.join(filter(str.isdigit, frag_current_str))
                       frag_total_str = ''.join(filter(str.isdigit, frag_total_str))



                       try:
                          frag_current = int(frag_current_str)
                          frag_total = int(frag_total_str)
                          #print(f"Extracted frag values: frag_current={frag_current}, frag_total={frag_total}")


                          # Calculate the percentage
                          percentage = (frag_current / frag_total) * 100
                          
                            
                          
                          # Check if the percentage reaches 10%
                          if percentage >= 10 and not percentage_10_reached:
                               prog1 = await m.reply_text(boom1+"**10%**")
                               percentage_10_reached = True
                          if percentage >= 20 and not percentage_20_reached:
                               await prog1.delete(True)
                               prog1 = await m.reply_text(boom1+"**20%**")
                               percentage_20_reached = True
                          if percentage >= 30 and not percentage_30_reached:
                               await prog1.delete(True)
                               prog1 = await m.reply_text(boom1+"**30%**")
                               percentage_30_reached = True
                          if percentage >= 40 and not percentage_40_reached:
                               await prog1.delete(True)
                               prog1 = await m.reply_text(boom1+"**40%**")
                               percentage_40_reached = True
                          if percentage >= 50 and not percentage_50_reached:
                               await prog1.delete(True)
                               prog1 = await m.reply_text(boom1+"**50%**")
                               percentage_50_reached = True
                          if percentage >= 60 and not percentage_60_reached:
                               await prog1.delete(True)
                               prog1 = await m.reply_text(boom1+"**60%**")
                               percentage_60_reached = True
                          if percentage >= 70 and not percentage_70_reached:
                               await prog1.delete(True)
                               prog1 = await m.reply_text(boom1+"**70%**")
                               percentage_70_reached = True
                          if percentage >= 80 and not percentage_80_reached:
                               await prog1.delete(True)
                               prog1 = await m.reply_text(boom1+"**80%**")
                               percentage_80_reached = True
                          if percentage >= 90 and not percentage_90_reached:
                               await prog1.delete(True)
                               prog1 = await m.reply_text(boom1+"**90%**")
                               percentage_90_reached = True
                          if percentage >= 100 and not percentage_100_reached:
                               await prog1.delete(True)
                               prog1 = await m.reply_text(boom1+"**100%**")
                               percentage_100_reached = True
                               await prog1.delete(True)
                       except ValueError:
                             print("Invalid frag values in the ETA string.")

                       
                       
                       #await editable.delete(True)
                
                if cmd == "pdf" or ".pdf" in url or ".pdf" in name:
                    try:
                        
                        ka = await helper.aio(url, name)
                        await prog.delete(True)
                        time.sleep(0.5)
                        reply = await m.reply_text(f"Uploading - ```{name}```")
                        time.sleep(0.5)
                        start_time = time.time()
                        await m.reply_document(
                            ka,
                            caption=
                            f'**Title »** {name1} {res}.pdf\n**Caption »** {raw_text0}\n**Index »** {str(count).zfill(3)}'
                        )
                        count +=1
                        # time.sleep(1)
                        await reply.delete(True)
                        time.sleep(0.5)
                        os.remove(ka)
                        time.sleep(0.5)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await helper.send_vid(bot, m, cc, filename, thumb, name,
                                          prog)
                    count += 1
                    time.sleep(0.5)

            except Exception as e:
                await m.reply_text(
                    f"**Downloading Failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`"
                )
                continue
                

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done")
    
    


    
    
bot.run()    
