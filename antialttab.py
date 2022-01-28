import keyboard
import win32clipboard
import time
import json
import ctypes

def main():
    file = open("asd.json", "r", encoding="utf-8")
    questions = json.load(file)

    while True:
        try:
            if keyboard.is_pressed('shift'):
                win32clipboard.OpenClipboard()
                data = win32clipboard.GetClipboardData()
                #win32clipboard.EmptyClipboard()
                win32clipboard.CloseClipboard()
                
                answer = ""
                for question in questions:
                    if data in question["q"]:
                        if not answer:
                            answer = question["a"]
                        else:
                            answer += " ; " + question["a"]

                if not answer:
                    answer = "Answer not found :("

                keyboard.write(answer)
                time.sleep(0.5)
                continue


            if keyboard.is_pressed('i'):
                dll = ctypes.cdll.LoadLibrary("AutoHotkey.dll")
                dll.ahktextdll(u"")
                dll.ahkExec('MouseGetPos, xPos, yPos, winId' \
                '\n    PixelGetColor, color, %xPos%, %yPos%, RGB' \
                '\n    WinGetTitle, winTitle, ahk_id %winId%' \
                '\n    ToolTip "%winTitle%"`n%xPos% %yPos% %color%')
                continue
        except:
            break

if __name__ == "__main__":
    main()