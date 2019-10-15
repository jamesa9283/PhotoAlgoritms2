import pygame

pygame.init()


def mirror_vertical(surface):
    width = surface.get_width()
    height = surface.get_height()
    mirror_point = width / 2
    for y in range(height):
        for x in range(int(mirror_point)):
            left_pixel = surface.get_at((x, y))
            right_pixel = surface.get_at((width - x - 1, y))
            surface.set_at((x, y), right_pixel)


main_window = pygame.display.set_mode((500, 500))

my_surface = pygame.image.load('GingerCat.jpg').convert()

mirror_vertical(my_surface)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_window.fill((255, 255, 255))
    main_window.blit(my_surface, (0, 0))
    pygame.display.update()

pygame.quit()