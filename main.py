import sys
import os
from PIL import Image

def check_folder_exist(path):
    if not os.path.exists(path):
        os.mkdir(path)

def JpegToPng(img_path, output_path):
    img = Image.open(img_path)
    img.save(output_path, 'png')

if __name__ == '__main__':
    print('-----start-----')

    img_folder = './origin'
    output_folder = './new'

    # img_folder = sys.argv[1]
    # output_folder = sys.argv[2]

    check_folder_exist(img_folder)
    check_folder_exist(output_folder)

    for filename in os.listdir(img_folder):
        img_path = f'{img_folder}/{filename}'
        output_path = f'{output_folder}/{filename.split(".")[0]}.png'

        JpegToPng(img_path, output_path)


