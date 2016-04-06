import subprocess

while True:
    for i in range(1,8):
        subprocess.call("omxplayer videos/"+str(i)+".mp4", shell=True)
