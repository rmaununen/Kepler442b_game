'''
Kepler-442b
Author: Rudolf M.
Created for Python Programming competition
April-May 2020
'''

import pygame
import random
import math
from image_loader import*
from sound_loader import*
from initial_values import*

t = pygame.time.Clock()
pygame.init()
win = pygame.display.set_mode((720, 480))
pygame.display.set_caption("Kepler-442 b ")


#INITIAL LEVEL SETTINGS
player = bl
bg = bg1
level = 1
stored_player = player
stored_bg = bg
stored_level = level


####################### FUNCTIONS:

#FUNCTION THAT PRINTS TEXT
def print_text(message, x, y, font_col, font_type, font_size):   
    pygame.display.init()
    pygame.font.init()
    font_type1 = pygame.font.Font(font_type, font_size)
    text = font_type1.render(message, True, font_col)
    win.blit(text, (x, y))


#FUNCTION THAT PAUSES THE GAME
def pause():
    paused = True
    global run
    while paused:
        #check for game quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                run = False
        print_text("PAUSED", 350, 220, (0, 255, 0), "fonts/Pixeboy.ttf", 50)
        print_text("Press ENTER to continue", 150, 290, (0, 255, 0), "fonts/Pixeboy.ttf ", 20)
        #check for un-pause
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RETURN]:
            paused = False
            pygame.mixer.unpause()
        pygame.display.update()
        pygame.time.delay(100)

#FUNCTION THAT SHOWS MAIN MENU
def show_menu(win, image):
    global shmenu, cy, dy, up, up2, dpy, dpx, cpy, cpx, run
    while shmenu:
        #check for game quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                shmenu = False
        #buttons
        start_but = button(130, 25, (178, 236, 166), (0, 255, 0))
        levels_but = button(155, 25, (178, 236, 166), (0, 255, 0))
        settings_but = button(130, 25, (201, 222, 31), (255, 255, 0))
        close_but = button(130, 25, (236, 174, 166), (255, 0, 0))
        win.blit(image, (0, 0))
        #drawing the two figures floating in space
        cx = 650
        dx = 420
        win.blit(xen_small, (cx, cy))
        win.blit(pl_small, (dx, dy))
        if cy>90 and up:
            cy-=1
        if cy == 90:
            up = False
        if cy<215 and not up:
            cy+=1
        if cy == 215:
            up = True
        if dy>150 and up2:
            dy-=1
        if dy == 150:
            up2 = False
        if dy<280 and not up2:
            dy+=1
        if dy == 280:
            up2 = True
        if dpx!= 0 and dpx<720 and not(cx<dpx<cx+25 and cy<dpy<cy+52):
            dpx+=2
            pygame.draw.circle(win, (255, 0, 0), (dpx, dpy), 1)
        else:
            dpx=dx
            dpy = dy
        if cpx!= 0 and cpx>300 and not (dx<cpx<dx+20 and dy<cpy<dy+42):
            cpx-=2
            pygame.draw.circle(win, (0, 0, 255), (cpx, cpy), 1)
        else:
            cpx=cx
            cpy = cy
        #drawing buttons
        start_but.buttondrawer(50, 180, "Start game", "start_intro", win, 25, 4)
        levels_but.buttondrawer(50, 220, "Show levels (cheating)", "show_menu1", win, 15, 8)
        settings_but.buttondrawer(50, 260, " Settings", "show_settings", win, 25, 4)
        close_but.buttondrawer(50, 300, " Quit game", "quit", win, 25, 4)
        print_text("Kepler-442 b ", 100, 60, (255, 255, 255), "fonts/VerminVibes.ttf", 50)
        pygame.display.update()
        pygame.time.delay(30)
        
        
#FUNCTION THAT SHOWS SETTINGS MENU
def show_settings(win, image):
    global shsettings, sliderx1, sliderx2, run
    while shsettings:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shsettings = False
                run = False
        #buttons
        mus_vol_but = slider(150, 8, 7, sliderx1, (170, 160, 179), (209, 97, 254), sliding1)
        eff_vol_but = slider(150, 8, 7, sliderx2, (170, 160, 179), (209, 97, 254), sliding2)
        close_but = button(55, 20, (236, 174, 166), (255, 0, 0))
        #drawing background, text and buttons
        win.blit(image, (0, 0))
        print_text("Settings", 280, 30, (255, 255, 255), "fonts/VerminVibes.ttf", 30)
        print_text("Music", 10, 145, (255, 255, 255), "fonts/Pixeboy.ttf", 20)
        print_text("sfx", 20, 195, (255, 255, 255), "fonts/Pixeboy.ttf", 20)
        print_text(str('{:.2f}'.format(round(mus_vol, 2))), 230, 145, (255, 255, 255), "fonts/Pixeboy.ttf", 20)
        print_text(str('{:.2f}'.format(round(eff_vol, 2))), 230, 195, (255, 255, 255), "fonts/Pixeboy.ttf", 20)
        mus_vol_but.sliderdrawer(70, 150, "change music")
        eff_vol_but.sliderdrawer(70, 200, "change sfx")
        close_but.buttondrawer(50, 30, "back", "show_menu", win, 20, 3)
        #setting volume
        music1.set_volume(mus_vol)
        music2.set_volume(mus_vol)
        music3.set_volume(mus_vol)
        music4.set_volume(mus_vol)
        music5.set_volume(mus_vol)
        musici.set_volume(mus_vol)
        music_int.set_volume(mus_vol)
        button_pressed.set_volume(eff_vol)
        durak_scream.set_volume(eff_vol)
        throw.set_volume(eff_vol+0.1)
        launch.set_volume(eff_vol-0.1)
        blaster.set_volume(eff_vol-0.1)
        expl_sound.set_volume(eff_vol-0.1)
        isolation_sound.set_volume(eff_vol)
        astronomia.set_volume(mus_vol)
        alien_scream.set_volume(eff_vol-0.45)
        alien_throw.set_volume(eff_vol-0.35)
        csound1.set_volume(eff_vol-0.45)
        csound2.set_volume(eff_vol-0.45)
        pygame.display.update()
        pygame.time.delay(30)
        

#FUNCTIONS THAT SHOWS "SELECT LEVEL" MENU
def show_scene_menu(win, image):
    global shmenu1, run
    while shmenu1:
        #check for game quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                shmenu1 = False
        #buttons
        scene0 = button(90, 63, None, (178, 236, 166))
        scene1 = button(90, 63, None, (178, 236, 166))
        scene2 = button(90, 63, None, (178, 236, 166))
        scene3 = button(90, 63, None, (178, 236, 166))
        scene4 = button(90, 63, None, (178, 236, 166))
        scene5 = button(90, 63, None, (178, 236, 166))
        scene6 = button(90, 63, None, (178, 236, 166))
        scene7 = button(90, 63, None, (178, 236, 166))
        close_but = button(55, 20, (236, 174, 166), (255, 0, 0))
        #drawing background, buttons and text  
        win.blit(image, (0, 0))
        scene0.buttondrawer2(50, 160, small_intro_bg, None, "Intro", "show_intro", win, 15, 3)
        scene1.buttondrawer2(200, 160, bg1_preview, bg1, "Level 1", "show_lvl1", win, 15, 3)
        scene2.buttondrawer2(350, 160, bg2_preview, bg2, "Level 2", "show_lvl2", win, 15, 3)
        scene3.buttondrawer2(500, 160, bg3_preview, bg3, "Level 3", "show_lvl3", win, 15, 3)
        scene4.buttondrawer2(50, 275, bg4_preview, bg4, "Level 4", "show_lvl4", win, 15, 3)
        scene5.buttondrawer2(200, 275, bg5_preview, bg5, "Level 5", "show_lvl5", win, 15, 3)
        scene6.buttondrawer2(350, 275, bg6_preview, bg6, "Level 6", "show_lvl6", win, 15, 3)
        scene7.buttondrawer2(50, 390, outro_preview, bg6, "Outro", "show_outro", win, 15, 3)
        close_but.buttondrawer(50, 30, "back", "show_menu", win, 20, 3)
        print_text("Select level", 250, 40, (255, 255, 255), "fonts/VerminVibes.ttf", 40)
        pygame.display.update()
        pygame.time.delay(30)


