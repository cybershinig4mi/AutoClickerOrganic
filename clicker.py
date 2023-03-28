import time
import threading
import win32api
import win32con

monke = int(input('input length of autoclicker: '))
def autoclick():
    
    
    delay = 0.02

   
    while not stop_flag:
        # Use the win32api and win32con modules to perform a left mouse click
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

        
        time.sleep(delay)


stop_flag = False


threading.Thread(target=autoclick).start()


time.sleep(monke)


stop_flag = not stop_flag
