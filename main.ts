while (true) {
    console.log("Sound level is -" + input.soundLevel())
    if (input.soundLevel() > 150) {
        light.setAll(light.rgb(255, 255, 255))
    } else {
        light.setAll(light.rgb(0, 0, 0))
    }
    
}
