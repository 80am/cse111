import math

def main():
    #storage_efficiency = volume/surface_area
    
    #my_dict = {{"Picnic": {6.83: 10.16}: "$0.28"}, "" 7.78: 8.73: 10.32: 10.79: 13.02: 5.40:8.89, 6.83:7.62, 15.72:17.78, 6.83:12.38, 7.62:11.27, 8.10:11.11}
    
    #for key in my_dict.items():

    name = '#1 picnic'
    radius = 6.83
    height = 10.16
    cost = "$0.28"
    
    x = compute_volume(radius , height)
    y = compute_surface_area(radius, height)

    effeciency = x / y 
    print(f'This is the one we want: {name}, {effeciency:.2f}')



    name = 'tall'
    volume = math.pi*radius**2 * height
    print(name , effeciency)


    compute_volume(radius,height)
    compute_surface_area(radius,height)

    print(f"This is the one we want: {name}, {effeciency:.2f}")

    name = '#2'
    radius = 8.73
    height = 11.91
    cost = "$0.28"
    
    x = compute_volume(radius , height)
    y = compute_surface_area(radius, height)

    effeciency = x / y 
    print(f'This is the one we want: {name}, {effeciency:.2f}')

    name = '#2'
    radius = 8.73
    height = 11.91
    cost = "$0.28"
    
    x = compute_volume(radius , height)
    y = compute_surface_area(radius, height)

    effeciency = x / y 
    print(f'This is the one we want: {name}, {effeciency:.2f}')

    name = '#2.5'
    radius = 10.32
    height = 11.91
    cost = "$0.61"
    
    x = compute_volume(radius , height)
    y = compute_surface_area(radius, height)

    effeciency = x / y 
    print(f'This is the one we want: {name}, {effeciency:.2f}')

    name = '#3 Cylinder'
    radius = 10.32
    height = 17.78
    cost = "$0.86"
    
    x = compute_volume(radius , height)
    y = compute_surface_area(radius, height)

    effeciency = x / y 
    print(f'This is the one we want: {name}, {effeciency:.2f}')

    name = '#5'
    radius = 13.02
    height = 14.29
    cost = "$0.83"
    
    x = compute_volume(radius , height)
    y = compute_surface_area(radius, height)

    effeciency = x / y 
    print(f'This is the one we want: {name}, {effeciency:.2f}')

    name = '#6Z'
    radius = 5.40
    height = 8.89
    cost = "$0.22"
    
    x = compute_volume(radius , height)
    y = compute_surface_area(radius, height)

    effeciency = x / y 
    print(f'This is the one we want: {name}, {effeciency:.2f}')

    name = '#8Z short'
    radius = 6.83
    height = 7.62
    cost = "$0.26"
    
    x = compute_volume(radius , height)
    y = compute_surface_area(radius, height)

    effeciency = x / y 
    print(f'This is the one we want: {name}, {effeciency:.2f}')

    name = '#10'
    radius = 15.72
    height = 17.78
    cost = "$1.53"
    
    x = compute_volume(radius , height)
    y = compute_surface_area(radius, height)

    effeciency = x / y 
    print(f'This is the one we want: {name}, {effeciency:.2f}')

    name = '#211'
    radius = 6.83
    height = 12.38
    cost = "$0.34"
    
    x = compute_volume(radius , height)
    y = compute_surface_area(radius, height)

    effeciency = x / y 
    print(f'This is the one we want: {name}, {effeciency:.2f}')


    name = '#300'
    radius = 7.62
    height = 11.27
    cost = "$0.38"
    
    x = compute_volume(radius , height)
    y = compute_surface_area(radius, height)

    effeciency = x / y 
    print(f'This is the one we want: {name}, {effeciency:.2f}')


    name = '#303'
    radius = 8.110
    height = 11.11
    cost = "$0.42"
    
    x = compute_volume(radius , height)
    y = compute_surface_area(radius, height)

    effeciency = x / y 
    print(f'This is the one we want: {name}, {effeciency:.2f}')

    pass
def compute_volume(radius, height):
    volume = math.pi*radius**2 * height
    #volume = π radius2 height
    return volume

def compute_surface_area(radius, height):
    #surface_area = 2π radius (radius + height)
    surface_area = 2*math.pi*radius*(radius+height)
    return surface_area

main()