class Asteroid(object):
    def __init__(self, x, y, velocity, height, width):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.height = height
        self.width = width
        self.hitbox = (self.x, self.y, 100, 100)

    def draw(self, window, ast):
        window.blit(ast, (self.x, self.y))
        self.hitbox = (self.x, self.y+10, 60, 50)

    def destroy(self, rocks, rock):
        rocks.pop(rocks.index(rock))
