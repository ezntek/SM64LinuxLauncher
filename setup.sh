#!/bin/bash

until [[ ${ANSWER,,} == "pacman" ]] || [[ ${ANSWER,,} == "apt" ]]; do
	read -p "Use pacman or apt? " ANSWER
done

if [[ ${ANSWER,,} == "pacman" ]]; then
	sudo pacman -S python3 python3-pip python3-tk sdl2_gfx sdl2_image sdl2_mixer sdl2_net git gcc-mips-linux-gnu make
else
	sudo apt-get install -y python3 python3-pip python3-tk libsdl2-dev git gcc-mips-linux-gnu make
fi

pip3 install pysimplegui
pip3 install tk

cp -R src ~/SM64LinuxLauncher
