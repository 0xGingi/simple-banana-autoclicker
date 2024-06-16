from pywinauto.application import Application
import time
import keyboard

app = Application().connect(path="C:\\Program Files (x86)\\Steam\\steamapps\\common\\Banana\\Banana.exe")
running = False

def toggle_running(e):
    global running
    if running:
        print("Stopped clicking banana")
    running = not running
    if running:
        print("Gonna start clicking banana")

keyboard.on_press_key("]", toggle_running, suppress=True)

print("Script started! Press ] to start and stop")

while True:
    if running:
        dlg = app.window(title='Banana')
        dlg.click_input(coords=(320, 320))
        print("Clicked Banana")
        time.sleep(3600)
