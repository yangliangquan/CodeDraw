'''
Filename: 
Author: Liangquan Yang
Date: 2024-01-25 17:30:39
Email: yangliangquan788@outlook.com
LastEditTime: 2024-02-04 13:40:34
'''

import sys
import os

from cv2 import VideoCapture
from cv2 import imwrite
from cv2 import waitKey
from cv2 import destroyAllWindows
import numpy as np

import time

from PIL import Image


"""
The above code captures video from the webcam, converts each frame into ASCII art, and displays it
in the console.
:param image_file: The `image_file` parameter is the input image file that you want to transform
into ASCII art
:return: The code is returning a string representation of the image converted into ASCII art.
"""

print("""                                                          
                                                          
  .--.--.                                 ,--,    ,--,    
 /  /    '.                             ,--.'|  ,--.'|    
|  :  /`. /            __  ,-.   ,---.  |  | :  |  | :    
;  |  |--`           ,' ,'/ /|  '   ,'\ :  : '  :  : '    
|  :  ;_       ,---. '  | |' | /   /   ||  ' |  |  ' |    
 \  \    `.   /     \|  |   ,'.   ; ,. :'  | |  '  | |    
  `----.   \ /    / ''  :  /  '   | |: :|  | :  |  | :    
  __ \  \  |.    ' / |  | '   '   | .; :'  : |__'  : |__  
 /  /`--'  /'   ; :__;  : |   |   :    ||  | '.'|  | '.'| 
'--'.     / '   | '.'|  , ;    \   \  / ;  :    ;  :    ; 
  `--'---'  |   :    :---'      `----'  |  ,   /|  ,   /  
             \   \  /                    ---`-'  ---`-'   
              `----'                                 
                     ____              ,--,    ,--,    
                   ,'  , `.          ,--.'|  ,--.'|    
                ,-+-,.' _ |          |  | :  |  | :    
  .--.--.    ,-+-. ;   , ||          :  : '  :  : '    
 /  /    '  ,--.'|'   |  || ,--.--.  |  ' |  |  ' |    
|  :  /`./ |   |  ,', |  |,/       \ '  | |  '  | |    
|  :  ;_   |   | /  | |--'.--.  .-. ||  | :  |  | :    
 \  \    `.|   : |  | ,    \__\/: . .'  : |__'  : |__  
  `----.   \   : |  |/     ," .--.; ||  | '.'|  | '.'| 
 /  /`--'  /   | |`-'     /  /  ,.  |;  :    ;  :    ; 
'--'.     /|   ;/        ;  :   .'   \  ,   /|  ,   /  
  `--'---' '---'         |  ,     .-./---`-'  ---`-'   
                          `--`---'                     
""")
time.sleep(2)

codeLib = """@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^'.//-|```` ```"""
count = len(codeLib)

cap = VideoCapture(0)

def transform1(image_file):
    codePic = ""
    for h in range(0, image_file.size[1]):
        for w in range(0, image_file.size[0]):
            g, r, b = image_file.getpixel((w, h))
            gray = int(r * 0.299 + g * 0.587 + b * 0.114)
            codePic = codePic + codeLib[int(((count - 1) - (count - 1) * gray) / 256)]
        codePic = codePic + "\n"
    return codePic


while True:
    
    # The code snippet `hx, frame = cap.read()` is reading a frame from the video capture object
    # `cap`.
    hx, frame = cap.read()

    if hx is False:
        print("read video error")

        exit(0)

    if waitKey(1) & 0xFF == ord("q"):  # 按q退出
        break

    imwrite("temp.jpg", frame)

    # The code snippet `images = Image.open("temp.jpg")` is opening the image file "temp.jpg" using
    # the PIL library.
    images = Image.open("temp.jpg")
    images = images.resize((int(images.size[0] * 0.45), int(images.size[1] * 0.20)))

    print("\033[3m"+transform1(images))
    time.sleep(0.1)
    os.system("cls")
    

# The code `with open("temp.txt", "w+") as f: f.write(transform1(images))` is opening a file named
# "temp.txt" in write mode (`"w+"`). It then writes the output of the `transform1(images)` function to
# the file. The `with` statement ensures that the file is properly closed after writing.
with open("temp.txt", "w+") as f:
    f.write(transform1(images))

cap.release()

destroyAllWindows()

os.system("pause")
