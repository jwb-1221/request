import pygame
import time
import os
import random
def play_music(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    time.sleep(100)

def  shuffle_play() :
    dir_list=os.listdir("music")
    random.shuffle(dir_list)
    file="music/"+random.choice(dir_list)
    play_music(file)
def specific_play():
    file="music/一分一寸.mp3"
    play_music(file)
def display():
    print("*****本程序由beautiful gril撰写**")
    print("*****定时播音程序已**")
    print("*****请勿关闭本程序*")
def main():
    display()
    while True:
        task_time=time.strftime("%H:%M:%S")
        time.sleep(0.8)
        print("\r当前系统时间为：",task_time,end="")
        if task_time=="10:01:00":
            specific_play()
        if task_time=="10:03:09":
            shuffle_play()

shuffle_play()
