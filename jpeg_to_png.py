from PIL import Image
import os
import sys
from pathlib import Path


if not Path(sys.argv[2]).is_dir():
    os.mkdir(sys.argv[2])

image_list = os.listdir(sys.argv[1])

for files in image_list:
    path_to_image_file = sys.argv[1]
    im = Image.open(path_to_image_file + files)
    files = files.replace(".jpg", ".png")
    im.save("./png/" + files, format="png")


