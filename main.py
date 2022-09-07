from os import walk
from PIL import Image
import shutil

# * Referencia de rutas
#rootPath = '/home/najimi/Ignite/Images/Anime/'
#finalPath = '/home/najimi/Ignite/Images/Wallpapers/'

# ? Tal vez pasar las constantes a otro archivo
HD = [1280, 720]
FULL_HD = [1920, 1080]
ULTRA_HD = [3840, 2160]
CUATRO_K = [4096, 2160]
OCHO_K = [7680, 4320]

QUALITIES = (HD, FULL_HD, ULTRA_HD, CUATRO_K, OCHO_K)


def run(originPath, destinyPath, quality, op_recursive):
    # Todo: Imprimir los ASCII
    emptyDir = 0
    # ? Mejores nombres xd
    quality_width, quality_height = quality
    for (root, dirs, files) in walk(originPath, topdown=op_recursive):
        print(f'\n\n\033[0;44mSearching in: {root}\033[0;0m')

        for img in files:
            imgPath = f'{root}/{img}'
            with Image.open(imgPath) as image:
                width, height = image.size
                if width >= quality_width and height >= quality_height and width > height:
                    shutil.copy(imgPath, f'{destinyPath}{img}')
                    # TODO: Hacer un contador de imagenes encontradas
                    # ? Deberia dejar como esta??
                    emptyDir = True
                    print(
                        f'\033[0;92mThe Image:\033[0;0m {imgPath} \033[0;92mwas copied to:\033[0;0m {destinyPath}')

        if emptyDir == 0:
            print(f'\033[0;91mNot image found\033[0;0m')

        emptyDir = 0


if __name__ == '__main__':
    # * Hacer de esto un menu
    originPath = str(input('Give me the origin path to search: '))
    recursive = str(input('You want to search recursively? (Y/n) '))
    # TODO: Checar que funcione con 'y' minuscula y ponerler un mejor nombre xd
    op_recursive = True if recursive == 'Y' else False
    destinyPath = str(input('Give me the destiny path: '))
    quality = int(input(
        'What quality do you want to look for\n1) HD+\n2) Full HD+\n3) Ultra HD+\n4) 4K+\n5) 8K+\n'))

    # TODO: Buscar como tener rutas por defecto
    run(originPath, destinyPath, QUALITIES[quality-1], op_recursive)
