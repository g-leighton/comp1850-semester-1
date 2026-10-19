# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file

with open("../images/feep.pgm", "r") as imagefile:
    
# You can use the relative path ../images/filename
# You could handle file errors with try/except.

# Read the file content
    max_gray_value = 0
    for line in imagefile:
        print(type(line))
        for i in line:
            if type(i) is int and i > max_gray_value:
                max_gray_value = i
                

    print(max_gray_value)           

# print image dimension (i.e., Dimensions: width x height pixels)
    image_dimension = imagefile.readlines()
    image_dimension_array = image_dimension[1:2]

# print max gray value (i.e., Max Gray Value: max_gray_value)
