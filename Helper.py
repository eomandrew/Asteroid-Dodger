import pygame
from Ship import Ship
import sys
class Helper(object):
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.spaceShip = Ship(500, 300, 15, 3, 187, 250)
        pygame.init()
        self.window = pygame.display.set_mode((1100, 700))
        pygame.display.set_caption("Asteroid Dodge")
        #self.music = pygame.mixer.music.load("")
        #pygame.mixer.music.play(-1)
        self.background = pygame.image.load("background.png")
        self.game_over = pygame.image.load("game_over.png")
        self.character = pygame.image.load("spaceship.png")
        self.ast = pygame.image.load("asteroid.png")
        self.black_heart = pygame.image.load("black_heart.png")
        self.red_heart = pygame.image.load("red_heart.png")
        self.font_score = pygame.font.SysFont("comicsans", 30, True, True)
        self.font_delay = pygame.font.SysFont("comicsans", 30, True, True)


    def heart_draw(self):
        self.window.blit(self.red_heart, (70, 10))
        self.window.blit(self.red_heart, (90, 10))
        self.window.blit(self.red_heart, (50, 10))
        if self.spaceShip.health == 2 or self.spaceShip.health < 2:
            self.window.blit(self.black_heart, (90, 10))
        if self.spaceShip.health == 1 or self.spaceShip.health < 1:
            self.window.blit(self.black_heart, (70, 10))
        pygame.display.update()


    def redrawGameWindow(self, score, rocks):
        text_score = self.font_score.render("Score: "+ str(score), 1, (255, 0, 0))
        self.window.blit(self.background, (-10,-10))
        self.window.blit(text_score, (950, 10))
        self.spaceShip.draw(self.window, self.character)
        for rock in rocks:
            rock.draw(self.window, self.ast)
        self.heart_draw()
        pygame.display.update()

    def main_menu(self):
        while True:
            self.font = pygame.font.SysFont("comicsans", 100, True, True)
            mainText = self.font.render("Main Menu ", 1, (100, 50, 100))
            self.font = pygame.font.SysFont("comicsans", 50, True, True)
            startText = self.font.render("Start", 1, (50, 50, 200))
            exitText = self.font.render("Exit", 1, (50, 50, 200))
            self.window.blit(self.background, (-10,-10))
            self.window.blit(mainText, (350, 100))
            mx, my = pygame.mouse.get_pos()
            startButton = pygame.Rect(450, 250, 200, 75)
            exitButton = pygame.Rect(450, 400, 200, 75)
            pygame.draw.rect(self.window, (100, 200, 150), startButton)
            pygame.draw.rect(self.window, (100, 200, 150), exitButton)
            self.window.blit(startText, (500, 270))
            self.window.blit(exitText,(500, 420))

            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            if startButton.collidepoint((mx,my)):
                if click:
                    return
            if exitButton.collidepoint((mx,my)):
                if click:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(30)

    def keysPressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.spaceShip.y > -50:
            self.spaceShip.y -= self.spaceShip.velocity
        if keys[pygame.K_DOWN] and self.spaceShip.y < 550:
            self.spaceShip.y += self.spaceShip.velocity
        if keys[pygame.K_LEFT] and self.spaceShip.x > 0:
            self.spaceShip.x -= self.spaceShip.velocity
        if keys[pygame.K_RIGHT] and self.spaceShip.x < 1000:
            self.spaceShip.x += self.spaceShip.velocity
