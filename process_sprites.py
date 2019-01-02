import os
from sprite_lib import *
from tqdm import tqdm

sprites_dir = 'sprites/original/'
sprites_dir_new = 'sprites/cropped/'
sprites_dir_ansi = 'sprites/ansi/'

files = os.listdir(sprites_dir)
print(len(files))

names = [f.rpartition('.') for f in files]
names = [n[0] for n in names if n[2]=='png']
names = [n for n in names if n.isnumeric()]
print(len(names))

for n in tqdm(names):
    trans2white(sprites_dir+n+'.png', sprites_dir+n+'.jpg')
    crop_to_contents(sprites_dir+n+'.jpg', sprites_dir_new+n+'.jpg')
    sprite2ansi(sprites_dir_new+n+'.jpg', sprites_dir_ansi+n+'.txt')
