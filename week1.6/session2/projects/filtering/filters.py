from image import Image

def blur(img):
    blurred = Image.create(img.width, img.height)
    for row in range(1, img.height - 1):
        for col in range(1, img.width - 1):
           
            pixel_group = [
                img.get(row - 1, col - 1), img.get(row - 1, col), img.get(row - 1, col + 1),
                img.get(row, col - 1),     img.get(row, col),     img.get(row, col + 1),
                img.get(row + 1, col - 1), img.get(row + 1, col), img.get(row + 1, col + 1)
            ]
            
            average_value = sum(pixel_group) // len(pixel_group)
            
            blurred.set(row, col, average_value)
            
    return blurred
            