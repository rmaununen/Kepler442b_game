import pygame

#LOADING IMAGES FROM images FOLDER

bg1 = pygame.image.load("images/bg_lvl1.jpg")
bg2 = pygame.image.load("images/bg_lvl2.jpg")
bg3 = pygame.image.load("images/bg_lvl3.jpg")
bg4 = pygame.image.load("images/bg_lvl4.jpg")
bg5 = pygame.image.load("images/bg_lvl5.jpg")
bg6 = pygame.image.load("images/bg_lvl6.jpg")
bg1_preview = pygame.image.load("images/bg1prev.jpg")
bg2_preview = pygame.image.load("images/bg2prev.jpg")
bg3_preview = pygame.image.load("images/bg3prev.jpg")
bg4_preview = pygame.image.load("images/bg4prev.jpg")
bg5_preview = pygame.image.load("images/bg5prev.jpg")
bg6_preview = pygame.image.load("images/bg6prev.jpg")
outro_preview = pygame.image.load("images/outprev.jpg")
lc1 = pygame.image.load("images/level1card.png")
lc2 = pygame.image.load("images/level2card.png")
lc3 = pygame.image.load("images/level3card.png")
lc4 = pygame.image.load("images/level4card.png")
lc5 = pygame.image.load("images/level5card.png")
lc6 = pygame.image.load("images/level6card.png")
cave = pygame.image.load("images/cave.jpg")
hell1 = pygame.image.load("images/hell1.jpg")
hell2 = pygame.image.load("images/hell2.jpg")
control = pygame.image.load("images/control.png")
control1 = pygame.image.load("images/control1.png")
control2 = pygame.image.load("images/control2.png")
out1 = pygame.image.load("images/out1.jpg")
out2 = pygame.image.load("images/out2.jpg")
out3 = pygame.image.load("images/out3.jpg")
missile = pygame.image.load("images/missile.png")
flame = pygame.image.load("images/flame.png")
jar = pygame.image.load("images/jar1.png")
cabbage = pygame.image.load("images/cabbage.png")
cabbage1 = pygame.image.load("images/cabbage1.png")
kem = pygame.image.load("images/kem1.png")
kem_walk = [pygame.image.load("images/kem1.png"), pygame.image.load("images/kem1.png"), pygame.image.load("images/kem2.png"), pygame.image.load("images/kem3.png"), pygame.image.load("images/kem4.png"), pygame.image.load("images/kem5.png"), pygame.image.load("images/kem6.png"), pygame.image.load("images/kem7.png"), pygame.image.load("images/kem8.png")]
corona = pygame.image.load("images/corona.png")
menu = pygame.image.load("images/menu.jpg")
settings_bg = pygame.image.load("images/settings_bg.jpg")
small_intro_bg = pygame.transform.scale(settings_bg, (80, 53))
stone1 = pygame.transform.scale(pygame.image.load("images/Stone.png"), (20, 17))
stone2 = pygame.transform.scale(pygame.image.load("images/Stone1.png"), (20, 17))
lasergun = pygame.image.load("images/blaster.png")
lasergunL = pygame.transform.flip(lasergun, True, False)
lasergunL1 = pygame.transform.scale(lasergunL, (25, 17))
lasergunL21 = pygame.transform.flip(pygame.image.load("images/blasterT.png"), True, False) 
lasergunL2 = pygame.transform.scale(lasergunL21, (25, 17))
blastp = pygame.image.load("images/blast_p.png")
blastt = pygame.transform.flip(pygame.image.load("images/blast_t.png"), True, False)
little_corona = pygame.image.load("images/coronochka.png")
scene = pygame.image.load("images/scene.jpg")
arrow_r = pygame.image.load("images/arrow.png")
arrow_l = pygame.transform.flip(arrow_r, True, False)
arrow_ar = pygame.image.load("images/arrow_a.png")
arrow_al = pygame.transform.flip(arrow_ar, True, False)

#LISTS FOR ANIMATIONS

blu = pygame.image.load("images/bl1.png")
blu_walk = [pygame.image.load("images/bl1.png"), pygame.image.load("images/bl1.png"), pygame.image.load("images/bl2.png"), pygame.image.load("images/bl3.png"), pygame.image.load("images/bl4.png"),
           pygame.image.load("images/bl5.png"), pygame.image.load("images/bl6.png"), pygame.image.load("images/bl7.png"), pygame.image.load("images/bl8.png")]
