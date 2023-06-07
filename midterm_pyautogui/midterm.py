import pyautogui
import os 
from time import sleep

links = "https://solvable-sheep-game.streakingman.com/"

pyautogui.hotkey('command', 'space')
pyautogui.typewrite('chrome')
pyautogui.press('enter')
sleep(0.5)

pyautogui.hotkey('command', 't')
pyautogui.typewrite(links)
pyautogui.press('enter')
sleep(1)

photo = os.listdir("/Users/johnsonhsiao/Desktop/109705056_蕭琪耀_midterm/photo")
photo.remove('.DS_Store')
photo.remove('shuffle.png')
photo.remove('voice.png')
shuffle = '/Users/johnsonhsiao/Desktop/109705056_蕭琪耀_midterm/photo/shuffle.png'

def find_pic(item):
    click = 0
    pic = '/Users/johnsonhsiao/Desktop/109705056_蕭琪耀_midterm/photo/' + item 
    previous = [0, 0]
    press_list = []
    for loc_i in pyautogui.locateAllOnScreen(pic, confidence=0.9, grayscale=False): 
        center = pyautogui.center(loc_i)
        print(center)
        if (center[0]-previous[0]) > 3 or (center[1]-previous[1]) > 3: #避免點辨識到同一個
            click += 1
            press_list.append(center)
            print(center)
        previous = center

    for _ in range(int(click / 3) + 1):
        if click >= 3:
            pyautogui.click(press_list[0])
            sleep(0.1)
            pyautogui.click(press_list[1])
            sleep(0.1)
            pyautogui.click(press_list[2])
            sleep(0.1)
            for _ in range(3):
                press_list.pop()
                click -= 1

    return click

if __name__ == '__main__':
    a = 0
    while True:
        for item in photo:
            a += 1
            click = find_pic(item)
            print(click)
            if a == 9:
                location = pyautogui.locateOnScreen("/Users/johnsonhsiao/Desktop/109705056_蕭琪耀_midterm/photo/voice.png",confidence=0.8)
                center = pyautogui.center(location)
                pyautogui.click(center)
            
        if click <= 3:
            location = pyautogui.locateOnScreen(shuffle,confidence = 0.8)
            center = pyautogui.center(location)
            pyautogui.click(center)
            sleep(0.3)

