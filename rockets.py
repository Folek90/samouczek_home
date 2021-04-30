
from random import randint

# metody typu d under - double underscore 
# __str__ - STRing

class Rocket:
    '''mozna dodac opis krotki 
    '''

    def __init__(self, speed=1):
        self.altitude = 0

        self.speed = speed


    def moveUp(self):
        '''poruszamy sie do gory(altitude) z szybkoscia (speed)
        '''
        self.altitude += self.speed
       


rockets = [Rocket(randint(1,6)) for i in range(5)]



for i in range(10):
    rocketIndexToMove = randint(0, 4)
    rockets[rocketIndexToMove].moveUp()

for rocket in rockets:
    print(rocket.altitude)


print(rocket)
