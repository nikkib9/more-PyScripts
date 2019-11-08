#!python3

import subprocess, datetime

# vboxApp = "/usr/bin/virtualbox"
kali = "virtualbox /media/cole/D2D46F31D46F174F/Cole/VMs/Kali-19.3/Kali-19.3.vbox"
ubuntu = "virtualbox /media/cole/D2D46F31D46F174F/Cole/VMs/Ubuntu 19_Full_50/Ubuntu 19_Full_50.vbox"

vboxDict = {(0, 8):"logs", (0, 13):"networks",
    (1, 8):"systems",(2, 8):"logs", (2, 13):"networks",
    (3, 8):"systems", (4, 13):"python"}

#get the date and hour at runtime
def dh():
    dt = datetime.datetime
    time = dt.today()
    day = time.weekday()
    hour = time.hour

    return [day, hour]

def vbox(time):
    for key in vboxDict:
        if key == time:
            return key

def main():
    time = dh()
    vm = vbox(time)

    file = subprocess.Popen(vm, shell = True)
    print(file)

if __name__ == "__main__":
    main()
