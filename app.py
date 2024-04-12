from math import ceil

def calculate_ttk(health, damage, magazine_size, rpm, reload_speed):
    if damage > health:
        ttk = 0
        return ttk

    rounds_needed = ceil((health / damage) - 1)
    reloads_needed = ceil(rounds_needed / magazine_size) - 1

    if magazine_size == None or reloads_needed == 0:
        ttk = round(rounds_needed / (rpm / 60), 2)
        return ttk

    ttk = round((reloads_needed * reload_speed) + (rounds_needed / (rpm / 60)), 2)
    return ttk