bl = pygame.transform.flip(blu, True, False)
bl_walk = []
for image in blu_walk:
    refl = pygame.transform.flip(image, True, False)
    bl_walk.append(refl)
pl_stand = pygame.image.load("images/pla1.png")
pl_small = pygame.transform.scale(pl_stand, (20, 42))
pl_walk = [pygame.image.load("images/pla1.png"), pygame.image.load("images/pla2.png"), pygame.image.load("images/pla3.png"), pygame.image.load("images/pla4.png"),
           pygame.image.load("images/pla5.png"), pygame.image.load("images/pla6.png"), pygame.image.load("images/pla7.png"), pygame.image.load("images/pla8.png")]
neo = [pygame.image.load("images/neo1.png"), pygame.image.load("images/neo2.png"), pygame.image.load("images/neo3.png"), pygame.image.load("images/neo4.png"), pygame.image.load("images/neo5.png"), pygame.image.load("images/neo6.png")]
atl = pygame.image.load("images/a1.png")
atl_walk = [pygame.image.load("images/a1.png"), pygame.image.load("images/a2.png"), pygame.image.load("images/a3.png"), pygame.image.load("images/a4.png"),
           pygame.image.load("images/a5.png"), pygame.image.load("images/a6.png"), pygame.image.load("images/a7.png"), pygame.image.load("images/a8.png")]
a_jump = pygame.image.load("images/a0.png")
ang = 10
atl_jump = []
for i in range (35):
    rotated = pygame.transform.rotate(a_jump, ang)
    atl_jump.append(rotated)
    ang+=10
term = pygame.image.load("images/term1.png")
term_sit1 = pygame.image.load("images/termsit1.png")
term_sit2 = pygame.image.load("images/termsit2.png")
term_walk = [pygame.image.load("images/term1.png"), pygame.image.load("images/term2.png"), pygame.image.load("images/term3.png"), pygame.image.load("images/term4.png"),
           pygame.image.load("images/term5.png"), pygame.image.load("images/term6.png"), pygame.image.load("images/term7.png"), pygame.image.load("images/term8.png")]
t_jump = pygame.transform.scale(pygame.image.load("images/term0.png"), (100, 80))
ang = 10
term_jump = []
for i in range (35):
    rotated = pygame.transform.rotate(t_jump, ang)
    term_jump.append(rotated)
    ang-=10
cof_dance = [pygame.image.load("images/cof1.png"), pygame.image.load("images/cof2.png"), pygame.image.load("images/cof3.png"), pygame.image.load("images/cof4.png"),
           pygame.image.load("images/cof5.png"), pygame.image.load("images/cof6.png")]
fire = [pygame.image.load("images/fire1.png"), pygame.image.load("images/fire2.png"), pygame.image.load("images/fire3.png"), pygame.image.load("images/fire4.png"),
           pygame.image.load("images/fire5.png"), pygame.image.load("images/fire6.png"), pygame.image.load("images/fire7.png"), pygame.image.load("images/fire8.png"), 
           pygame.image.load("images/fire9.png"), pygame.image.load("images/fire10.png")]

smoke = [pygame.image.load("images/IMG_4328.PNG"), pygame.image.load("images/IMG_4329.PNG"), pygame.image.load("images/IMG_4330.PNG"), pygame.image.load("images/IMG_4331.PNG"),
           pygame.image.load("images/IMG_4332.PNG"), pygame.image.load("images/IMG_4333.PNG"), pygame.image.load("images/IMG_4334.PNG"), pygame.image.load("images/IMG_4335.PNG"), pygame.image.load("images/IMG_4336.PNG"), pygame.image.load("images/IMG_4350.PNG"), pygame.image.load("images/IMG_4351.PNG"), pygame.image.load("images/IMG_4352.PNG"),
           pygame.image.load("images/IMG_4353.PNG"), pygame.image.load("images/IMG_4354.PNG"), pygame.image.load("images/IMG_4355.PNG"), pygame.image.load("images/IMG_4356.PNG"), pygame.image.load("images/IMG_4357.PNG"), pygame.image.load("images/IMG_4358.PNG"), pygame.image.load("images/IMG_4359.PNG"), pygame.image.load("images/IMG_4360.PNG"),
           pygame.image.load("images/IMG_4361.PNG"), pygame.image.load("images/IMG_4362.PNG"), pygame.image.load("images/IMG_4363.PNG"), pygame.image.load("images/IMG_4364.PNG"), pygame.image.load("images/IMG_4365.PNG"), pygame.image.load("images/IMG_4366.PNG"), pygame.image.load("images/IMG_4367.PNG"), pygame.image.load("images/IMG_4368.PNG"),
           pygame.image.load("images/IMG_4369.PNG")]
