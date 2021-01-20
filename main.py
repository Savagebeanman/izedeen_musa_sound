#Challenge 1 
#while True:
#    print("Sound level is- " + input.sound_level())
#    if input.sound_level() > 150:
#        light.show_animation_frame(light.rainbowAnimation)
#        pause(3000)
#    else:
#        light.clear()
        
#Challenge 2
#while True:
#    print("Light level is- " + input.light_level())
#    if input.light_level() < 5:
#        music.set_volume(100)
#        music.wawawawaa.play_until_done()    
#    else:
#        light.clear()        

#Challenge 3  
while True:
    music.set_volume(100)
    music.play_melody("C C G G A A G ", 120)
    pause(500)
    music.play_melody("F F E E D D C", 120)
    pause(500)
    music.play_melody("G G F F E E D ", 120)
    pause(500)
    music.play_melody("G G F F E E D ", 120)
    pause(500)
    music.play_melody("C C G G A A G ", 120)
    pause(500)
    music.play_melody("F F E E D D C", 120)
    pause(500)