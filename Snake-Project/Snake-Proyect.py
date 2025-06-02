import pygame
import random

#iniciar el juego
pygame.init()

#dimensiones de la ventana
ancho = 500
alto = 500

#creación de la ventana
little_window = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Snake Game :3")

#pintar el fondo
little_window.fill((1,19,10))

#frames per second
clock = pygame.time.Clock()

#color de la serpiente
green = pygame.Color(52, 232, 31)

#tamaño de comida
tamano_bloque = 10

#fuente del score
font = pygame.font.Font(None, 30)

#funcion de la puntuacion 
def show_score(score):
   text = font.render(str(score),0,(146,232,243))
   little_window.blit(text,(480, 20)) 

#bucle para jugar y moverse
def juego():
    score = 0
    largo_serpiente = 1
    change = "RIGHT"
    # Estructura de serpiente 
    S_position = [100, 50]
    S_body = [[100,50],[90,50],[80,50]]

    comida_pos = [random.randrange(0, 500, tamano_bloque),
                 random.randrange(0, 500, tamano_bloque)]

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                      run = False
                elif event.key == pygame.K_r:
                  run = True
                  
                elif event.key == pygame.K_RIGHT and change != "LEFT":
                 change = "RIGHT"
                elif event.key == pygame.K_LEFT and change != "RIGHT":
                 change = "LEFT"
                elif event.key == pygame.K_DOWN and change != "UP":
                 change = "DOWN"
                elif event.key == pygame.K_UP and change != "DOWN":
                 change = "UP"

        # movimiento de la serpiente según la dirección establecida
        if change == "RIGHT":
           S_position[0] += 10
        elif change == "LEFT":
           S_position[0] -= 10
        elif change == "DOWN":
           S_position[1] += 10
        elif change == "UP":
           S_position[1] -= 10


         #arma la serpiente y crecimiento
        S_body.insert(0,list(S_position))
        if S_position == comida_pos:
            comida_pos = [random.randrange(0, 500, tamano_bloque),
                  random.randrange(0, 500, tamano_bloque)] 
            largo_serpiente += 1
            score += 1
            print(score)
        else:
          S_body.pop()
   
        little_window.fill((1, 19, 10))
        
        #chocar con los bordes
        if S_position[0] < 0 or S_position[0] > 500 or S_position[1] < 0 or S_position[1] > 500 or S_position in S_body[1:]: 
           game_over(score)
        
           
    
        #mostrar la serpiente y la comida
        for pos in S_body:
            pygame.draw.rect(little_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    
        pygame.draw.rect(little_window,(169,6,6), pygame.Rect(comida_pos[0], comida_pos[1], 10, 10))
        show_score(score)
        
        #para cambiar la velocidad de la serpiente segun el puntaje
        if score < 10:
           clock.tick(10)
        if score >= 10:
           clock.tick(20)

        pygame.display.flip()

def game_over(score):
    while True:

        little_window.fill((0, 0, 0))
        mensaje = font.render("¡Perdiste! Puntaje:" +str(score), True, (255, 0, 0))
        little_window.blit(mensaje, (30, 200))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()
                elif event.key == pygame.K_r:
                     juego()
                
        
juego()
  