reentry_not_resized = [pygame.image.load("images/frame_00_delay-0.1s.jpg"), pygame.image.load("images/frame_01_delay-0.1s.jpg"), pygame.image.load("images/frame_02_delay-0.1s.jpg"), pygame.image.load("images/frame_03_delay-0.1s.jpg"), pygame.image.load("images/frame_04_delay-0.1s.jpg"), pygame.image.load("images/frame_05_delay-0.1s.jpg"), 
           pygame.image.load("images/frame_06_delay-0.1s.jpg"), pygame.image.load("images/frame_07_delay-0.1s.jpg"), pygame.image.load("images/frame_08_delay-0.1s.jpg"), pygame.image.load("images/frame_09_delay-0.1s.jpg"), pygame.image.load("images/frame_10_delay-0.1s.jpg"), pygame.image.load("images/frame_11_delay-0.1s.jpg"), pygame.image.load("images/frame_12_delay-0.1s.jpg")]
reentry = []
for image in reentry_not_resized:
    correct = pygame.transform.scale(image, (720, 480))
    reentry.append(correct)
expl_not_scaled = [pygame.image.load("images/08_delay-0.01s.png"), pygame.image.load("images/09_delay-0.01s.png"), pygame.image.load("images/10_delay-0.01s.png"), pygame.image.load("images/11_delay-0.01s.png"), pygame.image.load("images/12_delay-0.01s.png"), pygame.image.load("images/13_delay-0.01s.png"), 
           pygame.image.load("images/14_delay-0.01s.png"), pygame.image.load("images/15_delay-0.01s.png"), pygame.image.load("images/16_delay-0.01s.png"), pygame.image.load("images/17_delay-0.01s.png"), pygame.image.load("images/18_delay-0.01s.png"), pygame.image.load("images/19_delay-0.01s.png"), 
           pygame.image.load("images/20_delay-0.01s.png"), pygame.image.load("images/21_delay-0.01s.png"), pygame.image.load("images/22_delay-0.01s.png"), pygame.image.load("images/23_delay-0.01s.png"), pygame.image.load("images/24_delay-0.01s.png")]
explosion = []
for image in expl_not_scaled:
    correct = pygame.transform.scale(image, (110, 157))
    explosion.append(correct)
intro_bg_not_resized = [pygame.image.load("images/intro0.JPG"), pygame.image.load("images/intro1.JPG"), pygame.image.load("images/intro2.JPG"), pygame.image.load("images/intro3.JPG")]
intro_bg = []
for image in intro_bg_not_resized:
    correct = pygame.transform.scale(image, (720, 480))
    intro_bg.append(correct)
cof_dance_refl = []
for image in cof_dance:
    refl = pygame.transform.flip(image, True, False)
    cof_dance_refl.append(refl)
xen1 = pygame.image.load("images/xen1.png")
xenj = pygame.image.load("images/xenj.png")
xen_walk = [pygame.image.load("images/xen1.png"), pygame.image.load("images/xen2.png"), pygame.image.load("images/xen3.png"), pygame.image.load("images/xen4.png"),
           pygame.image.load("images/xen5.png"), pygame.image.load("images/xen6.png"), pygame.image.load("images/xen7.png"), pygame.image.load("images/xen8.png")]
xen_s = pygame.image.load("images/xen_s.png") 
xen_s1 = pygame.image.load("images/xen_s1.png") 
xen_small = pygame.transform.scale(xen1, (25, 50))
