import pyautogui
import time


def click_button(imgname, imagefile):
    imgdetected = pyautogui.locateOnScreen(imagefile)
    if imgdetected:
        while imgdetected:
            print(imgname + ' found at ' + str(imgdetected))
            x = imgdetected.left + 2
            y = imgdetected.top + 2
            pyautogui.click(x=(x), y=(y), button='left')
            imgdetected = pyautogui.locateOnScreen(imagefile)
    else:
        print('No ' + imgname + ' yet')


autoprogresscounter = 60
autoprogressdelay = 60

for i in range(100):
    # Check for Boss level
    bosstime = pyautogui.locateOnScreen('BossTime.png')
    if bosstime:
        print('BOSS FIGHT')
        time.sleep(15)
        pyautogui.click(x=(bosstime.left), y=(bosstime.top), button='left')
        pyautogui.typewrite(['1', '2', '3', '4', '5', '6', '7', '8'])

    # Check for Upgrades
    click_button('SelectButton', 'SelectButton.png')

    click_button('BlueCoin', 'BlueCoin.png')

    click_button('GreenCoin', 'GreenCoin.png')

    # Check for Autoprogress and if dying has triggered, wait for a minute to level up.
    autoprogress = pyautogui.locateOnScreen('autoprogress.png')
    if autoprogress:
        if autoprogresscounter < autoprogressdelay:
            print('Autoprogress delayed for ' + str(autoprogressdelay-autoprogresscounter))
            autoprogresscounter +=1
        else:
            click_button('AutoProgress', 'autoprogress.png')
    else:
        print('Auto progress [ON]')
        autoprogresscounter = 0

    #pyautogui.PAUSE = 1
