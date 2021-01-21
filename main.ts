// Challenge 1 
// while True:
//     print("Sound level is- " + input.sound_level())
//     if input.sound_level() > 150:
//         light.show_animation_frame(light.rainbowAnimation)
//         pause(3000)
//     else:
//         light.clear()
// Challenge 2
// while True:
//     print("Light level is- " + input.light_level())
//     if input.light_level() < 5:
//         music.set_volume(100)
//         music.wawawawaa.play_until_done()    
//     else:
//         light.clear()        
// Challenge 3  
// while True:
//     music.set_volume(100)
//     music.play_melody("C C G G A A G ", 120)
//     pause(500)
//     music.play_melody("F F E E D D C", 120)
//     pause(500)
//     music.play_melody("G G F F E E D ", 120)
//     pause(500)
//     music.play_melody("G G F F E E D ", 120)
//     pause(500)
//     music.play_melody("C C G G A A G ", 120)
//     pause(500)
//     music.play_melody("F F E E D D C", 120)
//     pause(500)
// Project 3
while (true) {
    music.setVolume(100)
    if (input.soundLevel() <= 40) {
        light
    } else if (input.soundLevel() >= 40) {
        light.setPixelColor(0, light.rgb(0, 255, 0))
        light.setPixelColor(1, light.rgb(0, 255, 0))
    } else if (input.soundLevel() > 60) {
        light.setPixelColor(0, light.rgb(0, 255, 0))
        light.setPixelColor(1, light.rgb(0, 255, 0))
        light.setPixelColor(2, light.rgb(20, 245, 0))
        light.setPixelColor(3, light.rgb(20, 245, 0))
        light.setPixelColor(4, light.rgb(40, 225, 0))
        light.setPixelColor(5, light.rgb(40, 225, 0))
    } else if (input.soundLevel() > 80) {
        light.setPixelColor(0, light.rgb(0, 255, 0))
        light.setPixelColor(1, light.rgb(0, 255, 0))
        light.setPixelColor(2, light.rgb(20, 245, 0))
        light.setPixelColor(3, light.rgb(20, 245, 0))
        light.setPixelColor(4, light.rgb(40, 225, 0))
        light.setPixelColor(5, light.rgb(40, 225, 0))
        light.setPixelColor(6, light.rgb(60, 195, 0))
        light.setPixelColor(7, light.rgb(60, 195, 0))
    } else if (input.soundLevel() > 100) {
        light.setPixelColor(0, light.rgb(0, 255, 0))
        light.setPixelColor(1, light.rgb(0, 255, 0))
        light.setPixelColor(2, light.rgb(20, 245, 0))
        light.setPixelColor(3, light.rgb(20, 245, 0))
        light.setPixelColor(4, light.rgb(40, 225, 0))
        light.setPixelColor(5, light.rgb(40, 225, 0))
        light.setPixelColor(6, light.rgb(60, 195, 0))
        light.setPixelColor(7, light.rgb(60, 195, 0))
        light.setPixelColor(4, light.rgb(80, 175, 0))
    } else if (input.soundLevel() > 125 && input.lightLevel() < 10) {
        music.wawawawaa.playUntilDone()
        pause(5000)
        light.setPixelColor(0, light.rgb(0, 255, 0))
        light.setPixelColor(1, light.rgb(20, 245, 0))
        light.setPixelColor(2, light.rgb(40, 225, 0))
        light.setPixelColor(3, light.rgb(60, 195, 0))
        light.setPixelColor(4, light.rgb(80, 175, 0))
        light.setPixelColor(5, light.rgb(110, 135, 0))
    }
    
    if (input.lightLevel() < 10 && input.soundLevel() > 125) {
        music.wawawawaa.playUntilDone()
        pause(5000)
    } else if (input.lightLevel() > 10 && input.soundLevel() > 175) {
        music.pewPew.playUntilDone()
        pause(5000)
    } else if (input.soundLevel() < 125) {
        pause(5000)
    }
    
}
