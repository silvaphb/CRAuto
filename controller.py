import pyautogui, keyboard, time
import presets as PRESET

class Actions():
    def __init__(self):
        pass

    def screenshot(self, filename):
        pyautogui.screenshot(filename)

    def click_on(self, pos_x, pos_y):
        pyautogui.click(int(pos_x), int(pos_y))

    def press_and_release(self, bind):
        keyboard.press(bind)
        keyboard.release(bind)

    def press_and_hold(self, bind, timer):
        keyboard.press(bind)
        time.sleep(int(timer))
        keyboard.release(bind)

    def write(self, text):
        keyboard.write(text)

class TextManager():
    def __init__(self):
        pass

    def getValueParam(self, line: str, double: bool):
        line = line.strip()

        cmd = line.split('(')
        if double: 
            params = cmd[1][:-1].split(',') 
            p1 = PRESET.variables[params[0][1:]] if '$' in params[0] else params[0]
            p2 = PRESET.variables[params[1][1:]] if '$' in params[1] else params[1]
            return p1, p2
        else:
            return cmd[1][:-1]
