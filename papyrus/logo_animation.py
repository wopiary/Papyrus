import os, time, math, msvcrt,random
import threading
art = """....      ..                                                                           .x+=:.
+^""000h. ~"888h                               ..                                       z`    ^%
0X.  ?0000X  8888f               .d``          @L             .u    .      x.    .          .   <k
'008x  8888X  8888~        u      @8Ne.   .u   9888i   .dL   .d88B :@8c   .@88k  z88u      .@8Ned8"
'88888 8888X   "88x:    us888u.   %8888:u@88N  `Y888k:*888. ="8888f8888r ~"8888 ^8888    .@^%8888"
 `8888 8888X  X88x.  .@88 "8888"   `888I  888.   888E  888I   4888>'88"    8888  888R   x88:  `)8b.
   `*` 8888X '88888X 9888  9888     888I  888I   888E  888I   4888> '      8888  888R   8888N=*8888
  ~`...8888X  "88888 9888  9888     888I  888I   888E  888I   4888>        8888  888R    %8"    R88
   x8888888X.   `%8" 9888  9888   uW888L  888'   888E  888I  .d888L .+     8888 ,888B .   @8Wou 9%
  '%"*8888888h.   "  9888  9888  '*88888Nu88P   x888N><888'  ^"8888*"     "8888Y 8888"  .888888P`
  ~    888888888!`   "888*""888" ~ '88888F`      "88"  888      "Y"        `Y"   'YP    `   ^"F
       X888^""      ^Y"   ^Y'     888 ^              88F
       `88f                         *8E               98"
        88                          '8>             ./"
        ""                           "             ~`"""

def wave_art(delay=0.07):
    shades_of_yellow_ansi = {
        "bright_yellow" : "\033[38;5;226m",
        "orange_yellow" : "\033[38;5;220m",
        "banana_yellow" : "\033[38;5;227m",
        "pale_yellow" : "\033[38;5;228m",
        "very_light_yellow" : "\033[38;5;229m",
    }
    reset_color = "\033[00m"
    shades_of_yellow_ansi_random = random.choice(list(shades_of_yellow_ansi.values()))
    
    print(shades_of_yellow_ansi_random)
    lines = art.splitlines()
    t = 0
    for _ in range(57):
        print("\033[2J\033[H", end=" ")
        for j, line in enumerate(lines):
            offset = int(5 * math.sin(t + j * 0.5))
            print(" " * (offset + 5) + line)
        time.sleep(delay)
        t += 0.3
    print("\033[2J\033[H", end='')
    os.system('cls' if os.name=='nt' else 'clear')
    for line in lines:
        print(line)
