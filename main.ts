// Challenge 1 
while (true) {
    console.log("Sound level is- " + input.soundLevel())
    if (input.soundLevel() > 150) {
        light.showAnimationFrame(light.rainbowAnimation)
    } else {
        light.clear()
    }
    
}
// Challenge 2
while (true) {
    console.log("Light level is- " + input.lightLevel())
    if (input.lightLevel() > 0) {
        music.setVolume(100)
        music.wawawawaa.play()
    } else {
        light.clear()
    }
    
}
