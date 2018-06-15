#
# Save the images from the lock screen of windows 10
# by luizfnunes
#

import os
from shutil import copyfile

user_profile = os.environ['userprofile']
path  = user_profile+"\\AppData\\Local\\Packages\\"
path += "Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\"
path += "LocalState\\Assets\\"
save_path = "./output/"
files = os.listdir(path)
print("Find {} files in directory!".format(len(files)))
for f in files:
    filename = path+f
    file = open(filename,'rb')
    bin_file = file.read(15) 
    header = "".join(chr(i) for i in bin_file)
    if "JFIF" in header:
        extension = 'jpg'
    elif "PNG" in header:
        extension = 'png'
    else:
        print("File {} is not image JPG or PNG".format(f))
        continue
    if not os.path.isdir(save_path):
        os.mkdir(save_path)
    copyfile(filename,save_path+f+"."+extension)
    print("file {} saved.".format(f))