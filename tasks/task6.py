import pygame
import math
from planet_class import Planet

def draw_lines_between_planets(planets, color, line_width, WIDTH, HEIGHT, SCALE):
    lines = []
    for i in range(len(planets) - 1):
        for j in range(i + 1, len(planets)):
            planet1, planet2 = planets[i], planets[j]
            if not planet1.sun and not planet2.sun:
                lines.append(((planet1.x * SCALE + WIDTH / 2, planet1.y * SCALE + HEIGHT / 2),
                              (planet2.x * SCALE + WIDTH / 2, planet2.y * SCALE + HEIGHT / 2), color, line_width))
    return lines


def task6(planets, SCALE, TIMESTEP):
    pygame.init()

    WIDTH, HEIGHT = 1600, 900
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Spirograph")

    run = True
    clock = pygame.time.Clock()

    all_lines = []  # Store all lines drawn between planets

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets, TIMESTEP  )
            planet.draw(WIN, WIDTH, HEIGHT, SCALE)

        lines = draw_lines_between_planets(planets, (128, 0, 128), 1, WIDTH, HEIGHT, SCALE)  # Purple color (R, G, B), line width 1

        # Update all_lines with the lines from the current frame
        all_lines.extend(lines)

        # Draw all the lines stored in all_lines
        for line in all_lines:
            pygame.draw.line(WIN, line[2], (int(line[0][0]), int(line[0][1])), (int(line[1][0]), int(line[1][1])), int(line[3]))

        pygame.display.update()

    pygame.quit()


