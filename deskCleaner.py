import os
import shutil

f = open("deskPath.txt", "r")

src_folder = f.readline().strip()
dest_folder = src_folder + f.readline().strip()

allowedSuffixes = ["url", "lnk"]

if not os.path.exists(src_folder):
    print("Source folder path incorrect!")
    exit(1)

if not os.path.exists(dest_folder):
    os.mkdir(dest_folder)

count = 0   # files moved

for filename in os.listdir(src_folder):
    test = filename.split(".")

    if len(test) > 1:  # check if there is a suffix
        if test[1] not in allowedSuffixes:  # check if suffix is on the guest list
            print(filename + " found!\nMove to: /" + test[1])
            if not os.path.exists(dest_folder + test[1]):   # check if we must create directory
                os.mkdir(dest_folder + test[1])
                print("New directory created: /" + test[1])
            shutil.move(os.path.join(src_folder, filename), dest_folder + test[1])
            print(filename + " moved to /" + test[1])
            count += 1
    else:
        print(filename + "is on the guest list.")

if count == 1:
    print(str(count) + " file moved.")
else:
    print(str(count) + " files moved.")
