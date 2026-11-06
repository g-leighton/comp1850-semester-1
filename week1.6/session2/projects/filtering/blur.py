from image import Image
from filters import blur
import sys

img = Image.read(sys.argv[1])

blurred_img = blur(img)

blurred_img.write_pgm(sys.argv[2])
