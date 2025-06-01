import math

print('==================')
print('Area Calculator 📐')
print('==================')

area = 0
valid = 0

while valid != 1:
    print('\nChoose Shape:')
    print('1. Square')
    print('2. Rectangle')
    print('3. Triangle')
    print('4. Circle')

    print('\nWhich shape1: ')

    answer = int(input())

    if answer < 1 or answer > 4:
        print('Invalid choice!')
    else:
        valid = 1

if answer == 1:
    side = int(input('\nEnter side in metres: ')) 
    area = side ** 2
elif answer == 2:
    length = int(input('\nEnter length in metres: ')) 
    width = int(input('Enter width in metres: ')) 
    area = length * width
elif answer == 3:
    base = int(input('\nEnter base in metres: ')) 
    height = int(input('Enter height in metres: ')) 
    area = base * height * 0.5
else:
    radius = int(input('\nEnter radius in metres: '))
    area = math.pi * (radius ** 2)
    
print('\nThe area is ', area, 'm^2')