#FUNCTION THAT DRAWS INTRO SLIDES IN "START GAME" MODE
def intro(win, image):
    global shintro, shintro_count, shmenu, shmenu1, fight, re_animcount, explosion_time, xpl_count, expl_b, Mode1, run, tut, tut_count, stored_player, stored_bg, stored_level, level, bg, player
    while shintro:
        #buttons
        arrowR = intro_button(80, 61, arrow_r, arrow_ar)
        arrowL = intro_button(80, 61, arrow_l, arrow_al)
        #the below describes what should happen when a certain slide is shown
        if shintro_count == 0 and not Mode1:
            shintro = False
            shmenu = True
            shintro_count = 1
            pygame.mixer.stop()
            show_menu(win, menu)
        elif shintro_count == 0 and Mode1:
            shintro = False
            shmenu = False
            shmenu1 = True
            shintro_count = 1
            Mode1 = False
            pygame.mixer.stop()
            show_scene_menu(win, scene)
        if shintro_count == 1:
            image = intro_bg[0]
            win.blit(image, (0, 0))
            print_text("You are an astronaut in the expedition", 30, 60, (0, 255, 0), "fonts/Digital7.ttf", 23)
            print_text("K42b15 to the planet Kepler-442b.", 30, 90, (0, 255, 0), "fonts/Digital7.ttf", 23)
        if shintro_count == 2:
            image = intro_bg[1]
            explosion_time = 0
            xpl_count = 0
            expl_b == True
            win.blit(image, (0, 0))
            print_text("Your mission is to investigate", 30, 120, (0, 255, 0), "fonts/Digital7.ttf", 23)
            print_text("what happened to the crew of K42b14.", 30, 150, (0, 255, 0), "fonts/Digital7.ttf", 23)
            print_text("Their signal was lost 4 days ago", 30, 210, (0, 255, 0), "fonts/Digital7.ttf", 23)
            print_text("and they do not respond.", 30, 240, (0, 255, 0), "fonts/Digital7.ttf", 23)
        if shintro_count == 3:
            if re_animcount+1 >= 14:
                re_animcount = 0
                explosion_time += 1
            win.blit(reentry[re_animcount], (0, 0))
            re_animcount += 1
            print_text("During the atmospheric entry", 370, 310, (0, 255, 0), "fonts/Digital7.ttf", 23)
            print_text("something important explodes", 370, 340, (0, 255, 0), "fonts/Digital7.ttf", 23)
            print_text("in your capsule.", 370, 370, (0, 255, 0), "fonts/Digital7.ttf", 23)
            if explosion_time == 3 and expl_b == True:
                win.blit(expl_not_scaled[xpl_count], (110, 165))
                xpl_count+=1
                if xpl_count >= 18:
                    xpl_count = 0
                    expl_b = False
            if explosion_time == 5:
                win.blit(explosion[xpl_count//2], (160, 280))
                xpl_count+=1
                if xpl_count >= 34:
                    xpl_count = 0
                    explosion_time == 6
        if shintro_count == 4:
            explosion_time = 0
            xpl_count = 0
            expl_b == True
            image = intro_bg[2]
            win.blit(image, (0, 0))
            print_text("You realize you are landing 10 km", 30, 60, (0, 255, 0), "fonts/Digital7.ttf", 23)
            print_text("away from K42b14 landing spot.", 30, 90, (0, 255, 0), "fonts/Digital7.ttf", 23)
        if shintro_count == 5:
            image = intro_bg[3]
            win.blit(image, (0, 0))
            print_text("The capsule is severely damaged.", 130, 105, (0, 255, 0), "fonts/Digital7.ttf", 23)
            print_text("Step on the surface of Kepler-442b", 368, 180, (0, 255, 0), "fonts/Digital7.ttf", 23)
            print_text("and walk your way", 460, 230, (0, 255, 0), "fonts/Digital7.ttf", 23)
            print_text("to find the missing crew.", 460, 260, (0, 255, 0), "fonts/Digital7.ttf", 23)
        if shintro_count == 6 and not Mode1:
            shintro_count = 1
            pygame.mixer.stop()
            shintro = False
            shmenu1 = False
            shmenu = False
            tut = True
            player = stored_player
            bg = stored_bg
            level = stored_level
            if level == 1:
                tut_count = 1
            elif level == 2:
                tut_count = 3
            elif level == 3:
                tut_count = 5
            elif level == 4:
                tut_count = 7
            elif level == 5:
                tut_count = 9
            elif level == 6:
                tut_count = 11
            elif level == 7:
                tut_count = 14
                pygame.mixer.Sound.play(music_int)
            tutorial(level)
        elif shintro_count == 6 and Mode1:
            shintro_count = 1
            pygame.mixer.stop()
            shintro = False
            shmenu1 = True
            Mode1 = False
            show_scene_menu(win, scene)
        #drawing buttons
        arrowR.intro_buttondrawer(625, 405, "Next", win)
        arrowL.intro_buttondrawer(15, 405, "Previous", win)
        pygame.display.update()
        pygame.time.delay(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shintro = False
                run = False



#FUNCTION THAT SHOWS TUTORIALS IN BETWEEN LEVELS (ALSO USED FOR GAME OUTRO)        
def tutorial(lvl):
    global tut, tut_count, fire_animcount, run
    while tut:
        #check for game quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tut = False
                run = False
        #buttons, background, static players
        arrowR = intro_button(80, 61, arrow_r, arrow_ar)
        arrowL = intro_button(80, 61, arrow_l, arrow_al)
        win.blit(bg, (0, 0))
        if lvl == 4:
            if fire_animcount+1 >= 11:
                fire_animcount = 0
            win.blit(fire[fire_animcount], (100, 99))
            win.blit(fire[fire_animcount], (555, 99))
            fire_animcount+=1
        win.blit(player, (x1, y1))
        win.blit(pl_stand, (x, y))
        
        #the below describes what must be shown at each slide at each level
        if lvl == 1:
            if tut_count == 1:
                win.blit(jar, (x1+20, y1-15))
                win.blit(cabbage, (x1-100, y1-50))
                print_text("Looks like you have landed in someone's garden", 10, 30, (0, 255, 0), "fonts/Pixeboy.ttf", 30)
                print_text("and were attacked by:", 200, 80, (0, 255, 0), "fonts/Pixeboy.ttf", 30)
                win.blit(lc1, (480, 65))
            elif tut_count == 2:
                win.blit(jar, (x1+20, y1-15))
                win.blit(control, (160, 140))
                print_text("Attack is the best defence.", 200, 30, (0, 255, 0), "fonts/Pixeboy.ttf", 30)
                print_text("Press SPACE to throw a cabbage", 185, 60, (0, 255, 0), "fonts/Pixeboy.ttf", 30)
            elif tut_count == 3:
                tut = False
                tut_count = 1
                pygame.mixer.Sound.play(music4)
        elif lvl == 2:
            if tut_count == 3:
                print_text("Apparently someone does not want", 50, 60, (0, 255, 0), "fonts/Pixeboy.ttf", 30)
                print_text("you to be on this planet...", 50, 90, (0, 255, 0), "fonts/Pixeboy.ttf", 30)
                win.blit(lc2, (480, 65))
            elif tut_count == 4:
                print_text("Throw stones at the robot", 70, 70, (0, 255, 0), "fonts/Pixeboy.ttf", 25)
                print_text("and dodge his shots by jumping", 60, 100, (0, 255, 0), "fonts/Pixeboy.ttf", 25)
                win.blit(control, (160, 140))
            elif tut_count == 5:
                tut = False
                tut_count = 3
                pygame.mixer.Sound.play(music3)
        elif lvl == 3:
            if tut_count == 5:
                win.blit(bg, (0, 0))
                win.blit(pl_stand, (x, y))
                win.blit(lasergunL, (x+40, y+38))
                print_text("You picked up the laser gun left by ATL-315,", 30, 100, (0, 255, 0), "fonts/Pixeboy.ttf", 20)
                print_text("now you can shoot it by pressing RIGHT SHIFT", 30, 130, (0, 255, 0), "fonts/Pixeboy.ttf", 20)
                win.blit(control1, (150, 160))
            elif tut_count == 6:
                win.blit(lasergunL, (x+40, y+38))
                print_text("Now it might come handy because your next enemy is:", 30, 130, (0, 255, 0), "fonts/Pixeboy.ttf", 20)
                win.blit(lc3, (480, 65))
            elif tut_count == 7:
                tut = False
                tut_count = 5
                pygame.mixer.Sound.play(music1)
        elif lvl == 4:
            if tut_count == 7:
                win.blit(cave, (0, 0))
                print_text("The path lies through a cave", 100, 60, (0, 255, 0), "fonts/Pixeboy.ttf", 30)
            elif tut_count == 8:
                print_text("It is the Alien!    (who would have thought?)", 20, 30, (0, 255, 0), "fonts/Pixeboy.ttf", 25)
                win.blit(lc4, (480, 65))
                print_text("Beware of facehuggers and acid blood", 200, 440, (0, 255, 0), "fonts/Pixeboy.ttf", 25)
            elif tut_count == 9:
                print_text("Now you can also dodge by pressing", 100, 70, (0, 255, 0), "fonts/Pixeboy.ttf", 25)
                print_text("and holding the DOWN ARROW", 150, 100, (0, 255, 0), "fonts/Pixeboy.ttf", 25)
                win.blit(control2, (150, 160))
            elif tut_count == 10:
                fire_animcount = 0
                tut = False
                tut_count = 7
                pygame.mixer.Sound.play(music2)
        elif lvl == 5:
            if tut_count == 9:
                print_text("You may have already noticed that", 10, 60, (0, 255, 0), "fonts/Pixeboy.ttf", 30)
                print_text("everything on this planet", 10, 90, (0, 255, 0), "fonts/Pixeboy.ttf", 30)
                print_text("wants to kill you.       Well,... ", 10, 120, (0, 255, 0), "fonts/Pixeboy.ttf", 30)
                win.blit(lc5, (480, 65))
            elif tut_count == 10:
                tut = False
                tut_count = 9
                pygame.mixer.Sound.play(music4)
        elif lvl == 6:
            if tut_count == 11:
                win.blit(hell1, (0, 0))
                print_text("Almost there!", 100, 60, (0, 255, 0), "fonts/Pixeboy.ttf", 30)
            elif tut_count == 12:
                win.blit(hell2, (0, 0))
                print_text("But before that you have to descend into hell real quick", 100, 40, (0, 255, 0), "fonts/Pixeboy.ttf", 25)
            elif tut_count == 13:
                print_text("the final battle", 110, 40, (0, 255, 0), "fonts/Pixeboy.ttf", 30)
                print_text("WOULD NOT BE FOUGHT IN THE FUTURE." , 60, 100, (0, 255, 0), "fonts/Pixeboy.ttf", 25)
                print_text("IT WOULD BE FOUGHT HERE, IN OUR PRESENT." , 40, 140, (0, 255, 0), "fonts/Pixeboy.ttf", 25)
                print_text("TONIGHT..." , 150, 180, (0, 255, 0), "fonts/Pixeboy.ttf", 25)
                win.blit(lc6, (480, 65))
            elif tut_count == 14:
                tut = False
                tut_count = 11
                pygame.mixer.Sound.play(music5)
        #outro (level7)    
        elif lvl == 7:
            if tut_count == 14:
                win.blit(out1, (0, 0))
                print_text("You found them!", 100, 60, (0, 255, 0), "fonts/Pixeboy.ttf", 30)
            elif tut_count == 15:
                win.blit(out1, (0, 0))
                print_text("It turns out the crew was just having some problems", 100, 40, (0, 255, 0), "fonts/Pixeboy.ttf", 25)
                print_text("with their antenna. They already fixed it by now.", 100, 70, (0, 255, 0), "fonts/Pixeboy.ttf", 25)
            elif tut_count == 16:
                win.blit(out2, (0, 0))
                print_text("It is time to set off for our home at Proxima Centauri", 50, 40, (0, 255, 0), "fonts/Pixeboy.ttf", 30)
            elif tut_count == 17:
                win.blit(out3, (0, 0))
                print_text("Kepler-442B turned out to be", 35, 30, (0, 255, 0), "fonts/Pixeboy.ttf", 25)
                print_text("not a very friendly place.", 35, 60, (0, 255, 0), "fonts/Pixeboy.ttf", 25)
                print_text("Still, there are plenty other worlds" , 60, 100, (0, 255, 0), "fonts/Pixeboy.ttf", 25)
                print_text("waiting for us to come!" , 60, 130, (0, 255, 0), "fonts/Pixeboy.ttf", 25)
                print_text("(maybe)" , 270, 170, (0, 255, 0), "fonts/Pixeboy.ttf", 20)
            #closes the "start game" mode and resets everyting
            elif tut_count == 18:
                global shmenu, shmenu1, shsettings, shintro, Mode1, question, level
                global fight, kamni1, kamni2, kamni, kamni_inner_list, viruses, rakety, home, locked, health, green, red, health1, green1, red1
                tut = False
                tut_count = 1
                fight = False
                kamni = []
                kamni1 = []
                kamni2 = []
                kamni_inner_list = []
                viruses = []
                rakety = []
                home = 0
                locked = False 
                pygame.mixer.stop()
                health = 100
                red=0
                green=255
                health1 = 100
                red1=0
                green1=255
                question = False
                if not Mode1:
                    level = 1
                    shmenu = True
                    shmenu1 = False
                    pygame.mixer.Sound.play(musici)
                    show_menu(win, menu)
                else:
                    Mode1 = False
                    shmenu1 = True
                    show_scene_menu(win, scene)
        #drawing buttons
        arrowR.intro_buttondrawer(625, 405, "Next_tut", win)
        #not drawing return button on certain slides
        if not tut_count == 1 and not tut_count == 3 and not tut_count == 5 and not tut_count == 7 and not tut_count == 9 and not tut_count == 11 and not tut_count == 14:
            arrowL.intro_buttondrawer(15, 405, "Previous_tut", win)
        pygame.display.update()
        pygame.time.delay(30)            
            



       

 
#THE MAIN DRAWING FUNCTION (THAT DRAWS EVERYTHING DURING FIGHT SCENES)       
def drawer(bg, opponent_image):
    win.blit(bg, (0, 0))
    pygame.draw.rect(win, (red, green, 0), (6, 10, health, 5))
    pygame.draw.rect(win, (red1, green1, 0), (714-health1, 10, health1, 5))
    global coffin, finish, animcount, a, fire_animcount, blcount, smoke_count, kemcount, atlcount, atl_jumpcount, neo_b, neo_count, expl_atl, expl_atl_count, termcount, term_jumpcount, sit, sit_count, xen_count
    if player == xen1:
        if fire_animcount+1 >= 11:
            fire_animcount = 0
        win.blit(fire[fire_animcount], (100, 99))
        win.blit(fire[fire_animcount], (555, 99))
        fire_animcount+=1
    elif player == bl:
        if smoke_count+1>=(3*len(smoke)):
                smoke_count = 0
        win.blit(smoke[smoke_count//3], (-45, -45))
        smoke_count+=1
    if not coffin: 
        #Xenomorph
        if opponent_image == xen1:
            if xen_count+1>=24:
                xen_count = 0
            if moving and not isJump1:
                win.blit(xen_walk[xen_count//3], (x1, y1))
                xen_count+=1
            elif isJump1:
                win.blit(xenj, (x1, y1))
            else:
                win.blit(xen1, (x1, y1))
        #BL-1050
        elif opponent_image == bl:
            if blcount+1 >= 27:
                blcount = 0
            if moving:
                win.blit(bl_walk[blcount//3], (x1, y1))
                win.blit(jar, (x1+20, y1-15))
                blcount+=1
            else:
                win.blit(bl, (x1, y1))
                win.blit(jar, (x1+20, y1-15))
        #Kem John-krem
        elif opponent_image == kem:
            if kemcount+1 >= 10:
                kemcount = 0
            if moving:
                win.blit(kem_walk[kemcount], (x1, y1))
                kemcount+=1
            else:
                win.blit(kem, (x1, y1))
        #ATL-315
        elif opponent_image == atl:
            if not isJump1:
                if atlcount+1 >= 24:
                    atlcount = 0
                if moving:
                    win.blit(atl_walk[atlcount//3], (x1, y1))
                    atlcount+=1
                else:
                    win.blit(atl, (x1, y1))
                win.blit(lasergun, (x1-5, y1+40))
            else:
                if atl_jumpcount+1 >= 36:
                    atl_jumpcount = 0
                win.blit(atl_jump[atl_jumpcount], (x1, y1))
                atl_jumpcount+=1
        #Terminator T-800
        elif opponent_image == term:
            if not isJump1:
                if termcount+1 >= 16:
                    termcount = 0
                if moving:
                    win.blit(term_walk[termcount//2], (x1-23, y1))
                    termcount+=1
                elif sit:
                    if sit_count<2:
                        win.blit(term_sit1, (x1-23, y1))
                    elif 2<=sit_count<=27:
                        win.blit(term_sit2, (x1-23, y1+51))
                    elif 28<=sit_count<=30:
                        win.blit(term_sit1, (x1-23, y1))
                    elif sit_count>30:
                        sit_count = -1
                        sit = False
                    sit_count+=1
                else:
                    win.blit(term, (x1, y1))
            else:
                if term_jumpcount+1 >= 36:
                    term_jumpcount = 0
                win.blit(term_jump[term_jumpcount], (x1-10, y1))
                term_jumpcount+=1
        else: 
            win.blit(opponent_image, (x1, y1))
        #drawing the left player
        if not neo_b:    
            if animcount+1 >= 24:
                animcount = 0
            if not (player == bl or player == atl):
                win.blit(lasergunL, (x+40, y+38))
            if walking: 
                win.blit(pl_walk[animcount//3], (x, y))
                animcount += 1
            else:
                win.blit(pl_stand, (x, y))
        else:
            if neo_count+1 >= 18:
                neo_count = 0
            win.blit(neo[neo_count//3], (x-70, y+58))
            neo_count+=1
        #drawing available weapons
        if p_blast_possible and not (player == bl or player == atl or player == term):
            win.blit(lasergunL1,(30, 80))
            print_text("1", 52,75, (255, 0, 0), "fonts/Pixeboy.ttf", 20)
        elif not (player == bl or player == atl or player == term):
            win.blit(lasergunL2,(30, 80))
        if len(kamni)==0 and not (player == bl or player == atl or player == term):
            win.blit(stone1, (33, 50))
            print_text("2", 47, 50, (255, 0, 0), "fonts/Pixeboy.ttf", 20)
        elif len(kamni)==1 and not (player == bl or player == atl or player == term):
            win.blit(stone1, (33, 50))
            print_text("1", 47, 50, (255, 0, 0), "fonts/Pixeboy.ttf", 20)
        elif len(kamni) == 2 and not (player == bl or player == atl or player == term):
            win.blit(stone2, (33, 50))
        elif len(kamni)==0 and player == atl:
            win.blit(stone1, (33, 50))
            print_text("2", 55, 50, (255, 0, 0), "fonts/Pixeboy.ttf", 25)
        elif p_blast_possible and player == term:
            win.blit(lasergunL1,(30, 50))
            print_text("1", 52,45, (255, 0, 0), "fonts/Pixeboy.ttf", 20)
        elif not p_blast_possible and player == term:
            win.blit(lasergunL2,(30, 50))
        elif len(kamni)==1 and player == atl:
            win.blit(stone1, (33, 50))
            print_text("1", 55, 50, (255, 0, 0), "fonts/Pixeboy.ttf", 25)
        elif len(kamni) == 2 and player == atl:
            win.blit(stone2, (33, 50))
        elif len(kamni)==0 and player == bl:
            win.blit(cabbage, (33, 50))
            print_text("2", 57, 50, (255, 0, 0), "fonts/Pixeboy.ttf", 25)
        elif len(kamni)==1 and player == bl:
            win.blit(cabbage, (33, 50))
            print_text("1", 57, 50, (255, 0, 0), "fonts/Pixeboy.ttf", 25)
        elif len(kamni) == 2 and player == bl:
            win.blit(cabbage1, (33, 50))
    #when one of the players die
    elif coffin and a-cof_start_time<7:
        #coffin dancers
        global animcount_c
        if animcount_c+1 >= 30:
            animcount_c = 0         
        if cof_left:
            win.blit(cof_dance_refl[animcount_c//5], (100, 303))
            animcount_c+=1
            win.blit(opponent_image, (x1, y1))
        elif cof_right and player != atl and player != term and player != bl:
            win.blit(cof_dance[animcount_c//5], (480, 303))
            animcount_c+=1
            if animcount+1 >= 24:
                animcount = 0
            if walking: 
                win.blit(pl_walk[animcount//3], (x, y))
                animcount += 1
            else:
                win.blit(pl_stand, (x, y))
        #just falling on the ground        
        elif cof_right and player == bl:
             win.blit(pygame.transform.rotate(bl, -90), (500, 400))
             win.blit(pygame.transform.rotate(jar, -90), (595, 420))
             if animcount+1 >= 24:
                animcount = 0
             if walking: 
                win.blit(pl_walk[animcount//3], (x, y))
                animcount += 1
             else:
                win.blit(pl_stand, (x, y))
        #explosions
        elif cof_right and player == atl or player == term:
            if expl_atl == True:
                if expl_atl_count >=50:
                    expl_atl = False
                    expl_atl_count = 0
                win.blit(explosion[expl_atl_count//3], (x1, y1))
                expl_atl_count+=1
            if animcount+1 >= 24:
                animcount = 0
            if player == atl:
                win.blit(lasergun, (x1-50, 440))
            if walking: 
                win.blit(pl_walk[animcount//3], (x, y))
                animcount += 1
            else:
                win.blit(pl_stand, (x, y))
    elif coffin and a-cof_start_time>=7:
        finish = True
    
    #drawing bullets, stones, etc
    for kamen in kamni:
        kamen[0].stonedrawer(win)
    for bullet in p_blaster:
        bullet.stonedrawer(win)
    for kamen1 in kamni1:
        kamen1.stonedrawer(win)
    for kamen2 in kamni2:
        kamen2.stonedrawer(win)
    for virus in viruses:
        virus.stonedrawer(win)
    for raketa in rakety:
        raketa.rocketdrawer(win)
    if home != 0:
        home.housedrawer(win, iso_time)
    if not coffin:
        back.buttondrawer(310, 20, "back", "end_fight", win, 35, 5)
    
    pygame.display.update()   



#THE FUNCTION THAT ALLOWS TO COME BACK TO LIFE AND TRY AGAIN
def resurrect():
    global question
    while question:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        yes = button(40, 30, (178, 236, 166), (0, 255, 0))
        no = button(40, 30, (248, 161, 166), (255, 0, 0))
        win.blit(bg, (0, 0))
        print_text("Would you like to", 250, 200, (255, 255, 255), "fonts/Pixeboy.ttf", 35) 
        print_text("resurrect yourself?", 250, 230, (255, 255, 255), "fonts/Pixeboy.ttf", 35)
        yes.buttondrawer(250, 280, "yes", "resurrect", win, 15, 4)
        no.buttondrawer(380, 280, "no", "end_fight", win, 15, 4)
        pygame.display.update()
        pygame.time.delay(30)
        

###################### BUTTONS:
        
#ARROWS IN INTRO
class intro_button():
    def __init__(self, width, height, inactive_image, active_image):
        self.width = width
        self.height = height
        self.inactive_image = inactive_image
        self.active_image = active_image
    #function that draws the arrows
    def intro_buttondrawer(self, x, y, action, window):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (x < mouse[0] < x+self.width) and (y < mouse[1] < y+self.height):
            win.blit(self.active_image, (x, y))
            if click[0] == 1:
                pygame.mixer.Sound.play(button_pressed)
                pygame.time.delay(300)
                global shintro_count, tut_count
                if action == "Next":
                    shintro_count+=1
                elif action == "Previous":
                    shintro_count-=1
                elif action == "Next_tut":
                    tut_count+=1
                elif action == "Previous_tut":
                    tut_count-=1       
        else:
            win.blit(self.inactive_image, (x, y))
            
#SLIDERS IN SETTINGS            
class slider():
    def __init__(self, width, height, slider_rad, sliderx, inactive_col, active_col, sliding_bool):
        self.width = width
        self.height = height
        self.inactive_col = inactive_col
        self.active_col = active_col
        self.rad = slider_rad
        self.slx = int(sliderx)
        self.sliding = sliding_bool
    #function that draws sliders
    def sliderdrawer(self, x, y, ctrl_object):
        global sliderx1, sliderx2, sliding1, sliding2, eff_vol, mus_vol
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #if a slider is held but mouse is outside the circle
        if click[0] == 1 and self.sliding:
            if x< mouse[0] < (x + self.width):
                if ctrl_object == "change music":
                    self.slx = mouse[0]
                    sliderx1 = mouse[0]
                elif ctrl_object == "change sfx":
                    self.slx = mouse[0]
                    sliderx2 = mouse[0]
            elif x > mouse[0]:
                if ctrl_object == "change music":
                    self.slx = x
                    sliderx1 = x
                elif ctrl_object == "change sfx":
                    self.slx = x
                    sliderx2 = x
            elif (x + self.width) < mouse[0]:
                if ctrl_object == "change music":
                    self.slx = x + self.width
                    sliderx1 = x + self.width
                elif ctrl_object == "change sfx":
                    self.slx = x + self.width
                    sliderx2 = x + self.width
        elif self.sliding and not click[0] == 1:
            if ctrl_object == "change music":
                sliding1 = False 
            elif ctrl_object == "change sfx":
                sliding2 = False 
        #if mouse is inside a circle
        if (self.slx-self.rad < mouse[0] < self.slx+self.rad) and ((y+int(self.height//2))-self.rad) < mouse[1] < (y+(self.height/2)+self.rad):
            pygame.draw.rect(win, self.inactive_col, (x, y, self.width, self.height)) 
            pygame.draw.rect(win, self.active_col, (x, y, self.slx-x, self.height)) 
            pygame.draw.circle(win, (168, 41, 219), (self.slx, y+int(self.height//2)), self.rad)
            if click[0] == 1 and  x< mouse[0] < (x + self.width):
                self.slx = mouse[0]
                if ctrl_object == "change music":
                    sliderx1 = mouse[0]
                    sliding1 = True 
                elif ctrl_object == "change sfx":
                    sliderx2 = mouse[0]
                    sliding2 = True
        else:
            pygame.draw.rect(win, self.inactive_col, (x, y, self.width, self.height)) 
            pygame.draw.rect(win, self.active_col, (x, y, self.slx-x, self.height)) 
            if self.sliding:
                pygame.draw.circle(win, (168, 41, 219), (self.slx, y+int(self.height/2)), self.rad)
            else:
                pygame.draw.circle(win, (94, 23, 122), (self.slx, y+int(self.height/2)), self.rad)
        if ctrl_object == "change music":
            mus_vol = (self.slx-x)/self.width
        elif ctrl_object == "change sfx":
            eff_vol = (self.slx-x)/self.width
                
#RECTANGULAR BUTTONS
class button():
    def __init__(self, width, height, inactive_col, active_col):
        self.width = width
        self.height = height
        self.inactive_col = inactive_col
        self.active_col = active_col
    #function that draws general rectangular buttons
    def buttondrawer(self, x, y, message, action, window, font_size, w):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #if mouse is inside a button:
        if (x < mouse[0] < x+self.width) and (y < mouse[1] < y+self.height):
            pygame.draw.rect(window, self.active_col, (x, y, self.width, self.height))
            if click[0] == 1:
                pygame.mixer.Sound.play(button_pressed)
                pygame.time.delay(300)
                if action != None:
                    global shmenu, shmenu1, shsettings, shintro, Mode1, question, run
                    global fight, kamni1, kamni2, kamni, kamni_inner_list, viruses, rakety, home, locked, health, green, red, health1, green1, red1, player, bg, stored_player, stored_bg, stored_level
                    #checking what each button does
                    if action == "quit":
                        pygame.time.delay(200)
                        run = False
                        shmenu = False
                    elif action == "start_game":
                        shintro = False
                        shmenu1 = False
                        shmenu = False
                    elif action == "start_intro":
                        pygame.mixer.stop()
                        pygame.mixer.Sound.play(music_int)
                        shmenu1 = False
                        shmenu = False
                        shintro = True
                        intro(win, intro_bg[0])
                    elif action == "show_menu":
                        shmenu1 = False
                        shmenu = True
                        shsettings = False
                        pygame.mixer.Sound.play(musici)
                        show_menu(window, menu)
                    elif action == "show_settings":
                        pygame.mixer.stop()
                        shsettings = True
                        shmenu = False
                        fight = False
                        show_settings(win, settings_bg)          
                    elif action == "resurrect":
                        question = False
                        if level == 1 or level == 5:
                            pygame.mixer.Sound.play(music4)
                        elif level == 2:
                            pygame.mixer.Sound.play(music3)
                        elif level == 3:
                            pygame.mixer.Sound.play(music1)
                        elif level == 4:
                            pygame.mixer.Sound.play(music2)
                        elif level == 6:
                            pygame.mixer.Sound.play(music5)            
                    elif action == "show_menu1":
                        fight = False
                        shmenu = False
                        shmenu1 = True
                        pygame.mixer.stop()
                        ######
                        kamni = []
                        kamni1 = []
                        kamni2 = []
                        kamni_inner_list = []
                        viruses = []
                        rakety = []
                        home = 0
                        locked = False 
                        show_scene_menu(window, scene)
                    elif action == "end_fight":
                        fight = False
                        kamni = []
                        kamni1 = []
                        kamni2 = []
                        kamni_inner_list = []
                        viruses = []
                        rakety = []
                        home = 0
                        locked = False 
                        pygame.mixer.stop()
                        health = 100
                        red=0
                        green=255
                        health1 = 100
                        red1=0
                        green1=255
                        question = False
                        if not Mode1:
                            stored_player = player
                            stored_bg = bg
                            stored_level = level
                            shmenu = True
                            shmenu1 = False
                            pygame.mixer.Sound.play(musici)
                            show_menu(window, menu)
                        else:
                            Mode1 = False
                            shmenu1 = True
                            show_scene_menu(window, scene)
                    else:    
                        action()
        #if mouse is outside a button:
        else:
            pygame.draw.rect(window, self.inactive_col, (x, y, self.width, self.height))
        print_text(message, x+10, y+w, (0, 0, 0), "fonts/Pixeboy.ttf", font_size)
    
    #another button function that draws buttons in the "select level" menu
    def buttondrawer2(self, x, y, image, corr_bg, message, action, window, font_size, w):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (x < mouse[0] < x+self.width-10) and (y < mouse[1] < y+self.height-10):
            pygame.draw.rect(window, self.active_col, (x-5, y-5, self.width, self.height))
            window.blit(image, (x, y))
            print_text(message, x+10, y-30, self.active_col, "fonts/Pixeboy.ttf", font_size)
            if click[0] == 1:
                pygame.mixer.Sound.play(button_pressed)
                pygame.font.init()
                pygame.time.delay(300)
                global shmenu1, Mode1
                global bg
                global shmenu, shintro, tut, tut_count
                global player, level
                if action == "show_intro":
                    pygame.mixer.Sound.play(music_int)
                    shmenu1 = False
                    shmenu = False
                    shintro = True
                    Mode1 = True
                    intro(win, intro_bg[0])
                elif action == "show_lvl1":
                    pygame.mixer.Sound.play(music4)
                    shmenu1 = False
                    bg = corr_bg
                    player = bl
                    level = 1
                    Mode1 = True
                elif action == "show_lvl2":
                    pygame.mixer.Sound.play(music3)
                    shmenu1 = False
                    bg = corr_bg
                    player = atl
                    level = 2
                    Mode1 = True
                elif action == "show_lvl3":
                    shmenu1 = False
                    bg = corr_bg
                    player = kem
                    level = 3
                    Mode1 = True
                    pygame.mixer.Sound.play(music1)
                elif action == "show_lvl4":
                    pygame.mixer.Sound.play(music2)
                    shmenu1 = False
                    bg = corr_bg
                    player = xen1
                    level = 4
                    Mode1 = True
                elif action == "show_lvl5":
                    pygame.mixer.Sound.play(music4)
                    shmenu1 = False
                    bg = corr_bg
                    player = corona
                    level = 5
                    Mode1 = True
                elif action == "show_lvl6":
                    shmenu1 = False
                    bg = corr_bg
                    player = term
                    level = 6
                    Mode1 = True
                    pygame.mixer.Sound.play(music5)
                elif action == "show_menu":
                        shmenu = True
                        shmenu1 = False
                        Mode1 = True
                        pygame.mixer.Sound.play(musici)
                        show_menu(window, menu)
                elif action == "show_outro":
                    pygame.mixer.Sound.play(music_int)
                    shmenu1 = False
                    shmenu = False
                    tut = True
                    Mode1 = True
                    level = 7
                    tut_count = 14
                    tutorial(level)
        else:
             win.blit(image, (x, y))
#the BACK button that appears in every fighting scene
back = button(85, 30, (255, 128, 101), (255, 0, 0))


#################### OBJECTS

#STONES (also used for cabbages)
class stone():
    def __init__(self, x, y, radius, col, facing, image):
        self.x = x
        self.y = y
        self.radius = radius
        self.col = col
        self.facing = facing
        self.vel = 11*facing
        self.vert_vel = -23
        self.image = image
    def stonedrawer(self, window):
        if self.image == None:
            pygame.draw.circle(window, self.col, (self.x, self.y), 5)
        else:
            window.blit(self.image, (self.x-6, self.y-5))

#MISSILES ON LEVEL 3
class rocket():
    def __init__(self, x, y, image, facing):
        self.x = x
        self.y = y
        self.image = image
        self.facing = facing
        self.vel = random.randint(14, 25)*facing
        self.vert_vel = -23
        self.im = pygame.transform.rotate(self.image, 90)
    def rocketdrawer(self, window):
        if self.vert_vel < 0:
            window.blit(self.image, (self.x, self.y))
        else:
            window.blit(self.im, (self.x, self.y))
            window.blit(flame, (self.x+21, self.y))

#ISOLATION THING ON LEVEL 5
class house():
    def __init__(self, x, y, col, vert_vel):
        self.x = x
        self.y = y
        self.vert_vel = vert_vel
        self.col = col
        self.roof = -10
    def housedrawer(self, window, time):
        if self.y < 480:
            pygame.draw.rect(window, self.col, (self.x-58, self.y-210, 8, 170))
            pygame.draw.rect(window, self.col, (self.x+50, self.y-210, 8, 170))
        else:
            pygame.draw.rect(window, self.col, (self.x-58, self.y-210, 8, 170))
            pygame.draw.rect(window, self.col, (self.x+50, self.y-210, 8, 170))
            pygame.draw.polygon(window, self.col, [(self.x-68, self.roof), (self.x+68, self.roof), (self.x, self.roof-50)])
            print_text(str(time), self.x-8, self.y-235, (0, 0, 0), "fonts/atomicage-regular.ttf", 15)
            if time%2 == 0:
                print_text("Isolation!", 280, 90, (255, 0, 0), "fonts/Pixeboy.ttf", 35)




##################################  THE MAIN GAME LOOP   #################################
                

pygame.mixer.Sound.play(musici)
show_menu(win, menu)
while run == True:
    #time
    t.tick(FPS)
    #Variable for time comparison (used to restrict amount of shots, jumps, etc)
    a = float(pygame.time.get_ticks()/1000)     
    #check if pause is pressed
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
        pygame.mixer.pause()
        pause()
    
    #CHECKING REMAINING HEALTH OF EACH PLAYER
    #if somebody dies:
    if health1==0 or health==0:
        pygame.mixer.stop()
        kamni = []
        kamni1 = []
        kamni2 = []
        kamni_inner_list = []
        viruses = []
        rakety = []
        home = 0
        locked = False 
        pygame.time.wait(500)
        coffin = True
        pygame.mixer.Sound.play(astronomia)
        cof_start_time = a
        #If player on the right dies:
        if health1 == 0:
            health1 = 1
            cof_right = True
            cof_left = False
            if player == atl or player == bl or player == term:
                pygame.mixer.stop()
                if player == atl or player == term:
                    expl_atl = True
                    pygame.mixer.Sound.play(expl_sound)
                    pygame.time.delay(800)
        #if player on the left dies:
        if health == 0:
            health = 1
            cof_left = True
            cof_right = False
    #when dancing or exploding is finished:    
    if finish:
        #reset variables
        fight = False
        health = 100
        red=0
        green=255
        health1 = 100
        red1=0
        green1=255
        finish = False
        coffin = False
        #If in "start game" mode, switch to next level
        if not Mode1 and cof_right: 
            level+=1
            if level == 2:
                bg = bg2
                player = atl
                tut_count = 3
                tut = True
                tutorial(level)
            if level == 3:
                bg = bg3
                player = kem
                tut_count = 5
                tut = True
                tutorial(level)
            if level == 4:
                bg = bg4
                player = xen1
                tut_count = 7
                tut = True
                tutorial(level)
            if level == 5:
                bg = bg5
                player = corona
                tut_count = 9
                tut = True
                tutorial(level)
            if level == 6:
                bg = bg6
                player = term
                tut_count = 11
                tut = True
                tutorial(level)
            if level == 7:
                bg = bg1
                player = bl
                tut_count = 14
                tut = True
                pygame.mixer.Sound.play(music_int)
                tutorial(level)
        #If lost the battle, ask if the player wants to try again
        elif not Mode1 and cof_left: 
            question = True
            resurrect()
        #if in "select level" mode, go back to menu
        elif Mode1 == True:
            shmenu1 = True
            Mode1 = False
            show_scene_menu(win, scene)
        cof_left = False
        cof_right = False

    
    #PHYSICS OF STONES AND CABBAGES   
    for kamen in kamni:
        if kamen[0].x < 720 and kamen[0].x > 0 and kamen[0].y < 475 and (kamen[0].x<x1 or kamen[0].x>(x1+width1) or kamen[0].y<y1 or kamen[0].y>(y1+height1)):
            kamen[0].x += kamen[0].vel
            if kamen[0].vert_vel<0:
                kamen[0].y-=round((kamen[0].vert_vel**2)/20)
            else:
                kamen[0].y+=round((kamen[0].vert_vel**2)/20)
            kamen[0].vert_vel+=1
        #If the player on the right gets hit by a stone
        elif kamen[0].x < 720 and kamen[0].x > 0 and kamen[0].y < 475 and (kamen[0].x>x1 and kamen[0].x<(x1+width1+10) and kamen[0].y>y1 and kamen[0].y<(y1+height1)):
            if player == kem or player == bl:
                pygame.mixer.Sound.play(durak_scream)
                health1-=10
                red1+=25.2
                green1-=25.2
            elif player == corona:
                if random.randint(0, 2) == 1:
                    pygame.mixer.Sound.play(csound1)
                else:
                    pygame.mixer.Sound.play(csound2)
                health1-=10
                red1+=9.1
                green1-=9.1
            elif player == xen1:
                pygame.mixer.Sound.play(alien_scream)
                health1-=10
                red1+=25.2
                green1-=25.2
            elif player == atl or player == atl:
                health1-=10
                red1+=25.2
                green1-=25.2
            kamni.pop(kamni.index(kamen))
        else:
            kamni.pop(kamni.index(kamen))
    #Physics of bullets and checking for collisions
    for bullet in p_blaster:
        if bullet.x < 720 and bullet.x > 0 and bullet.y < 475 and (bullet.x<x1 or bullet.x>(x1+width1) or bullet.y<y1+yofs or bullet.y>(y1+yofs+height1)):
            bullet.x += bullet.vel
        elif bullet.x < 720 and bullet.x > 0 and bullet.y < 475 and (bullet.x>x1 and bullet.x<(x1+width1+10) and bullet.y>y1+yofs and bullet.y<(y1+yofs+height1)) and not coffin:
            if player == kem or player == bl:
                pygame.mixer.Sound.play(durak_scream)
                health1-=10
                red1+=25.2
                green1-=25.2
            elif player == corona:
                if random.randint(0, 2) == 1:
                    pygame.mixer.Sound.play(csound1)
                else:
                    pygame.mixer.Sound.play(csound2)
                health1-=10
                red1+=9.1
                green1-=9.1
            elif player == xen1:
                pygame.mixer.Sound.play(alien_scream)
                health1-=10
                red1+=25.2
                green1-=25.2
            elif player == atl or player == term:
                health1-=10
                red1+=25.2
                green1-=25.2
            p_blaster.pop(p_blaster.index(bullet))
        else:
            p_blaster.pop(p_blaster.index(bullet))
    #Physics of stones thrown by the right player
    for kamen1 in kamni1:
        if kamen1.x < 720 and kamen1.x > 0 and kamen1.y < 475 and (kamen1.x>(x+width+x_of) or kamen1.x<x+x_of or kamen1.y<y+y_of or kamen1.y>(y+y_of+height)):
            kamen1.x += kamen1.vel
            if kamen1.vert_vel<0:
                kamen1.y-=round((kamen1.vert_vel**2)/20)
            else:
                kamen1.y+=round((kamen1.vert_vel**2)/20)
            kamen1.vert_vel+=1
        #If the player on the left gets hit by a stone
        elif kamen1.x < 720 and kamen1.x > 0 and kamen1.y < 475 and kamen1.x<(x+x_of+width) and kamen1.x>x+x_of and kamen1.y>y+y_of and kamen1.y<(y+y_of+height):
            kamni1.pop(kamni1.index(kamen1))
            health-=10
            red+=25.2
            green-=25.2
        else:
            kamni1.pop(kamni1.index(kamen1))
            
    #Physics of bullets etc (shot by the right player)
    for kamen2 in kamni2:
        if kamen2.x < 720 and kamen2.x > 0 and kamen2.y < 475 and (kamen2.x>(x+x_of+width) or kamen2.x<x+x_of or kamen2.y<y+y_of or kamen2.y>(y+y_of+height)):
            kamen2.x += kamen2.vel
        elif kamen2.x < 720 and kamen2.x > 0 and kamen2.y < 475 and kamen2.x<(x+x_of+width) and kamen2.x>x+x_of and kamen2.y>y+y_of and kamen2.y<(y+y_of+height):
            kamni2.pop(kamni2.index(kamen2))
            health-=10
            red+=25.2
            green-=25.2    
        else:
            kamni2.pop(kamni2.index(kamen2))
    
    
    #Missiles launched by Kem
    for raketa in rakety:
        if raketa.x < 720 and raketa.x > 0 and raketa.y < 475 and (raketa.x>(x+width) or raketa.x<x or raketa.y<y or raketa.y>(y+height)):
            if raketa.vert_vel<0:
                raketa.y-=round((raketa.vert_vel**2)/20)
            elif raketa.vert_vel == 0:
                pygame.mixer.Sound.play(launch)
            else:   
                raketa.x += raketa.vel
                raketa.y+=round((raketa.vert_vel**2)/20)
            raketa.vert_vel+=1
        elif raketa.x < 720 and raketa.x > 0 and raketa.y < 475 and raketa.x<(x+width) and raketa.x>x and raketa.y>y and raketa.y<(y+height):
            rakety.pop(rakety.index(raketa))
            health-=10
            red+=25.2
            green-=25.2    
        else:
            rakety.pop(rakety.index(raketa))
    
    
    #Viruses thrown by the Space Virus
    for virus in viruses:
        if virus.x < 720 and virus.x > 0 and virus.y < 475 and (virus.x>(x+x_of+width) or virus.x<x+x_of or virus.y<y+y_of or virus.y>(y+y_of+height)):
            if virus.vert_vel<0:
                virus.x += (virus.vel+6)
                virus.y-=round((virus.vert_vel**2)/30)
                virus.y+=round(10*math.sin(virus.x))
            else:   
                virus.x += virus.vel+r_speed
                virus.y+=round((virus.vert_vel**2)/80)
                virus.y+=round(10*math.sin(math.radians(virus.x)))
            virus.vert_vel+=1
        elif virus.x < 720 and virus.x > 0 and virus.y < 475 and virus.x<(x+x_of+width) and virus.x>x+x_of and virus.y>y+y_of and virus.y<(y+y_of+height):
            viruses.pop(viruses.index(virus))
            health-=5
            red+=12.6
            green-=12.6
            r_speed = random.randint(-8, 8)
        else:
            viruses.pop(viruses.index(virus))
            r_speed = random.randint(-8, 8)
    
    
    #Isolation arranged by the Space virus
    if home != 0 and home.y < 480:
        home.y += home.vert_vel
        home.vert_vel += 2
        if (0 < home.y < 480) and abs(x+30 - home.x) < 20:
            locked = True
    elif home != 0 and home.y >= 480:
        if home.roof < (home.y-220):
            home.roof += 31
    if locked and round(a, 0) > iso_timex and iso_time != 0:
        iso_time-=1
        iso_timex = round(a, 0)
    elif iso_time == 0:
        home = 0
        locked = False
        iso_time = 14
    
    
    
    ##############  CONTROLLING THE LEFT PLAYER:
    
    if not locked:#that is not in isolation
        #Walking left and right  
        if pressed[pygame.K_LEFT] and x>0 and not neo_b:
            x-= speed
            walking = True
        elif pressed[pygame.K_RIGHT] and x<300 and not neo_b:
            x+= speed
            facing = 1
            walking = True
        else:
            walking = False
            animcount = 0
        #dodging Neo-style
        if pressed[pygame.K_DOWN] and not isJump and not (player == bl or player == atl or player == kem):
            neo_b = True
            height = 77
            width = 135
            x_of = -70
            y_of = +58
        else:
            neo_b = False
            height = 135
            width = 65
            x_of = 0
            y_of = 0
       
        
        #Jumping
        if not isJump and not neo_b:
            if pressed[pygame.K_UP] and a-b>0.7:
                isJump = True
                b=a
        elif not neo_b:
            if jumpSpeed >= -7:
                if jumpSpeed<0:
                    y+=(jumpSpeed**2)/2
                else:
                    y-=(jumpSpeed**2)/2
                jumpSpeed-=(0.5)
            else:
                isJump = False
                jumpSpeed = 7
        
        
        #Throwing stones
        if pressed[pygame.K_SPACE] and len(kamni) < 2 and a-c>0.4 and not coffin and not neo_b and not player == term:
            pygame.mixer.Sound.play(throw)
            if player == bl:
                kamni_inner_list.append(stone(round(x + width/2), round(y + height/2), 5, (255, 0, 0), facing, cabbage)) 
            else:
                kamni_inner_list.append(stone(round(x + width/2), round(y + height/2), 5, (255, 0, 0), facing, stone1))    
            #Store the approximate location of where a stone will land. This will be used by players on the right to dodge the stones sometimes
            kamni_inner_list.append(x+530)
            kamni.append(kamni_inner_list)
            c = a
            kamni_inner_list = []
            
        #Shooting the laser gun
        if pressed[pygame.K_RSHIFT] and p_blast_possible and len(p_blaster) < 1 and a-j>1.5 and not coffin and not (player == bl or player == atl) and not neo_b:
            p_blaster.append(stone(round(x + width), round(y + 40), 8, (27, 149, 255), 2, blastp))
            j = a
            k = a
            p_blast_possible = False
            pygame.mixer.Sound.play(blaster)
        if not p_blast_possible:
            if a-k>1.5 and not (player == bl or player == atl):
                if random.randint(0, 3) == 1 and player != term:
                    p_blast_possible = True
                elif random.randint(0, 2) == 1 and player == term:
                    p_blast_possible = True
                else:
                    p_blast_possible = False    
                    k = a
    #preventing from jumping inside a house
    elif locked and isJump:
        isJump = False
        y = 320
        jumpSpeed = 7
    else:
        #Walking inside a house
        if pressed[pygame.K_LEFT] and x>(home.x-50):
            x-= speed
            walking = True
        elif pressed[pygame.K_RIGHT] and x<(home.x):
            x+= speed
            facing = 1 
            walking = True
        else:
            walking = False 
            animcount = 0
        
        
        
    ################################# BEHAVIOUR OF PLAYERS ON THE RIGHT

    
    #BL-1050
    if player == bl and level == 1:
        level = 1
        height1 = 135
        width1 = 80
        #setting correct values when entered this level
        if not fight:
            health1 = health_d
            y1 = 325
            fight = True
        #jumping
        if a-d > 2 and isJump1:      
            if jumpSpeed1 >= -8:
                if jumpSpeed1<0:
                    y1+=(jumpSpeed1**2)/2
                else:
                    y1-=(jumpSpeed1**2)/2
                jumpSpeed1-=(0.5)
            else:
                isJump1 = False
                jumpSpeed1 = 8            
        elif a-d <= 2:
            isJump1 = False    
        elif a-d > 2 and not isJump:
            if random.randint(0,1) == 1:
                isJump1 = True
            else:
                isJump1 = False
                d = a
 
        #In order to fix y position (which might change due to player switching)
        while y1+height1>460 and isJump1 == False:
            y1-=1
        while y1+height1<460 and isJump1 == False:
            y1+=1
            
        #walking
        if moving:
            if x1>x1t and x1-x1t>speed1:
                x1-=speed1
                moving = True
            elif x1<x1t and x1t-x1>speed1:
                x1+=speed1
                moving = True
            else:
                moving = False
        else:
            h = random.randint(0,3)
            if a-e>2 and (h == 0 or h == 1 or h == 3):            
                x1t = random.randint(380,680)
                moving = True
                e = a
            elif a-e>0 and h == 2:
                #dodge the stones thrown by the left player with certain probability
                #by just walking away from where a stone lands
                if len(kamni)!=0:
                    x1t = (kamni[0][1])-150
                    if (kamni[0][1]) < 690:
                        moving = True
                    else:
                        moving = False
                    if not isJump1:
                        d = a
    
            else:
                moving = False
    
        #Cabbages thrown with certain probability
        if kinul and len(kamni1) < 5 and a-f>0.8 and not coffin:
            kamni1.append(stone(round(x1 + width/2), round(y1 + height/2), 5, (255, 255, 255), -1, cabbage))
            f = a
            pygame.mixer.Sound.play(throw)
            kinul = False
        elif not kinul and len(kamni1) < 5 and a-f>0.8:
            if random.randint(0,50) == 1:
                kinul = True#False
            else:
                kinul = False
        else:
            kinul = False
    
    
    #ABOUT THE SAME LOGICS HOLD FOR ALL OTHER PLAYERS (WITH MINOR MODIFICATIONS)
    
    #######################################################
    #ATL-315
    if player == atl and level == 2:
        level = 2
        height1 = 80
        width1 = 65
        speed1 = 14
        if not fight:
            health1 = health_d
            fight = True
            y1 = 335
            jumpSpeed1 = 7 
        
        if a-d > 1.3 and isJump1:      
            if jumpSpeed1 >= -7:
                if jumpSpeed1<0:
                    y1+=(jumpSpeed1**2)/2
                else:
                    y1-=(jumpSpeed1**2)/2
                jumpSpeed1-=(0.5)
            else:
                isJump1 = False
                jumpSpeed1 = 7           
        elif a-d <= 1.3:
            isJump1 = False    
        elif a-d > 1.3 and not isJump:
            if random.randint(0,2) == 1 and moving:
                isJump1 = True
            else:
                isJump1 = False
                d = a
        
        #In order to fix y position
        while y1+height1>477 and isJump1 == False:
            y1-=1
        #while y1+height1<477 and isJump1 == False:
        #    y1+=1
        if moving and not cof_right:
            if x1>x1t and x1-x1t>speed1:
                x1-=speed1
                moving = True
            elif x1<x1t and x1t-x1>speed1:
                x1+=speed1
                moving = True
            else:
                moving = False
        else:
            h = random.randint(0,8)
            if a-e>1 and h == 0:            
                x1t = random.randint(380,680)
                moving = True
                e = a
            elif a-e>1 and (h == 1 or h == 2 or h == 3 or h == 4 or h == 5 or h == 6 or h == 7):
                if len(kamni)!=0:
                    if (kamni[0][1])>=540:
                        x1t = random.randint(360, 410)
                    else:
                        x1t = random.randint(630, 650)
                    if (kamni[0][1]) < 690:
                        moving = True
                    else:
                        moving = False
                    v = random.randint(0,5)
                    if not isJump1 and (v == 1) :
                        d = a
    
            else:
                moving = False
        
        if kinul2 and len(kamni2) < 1 and a-g>1.5 and not coffin:
            kamni2.append(stone(round(x1 + width/2-10), round(y1 + height/2-15), 8, (230, 230, 255), -2, pygame.transform.flip(blastp, True, False)))
            g = a
            pygame.mixer.Sound.play(blaster)
            kinul2 = False
        elif not kinul2 and len(kamni2) < 1 and a-f>1.5:
            if random.randint(0,80) == 1:
                kinul2 = True #False
            else:
                kinul2 = False
        else:
            kinul2 = False
   

    
    #########################################
    #Kem John-krem
    
    elif player == kem and level == 3:
        level = 3
        height1 = 135
        width1 = 80
        if not fight:
            health1 = health_kem
            fight = True
            y1 = 325
        
        if a-d > 2 and isJump1:      
            if jumpSpeed1 >= -8:
                if jumpSpeed1<0:
                    y1+=(jumpSpeed1**2)/2
                else:
                    y1-=(jumpSpeed1**2)/2
                jumpSpeed1-=(0.5)
            else:
                isJump1 = False
                jumpSpeed1 = 8            
        elif a-d <= 2:
            isJump1 = False
        elif a-d > 2 and not isJump:
            if random.randint(0,1) == 1:
                isJump1 = True
            else:
                isJump1 = False
                d = a
 
        
        #In order to fix y position
        while y1+height1>460 and isJump1 == False:
            y1-=1
        while y1+height1<460 and isJump1 == False:
            y1+=1
        if moving:
            if x1>x1t and x1-x1t>speed1:
                x1-=speed1
                moving = True
            elif x1<x1t and x1t-x1>speed1:
                x1+=speed1
                moving = True
            else:
                moving = False
        else:
            h = random.randint(0,2)
            if a-e>2 and (h == 0 or h == 1):            
                x1t = random.randint(380,680)
                moving = True
                e = a
            elif a-e>0 and h == 2:
                if len(kamni)!=0:
                    x1t = (kamni[0][1])-150
                    if (kamni[0][1]) < 690:
                        moving = True
                    else:
                        moving = False
                    if not isJump1:
                        d = a
            else:
                moving = False
    
        if kinul and len(rakety) < 5 and a-f>0.8 and not coffin:
            rakety.append(rocket(round(x1 + width/2), round(y1 + height/2), missile, -1))
            f = a
            pygame.mixer.Sound.play(throw)
            kinul = False
        elif not kinul and len(kamni1) < 5 and a-f>0.8:
            if random.randint(0,50) == 1:
                kinul = True 
            else:
                kinul = False
        else:
            kinul = False
            
            
    #######################################################
    
    #Xenomorph
    if player == xen1 and level == 4:
        level = 4
        height1 = 135
        width1 = 80
        if not fight:
            health1 = health_d
            fight = True
            y1 = 320
        
        if a-d > 2 and isJump1:      
            if jumpSpeed1 >= -8:
                if jumpSpeed1<0:
                    y1+=(jumpSpeed1**2)/2
                else:
                    y1-=(jumpSpeed1**2)/2
                jumpSpeed1-=(0.5)
            else:
                isJump1 = False
                jumpSpeed1 = 8            
        elif a-d <= 2:
            isJump1 = False    
        elif a-d > 2 and not isJump:
            if random.randint(0,2) == 1:
                isJump1 = True
            else:
                isJump1 = False
                d = a
        if len(p_blaster)!=0 and not isJump1:
            ha = random.randint(0,30)
            if ha == 2: 
                isJump1 = True
                d = a-3
        
        #In order to fix y position
        while y1+height1>460 and isJump1 == False:
            y1-=1
        while y1+height1<460 and isJump1 == False:
            y1+=1
        if moving:
            if x1>x1t and x1-x1t>speed1:
                x1-=speed1
                moving = True
            elif x1<x1t and x1t-x1>speed1:
                x1+=speed1
                moving = True
            else:
                moving = False
        else:
            h = random.randint(0,2)
            if a-e>2 and (h == 0 or h == 1):            
                x1t = random.randint(380,680)
                moving = True
                e = a
            elif a-e>0 and h == 2:
                if len(kamni)!=0:
                    x1t = (kamni[0][1])-150
                    if (kamni[0][1]) < 690:
                        moving = True
                    else:
                        moving = False
                    if not isJump1:
                        d = a
            else:
                moving = False
        
        #Adding face-huggers
        if kinul and len(kamni1) < 5 and a-f>0.8 and not coffin:
            kamni1.append(stone(round(x1 + width/2), round(y1 + height/2), 5, (255, 255, 255), -1, pygame.transform.rotate(xen_s1, -45)))
            f = a
            pygame.mixer.Sound.play(throw)
            kinul = False
        elif not kinul and len(kamni1) < 5 and a-f>0.8:
            if random.randint(0,100) == 1:
                kinul = True
            else:
                kinul = False
        else:
            kinul = False
        
        #Adding acid blood
        if kinul2 and len(kamni2) < 2 and a-g>1 and not coffin:
            kamni2.append(stone(round(x1), round(y1 + 20), 8, (255, 255, 255), -2, xen_s))
            g = a
            pygame.mixer.Sound.play(alien_throw)
            kinul2 = False
        elif not kinul2 and len(kamni2) < 3 and a-f>1:
            if random.randint(0,60) == 1:
                kinul2 = True #False
            else:
                kinul2 = False
        else:
            kinul2 = False
   

    
    #####################################################
    
    #The Space Virus
    elif player == corona and level == 5:
        level = 5
        height1 = coronaheight
        width1 = coronawidth
        if not fight:
            health1 = health_cor
            y1 = 342
            fight = True

        if a-d > 2 and isJump1:      
            if jumpSpeed1 >= -8:
                if jumpSpeed1<0:
                    y1+=(jumpSpeed1**2)/2
                else:
                    y1-=(jumpSpeed1**2)/2
                jumpSpeed1-=(0.5)
            else:
                isJump1 = False
                jumpSpeed1 = 8            
        elif a-d <= 2:
            isJump1 = False    
        elif a-d > 2 and not isJump:
            if random.randint(0,2) == 1:
                isJump1 = True
            else:
                isJump1 = False
                d = a
        
        if len(p_blaster)!=0 and not isJump1:
            ha = random.randint(0,30)
            if ha == 2: 
                isJump1 = True
                d = a-3
        
        #In order to fix y position
        while y1+coronaheight>460 and not isJump1:
            y1-=1
        while y1+coronaheight<460 and not isJump1:
            y1+=1
        if moving:
            if x1>x1t and x1-x1t>speed1:
                x1-=speed1
                moving = True
            elif x1<x1t and x1t-x1>speed1:
                x1+=speed1
                moving = True
            else:
                moving = False
        else:
            h = random.randint(0,2)
            if a-e>2 and (h == 0 or h == 1):            
                x1t = random.randint(380,680)
                moving = True
                e = a
            elif a-e>0 and h == 2:
                if len(kamni)!=0:
                    x1t = (kamni[0][1])-150
                    if (kamni[0][1]) < 690:
                        moving = True
                    else:
                        moving = False
                    if not isJump1:
                        d = a
    
            else:
                moving = False
    
        #little viruses
        if kinul and len(kamni1) < 5 and a-f>0.8 and not coffin:
            viruses.append(stone(round(x1 + width1/2), round(y1 + height1/2), None, None, -1, little_corona))
            f = a
            pygame.mixer.Sound.play(throw)
            kinul = False
        elif not kinul and len(kamni1) < 5 and a-f>0.8:
            if random.randint(0,40) == 1:
                kinul = True#False
            else:
                kinul = False
        else:
            kinul = False
        
        #Isolation
        if isolation and home == 0 and a-g > 15 and x > 20 and not coffin:
            home = house(x+30, -30, (255, 0, 0), 10)
            g = a
            pygame.mixer.Sound.play(isolation_sound)
            isolation = False
        elif not isolation and home == 0 and a-g>15:
            if random.randint(0,2) == 1:
                isolation = True 
            else:
                isolation = False
                g = a
        else:
            isolation = False
            


#######################################################
            
    #Terminator T-800
    if player == term and sit:
        yofs = 56
    else:
        yofs = 0
    if player == term and level == 6:
        level = 6
        if not sit and not isJump1:
            height1 = 135
        elif not sit and isJump1:
            height1 = 80
        elif sit and not isJump:
            height1 = 84
        width1 = 65
        speed1 = 14
        if not fight:
            health1 = health_d
            fight = True
            y1 = 320
            jumpSpeed1 = 7 
        
        if isJump1:      
            if jumpSpeed1 >= -7:
                if jumpSpeed1<0:
                    y1+=(jumpSpeed1**2)/2
                else:
                    y1-=(jumpSpeed1**2)/2
                jumpSpeed1-=(0.5)
            else:
                isJump1 = False
                jumpSpeed1 = 7  
                sit = True
    
        elif a-d > 1.3 and not isJump1 and not sit:
            if random.randint(0,2) == 1 and moving:
                isJump1 = True
            else:
                isJump1 = False
                d = a
 
        
        #In order to fix y position
        while y1+135>460 and not isJump1:
            y1-=1
        while y1+135<460 and not isJump1:
            y1+=1
            
        if moving and not cof_right:
            if x1>x1t and x1-x1t>speed1:
                x1-=speed1
                moving = True
            elif x1<x1t and x1t-x1>speed1:
                x1+=speed1
                moving = True
            else:
                moving = False
        else:
            h = random.randint(0,2)
            if a-e>1 and h == 0 and not sit:            
                x1t = random.randint(380,680)
                moving = True
                e = a
        ha = random.randint(1,3)
        if len(p_blaster)!=0 and ha == 2 and not isJump1 and not sit:
            isJump1 = True
        elif len(p_blaster)!=0 and ha == 1 and not isJump1 and not sit:
            sit = True
            height1 = 84
            
        #Shooting
        if kinul2 and len(kamni2) < 1 and a-g>1.5 and not coffin and not sit:
            kamni2.append(stone(round(x1 + width/2-20), round(y1 + height/2-28), 8, (230, 230, 255), -2, blastt))
            g = a
            pygame.mixer.Sound.play(blaster)
            kinul2 = False
        elif not kinul2 and len(kamni2) < 1 and a-f>1.5:
            if random.randint(0,80) == 1:
                kinul2 = True
            else:
                kinul2 = False
        else:
            kinul2 = False
   

    
    #########################################
        
    #CALLING THE DRAWER TO DRAW A FRAME
    drawer(bg, player)
        #ПCHECK FOR GAME QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    
    
pygame.quit()
