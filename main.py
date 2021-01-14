while True:
    print ("Sound level is -" + input.sound_level())
    if input.sound_level() > 150:
        light.set_all(light.rgb(255,255,255))
    else:
       light.set_all(light.rgb(0,0,0))