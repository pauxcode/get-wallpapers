import argparse

parser = argparse.ArgumentParser(description='Search images to use as wallpapers.')
parser.add_argument('-q', '--quality', required=True, help='Give a quality to search: HD, FHD, 2K, 4K.')
args = parser.parse_args()

