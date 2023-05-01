import pygame
import numpy as np
import imageio

# inicializar Pygame
pygame.init()

# definir las dimensiones de la ventana
width = 1000
height = 600

# crear la ventana
screen = pygame.display.set_mode((width, height))

# definir el tamaño de la cuadrícula
grid_size = (60, 100)

# crear una matriz aleatoria para la cuadrícula
grid = np.random.randint(0, 2, grid_size)

# definir los colores de las células
alive_color = (0, 255, 0)
dead_color = (0, 0, 0)

# definir la duración de cada imagen en el GIF en milisegundos
duration = 100

# crear una lista para almacenar las imágenes
images = []

# ejecutar el bucle principal del juego
running = True
while running:
    # manejar los eventos de Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # actualizar la cuadrícula
    next_grid = np.zeros_like(grid)
    for x in range(grid_size[0]):
        for y in range(grid_size[1]):
            # contar el número de vecinos vivos
            alive_neighbors = np.sum(grid[max(0,x-1):min(grid_size[0],x+2), max(0,y-1):min(grid_size[1],y+2)]) - grid[x, y]
            # aplicar las reglas del juego
            if grid[x, y] == 1 and (alive_neighbors < 2 or alive_neighbors > 3):
                next_grid[x, y] = 0
            elif grid[x, y] == 0 and alive_neighbors == 3:
                next_grid[x, y] = 1
            else:
                next_grid[x, y] = grid[x, y]
    grid = next_grid

    # dibujar la cuadrícula en la pantalla
    screen.fill(dead_color)
    for x in range(grid_size[0]):
        for y in range(grid_size[1]):
            if grid[x, y] == 1:
                rect = pygame.Rect(y * width // grid_size[1], x * height // grid_size[0], width // grid_size[1], height // grid_size[0])
                pygame.draw.rect(screen, alive_color, rect)

    # actualizar la pantalla
    pygame.display.update()

    # guardar la imagen en la lista
    images.append(pygame.surfarray.array3d(pygame.display.get_surface()).swapaxes(0, 1))


# guardar las imágenes en un archivo GIF en bucle infinito
imageio.mimsave('conway.gif', images, duration=duration, loop=0)
