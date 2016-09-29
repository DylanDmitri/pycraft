__author__ = 'dg'


class human:
    def __init__(self, items, cords):
        self.items = items
        self.cords = cords

    def update(self, view):
        x,y = self.cords
        print('---------')
        print('', view[x-1, y])
        print(view[x, y-1], view[x, y], view[x, y+1], sep='')
        print('', view[x + 1, y])
        return input('---------').split()



