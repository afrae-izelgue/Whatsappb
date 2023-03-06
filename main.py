import pyautogui as pt
from time import sleep
import pyperclip

sleep(2)

#gets message
def get_message():
    global x,y
    
    position = pt.locateOnScreen("whatsapp/emojis.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x+ 40, y - 70)
    pt.rightClick()
    pt.moveRel(20,-250)
    pt.doubleClick()
    whatsapp_message = pyperclip.paste()
    print("Message Received:" + whatsapp_message)
    
    return whatsapp_message

def post_response(message):

    global x,y
    
    position = pt.locateOnScreen("whatsapp/emojis.png", confidence=.5)
    x = position[0]
    y = position[1]
    pt.move(10,200)
    pt.click()
    pt.typewrite(message, interval = .01)
    pt.typewrite("\n", interval=.01)
    

#precesses response 
def process_response(message):
        
    if message.__eq__("Salam Alaykoum"):
        return "Wa Alaikoum Assalam"
    
    else:
        return "I will text you back later"
    
processed_message = process_response(get_message())  
post_response(processed_message)
