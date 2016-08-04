#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/6/29 12:30
@annotation = '' 
"""
from PIL import Image


def roll(image, delta):
    "Roll an image sideways"

    xsize, ysize = image.size

    delta = delta % xsize
    if delta == 0:
        return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize - delta, ysize))
    image.paste(part1, (xsize - delta, 0, xsize, ysize))

    return image


def parse(image):
    box = (100, 100, 400, 400)
    region = image.crop(box)
    region = region.transpose(Image.ROTATE_180)
    image.paste(region, box)
    return image


def tran(image):
    image = image.resize((128, 128))
    image = image.rotate(45)  # degrees counter-clockwise
    return image


def qu(image, quan):
    image.save("qu.jpg", quality=quan)


def wepbs(image):
    image.resize((345, 345))
    image.save("web.webp", "WEBP")


file_name = "36fe80963c0b3b9.jpg"
im = Image.open(file_name)
wepbs(im)
