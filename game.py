__author__ = 'dg'

from random import random, choice
from copy import deepcopy

GRAPHICS = {'ore':'*'}

DIRECT = {'up': (-1, 0),
          'down': (1, 0),
          'left': (0, -1),
          'right': (0, 1)}


class Tile:
    def __init__(self):
        self.items = []
        self.ore = choice((0,0,0,0,5,10))

    def symbol(self):
        if not self.items:
            return '*' if self.ore else ' '
        if len(self.items) == 1:
            return self.items[0].symbol
        return '%'

    def __str__(self):
        return self.symbol()

    def add(self, other):
        if sum(item.space for item in self.items) + other.space >= 3:
            self.items.append(other)


class Wall:
    def symbol(self):
        return '#'

    def add(self):
        pass


class World(dict):
    def __init__(self, width, height):
        self.width, self.height = width+2, height+2
        dict.__init__(self, {(i, j): Tile() for i in range(height+2) for j in range(width+2)})
        for key in self.keys():
            if 0 in key or key[0] == height+1 or key[1] == width+1:
                self[key] = Wall()

    def __iter__(self):
        for i in range(self.height):
            for j in range(self.width):
                yield self[i, j]

    def rows(self):
        for i in range(self.height):
            yield (self[i,j] for j in range(self.width))

    def show(self):
        for row in self.rows():
            print(''.join(tile.symbol() for tile in row))

    def adj(self, cords):
        x, y = cords
        return {cord: self[cord] for cord in ((x,y), (x+1,y), (x-1,y), (x,y+1), (x,y-1))}


class Thing:
    def __init__(self, x, y, world):
        self.HP = 1
        self.health = 1
        self.space = 1
        self.appearance = '?'

        self.cords = (x, y)
        self.world = world

        self.world[self.cords].add(self)

    def symbol(self):
        return self.appearance


class Camera(Thing):
    def __init__(self, x, y, world):
        Thing.__init__(self, x, y ,world)

    def update(self):
        print(self.world[self.cords])
        view = self.world.adj(self.cords)
        x, y = self.cords
        print('---------')
        print('', view[x-1, y])
        print(view[x, y-1], view[x, y], view[x, y+1], sep='')
        print('', view[x + 1, y])
        c = input('---------').split()

        if c == 'up':
            x -= 1
        elif c == 'down':
            x += 1
        elif c == 'left':
            y -= 1
        elif c == 'right':
            y += 1

        try:
            self.world[self.cords].add(self)



r = Camera(4,4, World(10,10))

while True:
    r.world.show()
    r.update()


