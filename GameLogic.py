import pygame

import App

clock = pygame.time.Clock()
isRunning = True

grid = [pygame.Rect(x * App.TILE, y * App.TILE, App.TILE, App.TILE) for x in range(App.W) for y in range(App.H)]

figures_pos = []  # массив с координатами кубов фигур
for figure_data in App.SETTINGS['figures']:
    figure = [(block['x'], block['y']) for block in figure_data['shape']]
    figures_pos.append(figure)
print(figures_pos)

figures = [[pygame.Rect(x + App.W // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
figure_rect = pygame.Rect(0, 0, App.TILE - 2, App.TILE - 2)
figure = figures[5]

while isRunning:
    App.sc.fill(pygame.Color('white'))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            isRunning = False

    [pygame.draw.rect(App.sc, (4, 4, 4), i_rect, 1) for i_rect in grid]

    for i in range(9):
        figure_rect.x = figure[i].x * App.TILE
        figure_rect.y = figure[i].y * App.TILE
        pygame.draw.rect(App.sc, pygame.Color("black"), figure_rect)



    print(figure_rect.x, figure_rect.y)
    pygame.display.flip()
    clock.tick(App.FPS)
