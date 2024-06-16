from pywinauto.application import Application
import time
import keyboard

app = Application().connect(path="C:\\Program Files (x86)\\Steam\\steamapps\\common\\Banana\\Banana.exe")
running = False

def toggle_running(e):
    global running
    running = not running

keyboard.on_press_key("]", toggle_running, suppress=True)

while True:
    if running:
        dlg = app.window(title='Banana')
        dlg.click_input(coords=(320, 320))
        time.sleep(1)