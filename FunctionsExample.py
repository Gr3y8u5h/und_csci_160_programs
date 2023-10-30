import math


def printMessage():
    print('Sample message in first program using functions')
    print('Anything you can do outside of a function you can do inside a function')
    print()


def areaOfCircle(radius):  # within () put the variables you need to address
    area = radius ** 2 * math.pi
    return area  # leave the function, go back to where you were called
    # print('Area is ', area)


def volumeOfCylinder(radius, height):
    volume = height * areaOfCircle(radius)
    return volume


def areaOfRectangle(length, width):
    area = width * length  # area lives in different scopes so you can reuse.
    return area

def main():
    print()
    x = 10
    radius2 = 10
    area = areaOfCircle(radius2)
    print('The area of the circle is      :', format(area, '10.2f'))

    area = areaOfCircle(100)
    print('The area of the circle is      :', format(area, '10.2f'))
    # printMessage()
    print()

    area = areaOfRectangle(100, 20)
    print('The area of the rectangular is :', format(area, '10.2f'))
    area2 = areaOfRectangle(20, 100)
    print('The area of the rectangular is :', format(area2, '10.2f'))
    # printMessage()
    # print('After the first function call')
    # printMessage()
    # print('After the second function call')
    volume = volumeOfCylinder(10, 20)
    print('The volume of the cylinder is  :', format(volume, '10.2f'))



main()