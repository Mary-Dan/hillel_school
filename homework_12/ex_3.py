def update_hero(**kwargs):
    with open("hero.ini", "r") as f:
        lines = f.readlines()
    hero = {}
    for line in lines:
        key, value = line.strip().split("=")
        hero[key] = value

    for key, value in kwargs.items():
        if key in hero:
            hero[key] = str(value)

    with open("hero.ini", "w") as f:
        for key, value in hero.items():
            f.write(f"{key} = {value}\n")
update_hero(hero="Halk", power=450, Y=2.3)