from controller import Actions, TextManager
import presets as PRESET
import time

arch_path = 'commands.txt'

with open(arch_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

auto = Actions()
texts = TextManager()

for line in lines:
    cmd = line.lower()

    if 'sleep' in cmd:
        temp = texts.getValueParam(line, double=False)
        time.sleep(int(temp))

    elif line.startswith('#'):
        pass

    elif 'screenshot' in cmd:
        filename = texts.getValueParam(line, double=False)
        auto.screenshot(filename)
    
    elif 'var' in cmd:
        var_name, value = texts.getValueParam(line, double=True)
        for n in PRESET.numbers:
            if n in str(value) and not '.' in str(value):
                value = int(value)
            elif n and '.' in str(value):
                value = float(value)
            else:
                value = str(value)
        PRESET.variables[var_name] = value
        
    elif 'click' in cmd:
        x, y = texts.getValueParam(line, double=True)
        auto.click_on(x, y)

    elif 'pressr' in cmd:
        bind = texts.getValueParam(line, double=False)
        auto.press_and_release(bind)
    
    elif 'pressh' in cmd:
        bind, timer = texts.getValueParam(line, double=True)
        auto.press_and_hold(bind, timer)

    elif 'write' in cmd:
        letters = texts.getValueParam(line, double=False)
        auto.write(letters)
    
    else:
        print(f'Erro na linha: {line}')