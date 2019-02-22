import math as mt
import numpy
"""
planets = [
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Jupiter',
    'Saturn',
    'Uranus',
    'Neptune'
]
"""
"""
planets.append("Pluto")
print(planets)
print(len(planets))
print(planets.pop())
print(planets)
planets[5] = "Chery"
print(planets)
planets[5] = "Saturn"
print(planets[0:3])
"""
"""
for planet in planets:
    print(planet, end=' ')
"""
"""
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
for char in s:
    if char.isupper():
        print(char, end='' )

multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
print("\n", product)

print("Hello")

for i in range(7):
    print("Doing important work. i =", i)

i = 0
while i < 10:
    print(i, end=' ')
    i += 1
squares = [n**2 for n in range(10)]
print("\n", squares)

short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets) 
"""
"""
numbers = {'one':1, 'two':2, 'three':3}
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)
print('Saturn' in planet_to_initial)
numbers['eleven'] = 11
print(numbers)
for k in numbers:
    print("{} = {}".format(k, numbers[k]))
print(' '.join(sorted(planet_to_initial.values())))
for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))
"""
"""
print("It's math! It has type {}".format(type(mt)))
print(dir(mt))
print("pi to 4 significant digits = {:.4}".format(mt.pi))
help(math.log)
print(mt.pi)
"""
"""
print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:]
     )
"""
rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls)
print(dir(list))