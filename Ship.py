import pygame
class Ship(object):
    def __init__(self, x, y, velocity, health, height, width):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.height = height
        self.width = width
        self.health = health
        self.hitbox = (self.x, self.y, 100, 100)

    def draw(self, window, character):
        window.blit(character, (self.x-75, self.y))
        self.hitbox = (self.x+9, self.y+55, 81, 74)

    def endGame(self, window, game_over, black_heart, score):
        window.blit(game_over, (0, 0))
        window.blit(black_heart, (50, 10))
        font_death_score = pygame.font.SysFont("comicsans", 50, True, True)
        text_death_score = font_death_score.render("Final Score : "+ str(score), 1, (220, 0, 0))
        window.blit(text_death_score, (1100/2 - (text_death_score.get_width()/2), 500))
        pygame.display.update()
        i = 0
        while i < 400:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 351
        pygame.quit()

    def hit(self, window, game_over, black_heart, score):
        if self.health > 1:
            self.health -= 1
        else:
            self.endGame(window, game_over, black_heart, score)
