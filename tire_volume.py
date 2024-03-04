#I added a couple input areas for more information about the car the tires were on. Then I made sure the first letters were capitalized. 
#Then they were printed to the volumes.txt page as well.

import math
from datetime import datetime

width = int(input(f'Enter the width of the tire in mm (ex 205):'))
ratio = int(input(f'Enter the aspect ratio of the tire (ex 60): '))
wheel = int(input(f'Enter the diameter of the wheel in inches (ex 15):'))
make = input('Enter the make of your car:')
model = input('Enter the model of your car:')

v = (math.pi * width**2 * (ratio * ( width * ratio + (2540 * wheel))))/ 10000000000

print (f'The aprox volume of the tire is: {v:.2f}')

#Gets the current date from the computer’s operating system.
date = datetime.now()

#Opens a text file named volumes.txt for appending.
with open("volumes.txt", "at") as volume:

    print(f'Date: {date.year}/{date.day}/{date.month}, Width: {width}, Ratio: {ratio}, Diameter: {wheel}, Volume: {v:.2f}', file = volume)
    print(f'This tire is from a {make.capitalize()} {model.capitalize()}', file = volume)
