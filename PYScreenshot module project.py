##write a program to take a screenshot of current screen after some time interval
import time
import pyscreenshot as p
import winsound as w
import os
no = 5
s="ssop"
os.makedirs(s,exist_ok=True)
for i in range (no):
    img = p.grab()
    filename=os.path.join(s,f"screenshot{i}.png")
    img.save(filename)
    if i<no:
        w.Beep(1000,200)
        time.sleep(3)

