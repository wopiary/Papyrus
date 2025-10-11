
import time
import os
import random
import logo_animation as module_animate
from curses import wrapper
import papyrus_mainfile
import help

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    module_animate.wave_art(delay=0.07)
    colors = {'gold' : "\033[38;5;220m", 'very_light_yellow' : "\033[38;5;229m", 'turquoise' : "\033[38;5;44m", 'clay_red' : "\033[38;5;160m", 'coyote_brown' : "\033[38;2;125;91;63m", 'cactus_green' : "\033[38;2;107;142;35m", 'golden_dune' : "\033[38;2;218;165;105m",
        'sahara_beige' : "\033[38;2;244;196;153m", 'reset_color' : "\033[0m"    }

    print(f"\n\n{colors['very_light_yellow']}Liber scriptum est. Et scientia? Sit libera{colors['reset_color']}")
    print(f"\n{colors['sahara_beige']}==========================================={colors['reset_color']}")
    print(f"{colors['gold']}[1] Start Program{colors['reset_color']}")
    print(f"{colors['turquoise']}[2] Settings{colors['reset_color']}")
    print(f"{colors['clay_red']}[3] ReadME{colors['reset_color']}")
    print(f"{colors['coyote_brown']}[4] Exit Program{colors['reset_color']}")
    print(f"{colors['sahara_beige']}==========================================={colors['reset_color']}")
    user_input = input(f"\n{colors['cactus_green']}➤ Select Option{colors['reset_color']} ")
    if len(user_input.strip()) == 0:
        main()

    match user_input:
        case '1':
            result = papyrus_mainfile.main()
            if result == 'back':
                main()
        case '2':
            pass
        case '3':
            result = help.help_info()
            if result =='back':
                main()
        case '4':
            print(f"{colors['golden_dune']}Exiting...{colors['reset_color']}")
            exit()      
        case _:
            return main()
            
    
main()
