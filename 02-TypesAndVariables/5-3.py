###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
cuboid_volume = a*b*c
cuboid_surface_area = a*b * 2 + a * c * 2 + a * c * 2
print(f'volume = {cuboid_volume} surface area = {cuboid_surface_area}')