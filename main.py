from PIL import Image

IMAGE_PATH = 'inara.jpeg'
ASCII = '@#S%?*+;:,. '[::-1]
SCALE = 190

image = Image.open(IMAGE_PATH)


image = image.convert('L')
image = image.convert('RGB')

size_x, size_y = image.size

new_size = (SCALE, SCALE * size_y // size_x)
new_size_x, new_size_y = new_size

image = image.resize(new_size, Image.ANTIALIAS)

ascii_range = 255/len(ASCII)

file = open('result.txt', 'w')

line_break = 0

for pixel in image.getdata():
        index = int(round(pixel[0] / ascii_range)) - 1
        char = ASCII[index]
        file.write(char + ' ')
        line_break += 1
        if line_break == SCALE:
            line_break = 0
            file.write('\n')

