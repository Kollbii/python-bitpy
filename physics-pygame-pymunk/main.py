import pygame, pymunk, sys, random


def create_circle(space):
    body = pymunk.Body(1,100,body_type=pymunk.Body.DYNAMIC)
    body.position = (random.randint(0,800),random.randint(0,200))
    shape = pymunk.Circle(body, 20)
    space.add(body, shape)
    return shape

def draw_circles(circles):
    for circle in circles:
        pos_x = int(circle.body.position.x)
        pos_y = int(circle.body.position.y)
        pygame.draw.circle(screen, (255,0,0), (pos_x, pos_y), 20)

def create_line(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (400,200)
    shape = pymunk.Segment(body,(0, 0),(300,300), 10)
    space.add(body, shape)
    return shape

def draw_lines(lines):
    for line in lines:
        pygame.draw.line(screen, (0,0,0), (0,0),(300,300), 10)    

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 200)

circles = []
for _ in range (10):
    circles.append(create_circle(space))

lines = []
lines.append(create_line(space))

if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((20, 31, 36))
        draw_circles(circles)
        draw_lines(lines)
        space.step(1/50)
        pygame.display.update()
        clock.tick(120)