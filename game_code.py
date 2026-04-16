import pygame
import math

pygame.init()


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# load and scale the background image to fit perfectly on the screen
background = pygame.image.load("football_ground.png") 

# load and scale the football image
football = pygame.image.load("football.png").convert_alpha()
# let's resize our football to an appropriate size so that it doesn't cover the whole screen
football = pygame.transform.scale(football, (40, 40))

goalkeeper = pygame.image.load("goalkeeper.png").convert_alpha()
goalkeeper = pygame.transform.scale(goalkeeper, (150, 150)) 

font = pygame.font.SysFont(None, 80)
goal_text = font.render("Goal!", True, (25, 0, 0))
save_text = font.render("Saved!", True, (25, 0, 0))

# =====================GAME VARIABLES=============================
ball_start_x, ball_start_y = 751, 758
# Football
x, y = ball_start_x, ball_start_y
target_x, target_y = None, None
moving = False
waiting_to_reset = False
# Goalkeeper
gx, gy = 720, 430
# Speed
speed = 7
# Timer
reset_timer = 0
# Result variable
result = None
running = True
clock = pygame.time.Clock()

# ======================= is_save_function ========================
def is_save(ball_x, ball_y, gk_x, gk_y):
    dx = ball_x-gk_x
    dy = ball_y-gk_y
    distance = math.sqrt(dx**2 + dy**2)
    return distance < 40


while running == True:
    for event in pygame.event.get():
        # If user click the close button
        if event.type == pygame.QUIT:
            running = False
        
        # Shoot the football on key press
        if event.type == pygame.KEYDOWN and not moving and not waiting_to_reset:
            if event.key == pygame.K_d:
                target_x, target_y = 860, 460
                moving = True 
            elif event.key == pygame.K_a:
                target_x, target_y = 630, 460
                moving = True
            elif event.key == pygame.K_w:
                target_x, target_y = 750, 460
                moving = True

             
    # Get the state of all keyboard keys
    keys = pygame.key.get_pressed()
    #Move the goalie left if LEFT arrow is pressed
    if keys[pygame.K_LEFT]:
        gx -= 5
    #Move the goalie right if right arrow/d key is pressed
    if keys[pygame.K_RIGHT]:
        gx += 5

    # Ball movement
    if moving:
        dx = target_x-x
        dy = target_y-y
        # we are using distance formula from mathematics to calculate distance between target position and starting position of football
        distance = math.sqrt(dx**2 + dy**2)

        if distance > speed:
            # keep on moving the ball towards target rather than directly teleporting it to the target
            x += speed * dx / distance
            y += speed * dy / distance
        else:
            # Ball reached the target
            x, y = target_x, target_y
            moving = False
            waiting_to_reset = True
            reset_timer = pygame.time.get_ticks()

    # -------- Reset after delay of 1 second ----------
    if waiting_to_reset:
        if pygame.time.get_ticks()-reset_timer > 1000:
            x, y = ball_start_x, ball_start_y
            waiting_to_reset = False
    
    # fill the screen with this color and create a background
    # screen.fill((255, 255, 255))
    # Draw the background image starting from the top-left corner till bottom right cornet             x  y    
    screen.blit(background, (0, 0))

    screen.blit(goalkeeper, (gx, gy))
    # Draw the blue circle(the ball)
    # screen -> where to draw
    # (0, 0, 255) -> blue color
    # (x, y) -> center positon of the circle
    # 20 radius of the circle in pixels 
    # pygame.draw.circle(screen, (0, 0, 255), (x, y), 20)
    screen.blit(football, (x, y))

    # Update the screen so the drawing appears
    pygame.display.flip()
    clock.tick(50)
# Quit pygame when the loop ends
pygame.quit()

    
