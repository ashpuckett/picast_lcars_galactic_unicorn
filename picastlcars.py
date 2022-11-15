import time
from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN as DISPLAY
from random import randint

gu = GalacticUnicorn()
graphics = PicoGraphics(DISPLAY)

gu.set_brightness(0.3)
width = GalacticUnicorn.WIDTH
height = GalacticUnicorn.HEIGHT

@micropython.native  # noqa: F821
def picars():

#Row 1
    graphics.set_pen(graphics.create_pen(int(65), int(208), int(194)))
    graphics.pixel(1, 1)
    graphics.pixel(2, 1)
    graphics.pixel(3, 1)
    graphics.pixel(4, 1)
    graphics.pixel(5, 1)
    graphics.pixel(6, 1)
    graphics.set_pen(graphics.create_pen(int(249), int(215), int(119)))
    graphics.pixel(31, 1)
    graphics.pixel(32, 1)
    graphics.pixel(33, 1)
    graphics.pixel(35, 1)
    graphics.pixel(37, 1)
    graphics.pixel(38, 1)
    graphics.pixel(39, 1)
    graphics.pixel(41, 1)
    graphics.pixel(42, 1)
    graphics.pixel(43, 1)
    graphics.pixel(45, 1)
    graphics.pixel(46, 1)
    graphics.pixel(47, 1)

    graphics.pixel(49, 1)
    graphics.pixel(50, 1)
    graphics.pixel(51, 1)

#Row 2

    graphics.set_pen(graphics.create_pen(int(65), int(208), int(194)))
    graphics.pixel(1, 2)
    graphics.pixel(2, 2)
    graphics.pixel(3, 2)
    graphics.pixel(4, 2)
    graphics.pixel(5, 2)
    graphics.pixel(6, 2)
    graphics.set_pen(graphics.create_pen(int(213), int(80), int(124)))
    graphics.pixel(10, 2)
    graphics.pixel(11, 2)
    graphics.pixel(12, 2)
    graphics.pixel(13, 2)
    graphics.pixel(14, 2)
    graphics.pixel(15, 2)
    graphics.pixel(16, 2)
    graphics.pixel(17, 2)
    graphics.pixel(18, 2)
    graphics.set_pen(graphics.create_pen(int(249), int(215), int(119)))
    graphics.pixel(31, 2)
    graphics.pixel(33, 2)
    graphics.pixel(35, 2)
    graphics.pixel(37, 2)
    graphics.pixel(41, 2)
    graphics.pixel(43, 2)
    graphics.pixel(45, 2)
    graphics.pixel(46, 2)
    graphics.pixel(50, 2)

# Row 3

    graphics.set_pen(graphics.create_pen(int(65), int(208), int(194)))
    graphics.pixel(1, 3)
    graphics.pixel(2, 3)
    graphics.pixel(3, 3)
    graphics.pixel(4, 3)
    graphics.pixel(5, 3)
    graphics.pixel(6, 3)
    graphics.set_pen(graphics.create_pen(int(213), int(80), int(124)))
    graphics.pixel(10, 3)
    graphics.pixel(11, 3)
    graphics.pixel(12, 3)
    graphics.pixel(13, 3)
    graphics.pixel(14, 3)
    graphics.pixel(15, 3)
    graphics.pixel(16, 3)
    graphics.pixel(17, 3)
    graphics.pixel(18, 3)
    graphics.set_pen(graphics.create_pen(int(249), int(215), int(119)))
    graphics.pixel(31, 3)
    graphics.pixel(32, 3)
    graphics.pixel(33, 3)
    graphics.pixel(35, 3)
    graphics.pixel(37, 3)
    graphics.pixel(41, 3)
    graphics.pixel(42, 3)
    graphics.pixel(43, 3)
    graphics.pixel(46, 3)
    graphics.pixel(47, 3)
    graphics.pixel(50, 3)

# Row 4

    graphics.set_pen(graphics.create_pen(int(65), int(208), int(194)))
    graphics.pixel(1, 4)
    graphics.pixel(2, 4)
    graphics.pixel(3, 4)
    graphics.pixel(4, 4)
    graphics.pixel(5, 4)
    graphics.pixel(6, 4)
    graphics.set_pen(graphics.create_pen(int(249), int(215), int(119)))
    graphics.pixel(31, 4)
    graphics.pixel(35, 4)
    graphics.pixel(37, 4)
    graphics.pixel(38, 4)
    graphics.pixel(39, 4)
    graphics.pixel(41, 4)
    graphics.pixel(43, 4)
    graphics.pixel(45, 4)
    graphics.pixel(46, 4)
    graphics.pixel(47, 4)
    graphics.pixel(50, 4)

# Row 5

    graphics.set_pen(graphics.create_pen(int(65), int(208), int(194)))
    graphics.pixel(1, 5)
    graphics.pixel(2, 5)
    graphics.pixel(3, 5)
    graphics.pixel(4, 5)
    graphics.pixel(5, 5)
    graphics.pixel(6, 5)
    graphics.set_pen(graphics.create_pen(int(213), int(80), int(124)))
    graphics.pixel(10, 5)
    graphics.pixel(11, 5)
    graphics.pixel(12, 5)
    graphics.pixel(13, 5)
    graphics.pixel(14, 5)
    graphics.pixel(15, 5)
    graphics.pixel(16, 5)
    graphics.pixel(17, 5)
    graphics.pixel(18, 5)

