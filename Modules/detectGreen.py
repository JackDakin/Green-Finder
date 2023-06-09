import os
import cv2
import numpy as np
from PIL import Image

## this is the most important module.
## this module appears to be responsible for the detection of the green colour specifically.

# showimage is a function just to show the image
# if this is not here the image shown would be far too big, this resizes it to something sensible for display and quick
# turn around/problem solving.
def showimage(NAME, im):
    print('\n', NAME)

    size = 1000
    height, width = im.shape[:2]
    #print("\nHeight = {} \nWidth = {}".format(height, width))

    ratio = size / width
    dim = (size, int(height * ratio))
    resize_aspect = cv2.resize(im, dim)

    cv2.imshow(NAME, resize_aspect)


    return


#function for saving mask files
#this one contains the bits such as denoise, and then the colour specificity.
#output is the black and white mask
def do_makemask(name, source, destination):
    src_filename = os.path.join(source, name)
    dst_filename = os.path.join(destination, name)

    # Reading image from folder where it is stored
    img = cv2.imread(src_filename)

    # denoising of image saving it into dst image
    denoised = cv2.fastNlMeansDenoisingColored(img, None, 20, 10, 21, 7)

    # It converts the BGR color space of image to HSV color space
    hsv = cv2.cvtColor(denoised, cv2.COLOR_BGR2HSV)

    # Threshold of green in HSV space
    # for cropping, need to make this part brighter
    # and the green more specific, less yellow
    lower_green = np.array([30, 60, 60])
    upper_green = np.array([60, 255, 255])

    # preparing the mask to overlay
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # should save the mask files to a new directory
    # I think once I have the mask I need to see what the mask file actually looks like, perhaps just with pillow/PIL
    # showimage('Mask', mask)


    try:
        cv2.imwrite(dst_filename, mask)
    except FileExistsError:
        print("Replacing existing file")
        os.remove(dst_filename)
        cv2.imwrite(dst_filename, mask)

    return()

#this must be the function responsible for the counting of all of the white pixels
#the output is the pixel count only, this does not save it to excel.
def countGreen(name, source):
    src_file = os.path.join(source, name)

    # image data
    im = Image.open(src_file).convert('L')


    w, h = im.size
    pix = im.load()

    # Get number of white pixels for current image
    white_pix_count = 0
    for col in range(w):
        for row in range(h):
            if pix[col, row] > 200:
                white_pix_count += 1
            else:
                pass
    print(white_pix_count)
    im.close()

    return white_pix_count
