import eel
import os
try:
    eel.init('web')
    eel.start('index.html.html', size=(1980, 1080))
except OSError:
    print(' Chrome browser is not installed\n   Installing...')
    os.system('start ChromeSetup.exe')
    print('After the installation is complete, run the program again!')
    input('  Press enter...')
