import shutil
from os import walk
from PIL import Image
from screen_resolutions import resolutions


# ? Make a list of excluded folders

# * Route reference
# rootPath = '/home/bridget/Ignite/Images/Anime/'
# finalPath = '/home/bridget/Ignite/Images/Wallpapers/Maybe/'

def menu():
    origin_path = str(input('Give me the path to search: '))
    destiny_path = str(input('Give me the path to save: '))
    resolution = int(input('What quality do you want to look for?\n'
                           '1) HD or higher\n'
                           '2) Full HD or higher\n'
                           '3) Ultra HD or higher\n'
                           '4) 4K or higher\n'
                           '> '))

    # TODO: Search how to have default routes
    searcher(origin_path, destiny_path, resolutions[resolution - 1])


def searcher(origin_path, destiny_path, resolution):
    # Todo: Print ASCII
    empty_dir = 0
    files_found = 0
    resolution_width, resolution_height = resolution

    for (root, dirs, files) in walk(origin_path, topdown=True):
        print(f'\n\n\033[0;44mSearching in: {root}\033[0;0m')

        for img in files:
            try:
                img_path = f'{root}/{img}'
                with Image.open(img_path) as image:
                    width, height = image.size
                    if width >= resolution_width and resolution_height <= height < width:
                        # width >= quality_width and height >= quality_height and width > height:
                        shutil.copy(img_path, f'{destiny_path}{img}')
                        # ? Should I quit?
                        empty_dir = True
                        files_found += 1
                        print(f'\033[0;92mThe Image:\033[0;0m {img_path} \033[0;92mwas copied to:\033[0;0m {destiny_path}')
            except OSError as err:
                print(f'Error: {err}')

        if empty_dir == 0:
            print(f'\033[0;91mNot image found\033[0;0m')

        empty_dir = 0

    print(f'\n\nTotal images found: \033[0;92m{files_found}\033[0;0m\n\n')


if __name__ == '__main__':
    while True:
        print('\033[0;96mWelcome to my program to search for possible wallpapers\033[0;0m\n')
        menu_op = str(input('Do you want to start? (Y/n): '))

        if menu_op == 'n':
            print('Good bye, see you later')
            break

        menu()
    # * Export libraries
