import pyautogui

def main():
    screenshot()

def screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")

if __name__ == "__main__":
    main()