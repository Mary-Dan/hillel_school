def update_hero(**kwargs):
    with open("hero.ini", "r") as f:
        lines = f.readlines()
    hero_data = {}
    for line in lines:
        key, value = line.strip().split("=")
        hero_data[key] = value

    for key, value in kwargs.items():
        if key in hero_data:
            hero_data[key] = str(value)

    with open("hero.ini", "w") as f:
        for key, value in hero_data.items():
            f.write(f"{key} = {value}\n")
update_hero(hero="Halk", power=450, Y=2.3)