import pygame
import random
from Helper import Helper
import Ship
from Asteroid import Asteroid
import sys

def main():
    help = Helper()
    help.main_menu()
    rocks = []
    counter = 0
    score = 0
    run = True
    while run:
        help.clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if counter < 8:
            rocks.append(Asteroid(round(random.randint(20, 1050)), -175, random.randint(5, 30), 160, 160))
            counter += 1

        for rock in rocks:
            if help.spaceShip.hitbox[1] < rock.hitbox[1] + rock.hitbox[3] and help.spaceShip.hitbox[1] + help.spaceShip.hitbox[3] > rock.hitbox[1]:
                if help.spaceShip.hitbox[0] < rock.hitbox[0] + rock.hitbox[2] and help.spaceShip.hitbox[0] + help.spaceShip.hitbox[2] > rock.hitbox[0]:
                    help.spaceShip.hit(help.window, help.game_over, help.black_heart, score)
                    rock.destroy(rocks, rock)
                    counter -= 1
                    score += 1
            if rock.y < 700:
                rock.y += rock.velocity
            else:
                rock.destroy(rocks, rock)
                counter -= 1
                score += 1

        help.keysPressed()
        help.redrawGameWindow(score, rocks)

main()
pygame.quit()
