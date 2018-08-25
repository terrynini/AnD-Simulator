from threading import Timer
import time
import subprocess

def attack():
    output = ""
    try:
        subprocess.Popen("python ./attack1.py", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    except:
        pass

if __name__ == '__main__':
    while True:
        time.sleep(60*2)
        attack()
