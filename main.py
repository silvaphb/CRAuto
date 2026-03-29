from controller import Actions, TextManager
import time

arch_path = 'commands.txt'

with open(arch_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

auto = Actions()
texts = TextManager()

for line in lines:

    if 'sleep' in line.lower():
        temp = texts.getValueParam(line, double=False)
        time.sleep(int(temp))

    elif line.startswith('#'):
        pass

    elif 'screenshot' in line.lower():
        filename = texts.getValueParam(line, double=False)
        auto.screenshot(filename)

    elif 'click' in line.lower():
        x, y = texts.getValueParam(line, double=True)
        auto.click_on(x, y)

    elif 'pressr' in line.lower():
        bind = texts.getValueParam(line, double=False)
        auto.press_and_release(bind)
    
    elif 'pressh' in line.lower():
        bind, timer = texts.getValueParam(line, double=True)
        auto.press_and_hold(bind, timer)

    elif 'write' in line.lower():
        letters = texts.getValueParam(line, double=False)
        auto.write(letters)