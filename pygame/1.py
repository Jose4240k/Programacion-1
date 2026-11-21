import pygame 
pygame.init() 
screen = pygame.display.set_mode((640, 360)) 
pygame.display.set_caption("Hola, pygame") 
clock = pygame.time.Clock() 
running = True 
while running: 
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # 1) ENTRADA # 2) ACTUALIZAR: aquí irá la lógica del juego    
            screen.fill((30, 30, 46))
            clock.tick(60)
                                                # 3) DIBUJAR    
            pygame.draw.circle(screen, (255, 200, 60), (320, 180), 60)    
            pygame.display.flip()                     # mostrar lo dibujado # máximo 60 FPS 
pygame.quit()