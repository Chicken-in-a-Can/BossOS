from os import system
import subprocess

OUTPUT = subprocess.check_output('xfconf-query -c xfce4-desktop -p /backdrop/screen0 -l | grep "last-image"', shell=True)

OUTPUT = OUTPUT.split(b"\n")

for walls in OUTPUT:
    walls = walls.decode("UTF-8")
    walls = "xfconf-query -c xfce4-desktop -p "+walls+" -s ~/Downloads/BossOS/Configs/bossOSWallpaper1.jpg"
    system(walls)
