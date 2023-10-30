import FileUtils
import math

def main():
    fileName = FileUtils.selectOpenFile('Select shapes file')
    if fileName == None:
        print('No File Selected')
        exit()

    shapesFile = open(fileName, 'r')

    for line in shapesFile:
        line = line.strip()
        commaAt = line.find(',')
        shape = line[0:commaAt]
        info = line[commaAt + 1:]
        if shape == 'circle':
            radius = int(info)
            area = radius ** 2 * math.pi
        elif shape == 'square':
            side = int(info)
            area = side ** 2
        elif shape == 'triangle':
            base, height = info.split(',')
            area = int(base) * int(height) * 0.5
        elif shape == 'rectangle':
            length, width = info.split(',')
            area = int(length) * int(width)
        print(shape, format(area, '1.2f'))

    shapesFile.close()

main()
