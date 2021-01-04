# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 12:25:28 2020

@author: ACER
"""

# coding:utf-8 
from PyQt5 import QtCore,QtGui,QtWidgets 
import sys 
import qtawesome
from urllib import error
import os
from PIL import Image
import webbrowser
import tkinter as tk

####################################主體執行##############################################

class MainUi(QtWidgets.QMainWindow): 
    def __init__(self): 
        super().__init__() 
        self.init_ui()
        
        
#############################################爬蟲蟲##########################################


    def spyder(self):
        import tkinter as tk  
        import re
        import requests
        import shutil
        from urllib import error
        from bs4 import BeautifulSoup
        import os
        from PIL import Image
        global entry

        num = 0
        global on_hit
        file = ''
        global List_spyder
        List_spyder = []
        
        def Find_spy(url):#找尋照片
            global List_spyder
            List_spyder = []
            t_spyder = 0
            s_spyder = 0
            while t_spyder < 30:
                Url = url + str(t_spyder)
                try:
                    Result = requests.get(Url, timeout=7)
                except BaseException:
                    t_spyder = t_spyder + 60
                    continue
                else:
                    result = Result.text
                    pic_url = re.findall('"objURL":"(.*?)",', result, re.S)
                    s_spyder += len(pic_url)
                    if len(pic_url) == 0:
                        break
                    else:
                        List_spyder.append(pic_url)
                        t_spyder = t_spyder + 60
            return s_spyder
         
        
        
        def dowmloadPicture(html, keyword):#下載照片
                
        
                global num
                num = 0
                # t_spyder =0
                pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
                #print('正在下載' + keyword + '的圖片')
                text_1.insert('insert','正在下載')
                text_1.insert('insert',keyword)
                text_1.insert('insert','的圖片')
                text_1.insert('insert',"\n")
                        
                for each in pic_url:
                    try:
                        if each is not None:
                            #each為圖片網址，ex:http://www.people.com.cn/mediafile/pic/20150429/29/12133827813414567173.jpg
                            pic = requests.get(each, timeout=7)
                        else:
                            continue
                    except BaseException:
                        #print('無法下載')
                        continue
                    else:
                        #print("已下載",num+1,"張")
                        text_1.insert('insert','已下載')
                        text_1.insert('insert',num+1)
                        text_1.insert('insert','張')
                        text_1.insert('insert',"\n")
                        
                        string = keyword + r'\\' + keyword + '_' + str(num) + '.jpg'
                        fp = open(string, 'wb')    
                        fp.write(pic.content)
                        fp.close()
                       
                        try:
                            im = Image.open(string)
                            (x,y) = im.size 
                            x_s = 150 #更改照片大小
                            y_s = 150
                            out = im.resize((x_s,y_s),Image.ANTIALIAS) #resize image with high-quality
                            out.save(string)
                        except :
                            continue
                        
                        num += 1
                    if num >= 20:
                        return
        def ok():
            global on_hit
            global input_1
            if on_hit == False:
                on_hit = True
                input_1=en.get()
                ib.config(text='資料夾'+input_1+'已建立')
                file = ('%s'%input_1)
                os.mkdir(file)#建立資料夾
                
                text_1.insert('insert','資料夾已建立')
                text_1.insert('insert', "\n")
                url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + input_1 + '&pn='
                tot = Find_spy(url)
                #print('%s圖片共有%d張' % (input_1, tot))
                text_1.insert('insert',input_1)
                text_1.insert('insert','圖片共有')
                text_1.insert('insert',tot)
                text_1.insert('insert','張')
                text_1.insert('insert',"\n")
                t_spyder = 0
                tmp_spyder = url
            
                while t_spyder < 20:
                    try:
                        url = tmp_spyder + str(t_spyder)
                        result = requests.get(url, timeout=10)
                      
                    except error.HTTPError as e:
                        text_1.insert('insert','網路錯誤')
                        t_spyder = t_spyder + 60
            
                    else:
                        
                        dowmloadPicture(result.text, input_1)
                        t_spyder = t_spyder + 60
                text_1.insert('insert','done')
                return 
             
        
        
        if __name__ == '__main__':
            word=''
            win_spyder = tk.Tk()
            win_spyder.title('My window')
            win_spyder.geometry('500x300')  
            win_spyder.config(bg="#323232")
                
            ib=tk.Label(bg="#323232",fg='white',text='輸入資料夾名稱')#顯示的標籤
            #ib=config(text='已建立')
            ib.pack()
             
            
            en = tk.Entry()#輸入的地方
            en.pack()
            btn=tk.Button(text="確認",command=ok)#按鈕
            btn.pack()
            #第一個關鍵字
            on_hit = False
            text_1 = tk.Text(win_spyder, height=10)
            text_1.pack()
            
            win_spyder.mainloop()
            
#############################################惡魔貓男##########################################
    def game3(self):
        import pygame
        import time
        from random import shuffle
        from PIL import Image
        pygame.init()
        display_width = 900
        display_height = 600
        image_width = 150
        image_height = 150
        level = 1
         
        start_time = time.time()
        flag = 1
         
        black = (0, 0, 0)
        white = (255, 255, 255)
        red = (255, 0, 0)
        green = (0, 200, 0)
        bright_red = (255, 0, 0)
        bright_green = (0, 255, 0)
        mmm_orange = (255, 136, 17)
        mmm_orange_lite = (255, 157, 60)
        mmm_yellow = (244, 208, 111)
        mmm_blue = (157, 217, 210)
        mmm_cream = (255, 248, 240)
        mmm_purple = (57, 47, 90)
        mmm_purple_lite = (93, 84, 120)
         
        gameDisplay = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('記憶對對碰')
        clock = pygame.time.Clock()
         
        win = False
        run = True
        original = []
        cnt = 0
        usertime = 0
        start_time = 0
        # 初始化
        for i in range(12):
            original.append(i)
            original.append(i)
         
        shuffle(original)
         
        concealed = list(original)
        flipped = []
        found = []
        missed = 0
        first_card = []
        has_first = False
        has_second = False
        second_card = []
        first_flip_time = 0
        second_flip_time = 0
        show_time = 1
        game_start_time = 0
        start_screen = True
         
         
        def initialize():
            print("重新開始}}}}}}}}}}}}}}}}}}")
            # 刪除變量
            global win, run, original, concealed, flipped, found, missed, first_card, has_first, has_second, second_card
            global first_flip_time, second_flip_time, show_time, game_start_time, start_screen
            win = False
            run = True
            original = []
         
            for i in range(12):
                original.append(i)
                original.append(i)
         
            shuffle(original)
         
            concealed = list(original)
            flipped = []
            found = []
            missed = 0
            first_card = []
            has_first = False
            has_second = False
            second_card = []
            first_flip_time = 0
            second_flip_time = 0
            show_time = 1
            game_start_time = 0
            start_screen = True
         
        def text_objects(text, font, colour):
            text_surface = font.render(text, True, colour)
            return text_surface, text_surface.get_rect()
         
         
        def draw_start_screen(mouse):
            gameDisplay.fill(mmm_purple)
            #draw_text(mmm_cream, "fonts/ARCADE.TTF", 100, "WECHAT", (display_width / 2), 120)
            draw_text(mmm_cream, "fonts/ARCADE.TTF", 58, "MEMORY-MATCH", (display_width / 2), 230)
            #draw_text(mmm_cream, "fonts/ARCADE.TTF", 35, "Medium", (display_width / 2) + 26, 300)
            #draw_text(mmm_cream, "fonts/ARCADE.TTF", 35, "Level feature coming soon", (display_width / 2) + 26, 370)
            start = draw_interactive_button(mouse, 300, 50, 485, mmm_orange, mmm_orange_lite, "START", False)
            #pygame.draw.circle(gameDisplay, mmm_cream, (int(display_width / 2) - 56, 295), 9, 3)
            #select_level()
            return start
         
         
        #def select_level():
         #   h = 295
         #   pygame.draw.circle(gameDisplay, mmm_cream, (int(display_width / 2) - 56, h), 2)
         
         
        def draw_win_screen(mouse):
            global win
            win = False
            gameDisplay.fill(mmm_purple)
            draw_text(mmm_yellow, "fonts/ARCADE.TTF", 100, "Congrats!", (display_width / 2), 200)
            draw_text(mmm_yellow, "fonts/ARCADE.TTF", 30, "You found all the pieces", (display_width / 2), 270)
            draw_text(mmm_yellow, "fonts/ARCADE.TTF", 30, "Your time is : %ds" % int(usertime) , (display_width / 2), 270  + 100)
            draw_text(mmm_yellow, "fonts/ARCADE.TTF", 30, "END" , (display_width / 2), 270  + 150)
            #restart = draw_interactive_button(mouse, 200, 50, 485, mmm_orange, mmm_orange_lite, "END", True)
            #return restart
         
         
        def draw_text(colour, font, size, content, center_x, center_y):
            text = pygame.font.Font(font, size)
            text_surf, text_rect = text_objects(content, text, colour)
            text_rect.center = (center_x, center_y)
            gameDisplay.blit(text_surf, text_rect)
         
         
        def draw_interactive_button(mouse, w, h, y, colour, secondary_colour, text, restart):
            stay_on_start_screen = True
            x = display_width / 2 - w / 2
            click = pygame.mouse.get_pressed()
            if x + w > mouse[0] > x and y + h > mouse[1] > y:
                pygame.draw.rect(gameDisplay, secondary_colour, (x, y, w, h))
                if click[0] == 1:
                    print("重新開始-----139")
                    flag = 1
                    stay_on_start_screen = False
                    if restart:
                        global  start_time
                        start_time = time.time()
                        initialize()
            else:
                pygame.draw.rect(gameDisplay, colour, (x, y, w, h))
         
            draw_text(mmm_cream, "fonts/ARCADE.TTF", 50, text, display_width / 2, y + 32)
            return stay_on_start_screen
         
         
        def load_card_face(image_id):
            card = "./"+ "你今晚的噩夢" + "/" + "惡魔貓男"+"_%s.JPG" % image_id
            img = pygame.image.load(card)
            return img
         
         
        def load_card_back():
            card = "./"+"cardback"+"/"+"card_back2_2"+".JPG"
            img = pygame.image.load(card)
            return img
         
        def calculate_coord(index):
            y = int(index / 6)
            x = index - y * 6
            return [x, y]
         
         
        def load_images():
            for n, j in enumerate(concealed):
                card_coord = calculate_coord(n)
                if (j == 's') or (j == 'f'):
                    img = load_card_face(original[n])
                else:
                    img = load_card_back()
                gameDisplay.blit(img, (card_coord[0] * image_width, card_coord[1] * image_height))
         
         
        def identify_card(position_pressed):
            x_coord = int(position_pressed[0] / image_width)
            y_coord = int(position_pressed[1] / image_height)
            card = [x_coord, y_coord]
            return card
         
         
        def calculate_index(card_pos):
            return card_pos[1] * 6 + card_pos[0]
         
         
        def show_card(card_pos):
            if card_pos:
                concealed[calculate_index(card_pos)] = 's'
         
         
        def flip_card(card_pos):
            if card_pos:
                concealed[calculate_index(card_pos)] = 'f'
         
         
        def hide_card(card_pos):
            if card_pos:
                ind = calculate_index(card_pos)
                if concealed[ind] == 's':
                    concealed[ind] = original[ind]
         
         
        def check_same(card1, card2):
            if card1 and card2:
                return original[calculate_index(card1)] == original[calculate_index(card2)]
         
         
        def check_win():
            is_win = True
            for item in concealed:
                if isinstance(item, int):
                    is_win = False
            return is_win
         
             
        while run:
            ev = pygame.event.get()
            key = pygame.key.get_pressed()
            for event in ev:
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if start_screen:
                        if event.key == pygame.K_RETURN:
                            start_screen = False
                            # start_time = time.time()
                            # flag = 1
                            print("開始------")
                        elif event.key == pygame.K_ESCAPE:
                            run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    cnt = cnt + 1
                    card_flipped = identify_card(pygame.mouse.get_pos())
                    card_index = calculate_index(card_flipped)
                    if concealed[card_index] != 's' and concealed[card_index] != 'f' and not start_screen:
                        if not has_first:
                            first_flip_time = time.time()
                            first_card = card_flipped
                            show_card(card_flipped)
                            is_first_flip = False
                            has_first = True
                        elif not has_second:
                            second_flip_time = time.time()
                            second_card = card_flipped
                            show_card(card_flipped)
                            has_second = True
         
            if has_first and has_second and check_same(first_card, second_card):
                flip_card(first_card)
                flip_card(second_card)
            if has_second and (time.time() - second_flip_time > show_time):
                hide_card(second_card)
                hide_card(first_card)
                has_first = has_second = False
         
            win = check_win()
         
            # if cnt > 2 and cnt < 4:
            #     win = True
            mouse = pygame.mouse.get_pos()
            if start_screen:
                # print("遊戲開始！")
                flag = 1
                start_time = time.time()
                start_screen = draw_start_screen(mouse)
            elif not win:
                load_images()
            else:
                # print("win")
                if flag == 1:
                    # print("sta: ", start_time)
                    usertime = time.time() - start_time   #计算用时
                    print("win: ", win, start_time)
                    flag = 0
                restart = draw_win_screen(mouse)
            pygame.display.update()
            clock.tick(60)  
        pygame.quit()
        #quit()
        
        
        
######################################自訂遊戲實體######################################
    def game4(self):    
        
        import pygame
        import time
        from random import shuffle
        from PIL import Image
        
        pygame.init()
         
        display_width = 900
        display_height = 600
        image_width = 150
        image_height = 150
        level = 1
         
        start_time = time.time()
        flag = 1
         
        black = (0, 0, 0)
        white = (255, 255, 255)
        red = (255, 0, 0)
        green = (0, 200, 0)
        bright_red = (255, 0, 0)
        bright_green = (0, 255, 0)
        mmm_orange = (255, 136, 17)
        mmm_orange_lite = (255, 157, 60)
        mmm_yellow = (244, 208, 111)
        mmm_blue = (157, 217, 210)
        mmm_cream = (255, 248, 240)
        mmm_purple = (57, 47, 90)
        mmm_purple_lite = (93, 84, 120)
         
        gameDisplay = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('記憶對對碰')
        clock = pygame.time.Clock()
         
        win = False
        run = True
        original = []
        cnt = 0
        usertime = 0
        start_time = 0
        # 初始化
        for i in range(12):
            original.append(i)
            original.append(i)
         
        shuffle(original)
         
        concealed = list(original)
        flipped = []
        found = []
        missed = 0
        first_card = []
        has_first = False
        has_second = False
        second_card = []
        first_flip_time = 0
        second_flip_time = 0
        show_time = 1
        game_start_time = 0
        start_screen = True
         
         
        def initialize():
            print("重新開始}}}}}}}}}}}}}}}}}}")
            # 删除全局变量
            global win, run, original, concealed, flipped, found, missed, first_card, has_first, has_second, second_card
            global first_flip_time, second_flip_time, show_time, game_start_time, start_screen
            win = False
            run = True
            original = []
         
            for i in range(12):
                original.append(i)
                original.append(i)
         
            shuffle(original)
         
            concealed = list(original)
            flipped = []
            found = []
            missed = 0
            first_card = []
            has_first = False
            has_second = False
            second_card = []
            first_flip_time = 0
            second_flip_time = 0
            show_time = 1
            game_start_time = 0
            start_screen = True
         
        def text_objects(text, font, colour):
            text_surface = font.render(text, True, colour)
            return text_surface, text_surface.get_rect()
         
         
        def draw_start_screen(mouse):
            gameDisplay.fill(mmm_purple)
            #draw_text(mmm_cream, "fonts/ARCADE.TTF", 100, "WECHAT", (display_width / 2), 120)
            draw_text(mmm_cream, "fonts/ARCADE.TTF", 58, "MEMORY-MATCH", (display_width / 2), 230)
            #draw_text(mmm_cream, "fonts/ARCADE.TTF", 35, "Medium", (display_width / 2) + 26, 300)
            #draw_text(mmm_cream, "fonts/ARCADE.TTF", 35, "Level feature coming soon", (display_width / 2) + 26, 370)
            start = draw_interactive_button(mouse, 300, 50, 485, mmm_orange, mmm_orange_lite, "START", False)
            #pygame.draw.circle(gameDisplay, mmm_cream, (int(display_width / 2) - 56, 295), 9, 3)
            #select_level()
            return start
         
         
        #def select_level():
         #   h = 295
          #  pygame.draw.circle(gameDisplay, mmm_cream, (int(display_width / 2) - 56, h), 2)
         
         
        def draw_win_screen(mouse):
            global win
            win = False
            gameDisplay.fill(mmm_purple)
            draw_text(mmm_yellow, "fonts/ARCADE.TTF", 100, "Congrats!", (display_width / 2), 200)
            draw_text(mmm_yellow, "fonts/ARCADE.TTF", 30, "You found all the pieces", (display_width / 2), 270)
            draw_text(mmm_yellow, "fonts/ARCADE.TTF", 30, "Your time is : %ds" % int(usertime) , (display_width / 2), 270  + 100)
            draw_text(mmm_yellow, "fonts/ARCADE.TTF", 30, "END" , (display_width / 2), 270  + 150)
            #restart = draw_interactive_button(mouse, 200, 50, 485, mmm_orange, mmm_orange_lite, "END", True)
            #return restart
         
         
        def draw_text(colour, font, size, content, center_x, center_y):
            text = pygame.font.Font(font, size)
            text_surf, text_rect = text_objects(content, text, colour)
            text_rect.center = (center_x, center_y)
            gameDisplay.blit(text_surf, text_rect)
         
         
        def draw_interactive_button(mouse, w, h, y, colour, secondary_colour, text, restart):
            stay_on_start_screen = True
            x = display_width / 2 - w / 2
            click = pygame.mouse.get_pressed()
            if x + w > mouse[0] > x and y + h > mouse[1] > y:
                pygame.draw.rect(gameDisplay, secondary_colour, (x, y, w, h))
                if click[0] == 1:
                    print("重新開始-----139")
                    flag = 1
                    stay_on_start_screen = False
                    if restart:
                        global  start_time
                        start_time = time.time()
                        initialize()
            else:
                pygame.draw.rect(gameDisplay, colour, (x, y, w, h))
         
            draw_text(mmm_cream, "fonts/ARCADE.TTF", 50, text, display_width / 2, y + 32)
            return stay_on_start_screen
         
         
        def load_card_face(image_id):
            card = "./"+input_1+"/"+input_1+"_%s.JPG" % image_id
            img = pygame.image.load(card)
            return img
         
         
        def load_card_back():
            card = "./cardback/card_back2_2.JPG"
            img = pygame.image.load(card)
            return img
         
        def calculate_coord(index):
            y = int(index / 6)
            x = index - y * 6
            return [x, y]
         
         
        def load_images():
            for n, j in enumerate(concealed):
                card_coord = calculate_coord(n)
                if (j == 's') or (j == 'f'):
                    img = load_card_face(original[n])
                else:
                    img = load_card_back()
                gameDisplay.blit(img, (card_coord[0] * image_width, card_coord[1] * image_height))
         
         
        def identify_card(position_pressed):
            x_coord = int(position_pressed[0] / image_width)
            y_coord = int(position_pressed[1] / image_height)
            card = [x_coord, y_coord]
            return card
         
         
        def calculate_index(card_pos):
            return card_pos[1] * 6 + card_pos[0]
         
         
        def show_card(card_pos):
            if card_pos:
                concealed[calculate_index(card_pos)] = 's'
         
         
        def flip_card(card_pos):
            if card_pos:
                concealed[calculate_index(card_pos)] = 'f'
         
         
        def hide_card(card_pos):
            if card_pos:
                ind = calculate_index(card_pos)
                if concealed[ind] == 's':
                    concealed[ind] = original[ind]
         
         
        def check_same(card1, card2):
            if card1 and card2:
                return original[calculate_index(card1)] == original[calculate_index(card2)]
         
         
        def check_win():
            is_win = True
            for item in concealed:
                if isinstance(item, int):
                    is_win = False
            return is_win
         
         
         
        # 用
        while run:
            ev = pygame.event.get()
            key = pygame.key.get_pressed()
            for event in ev:
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if start_screen:
                        if event.key == pygame.K_RETURN:
                            start_screen = False
                            # start_time = time.time()
                            # flag = 1
                            print("開始------")
                        elif event.key == pygame.K_ESCAPE:
                            run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    cnt = cnt + 1
                    card_flipped = identify_card(pygame.mouse.get_pos())
                    card_index = calculate_index(card_flipped)
                    if concealed[card_index] != 's' and concealed[card_index] != 'f' and not start_screen:
                        if not has_first:
                            first_flip_time = time.time()
                            first_card = card_flipped
                            show_card(card_flipped)
                            is_first_flip = False
                            has_first = True
                        elif not has_second:
                            second_flip_time = time.time()
                            second_card = card_flipped
                            show_card(card_flipped)
                            has_second = True
         
            if has_first and has_second and check_same(first_card, second_card):
                flip_card(first_card)
                flip_card(second_card)
            if has_second and (time.time() - second_flip_time > show_time):
                hide_card(second_card)
                hide_card(first_card)
                has_first = has_second = False
         
            win = check_win()
         
            # if cnt > 2 and cnt < 4:
            #     win = True
            mouse = pygame.mouse.get_pos()
            if start_screen:
                # print("遊戲開始！")
                flag = 1
                start_time = time.time()
                start_screen = draw_start_screen(mouse)
            elif not win:
                load_images()
            else:
                # print("win")
                if flag == 1:
                    # print("sta: ", start_time)
                    usertime = time.time() - start_time   #计算用时
                    print("win: ", win, start_time)
                    flag = 0
                restart = draw_win_screen(mouse)
         
            pygame.display.update()
            clock.tick(60)
         
        pygame.quit()
        #quit()
        
######################################韓國瑜############################################

    def game2(self):
        
        import pygame
        import time
        from random import shuffle
        from PIL import Image
        pygame.init()
        file=r'0803韓國瑜桃園造勢高唱夜襲.mp3'
        pygame.mixer.init()
        track = pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        display_width = 900
        display_height = 600
        image_width = 150
        image_height = 150
        level = 1
         
        start_time = time.time()
        flag = 1
         
        black = (0, 0, 0)
        white = (255, 255, 255)
        red = (255, 0, 0)
        green = (0, 200, 0)
        bright_red = (255, 0, 0)
        bright_green = (0, 255, 0)
        mmm_orange = (255, 136, 17)
        mmm_orange_lite = (255, 157, 60)
        mmm_yellow = (244, 208, 111)
        mmm_blue = (157, 217, 210)
        mmm_cream = (255, 248, 240)
        mmm_purple = (57, 47, 90)
        mmm_purple_lite = (93, 84, 120)
         
        gameDisplay = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('記憶對對碰')
        clock = pygame.time.Clock()
         
        win = False
        run = True
        original = []
        cnt = 0
        usertime = 0
        start_time = 0
        # 初始化
        for i in range(12):
            original.append(i)
            original.append(i)
         
        shuffle(original)
         
        concealed = list(original)
        flipped = []
        found = []
        missed = 0
        first_card = []
        has_first = False
        has_second = False
        second_card = []
        first_flip_time = 0
        second_flip_time = 0
        show_time = 1
        game_start_time = 0
        start_screen = True
         
         
        def initialize():
            print("重新開始}}}}}}}}}}}}}}}}}}")
            # 刪除變量
            global win, run, original, concealed, flipped, found, missed, first_card, has_first, has_second, second_card
            global first_flip_time, second_flip_time, show_time, game_start_time, start_screen
            win = False
            run = True
            original = []
         
            for i in range(12):
                original.append(i)
                original.append(i)
         
            shuffle(original)
         
            concealed = list(original)
            flipped = []
            found = []
            missed = 0
            first_card = []
            has_first = False
            has_second = False
            second_card = []
            first_flip_time = 0
            second_flip_time = 0
            show_time = 1
            game_start_time = 0
            start_screen = True
         
        def text_objects(text, font, colour):
            text_surface = font.render(text, True, colour)
            return text_surface, text_surface.get_rect()
         
         
        def draw_start_screen(mouse):
            gameDisplay.fill(mmm_purple)
            #draw_text(mmm_cream, "fonts/ARCADE.TTF", 100, "WECHAT", (display_width / 2), 120)
            draw_text(mmm_cream, "fonts/ARCADE.TTF", 58, "MEMORY-MATCH", (display_width / 2), 230)
            #draw_text(mmm_cream, "fonts/ARCADE.TTF", 35, "Medium", (display_width / 2) + 26, 300)
            #draw_text(mmm_cream, "fonts/ARCADE.TTF", 35, "Level feature coming soon", (display_width / 2) + 26, 370)
            start = draw_interactive_button(mouse, 300, 50, 485, mmm_orange, mmm_orange_lite, "START", False)
            #pygame.draw.circle(gameDisplay, mmm_cream, (int(display_width / 2) - 56, 295), 9, 3)
            #select_level()
            return start
         
         
        #def select_level():
         #   h = 295
         #   pygame.draw.circle(gameDisplay, mmm_cream, (int(display_width / 2) - 56, h), 2)
         
         
        def draw_win_screen(mouse):
            global win
            win = False
            gameDisplay.fill(mmm_purple)
            draw_text(mmm_yellow, "fonts/ARCADE.TTF", 100, "Congrats!", (display_width / 2), 200)
            draw_text(mmm_yellow, "fonts/ARCADE.TTF", 30, "You found all the pieces", (display_width / 2), 270)
            draw_text(mmm_yellow, "fonts/ARCADE.TTF", 30, "Your time is : %ds" % int(usertime) , (display_width / 2), 270  + 100)
            draw_text(mmm_yellow, "fonts/ARCADE.TTF", 30, "END" , (display_width / 2), 270  + 150)
            #restart = draw_interactive_button(mouse, 200, 50, 485, mmm_orange, mmm_orange_lite, "END", True)
            #return restart
         
         
        def draw_text(colour, font, size, content, center_x, center_y):
            text = pygame.font.Font(font, size)
            text_surf, text_rect = text_objects(content, text, colour)
            text_rect.center = (center_x, center_y)
            gameDisplay.blit(text_surf, text_rect)
         
         
        def draw_interactive_button(mouse, w, h, y, colour, secondary_colour, text, restart):
            stay_on_start_screen = True
            x = display_width / 2 - w / 2
            click = pygame.mouse.get_pressed()
            if x + w > mouse[0] > x and y + h > mouse[1] > y:
                pygame.draw.rect(gameDisplay, secondary_colour, (x, y, w, h))
                if click[0] == 1:
                    print("重新開始-----139")
                    flag = 1
                    stay_on_start_screen = False
                    if restart:
                        global  start_time
                        start_time = time.time()
                        initialize()
            else:
                pygame.draw.rect(gameDisplay, colour, (x, y, w, h))
         
            draw_text(mmm_cream, "fonts/ARCADE.TTF", 50, text, display_width / 2, y + 32)
            return stay_on_start_screen
         
         
        def load_card_face(image_id):
            card = "./"+ "非韓不投" + "/" + "韓國瑜"+"_%s.JPG" % image_id
            img = pygame.image.load(card)
            return img
         
         
        def load_card_back():
            card = "./"+"cardback"+"/"+"card_back2_2"+".JPG"
            img = pygame.image.load(card)
            return img
         
        def calculate_coord(index):
            y = int(index / 6)
            x = index - y * 6
            return [x, y]
         
         
        def load_images():
            for n, j in enumerate(concealed):
                card_coord = calculate_coord(n)
                if (j == 's') or (j == 'f'):
                    img = load_card_face(original[n])
                else:
                    img = load_card_back()
                gameDisplay.blit(img, (card_coord[0] * image_width, card_coord[1] * image_height))
         
         
        def identify_card(position_pressed):
            x_coord = int(position_pressed[0] / image_width)
            y_coord = int(position_pressed[1] / image_height)
            card = [x_coord, y_coord]
            return card
         
         
        def calculate_index(card_pos):
            return card_pos[1] * 6 + card_pos[0]
         
         
        def show_card(card_pos):
            if card_pos:
                concealed[calculate_index(card_pos)] = 's'
         
         
        def flip_card(card_pos):
            if card_pos:
                concealed[calculate_index(card_pos)] = 'f'
         
         
        def hide_card(card_pos):
            if card_pos:
                ind = calculate_index(card_pos)
                if concealed[ind] == 's':
                    concealed[ind] = original[ind]
         
         
        def check_same(card1, card2):
            if card1 and card2:
                return original[calculate_index(card1)] == original[calculate_index(card2)]
         
         
        def check_win():
            is_win = True
            for item in concealed:
                if isinstance(item, int):
                    is_win = False
            return is_win
         
             
        while run:
            ev = pygame.event.get()
            key = pygame.key.get_pressed()
            for event in ev:
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if start_screen:
                        if event.key == pygame.K_RETURN:
                            start_screen = False
                            # start_time = time.time()
                            # flag = 1
                            print("開始------")
                        elif event.key == pygame.K_ESCAPE:
                            run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    cnt = cnt + 1
                    card_flipped = identify_card(pygame.mouse.get_pos())
                    card_index = calculate_index(card_flipped)
                    if concealed[card_index] != 's' and concealed[card_index] != 'f' and not start_screen:
                        if not has_first:
                            first_flip_time = time.time()
                            first_card = card_flipped
                            show_card(card_flipped)
                            is_first_flip = False
                            has_first = True
                        elif not has_second:
                            second_flip_time = time.time()
                            second_card = card_flipped
                            show_card(card_flipped)
                            has_second = True
         
            if has_first and has_second and check_same(first_card, second_card):
                flip_card(first_card)
                flip_card(second_card)
            if has_second and (time.time() - second_flip_time > show_time):
                hide_card(second_card)
                hide_card(first_card)
                has_first = has_second = False
         
            win = check_win()
         
            # if cnt > 2 and cnt < 4:
            #     win = True
            mouse = pygame.mouse.get_pos()
            if start_screen:
                # print("遊戲開始！")
                flag = 1
                start_time = time.time()
                start_screen = draw_start_screen(mouse)
            elif not win:
                load_images()
            else:
                # print("win")
                if flag == 1:
                    # print("sta: ", start_time)
                    usertime = time.time() - start_time   #计算用时
                    print("win: ", win, start_time)
                    flag = 0
                restart = draw_win_screen(mouse)
            pygame.display.update()
            clock.tick(60)  
        pygame.quit()
        #quit()
        
        
        
        
#######################################貓咪##########################################




    def game1(self):    
        
        import pygame
        import time
        from random import shuffle
        from PIL import Image
        
        pygame.init()
         
        display_width = 900
        display_height = 600
        image_width = 150
        image_height = 150
        level = 1
         
        start_time = time.time()
        flag = 1
         
        black = (0, 0, 0)
        white = (255, 255, 255)
        red = (255, 0, 0)
        green = (0, 200, 0)
        bright_red = (255, 0, 0)
        bright_green = (0, 255, 0)
        mmm_orange = (255, 136, 17)
        mmm_orange_lite = (255, 157, 60)
        mmm_yellow = (244, 208, 111)
        mmm_blue = (157, 217, 210)
        mmm_cream = (255, 248, 240)
        mmm_purple = (57, 47, 90)
        mmm_purple_lite = (93, 84, 120)
         
        gameDisplay = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('記憶對對碰')
        clock = pygame.time.Clock()
         
        win = False
        run = True
        original = []
        cnt = 0
        usertime = 0
        start_time = 0
        # 初始化
        for i in range(12):
            original.append(i)
            original.append(i)
         
        shuffle(original)
         
        concealed = list(original)
        flipped = []
        found = []
        missed = 0
        first_card = []
        has_first = False
        has_second = False
        second_card = []
        first_flip_time = 0
        second_flip_time = 0
        show_time = 1
        game_start_time = 0
        start_screen = True
         
         
        def initialize():
            print("重新開始}}}}}}}}}}}}}}}}}}")
            # 删除全局变量
            global win, run, original, concealed, flipped, found, missed, first_card, has_first, has_second, second_card
            global first_flip_time, second_flip_time, show_time, game_start_time, start_screen
            win = False
            run = True
            original = []
         
            for i in range(12):
                original.append(i)
                original.append(i)
         
            shuffle(original)
         
            concealed = list(original)
            flipped = []
            found = []
            missed = 0
            first_card = []
            has_first = False
            has_second = False
            second_card = []
            first_flip_time = 0
            second_flip_time = 0
            show_time = 1
            game_start_time = 0
            start_screen = True
         
        def text_objects(text, font, colour):
            text_surface = font.render(text, True, colour)
            return text_surface, text_surface.get_rect()
         
         
        def draw_start_screen(mouse):
            gameDisplay.fill(mmm_purple)
            #draw_text(mmm_cream, "fonts/ARCADE.TTF", 100, "WECHAT", (display_width / 2), 120)
            draw_text(mmm_cream, "fonts/ARCADE.TTF", 58, "MEMORY-MATCH", (display_width / 2), 230)
            #draw_text(mmm_cream, "fonts/ARCADE.TTF", 35, "Medium", (display_width / 2) + 26, 300)
            #draw_text(mmm_cream, "fonts/ARCADE.TTF", 35, "Level feature coming soon", (display_width / 2) + 26, 370)
            start = draw_interactive_button(mouse, 300, 50, 485, mmm_orange, mmm_orange_lite, "START", False)
            #pygame.draw.circle(gameDisplay, mmm_cream, (int(display_width / 2) - 56, 295), 9, 3)
            #select_level()
            return start
         
         
        #def select_level():
         #   h = 295
          #  pygame.draw.circle(gameDisplay, mmm_cream, (int(display_width / 2) - 56, h), 2)
         
         
        def draw_win_screen(mouse):
            global win
            win = False
            gameDisplay.fill(mmm_purple)
            draw_text(mmm_yellow, "fonts/ARCADE.TTF", 100, "Congrats!", (display_width / 2), 200)
            draw_text(mmm_yellow, "fonts/ARCADE.TTF", 30, "You found all the pieces", (display_width / 2), 270)
            draw_text(mmm_yellow, "fonts/ARCADE.TTF", 30, "Your time is : %ds" % int(usertime) , (display_width / 2), 270  + 100)
            draw_text(mmm_yellow, "fonts/ARCADE.TTF", 30, "END" , (display_width / 2), 270  + 150)
            #restart = draw_interactive_button(mouse, 200, 50, 485, mmm_orange, mmm_orange_lite, "END", True)
            #return restart
         
         
        def draw_text(colour, font, size, content, center_x, center_y):
            text = pygame.font.Font(font, size)
            text_surf, text_rect = text_objects(content, text, colour)
            text_rect.center = (center_x, center_y)
            gameDisplay.blit(text_surf, text_rect)
         
         
        def draw_interactive_button(mouse, w, h, y, colour, secondary_colour, text, restart):
            stay_on_start_screen = True
            x = display_width / 2 - w / 2
            click = pygame.mouse.get_pressed()
            if x + w > mouse[0] > x and y + h > mouse[1] > y:
                pygame.draw.rect(gameDisplay, secondary_colour, (x, y, w, h))
                if click[0] == 1:
                    print("重新開始-----139")
                    flag = 1
                    stay_on_start_screen = False
                    if restart:
                        global  start_time
                        start_time = time.time()
                        initialize()
            else:
                pygame.draw.rect(gameDisplay, colour, (x, y, w, h))
         
            draw_text(mmm_cream, "fonts/ARCADE.TTF", 50, text, display_width / 2, y + 32)
            return stay_on_start_screen
         
         
        def load_card_face(image_id):
            card = "./bundle2/img%s.JPG" % image_id
            img = pygame.image.load(card)
            return img
         
         
        def load_card_back():
            card = "./cardback/card_back2_2.JPG"
            img = pygame.image.load(card)
            return img
         
        def calculate_coord(index):
            y = int(index / 6)
            x = index - y * 6
            return [x, y]
         
         
        def load_images():
            for n, j in enumerate(concealed):
                card_coord = calculate_coord(n)
                if (j == 's') or (j == 'f'):
                    img = load_card_face(original[n])
                else:
                    img = load_card_back()
                gameDisplay.blit(img, (card_coord[0] * image_width, card_coord[1] * image_height))
         
         
        def identify_card(position_pressed):
            x_coord = int(position_pressed[0] / image_width)
            y_coord = int(position_pressed[1] / image_height)
            card = [x_coord, y_coord]
            return card
         
         
        def calculate_index(card_pos):
            return card_pos[1] * 6 + card_pos[0]
         
         
        def show_card(card_pos):
            if card_pos:
                concealed[calculate_index(card_pos)] = 's'
         
         
        def flip_card(card_pos):
            if card_pos:
                concealed[calculate_index(card_pos)] = 'f'
         
         
        def hide_card(card_pos):
            if card_pos:
                ind = calculate_index(card_pos)
                if concealed[ind] == 's':
                    concealed[ind] = original[ind]
         
         
        def check_same(card1, card2):
            if card1 and card2:
                return original[calculate_index(card1)] == original[calculate_index(card2)]
         
         
        def check_win():
            is_win = True
            for item in concealed:
                if isinstance(item, int):
                    is_win = False
            return is_win
         
         
         
        # 用
        while run:
            ev = pygame.event.get()
            key = pygame.key.get_pressed()
            for event in ev:
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if start_screen:
                        if event.key == pygame.K_RETURN:
                            start_screen = False
                            # start_time = time.time()
                            # flag = 1
                            print("開始------")
                        elif event.key == pygame.K_ESCAPE:
                            run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    cnt = cnt + 1
                    card_flipped = identify_card(pygame.mouse.get_pos())
                    card_index = calculate_index(card_flipped)
                    if concealed[card_index] != 's' and concealed[card_index] != 'f' and not start_screen:
                        if not has_first:
                            first_flip_time = time.time()
                            first_card = card_flipped
                            show_card(card_flipped)
                            is_first_flip = False
                            has_first = True
                        elif not has_second:
                            second_flip_time = time.time()
                            second_card = card_flipped
                            show_card(card_flipped)
                            has_second = True
         
            if has_first and has_second and check_same(first_card, second_card):
                flip_card(first_card)
                flip_card(second_card)
            if has_second and (time.time() - second_flip_time > show_time):
                hide_card(second_card)
                hide_card(first_card)
                has_first = has_second = False
         
            win = check_win()
         
            # if cnt > 2 and cnt < 4:
            #     win = True
            mouse = pygame.mouse.get_pos()
            if start_screen:
                # print("遊戲開始！")
                flag = 1
                start_time = time.time()
                start_screen = draw_start_screen(mouse)
            elif not win:
                load_images()
            else:
                # print("win")
                if flag == 1:
                    # print("sta: ", start_time)
                    usertime = time.time() - start_time   #计算用时
                    print("win: ", win, start_time)
                    flag = 0
                restart = draw_win_screen(mouse)
         
            pygame.display.update()
            clock.tick(60)
         
        pygame.quit()
        #quit()
        
        
#########################################介面部分#########################################



    def init_ui(self): 
        self.setFixedSize(960,700) 
        self.main_widget = QtWidgets.QWidget() # 窗口主部件 
        self.main_layout = QtWidgets.QGridLayout() # 主部件的網格布局 
        self.main_widget.setLayout(self.main_layout) # 設置窗口主部件布局為網格布局 
        self.left_widget = QtWidgets.QWidget() # 左側部件
        self.left_widget.setObjectName('left_widget') 
    
        self.left_layout = QtWidgets.QGridLayout() # 創建左側部件的網格布局層 
        self.left_widget.setLayout(self.left_layout) # 設置左側部件布局為網格
        self.right_widget = QtWidgets.QWidget() #右側部件 
        self.right_widget.setObjectName('right_widget') 
        self.right_layout = QtWidgets.QGridLayout() 
        self.right_widget.setLayout(self.right_layout) # 設置右側部件布局為網格 
        self.main_layout.addWidget(self.left_widget,0,0,12,2) # 左側部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget,0,2,12,10) # 右側部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget) # 設置窗口主部件
        self.left_close = QtWidgets.QPushButton("") # 關閉按钮
        self.left_visit = QtWidgets.QPushButton("") # 空白按钮
        self.left_mini = QtWidgets.QPushButton("") # 最小化按钮
         
        self.left_label_1 = QtWidgets.QPushButton("遊戲介紹")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("創作理念")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("分工表")
        self.left_label_3.setObjectName('left_label')
         
       ##########################################按鈕內容設定######################################
        def open_lb1():
            webbrowser.open("https://docs.google.com/document/d/1-ze_6qM6Dt25SODTpfgSvv_S-XZ5WdBBgbrNOZQdTNM/edit")
        def open_lb3():
            webbrowser.open("https://youtu.be/OZNGruHcTBA")
        def open_lb4():
            webbrowser.open("https://docs.google.com/document/d/1-wCEhQkctOT9fa9McrOiC1q69TTK-dKRrn6leSUlRkM/edit?fbclid=IwAR18C8EkN4w8vERyebMFVz95kT8JfLHXWumApm6uMcr6C-fxGGcGHCXd6DU")
        def open_lb6():
            webbrowser.open("https://docs.google.com/document/d/101tFsjyj2Ks-3mxvkWEYazIvy-YgguO37t4YsbY_vwk/edit?fbclid=IwAR0_CqEy5le3kHt7v1qRWsNe6mt5VXv8yn7SLITuKFTIZ17nj0KXYPifKX8")
        def open_lb7():
            webbrowser.open("https://docs.google.com/spreadsheets/d/1-jhbNj5TFrxJF_jfOEgxWSlaaj18cTzgbwXWtBixQNs/edit?fbclid=IwAR291bBF5h6toE8ktlbZL7AQsPVywhV5okU4j1UoeEkwV2wXMNv4GxwYylE")
        def open_lb8():
            webbrowser.open('http://www.google.com')
        
        
        ##########################################左欄按鍵安裝###############################################
         
        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.spinner',color='blue'),"如何遊玩")
        self.left_button_1.setObjectName('left_button')
        self.left_button_1.clicked.connect(open_lb1)
        
        ##self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.legal',color='red'),"各式規則")
        ##self.left_button_2.setObjectName('left_button')
        
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.film',color='yellow'),"DEMO影片")
        self.left_button_3.setObjectName('left_button')
        self.left_button_3.clicked.connect(open_lb3)
        
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.heart',color='pink'),"創意構想")
        self.left_button_4.setObjectName('left_button')
        self.left_button_4.clicked.connect(open_lb4)
        
        ##self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.star',color='blue'),"ML應用")
        ##self.left_button_5.setObjectName('left_button')
        
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.home',color='orange'),"實作部分")
        self.left_button_6.setObjectName('left_button')
        self.left_button_6.clicked.connect(open_lb6)
        
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.home',color='white'),"組員名單")
        self.left_button_7.setObjectName('left_button')
        self.left_button_7.clicked.connect(open_lb7)
        
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.comment',color='white'),"意見回饋")
        self.left_button_8.setObjectName('left_button')
        self.left_button_8.clicked.connect(open_lb8)
        
        ##self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question',color='white'),"遇到问题")
        ##self.left_button_9.setObjectName('left_button')
        
        self.left_xxx = QtWidgets.QPushButton(" ")


 
        self.left_layout.addWidget(self.left_mini, 0, 0,1,1)
        self.left_layout.addWidget(self.left_close, 0, 2,1,1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1,1,0,1,3)
        self.left_layout.addWidget(self.left_button_1, 2, 0,1,3)
        #self.left_layout.addWidget(self.left_button_2, 3, 0,1,3)
        self.left_layout.addWidget(self.left_button_3, 4, 0,1,3)
        self.left_layout.addWidget(self.left_label_2, 5, 0,1,3)
        self.left_layout.addWidget(self.left_button_4, 6, 0,1,3)
        #self.left_layout.addWidget(self.left_button_5, 7, 0,1,3)
        self.left_layout.addWidget(self.left_button_6, 8, 0,1,3)
        self.left_layout.addWidget(self.left_label_3, 9, 0,1,3)
        self.left_layout.addWidget(self.left_button_7, 10, 0,1,3)
        self.left_layout.addWidget(self.left_button_8, 11, 0,1,3)
        #self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)
        
################################################右欄功能#################################################################3
        
        self.right_bar_widget = QtWidgets.QWidget() # 右侧顶部搜索框部件
        self.right_bar_layout = QtWidgets.QGridLayout() # 右侧顶部搜索框网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout)
        #self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' '+'搜尋下載圖片 ')
        #self.search_icon.setFont(qtawesome.font('fa', 16))
        #關鍵字
        #self.right_bar_widget_search_input = QtWidgets.QLineEdit()
        #word = QLineEdit.text()
        #self.right_bar_widget_search_input.setPlaceholderText("輸入關鍵字")
		#self.right_bar_widget_search_input.setPlac
        
         
        #self.right_bar_layout.addWidget(self.search_icon,0,0,1,1)
        #self.right_bar_layout.addWidget(self.right_bar_widget_search_input,0,1,1,8)
         
        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)
        self.right_recommend_label = QtWidgets.QLabel("ㄏ勝ㄟ喔")
        self.right_recommend_label.setObjectName('right_lable')
         
        self.right_recommend_widget = QtWidgets.QWidget() # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout() # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)
#---------------遊戲選擇------------------------------------------------------------------         
        self.recommend_button_1 = QtWidgets.QToolButton()
        self.recommend_button_1.setText("遊戲1") 
        self.recommend_button_1.setIcon(QtGui.QIcon('GUI_picture/catface.jpg')) 
        self.recommend_button_1.setIconSize(QtCore.QSize(150,150)) 
        self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon) 
        self.recommend_button_1.clicked.connect(self.game1) 
        
        self.recommend_button_2 = QtWidgets.QToolButton()
        self.recommend_button_2.setText("遊戲2")
        self.recommend_button_2.setIcon(QtGui.QIcon('GUI_picture/korea_fish.jpg'))
        self.recommend_button_2.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.recommend_button_2.clicked.connect(self.game2)

        self.recommend_button_3 = QtWidgets.QToolButton()
        self.recommend_button_3.setText("遊戲3")
        self.recommend_button_3.setIcon(QtGui.QIcon('GUI_picture/惡魔貓男.jpg'))
        self.recommend_button_3.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.recommend_button_3.clicked.connect(self.game3) 
        
        self.recommend_button_4 = QtWidgets.QToolButton()
        self.recommend_button_4.setText("遊戲4")
        self.recommend_button_4.setIcon(QtGui.QIcon('GUI_picture/自訂.jpg'))
        self.recommend_button_4.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.recommend_button_4.clicked.connect(self.game4) 
    
#--------------------------------------------------------------------------------------         
         
        self.right_recommend_layout.addWidget(self.recommend_button_1,0,0)
        self.right_recommend_layout.addWidget(self.recommend_button_2,0,1)
        self.right_recommend_layout.addWidget(self.recommend_button_3,1,0)
        self.right_recommend_layout.addWidget(self.recommend_button_4,1,1)
        
        self.right_layout.addWidget(self.right_recommend_label, 1, 0, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 2, 0, 2, 9)
        self.right_newsong_lable = QtWidgets.QLabel("蝦咪")
        self.right_newsong_lable.setObjectName('right_lable')
         
        self.right_playlist_lable = QtWidgets.QLabel("自訂遊戲")
        self.right_playlist_lable = QtWidgets.QPushButton("搜尋圖片以自訂主題")
        self.right_playlist_lable.setObjectName('right_lable')        
        self.right_playlist_lable.clicked.connect(self.spyder)
         
        self.right_newsong_widget = QtWidgets.QWidget() # 最新歌曲部件
        self.right_newsong_layout = QtWidgets.QGridLayout() # 最新歌曲部件网格布局
        self.right_newsong_widget.setLayout(self.right_newsong_layout)
         
###########################################公告欄連接部分#####################################################


        def nb1():
            a = open("打得好累.txt",'r',encoding="utf-8")
            text_1 = a.read()
            news_window = tk.Tk()
            news_window.title('打得好累')
            news_window.geometry("600x400")
            label_1 = tk.Label(news_window, text = "\n")
            label_2 = tk.Label(news_window,text = text_1)
            label_1.pack()
            label_2.pack()
            news_window.mainloop()
        
        def nb2():
            a = open("看了一堆.txt",'r',encoding="utf-8")
            text_1 = a.read()
            news_window = tk.Tk()
            news_window.title('看了一堆')
            news_window.geometry("600x400")
            label_1 = tk.Label(news_window, text = "\n")
            label_2 = tk.Label(news_window,text = text_1)
            label_1.pack()
            label_2.pack()
            news_window.mainloop()
        
        def nb3():
            a = open("韓導照片.txt",'r',encoding="utf-8")
            text_1 = a.read()
            news_window = tk.Tk()
            news_window.title('韓導照片')
            news_window.geometry("600x400")
            label_1 = tk.Label(news_window, text = "\n")
            label_2 = tk.Label(news_window,text = text_1)
            label_1.pack()
            label_2.pack()
            news_window.mainloop()
            
        def nb4():
            a = open("好不蘇服.txt",'r',encoding="utf-8")
            text_1 = a.read()
            news_window = tk.Tk()
            news_window.title('好不蘇服')
            news_window.geometry("600x400")
            label_1 = tk.Label(news_window, text = "\n")
            label_2 = tk.Label(news_window,text = text_1)
            label_1.pack()
            label_2.pack()
            news_window.mainloop()
        
        def nb5():
            a = open("我好想喝.txt",'r',encoding="utf-8")
            text_1 = a.read()
            news_window = tk.Tk()
            news_window.title('我好想喝')
            news_window.geometry("600x400")
            label_1 = tk.Label(news_window, text = "\n")
            label_2 = tk.Label(news_window,text = text_1)
            label_1.pack()
            label_2.pack()
            news_window.mainloop()
            
        def nb6():
            a = open("珍珠奶茶.txt",'r',encoding="utf-8")
            text_1 = a.read()
            news_window = tk.Tk()
            news_window.title('珍珠奶茶')
            news_window.geometry("600x400")
            label_1 = tk.Label(news_window, text = "\n")
            label_2 = tk.Label(news_window,text = text_1)
            label_1.pack()
            label_2.pack()
            news_window.mainloop()
                




#################################一堆有的沒的公告欄按鈕############################     

    
        self.newsong_button_1 = QtWidgets.QPushButton("打得好累")
        self.newsong_button_1.clicked.connect(nb1)
        
        self.newsong_button_2 = QtWidgets.QPushButton("看了一堆")
        self.newsong_button_2.clicked.connect(nb2)
        
        self.newsong_button_3 = QtWidgets.QPushButton("韓導照片")
        self.newsong_button_3.clicked.connect(nb3)
        
        self.newsong_button_4 = QtWidgets.QPushButton("好不蘇服")
        self.newsong_button_4.clicked.connect(nb4)
        
        self.newsong_button_5 = QtWidgets.QPushButton("我好想喝")
        self.newsong_button_5.clicked.connect(nb5)
        
        self.newsong_button_6 = QtWidgets.QPushButton("珍珠奶茶")
        self.newsong_button_6.clicked.connect(nb6)
       
        self.right_newsong_layout.addWidget(self.newsong_button_1,0,1,)
        self.right_newsong_layout.addWidget(self.newsong_button_2, 1, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_3, 2, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_4, 3, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_5, 4, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_6, 5, 1, )
        self.right_playlist_widget = QtWidgets.QWidget() # 播放歌单部件
        self.right_playlist_layout = QtWidgets.QGridLayout() # 播放歌单网格布局
        self.right_playlist_widget.setLayout(self.right_playlist_layout)
        
########################################右側自訂按紐####################################   
     
        self.playlist_button_1 = QtWidgets.QToolButton()
        self.playlist_button_1.setText("這邊放自訂")
        self.playlist_button_1.setIcon(QtGui.QIcon('./p1.jpg'))
        self.playlist_button_1.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
         
        self.playlist_button_2 = QtWidgets.QToolButton()
        self.playlist_button_2.setText("我思考一下")
        self.playlist_button_2.setIcon(QtGui.QIcon('./p2.jpg'))
        self.playlist_button_2.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
         
         
        self.right_playlist_layout.addWidget(self.playlist_button_1,0,0)
        self.right_playlist_layout.addWidget(self.playlist_button_2, 0, 1)


        self.right_layout.addWidget(self.right_newsong_lable, 4, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_lable, 4, 5, 1, 4)
        self.right_layout.addWidget(self.right_newsong_widget, 5, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_widget, 5, 5, 1, 4)
        
        self.right_process_bar = QtWidgets.QProgressBar() 
        self.right_process_bar.setValue(49)
        self.right_process_bar.setFixedHeight(3) 
        self.right_process_bar.setTextVisible(False) 
         
        self.right_playconsole_widget = QtWidgets.QWidget() 
        self.right_playconsole_layout = QtWidgets.QGridLayout() 
        self.right_playconsole_widget.setLayout(self.right_playconsole_layout)
         

         
        self.right_layout.addWidget(self.right_process_bar, 9, 0, 1, 9)
        self.right_layout.addWidget(self.right_playconsole_widget, 10, 0, 1, 9)
        
        
        self.left_close.setFixedSize(15,15) # 設置按鈕
        self.left_visit.setFixedSize(15, 15) 
        self.left_mini.setFixedSize(15, 15)
        
        self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
          QPushButton{border:none;color:white;}
          QPushButton#left_label{
            border:none;
            border-bottom:1px solid white;
            font-size:18px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
          }
          QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')
        self.right_widget.setStyleSheet('''
          QWidget#right_widget{
            color:#232C51;
            background:white;
            border-top:1px solid darkGray;
            border-bottom:1px solid darkGray;
            border-right:1px solid darkGray;
            border-top-right-radius:10px;
            border-bottom-right-radius:10px;
          }
          QLabel#right_lable{
            border:none;
            font-size:16px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
          }
        ''')
        self.right_recommend_widget.setStyleSheet(
          '''
            QToolButton{border:none;}
            QToolButton:hover{border-bottom:2px solid #F76677;}
          ''')
        self.right_playlist_widget.setStyleSheet(
          '''
            QToolButton{border:none;}
            QToolButton:hover{border-bottom:2px solid #F76677;}
          ''')
        self.right_newsong_widget.setStyleSheet('''
          QPushButton{
            border:none;
            color:gray;
            font-size:12px;
            height:40px;
            padding-left:5px;
            padding-right:10px;
            text-align:left;
          }
          QPushButton:hover{
            color:black;
            border:1px solid #F3F3F5;
            border-radius:10px;
            background:LightGray;
          }
        ''')
        self.right_process_bar.setStyleSheet('''
          QProgressBar::chunk {
            background-color: #F76677;
          }
        ''')
         
        self.right_playconsole_widget.setStyleSheet('''
          QPushButton{
            border:none;
          }
        ''')
        self.setWindowOpacity(0.9) # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
       #self.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框
       
      
        self.main_layout.setSpacing(0)
        

         
def main(): 
    
    app = QtWidgets.QApplication(sys.argv)  
    gui = MainUi()   
    gui.show()        
    sys.exit(app.exec_()) 
if __name__ == '__main__': 
    main()
