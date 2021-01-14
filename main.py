#Challenge 1 
while True:
    print("Sound level is- " + input.sound_level())
    if input.sound_level() > 150:
        light.show_animation_frame(light.rainbowAnimation)
    else:
        pause(0)
        

#Challenge 2
while True:
    print("Light level is- " + input.light_level())
    if input.light_level() > 0:
        music.set_volume(100)
        music.wawawawaa.play()
    else:
        pause(0)

#Challenge 3