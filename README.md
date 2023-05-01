# El juego de la vida de Conway
![conway2](https://user-images.githubusercontent.com/122236197/235390275-f7ba0d33-e6f4-4fef-a286-ccf70793f305.gif)

## Explicación

El juego de la vida es un modelo matemático que simula la evolución de células en un tablero de cuadrícula bidimensional.  Fue inventado por el matemático británico John Horton Conway en 1970. 

En el juego de la vida, cada célula puede estar en uno de dos estados posibles: viva o muerta. El estado de cada célula en el siguiente paso de la simulación depende de sus estados actuales y de los estados de sus ocho vecinos inmediatos. Las reglas que determinan si una célula vive o muere se basan en el número de células vivas en su entorno inmediato.

Aunque las reglas son muy simples, el juego de la vida puede generar patrones complejos y a veces sorprendentes. Muchos patrones interesantes, como los "osciladores", las "naves espaciales" y las "construcciones" pueden emerger de la interacción de las células en el tablero.

El juego de la vida ha sido objeto de estudio en la ciencia de la computación, las matemáticas y otras áreas, y ha sido utilizado para modelar fenómenos naturales y sociales como la propagación de enfermedades, la evolución biológica y la difusión cultural. También ha sido objeto de interés en la cultura popular, apareciendo en películas, programas de televisión, música y otras formas de arte.

## Programa

El programa del juego de la vida es un programa que simula la evolución de células en un tablero de cuadrícula bidimensional. El programa típicamente funciona de la siguiente manera:

1. Se crea una cuadrícula bidimensional, que es una matriz de celdas cuadradas que representan el estado de cada célula en el tablero.

2. Se establece el estado inicial de las células en la cuadrícula. El estado inicial puede ser aleatorio o predefinido por el usuario.

3. Se aplica una serie de reglas para determinar el estado de cada célula en el siguiente paso de la simulación. Las reglas se basan en el número de células vivas en el entorno inmediato de cada célula.

4. Se actualiza la cuadrícula para reflejar el nuevo estado de las células en el siguiente paso de la simulación.

5. Se repite el proceso de aplicar las reglas y actualizar la cuadrícula para cada paso subsiguiente de la simulación.

## Crea un GIF

Este programa es una implementación del "Juego de la vida" utilizando la biblioteca Pygame. 

En el programa inicialmente, se crea una ventana de tamaño 1000x600 píxeles en la que se dibuja una cuadrícula de 60x100 células. 
Cada célula puede estar viva o muerta, y se representa con un rectángulo de color verde o negro respectivamente. 
El programa ejecuta un bucle principal que actualiza la cuadrícula según las reglas del juego de la vida y dibuja la nueva cuadrícula en la ventana.

![1](https://user-images.githubusercontent.com/122236197/235392061-3c139c9b-7150-4e47-a5af-45a0e951552d.png)

Además, el programa guarda cada imagen dibujada en la pantalla en una lista, y luego utiliza la biblioteca imageio para guardar todas las imágenes como un archivo GIF en bucle infinito llamado "conway.gif". 
Este archivo puede usarse para visualizar la evolución de la población de células a lo largo del tiempo.

![2](https://user-images.githubusercontent.com/122236197/235392147-c42a95ed-a6c5-461f-9472-2e8f1bb6769e.png)

Diviértete cambiando los parametros iniciales, el tamaño de la ventana, los colores de células vivas y muertas, etc...
