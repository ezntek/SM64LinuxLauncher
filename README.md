# SM64LinuxLauncher
A launcher for the Super Mario 64 PC Port.

![screenshot](https://cdn.discordapp.com/attachments/775908791417700363/996196405708329030/Screenshot_from_2022-07-11_18-28-18.png?size=4096)

## GNU/Linux installation
1. Install git if you have not already:
 * `sudo apt-get install git` on Debian/Ubuntu based systems,
 * `sudo pacman install git` on arch based systems, or

2. Clone the repo using this command:
`git clone https://github.com/Bloxxel64/SM64LinuxLauncher`.

3. Pipe the installer directly into the python interpreter with this command: `/path/to/your/python -c "$(curl -fsSL https://raw.githubusercontent.com/ezntek/SM64LinuxLauncher/master/setup.py)"`
4. Open the directory in the terminal or file explorer, if you open it in terminal run `python3 launcher.py`. If you run it from your file explorer, just double-click it.

## Manual GNU/Linux Installation (no exact comands because you probably smart)

1. Clone the repo
2. Install the dependencies, which include: 
  1. pip
  2. tk
  3. sdl2 headers
  4. git
  5. mips cross-compiler (optional)
  6. make (gnu make)
3. Install PySimpleGUI through pip
4. profit

## Supported Distros (through the installer)

* `apt` Based Distros (Ubuntu, Debian, Mint, etc.)
* `pacman` Based Distros (EndeavourOS, Arch, Artix, Arco, Manjaro, etc.)

## Windows installation
This repo is focused on Linux. yould be better off using SM64Builder2 or SM64NXBuilder, you can also use the original sm64pclauncher, but it's not recommended.

## Usage
### Running on Linux

type in terminal `python3 launcher.py` (you must be in launcher directory) or  
doubleclick `launcher.py`

### Using it

To build sm64, press "Build"  
To play, select existing build and click "Play"  

## How to build

* In the drop down menu, select a repo. and in the box next to it type the branch.  
* In the second box, type any name you want for your repo folder. it will display like that in the launcher build selection.  
* In the other two boxes you can specify modelpack and texture pack folder. Note: when you browse for the folder, you have to be in this folder to select it.  
* Click "Ok". it will freeze for a while this is because it is downloading the repo. 
* Click "Browse" and find your Super Mario 64 rom. Click "Ok"  
* Specify the build flags, you can find which build flags are avaible for your repo by checking the makefile or checking your repo's wiki if it exists. Optionally, you can add a `-j` argument to set how many simoultaneous build jobs can be done at one time. The guideline is one job for one core and 2GB of ram. Example: `-j4` for a quad-core processor with 8GB of RAM.
* Click "Build". Now wait patiently for the build to finish. When it finishes, game should lauch shortly after. If you see a text box and the game does not launch for like 2 minutes, it means that your build failed. delete the repo folder and try to build again. If the game launches, it is ok. When you restart the launcher, it should show the new build on the list.

### Protip
If you want a shortcut to the laucher, you can do this by making a file called `sm64launcher.desktop` in `/home/username/.local/share/applications/` containing the following:  

```
[Desktop Entry]
Name=SM64 launcher  
Type=Application
Exec=path/into/sm64pclauncher/launcher.py
Categories=Game;  
```
