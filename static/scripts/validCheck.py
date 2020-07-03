import os
import math
from PIL import Image

texturePath = "../Korean"

def checkChild(mN):
    path = texturePath + "/" + mN + "/"
    files = []
    files.append(path + "MOC." + mN + ".json")
    files.append(path + "character.dat")
    files.append(path + mN + "_idle.mtn")
    files.append(path + mN + "_attack.mtn")
    files.append(path + "texture_00.png")

    for f in files:
        if not os.path.isfile(f):
            print mN + ": file not found - " + f

    if os.path.isfile(path + "texture_00.png"):
        img = Image.open(path + "texture_00.png")
        width, height = img.size
        if not math.log(width, 2).is_integer() or not math.log(height, 2).is_integer():
            print mN + ": invalid texture image - texture_00.png"

    if os.path.isfile(path + "texture_01.png"):
        img = Image.open(path + "texture_01.png")
        width, height = img.size
        if not math.log(width, 2).is_integer() or not math.log(height, 2).is_integer():
            print mN + ": invalid texture image - texture_01.png"


def checkSpa(mN):
    path = texturePath + "/" + mN + "/"
    files = []
    files.append(path + "MOC." + mN + ".json")
    files.append(path + "character.dat")
    files.append(path + mN + "_idle.mtn")
    files.append(path + mN + "_touch.mtn")
    files.append(path + mN + "_max.mtn")
    files.append(path + mN + "_maxtouch.mtn")
    files.append(path + "texture_00.png")

    for f in files:
        if not os.path.isfile(f):
            print mN + ": file not found - " + f


def main():
    for mN in next(os.walk(texturePath))[1]:
        if mN[0] == 'c' or mN[0] == 'm':
            checkChild(mN)

        elif mN[0] == 's':
            checkSpa(mN)

        else:
            print mN + ": unknown modelName"


if __name__ == "__main__":
    main()
