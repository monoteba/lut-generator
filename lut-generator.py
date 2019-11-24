#!/usr/bin/env python
# coding: UTF-8

# install cv2 with 'pip install opencv-python'
# install numpy with 'pip install numpy' or 'pip install scipy'

import argparse
import math
import sys

import cv2
import numpy as np


def make_image_strip(samples=16, flipy=False):
    """
    Creates the array containing the image data.

    :param samples: The number of samples, should be 16, 32 or 64
    :type samples: int
    :param flipy: Flip the image vertically
    :type flipy: bool
    :return: List of lists containing each image row as a list of [b, g, r]
    :rtype: list of list of [int, int, int]
    """
    s = float(samples)
    mult = 255.0 / (s - 1)

    image = []

    if flipy:
        start = samples - 1
        end = -1
        step = -1
    else:
        start = 0
        end = samples
        step = 1
    
    # cv2 uses bgr instead of rgb
    p = 0.0
    for y in range(start, end, step):
        rows = []
        for x in range(0, samples * samples):
            rows.append([
                int(round((x / samples) * mult)),  # blue
                int(round(y * mult)),  # green
                int(round((x % samples) * mult))  # red
                ])
        image.append(rows)

        p += 1.0
        sys.stdout.write('>> Generating image... %d%%\r' % (p / samples * 100))
        sys.stdout.flush()

    return image

def make_image_square(samples=16, flipy=False):
    """
    Creates the array containing the image data.

    :param samples: The number of samples, should be 16, 64 or 256
    :type samples: int
    :param flipy: Flip the image vertically
    :type flipy: bool
    :return: List of lists containing each image row as a list of [b, g, r]
    :rtype: list of list of [int, int, int]
    """
    s = float(samples)
    root = int(math.sqrt(samples))  # should be 
    mult = 255.0 / (s - 1)

    image = []

    if flipy:
        start = samples * root - 1
        end = -1
        step = -1
    else:
        start = 0
        end = samples * root
        step = 1
    
    # cv2 uses bgr instead of rgb
    p = 0.0
    for y in range(start, end, step):
        rows = []
        for x in range(0, samples * root):
            ri = (x % samples)
            gi = (y % samples)
            bi = int(y / samples * root) + int((x / samples) % root)
            rows.append([
                int(round(bi * mult)),  # blue
                int(round(gi * mult)),  # green
                int(round(ri * mult))  # red
                ])
        image.append(rows)

        p += 1.0
        sys.stdout.write('>> Generating image... %d%%\r' % (p / (samples * root) * 100))
        sys.stdout.flush()

    return image

def write_image(path, image):
    """
    Write the image to disk.

    :param image: Image list generated from make_image()
    :param path: File export path
    :type image: list of list of [b, g, r]
    :type path: string
    """
    sys.stdout.write('\n>> Writing image to disk...\n')
    sys.stdout.flush()

    image = np.array(image)
    
    try:
        if cv2.imwrite(path, image):
            print('>> Done!')
    except Exception as e:
        sys.exit(str(e))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='LUT Texture Generator')

    parser.add_argument('path',
                        type=str,
                        nargs='?',
                        default='lut.png',
                        help='output filename')
    parser.add_argument('-st', '--strip',
                        type=str,
                        nargs='?',
                        default='',
                        help='16, 32 or 64')
    parser.add_argument('-sq', '--square',
                        type=str,
                        nargs='?',
                        default='',
                        help='16, 64 or 256')
    parser.add_argument('-fy', '--flipy',
                        action='store_true',
                        help='Option to flip the image vertically')
    args = parser.parse_args()

    if args.strip and args.square:
        sys.exit('--strip and --square cannot be combined')

    if args.strip:
        if args.strip in ['16', '32', '64']:
            image = make_image_strip(int(args.strip), flipy=args.flipy)
            write_image(args.path, image)
        else:
            sys.exit('Unsupported size: use 16, 32 or 64')

    if args.square:
        if args.square in ['16', '64', '256']:
            image = make_image_square(int(args.square), flipy=args.flipy)
            write_image(args.path, image)
        else:
            sys.exit('Unsupported size: use 16, 64 or 256')




