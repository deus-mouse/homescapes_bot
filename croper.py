from PIL import Image
import os
import time


def crop(path, input, height, width, area):
    index_1 = 0
    index_2 = 0
    im = Image.open(input)
    a = im.crop(area)
    img_width, img_height = a.size
    a.show()
    for i in range(0, img_height, height):
        for j in range(0, img_width, width):
            box = (j, i, j+width, i+height)
            b = a.crop(box)
            try:
                o = b.crop()
                # o.show()
                index = '[' + str(index_1) + '][' + str(index_2) + ']'
                full_path = os.path.join(path, "IMG-%s.png" % index)
                print(full_path)
                o.save(full_path, 'PNG')
                print('save')
            except Exception as ex:
                print('except', ex)
                pass
            if index_2 == 13:
                index_2 = 0
                index_1 += 1
            else:
                index_2 += 1

center_x = 706
center_y = 384
box_side = 68

area = (center_x - box_side * 7, center_y - box_side * 5,
        center_x + box_side * 7, center_y + box_side * 5)
# crop('/Users/roman/Documents/Documents_iMac/CodeProjects/PythonProjects/Homescapes_bot/needles/crop', 'needles/table3.png', 68, 68, 1, area)

crop('/Users/roman/Documents/Documents_iMac/CodeProjects/PythonProjects/Homescapes_bot/needles/crops', 'needles/table3.png', 68, 68, area)


