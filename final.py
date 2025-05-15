import time
import webbrowser as web
import pyautogui as pg
import keyboard as kb
from tkinter import Tk
from PIL import Image
import pytesseract
import pygetwindow
import cv2
import numpy as np

message = 'जो मोबाइल की दुकान लोहे का जीना चढ़कर फर्स्ट फ्लोर पर G-101 सेक्टर- 9 में थी, \nअब वह पिछली गली में G-52 में चली गई है । \nMobile Repair Institute (MRI)\nNoida (नोएडा)\nजो पहले G-101, sector-9 में था अब G-52, First floor, Sector-9 में shift हो गया हैं।\nLocation share किया गया है।\nAnil Singh\nMob. No. 9811684490 /7373735462'
message2 = 'https://maps.app.goo.gl/boykX4fDAkv4tViNA'

path = 'C:\\Users\\Shobhit\Desktop\\Projects\\Python\\sms\\trash\\check.png'


def pastemessage1():
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(message)
    with pg.hold('ctrl'):
        pg.press('v')
    r.destroy()

def pastemessage2():
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(message2)
    with pg.hold('ctrl'):
        pg.press('v')
    r.destroy()
    
def checkAlreadySent():
    window = pygetwindow.getActiveWindow()
    left, top = window.topleft
    right, bottom = window.bottomright
    
    #take screenshot
    pg.screenshot(path)
    im = Image.open(path)

    im = im.crop((left + 600, top + 200, right, bottom))
    im.save(path)
    #apply filters and preprocessing
    img_cv = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)


    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)


    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    scale_percent = 150
    width = int(thresh.shape[1] * scale_percent / 100)
    height = int(thresh.shape[0] * scale_percent / 100)
    resized = cv2.resize(thresh, (width, height), interpolation=cv2.INTER_LINEAR)
    #convert image to string
    text = pytesseract.image_to_string(resized)


    keys = ["Mobile Repair Institute", "Anil Singh", "Noida", "9811684490"]
    im.save(path)
    if any(k.lower() in text.lower() for k in keys):
        print("Don't proceed — already sent\n")
        return False

    print("PROCEED\n")
    return True 

web.open(f"https://web.whatsapp.com/")
time.sleep(10)
f = open("num.txt")
r = Tk()
for phone_num in f:
    phone_num = phone_num[:-1]
    pg.click(540,164) #this is the location of adding new number. use mousecords.py for mouse coords
    time.sleep(2)
    #x1f6kntn x1fc57z9 x16cd2qt  unique class if search result not found
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append("+91"+ phone_num)
    r.update() 
    with pg.hold('ctrl'):
        pg.press('v')
    r.destroy()
    time.sleep(3)
    pg.click(351,402) #contact number hit list
    time.sleep(3)
    check = checkAlreadySent()
    time.sleep(2)
    if check:
        pastemessage1()
        time.sleep(1)
        pg.press('enter')
        time.sleep(1)
        pastemessage2()
        time.sleep(1)
        pg.press('enter')
        time.sleep(1)
    pg.click(125,166)  #go back button if not found result
    time.sleep(1)