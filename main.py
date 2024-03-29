import shutil
import os
from PIL import Image
from screen_resolutions import resolutions
from directories import origin_path, destiny_path
from argparse_config import args

# ? Make a list of excluded folders

def walk_generator(path, topdown=True):
    for root, dirs, files in os.walk(path, topdown=topdown):
        yield root, dirs, files

def is_valid_image(image, resolution_width, resolution_height):
    return image.width >= resolution_width and resolution_height <= image.height < image.width

def copy_image(image_path, destination_path):
    shutil.copy(image_path, destination_path)

def searcher(origin_path, destiny_path, resolution):
    files_found = 0
    resolution_width, resolution_height = resolution

    for root, dirs, files in walk_generator(origin_path):
        empty_dir = True
        print(f'\n\n\033[0;44mSearching in: {root}\033[0;0m')
        for img in files:
            try:
                if is_valid_image(Image.open(f'{root}/{img}'), resolution_width, resolution_height):
                    copy_image(f'{root}/{img}', f'destiny_path')
                    files_found += 1
                    empty_dir = False
                    print(f'\033[0;92mThe Image:\033[0;0m {img} \033[0;92mwas copied to:\033[0;0m {destiny_path}')
            except OSError as err:
                print(f'\033[0;91mError: {err}\033[0;0m')

        if empty_dir:
            print(f'\033[0;91mNot images found\033[0;0m')

    print(f'\n\nTotal images found: \033[0;92m{files_found}\033[0;0m\n\n')


if __name__ == '__main__':
    resolution = None

    if args.quality.upper() == 'HD':
        resolution = 1
    elif args.quality.upper() == 'FHD':
        resolution = 2
    elif args.quality.upper() == '2K':
        resolution = 3
    elif args.quality.upper() == '4K':
        resolution = 4
    else:
        raise ValueError(f'{args.quality.upper()} is not a valid option. See --help.')

    searcher(origin_path, destiny_path, resolutions[resolution - 1])

