from pywinauto.application import Application
import time
import keyboard
import sys

app_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Banana\\Banana.exe"
window_title = "Banana"

def start_application():
    try:
        app = Application().start(app_path)
        print("Started Banana application")
        return app
    except Exception as e:
        print(f"Failed to start Banana application: {e}")
        sys.exit(1)

def connect_to_application():
    try:
        app = Application().connect(path=app_path)
        print("Connected to Banana application")
        return app
    except Exception as e:
        print(f"Failed to connect to Banana application: {e}")
        return None

running = False
app = None

def toggle_running(e):
    global running, app
    if running:
        print("Stopped clicking banana")
    else:
        print("Gonna start clicking banana")
        if not app:
            app = connect_to_application()
            if not app:
                print("Application is not running. Please start the application manually or press 'o' to open it.")
                return
    running = not running

keyboard.on_press_key("]", toggle_running, suppress=True)

print("Script started! Press 'o' to open Banana application. Press ']' to start and stop clicking. Press [ESC] to exit.")

try:
    while True:
        if keyboard.is_pressed('o'):
            app = start_application()
            print("Waiting for the application to load...")
            time.sleep(10)  # Wait for the application to fully load (adjust as needed)
            app = connect_to_application()
            print("Application loaded and connected. Now you can press ']' to start/stop clicking.")

        if running and app:
            try:
                dlg = app.window(title=window_title)
                dlg.click_input(coords=(960, 540))
                print("Clicked Banana")
            except Exception as e:
                print(f"Failed to click banana: {e}")
            time.sleep(3600)
        else:
            time.sleep(0.1)  # Sleep briefly to reduce CPU usage
except KeyboardInterrupt:
    print("Script terminated by user")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Exiting script")

# To exit gracefully on ESC key press
keyboard.wait('esc')
print("ESC pressed. Exiting...")
