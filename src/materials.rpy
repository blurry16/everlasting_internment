init 1:
    $ NOTHING_PATH = "mods/everlasting_internment/materials/nothing.png"

    $ config.developer = True

    $ rm = Character(u"Рома", color="#f8b05e", what_color="E2C778")
    $ rm_scores = 0

    $ vi = Character(u'Вика', color="#ee4a3e", what_color="E2C778")
    image vi normal pioneer = initsprite("mods/everlasting_internment/materials/sprites/vi_normal_pioneer.png")
    image vi happy pioneer = initsprite("mods/everlasting_internment/materials/sprites/vi_happy_pioneer.png")

    
    $ le = Character(u'Андрей', color="#2791d8", what_color="E2C778")
    image le normal pioneer = initsprite("mods/everlasting_internment/materials/sprites/le_normal_pioneer.png")
    image le happy pioneer = initsprite("mods/everlasting_internment/materials/sprites/le_happy_pioneer.png")



    $ sn = Character(u"Соня", color="#e00bc4", what_color="E2C778")
    image sn happy pioneer = initsprite("mods/everlasting_internment/materials/sprites/sn_happy_pioneer.png")
    image sn confused pioneer = initsprite("mods/everlasting_internment/materials/sprites/sn_confused_pioneer.png")


init 0 python:
    from os import path


    def initsprite(sprite_path):
        global NOTHING_PATH
        return ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), sprite_path,
            (0, 0), NOTHING_PATH), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), sprite_path,
            (0, 0), NOTHING_PATH), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), sprite_path, (0, 0), NOTHING_PATH)
        )

    
    MOD_ID = "label_selector" if config.developer else "prolog_dream"
    MOD_NAME = "Бесконечный Концлагерь"
    COLOR_SPRITES = False # True

    mods[MOD_ID] = MOD_NAME

    for file in renpy.list_files():
        if MOD_ID in file:
            file_name = path.splitext(path.basename(file))[0]
            file_split = file.split("/")

            if file.endswith((".png", ".jpg")):
                if "sprites" in file_split:
                    renpy.image(
                        file_name,
                        ConditionSwitch(
                            "persistent.sprite_time == 'sunset'",
                            im.MatrixColor(
                                file,
                                im.matrix.tint(0.94, 0.82, 1.0)
                            ),
                            "persistent.sprite_time == 'night'",
                            im.MatrixColor(
                                file,
                                im.matrix.tint(0.63, 0.78, 0.82)
                            ),
                            True,
                            file
                        )
                    )
                else:
                    renpy.image(file_name, file)
            elif file.endswith((".wav", ".mp2", ".mp3", ".ogg", ".opus")):
                globals()[file_name] = file
