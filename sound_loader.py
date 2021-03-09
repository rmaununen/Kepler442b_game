import pygame
pygame.mixer.init()


#Звуки
mus_vol = 0.2
eff_vol = 0.5
sliderx1 = 100
sliderx2 = 145

music1 = pygame.mixer.Sound("sounds/music1.wav")
music2 = pygame.mixer.Sound("sounds/music2.wav")
music3 = pygame.mixer.Sound("sounds/music3.wav")
music4 = pygame.mixer.Sound("sounds/music4.wav")
music5 = pygame.mixer.Sound("sounds/music5.wav")
musici = pygame.mixer.Sound("sounds/music_intro.wav")
music_int = pygame.mixer.Sound("sounds/music_int.wav")
button_pressed = pygame.mixer.Sound("sounds/button.wav")
durak_scream = pygame.mixer.Sound("sounds/Scream.wav")
throw = pygame.mixer.Sound("sounds/Throw.wav")
launch = pygame.mixer.Sound("sounds/missile.wav")
blaster = pygame.mixer.Sound("sounds/Blaster.wav")
expl_sound = pygame.mixer.Sound("sounds/expl_sound.wav")
isolation_sound = pygame.mixer.Sound("sounds/isolation.wav")
astronomia = pygame.mixer.Sound("sounds/astronomia.wav")
alien_scream = pygame.mixer.Sound("sounds/Alien1.wav")
alien_throw = pygame.mixer.Sound("sounds/Alien2.wav")
csound1 = pygame.mixer.Sound("sounds/csound1.wav")
csound2 = pygame.mixer.Sound("sounds/csound2.wav")
music1.set_volume(mus_vol)
music2.set_volume(mus_vol)
music3.set_volume(mus_vol)
music4.set_volume(mus_vol-0.1)
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
alien_scream.set_volume(eff_vol-0.45)
alien_throw.set_volume(eff_vol-0.35)
csound1.set_volume(eff_vol-0.45)
csound2.set_volume(eff_vol-0.45)
astronomia.set_volume(mus_vol)