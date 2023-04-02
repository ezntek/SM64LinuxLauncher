#!/usr/bin/env python
import subprocess
import shutil
import os

def setup() -> None:
    while True: # start a loop
        ans: str = input("Use pacman or apt? ")
        if ans.lower() == "pacman":
            # use su
            r = subprocess.run('su -c "pacman -S python3\
                                python3-pip\
                                python3-tk\
                                sdl2_gfx\
                                sdl2_image\
                                sdl2_mixer\
                                sdl2_net\
                                git\
                                gcc-mips-linux-gnu\
                                make"', shell=True).returncode
            if r == 127: # on failure
                print("An error has occured when running a command! please try again later.")
                exit()
            break

        elif ans.lower() == "apt":
            r = subprocess.run('su -c "apt-get install python3\
                                                python3-pip\
                                                python3-tk\
                                                libsdl2-dev\
                                                git\
                                                gcc-mips-linux-gnu\
                                                make"', shell=True).returncode
            if r == 127: # on failure
                print("An error has occured when running a command! please try again later.")
                exit()
            break
        else:
            print("Invalid Answer, try again!")
        # return to top
    
    subprocess.run(["python3", "-m", "pip", "install", "pysimplegui"])
    shutil.copytree("./src", f"{os.environ['HOME']}/SM64LinuxLauncher") # copy into home folder

if __name__ == "__main__":
    setup()