# Row 6

    graphics.set_pen(graphics.create_pen(int(65), int(208), int(194)))
    graphics.pixel(1, 6)
    graphics.pixel(2, 6)
    graphics.pixel(3, 6)
    graphics.pixel(4, 6)
    graphics.pixel(5, 6)
    graphics.pixel(6, 6)
    graphics.set_pen(graphics.create_pen(int(213), int(80), int(124)))
    graphics.pixel(10, 6)
    graphics.pixel(11, 6)
    graphics.pixel(12, 6)
    graphics.pixel(13, 6)
    graphics.pixel(14, 6)
    graphics.pixel(15, 6)
    graphics.pixel(16, 6)
    graphics.pixel(17, 6)
    graphics.pixel(18, 6)

#Row 7

    graphics.set_pen(graphics.create_pen(int(65), int(208), int(194)))
    graphics.pixel(1, 7)
    graphics.pixel(2, 7)
    graphics.pixel(3, 7)
    graphics.pixel(4, 7)
    graphics.pixel(5, 7)
    graphics.pixel(6, 7)
    graphics.pixel(7, 7)
    
# Row 8

    graphics.set_pen(graphics.create_pen(int(65), int(208), int(194)))
    graphics.pixel(2, 8)
    graphics.pixel(3, 8)
    graphics.pixel(4, 8)
    graphics.pixel(5, 8)
    graphics.pixel(6, 8)
    graphics.pixel(7, 8)
    graphics.pixel(8, 8)
    graphics.pixel(9, 8)
    graphics.pixel(10, 8)
    graphics.pixel(11, 8)
    graphics.pixel(12, 8)
    graphics.pixel(13, 8)
    graphics.pixel(14, 8)
    graphics.pixel(15, 8)
    graphics.pixel(16, 8)
    graphics.pixel(17, 8)
    graphics.pixel(18, 8)
    graphics.pixel(19, 8)
    graphics.pixel(20, 8)
    graphics.pixel(21, 8)
    graphics.pixel(22, 8)
    graphics.pixel(23, 8)
    graphics.pixel(24, 8)
    graphics.pixel(25, 8)
    graphics.pixel(26, 8)
    graphics.pixel(27, 8)
    graphics.pixel(28, 8)
    graphics.pixel(29, 8)
    graphics.pixel(30, 8)
    graphics.pixel(31, 8)
    graphics.pixel(32, 8)
    graphics.pixel(33, 8)
    graphics.pixel(34, 8)
    graphics.pixel(35, 8)
    graphics.pixel(36, 8)
    graphics.pixel(37, 8)
    graphics.pixel(38, 8)
    graphics.pixel(39, 8)
    graphics.set_pen(graphics.create_pen(int(249), int(215), int(119)))
    graphics.pixel(41, 8)
    graphics.pixel(42, 8)
    graphics.set_pen(graphics.create_pen(int(213), int(80), int(124)))
    graphics.pixel(44, 8)
    graphics.pixel(45, 8)
    graphics.pixel(46, 8)
    graphics.pixel(47, 8)
    graphics.pixel(48, 8)
    graphics.pixel(49, 8)
    graphics.pixel(50, 8)
    graphics.pixel(51, 8)
    
# Row 9

    graphics.set_pen(graphics.create_pen(int(65), int(208), int(194)))
    graphics.pixel(4, 9)
    graphics.pixel(5, 9)
    graphics.pixel(6, 9)
    graphics.pixel(7, 9)
    graphics.pixel(8, 9)
    graphics.pixel(9, 9)
    graphics.pixel(10, 9)
    graphics.pixel(11, 9)
    graphics.pixel(12, 9)
    graphics.pixel(13, 9)
    graphics.pixel(14, 9)
    graphics.pixel(15, 9)
    graphics.pixel(16, 9)
    graphics.pixel(17, 9)
    graphics.pixel(18, 9)
    graphics.pixel(19, 9)
    graphics.pixel(20, 9)
    graphics.pixel(21, 9)
    graphics.pixel(22, 9)
    graphics.pixel(23, 9)
    graphics.pixel(24, 9)
    graphics.pixel(25, 9)
    graphics.pixel(26, 9)
    graphics.pixel(27, 9)
    graphics.pixel(28, 9)
    graphics.pixel(29, 9)
    graphics.pixel(30, 9)
    graphics.pixel(31, 9)
    graphics.pixel(32, 9)
    graphics.pixel(33, 9)
    graphics.pixel(34, 9)
    graphics.pixel(35, 9)
    graphics.pixel(36, 9)
    graphics.pixel(37, 9)
    graphics.pixel(38, 9)
    graphics.pixel(39, 9)
    graphics.set_pen(graphics.create_pen(int(249), int(215), int(119)))
    graphics.pixel(41, 9)
    graphics.pixel(42, 9)
    graphics.set_pen(graphics.create_pen(int(213), int(80), int(124)))
    graphics.pixel(44, 9)
    graphics.pixel(45, 9)
    graphics.pixel(46, 9)
    graphics.pixel(47, 9)
    graphics.pixel(48, 9)
    graphics.pixel(49, 9)
    graphics.pixel(50, 9)
    graphics.pixel(51, 9)
    
    gu.update(graphics)
while True:
    picars()
