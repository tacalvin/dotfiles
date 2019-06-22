import glob

for filename in glob.iglob("/home/cta/WallPAPERS/**/*.jpg"):
    print(filename)
