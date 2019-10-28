import pyautogui
import time


def click_button(imgdetected, imgname):
    if imgdetected:
        print(imgname + ' found at ' + str(imgdetected))
        x = imgdetected.left + 2
        y = imgdetected.top + 2
        pyautogui.click(x=(x), y=(y), button='left')
    else:
        print('No ' + imgname + ' yet')

for i in range(100):
    selectbutton = pyautogui.locateOnScreen('SelectButton.png')
    click_button(selectbutton, 'SelectButton')
    bluecoin = pyautogui.locateOnScreen('BlueCoin.png')
    greencoin = pyautogui.locateOnScreen('GreenCoin.png')
    click_button(greencoin, 'GreenCoin')
    autoprogress = pyautogui.locateOnScreen('autoprogress.png')
    '''
    if selectbutton:
        print('Green button found at ' + str(selectbutton))
        x = selectbutton.left + 2
        y = selectbutton.top + 2
        pyautogui.click(x=(x), y=(y), button='left')
    else:
        print('No Select buttons yet')
    '''

    if bluecoin:
        print('Blue Coin found at ' + str(bluecoin))
        x = bluecoin.left + 2
        y = bluecoin.top + 2
        pyautogui.click(x=(x), y=(y), button='left')
    else:
        print('No blue coin yet')

    if autoprogress:
        print('Auto Progress is off: ' + str(autoprogress))
        x = autoprogress.left + 2
        y = autoprogress.top + 2
        pyautogui.click(x=(x), y=(y), button='left')
    else:
        print('Auto progress [ON]')

    pyautogui.PAUSE = 1
