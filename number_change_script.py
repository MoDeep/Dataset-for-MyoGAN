import os

i = 0

for filename in os.listdir("."):
    if filename.startswith("hand"):
        os.rename(filename, filename[0:4] + str(i).zfill(5) + ".png")
        i += 1
