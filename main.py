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
    if input.sound_level() <= 40:
        light.set.all
    elif  input.sound_level() >= 40:
        light.set_pixel_color(0, light.rgb(0, 255, 0))
        light.set_pixel_color(1, light.rgb(0, 255, 0))
        
    
    elif input.sound_level() > 60:
        light.set_pixel_color(0, light.rgb(0, 255, 0))
        light.set_pixel_color(1, light.rgb(0, 255, 0))  
        light.set_pixel_color(2, light.rgb(20, 245, 0))
        light.set_pixel_color(3, light.rgb(20, 245, 0))

    elif input.sound_level() > 80:
        light.set_pixel_color(0, light.rgb(0, 255, 0))
        light.set_pixel_color(1, light.rgb(0, 255, 0))  
        light.set_pixel_color(2, light.rgb(20, 245, 0))
        light.set_pixel_color(3, light.rgb(20, 245, 0))
        light.set_pixel_color(4, light.rgb(40, 225, 0))
        light.set_pixel_color(5, light.rgb(40, 225, 0))

        light.set_pixel_color(0, light.rgb(0, 255, 0))
        light.set_pixel_color(1, light.rgb(0, 255, 0))  
        light.set_pixel_color(2, light.rgb(20, 245, 0))
        light.set_pixel_color(3, light.rgb(20, 245, 0))
        light.set_pixel_color(4, light.rgb(40, 225, 0))
        light.set_pixel_color(5, light.rgb(40, 225, 0))
        light.set_pixel_color(6, light.rgb(60, 195, 0))
        light.set_pixel_color(7, light.rgb(60, 195, 0))
    
    elif input.sound_level() > 100:

        light.set_pixel_color(0, light.rgb(0, 255, 0))
        light.set_pixel_color(1, light.rgb(0, 255, 0))  
        light.set_pixel_color(2, light.rgb(20, 245, 0))
        light.set_pixel_color(3, light.rgb(20, 245, 0))
        light.set_pixel_color(4, light.rgb(40, 225, 0))
        light.set_pixel_color(5, light.rgb(40, 225, 0))
        light.set_pixel_color(6, light.rgb(60, 195, 0))
        light.set_pixel_color(7, light.rgb(60, 195, 0))
        light.set_pixel_color(8, light.rgb(80, 175, 0))
    
    elif input.sound_level() > 125 and input.light_level() < 10:
        music.wawawawaa.play_until_done()
        pause(5000)
        light.set_pixel_color(0, light.rgb(0, 255, 0))
        light.set_pixel_color(2, light.rgb(51, 204, 0))
        light.set_pixel_color(5, light.rgb(102, 225, 0))
        light.set_pixel_color(5, light.rgb(102, 225, 0))
        light.set_pixel_color(4, light.rgb(153, 175, 0))
        light.set_pixel_color(5, light.rgb(153, 175, 0))
        light.set_pixel_color(6, light.rgb(204, 175, 0))
        light.set_pixel_color(7, light.rgb(204, 175, 0))
        light.set_pixel_color(8, light.rgb(255, 175, 0))
        light.set_pixel_color(9, light.rgb(255, 175, 0))
   
    
        
    if input.light_level() < 10 and input.sound_level() > 125:

        music.wawawawaa.play_until_done() 
        pause(5000)

    elif input.light_level() > 10 and input.sound_level() > 175:
        music.pew_pew.play_until_done()
        pause(5000)

    elif input.sound_level() < 125:
        pause(5000)

    