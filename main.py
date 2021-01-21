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
#while True:
#    music.set_volume(100)
#    music.play_melody("C C G G A A G ", 120)
#    pause(500)
#    music.play_melody("F F E E D D C", 120)
#    pause(500)
#    music.play_melody("G G F F E E D ", 120)
#    pause(500)
#    music.play_melody("G G F F E E D ", 120)
#    pause(500)
#    music.play_melody("C C G G A A G ", 120)
#    pause(500)
#    music.play_melody("F F E E D D C", 120)
#    pause(500)

#Project 3
while True:
    music.set_volume(100)
    if input.light_level() < 20:
        light.set_pixel_color(0, light.rgb(0, 255, 0))  
    elif  input.light_level() < 40:
        light.set_pixel_color(0, light.rgb(20, 245, 0))
    elif input.light_level() < 60:
        light.set_pixel_color(0, light.rgb(40, 225, 0))
    elif input.light_level() < 80:
        light.set_pixel_color(0, light.rgb(60, 195, 0))
    elif input.light_level() < 100:
        light.set_pixel_color(0, light.rgb(80, 175, 0))
    elif input.light_level() < 120:
        light.set_pixel_color(0, light.rgb(110, 135, 0))
    elif input.light_level() < 140:
        light.set_pixel_color(0, light.rgb(140, 110, 0))
    elif input.light_level() < 160:
        light.set_pixel_color(0, light.rgb(170, 90, 0))
    elif input.light_level() < 180:
        light.set_pixel_color(0, light.rgb(200, 45, 0))
    elif input.light_level() < 200:
        light.set_pixel_color(0, light.rgb(255, 0, 0))
        
    if input.light_level() < 10 and input.sound_level() > 125:

        music.wawawawaa.play_until_done() 
        pause(5000)

    elif input.light_level() > 10 and input.sound_level() > 175:
        music.pew_pew.play_until_done()
        pause(5000)

    elif input.sound_level() < 125:
        pause(5000)

    