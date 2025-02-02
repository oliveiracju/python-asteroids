import pygame


from shared.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from game_elements import player, asteroid, asteroidfield, shot

def main():
    print('Starting asteroids!')

    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame_time_clock = pygame.time.Clock()
    
    delta_time = 0

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    shot.Shot.containers = (shots, drawable, updatable)
    player.Player.containers = (drawable, updatable)
    asteroid.Asteroid.containers = (asteroids, drawable, updatable)
    asteroidfield.AsteroidField.containers = (updatable)

    new_player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield.AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0))
        
        delta_time = pygame_time_clock.tick(60) / 1000

        new_player.rotate(delta_time)
        updatable.update(delta_time)

        for asteroid_object in asteroids:
            for shot_object in shots:

                if asteroid_object.check_collision(shot_object):
                    shot_object.kill()
                    asteroid_object.split()
           
            if asteroid_object.check_collision(new_player):
                print('Game over!')
                return

        for drawable_object in drawable:
            drawable_object.draw(screen)

        pygame.display.flip()

    

if __name__ == "__main__":
    main()