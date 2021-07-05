import pygame
import os

WIDTH, HEIGHT = 900, 700 
VELOCITY = 3
BULL_VELOCITY = 2
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE WAR")
WALL_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join( 'spaceimg.jpg')), (WIDTH, HEIGHT))
SPACESHIP_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('HMM.png')), (200, 200))
BULLET_IMAGE = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('bullet.png')), (85, 45)), 90)
def draw(spaceship_rect, bullet_list):
    DISPLAY.blit(WALL_IMAGE, (0, 0))
    DISPLAY.blit(SPACESHIP_IMAGE,(spaceship_rect.x, spaceship_rect.y))
    for bullets in bullet_list:
        DISPLAY.blit(BULLET_IMAGE,(bullets.x,bullets.y))
    pygame.display.update()


def bullet_movement(bullet_list):
    for bullets in bullet_list:
        bullets.y -= BULL_VELOCITY
        if bullets.y < 0:
            bullet_list.remove(bullets)


def main():
    control = True
    spaceship_rect = pygame.Rect(WIDTH//2-100, 500, 200, 200)
    bullet_list = []
    while control:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                control = False
                pygame.quit()
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_SPACE:
                    bullet = pygame.Rect(spaceship_rect.x+75, spaceship_rect.y,50,50)
                    bullet_list.append(bullet)
        p = pygame.key.get_pressed()
        if p[pygame.K_RIGHT] and spaceship_rect.x+100+VELOCITY < WIDTH-90:
            spaceship_rect.x += VELOCITY
        if p[pygame.K_LEFT] and spaceship_rect.x-VELOCITY > 0:
            spaceship_rect.x -= VELOCITY
        if p[pygame.K_UP] and spaceship_rect.y-VELOCITY > 0:
            spaceship_rect.y -= VELOCITY
        if p[pygame.K_DOWN] and spaceship_rect.y+150+VELOCITY < HEIGHT-30:
            spaceship_rect.y += VELOCITY
        bullet_movement(bullet_list)
        draw(spaceship_rect,bullet_list)
if __name__=='__main__':
    main()
