from sprite_lib import *

logo_dir = 'sprites/logo/'

trans2white(logo_dir+'logo.png', logo_dir+'logo.jpg')
crop_to_contents(logo_dir+'logo.jpg', logo_dir+'croppedlogo.jpg')
sprite2ansi(logo_dir+'croppedlogo.jpg', logo_dir+'ansilogo.txt')
