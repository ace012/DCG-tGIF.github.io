import os
import math
import json
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

    with open(path + "MOC." + mN + ".json") as json_file:
        data = json.load(json_file)

        for t in data["textures"]:
            if t != "texture_00.png" and t != "texture_01.png":
                print mN + ": weird texture file name - " + t

        if data["model"] != "character.dat":
            print mN + ": weird model file name - " + data["model"]

        for m in data["motions"]:
            if data["motions"][m][0]["file"] != mN + "_" + m + ".mtn":
                print mN + ": weird motion file name - " + data["motions"][m][0]["file"]

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
