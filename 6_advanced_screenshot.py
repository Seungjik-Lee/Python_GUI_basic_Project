import keyboard
from PIL import ImageGrab

def screenshot():
    # 2021년 1월 27일 10시 30분 30초 > _20210127_103030
    curr_time = time.strftime("_%Y%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png". format(curr_time)) #ex) image_20210127_103030.png

keyboard.add_hotkey("F9", screenshot) #사용자가 F9 키를 누르면 스크린샷 저장

keyboard.wait("esc") #사용자가 esc를 누를 때까지 프로그램 수행