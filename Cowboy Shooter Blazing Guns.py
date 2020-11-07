import pygame, random
pygame.init()

#Colors
white = (255, 255, 255)
black = (0, 0, 0)
brown = (155, 118, 83)
red = (255, 0, 0)

#Screen Size
screen_width = 600
screen_height = 600

#Drawing Screen
gameScreen = pygame.display.set_mode((screen_width, screen_height))
gameScreen.fill(brown)
pygame.display.set_caption('Blazing Guns')

#Clock
clock = pygame.time.Clock()

#Movement
player_x_change = 0
player_y_change = 0

#Player Size
player_height = 20
player_width = 20

#Bullet Variables
bullet_radius = 5


#Telling Where to spawn character
player_x = screen_width/2 - player_width/2
player_y = screen_height/2 - player_height/2

#Telling Computer we aren't dead
player_dead = False

#Defining Cowboy/Drawing
def cowboy_player():
    pygame.draw.rect(gameScreen, black, (player_x, player_y, player_width, player_height))

#Bullet Variables
bullet_speed = 7.5

#Random Variables
def variablesBullet():
    y_intercept = 0
    slope_formula = 0
    y_change_bullet = 0
    x_change_bullet = player_x

#Defining Bullets
def bullet_shot():
    pygame.draw.circle(gameScreen, white, (bullet_x, bullet_y), bullet_radius) #Draw Bullet on Screen
    bullet_slope = (((mouse_y - player_y) / (mouse_x - player_x)) * -1) #Bullet Slope
    print(player_x, player_y, mouse_x, mouse_y, bullet_slope) #Typing Out Numbers
    y_intercept = (player_y - (bullet_slope * player_x))
    x_change_bullet += 1
    y_change_bullet = ((bullet_slope * x_change_bullet) + y_intercept)
    pygame.draw.circle(gameScreen, white, (x_change_bullet, y_change_bullet), bullet_radius)
  


#Main Loop
while not player_dead:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player_dead = True

    #Key List for Movement
    keys = pygame.key.get_pressed()
    
    #Moving Player
    if keys[pygame.K_a]:
        player_x -= 5
    if keys[pygame.K_d]:
        player_x += 5
    if keys[pygame.K_w]:
        player_y -= 5
    if keys[pygame.K_s]:
        player_y += 5

    #Def Bullet Position by Character
    bullet_x = player_x + (player_width/2)
    bullet_y = player_y + (player_height/2)


    #Adding Colored Background
    gameScreen.fill(brown)

    #Drawing Character
    cowboy_player()
    
    #Putting Collisions into Game Loop
    if player_x < 0:
        player_x = 0
    if player_x > screen_width - player_width:
        player_x = screen_width - player_width
    if player_y < 0:
        player_y = 0
    if player_y > screen_height - player_height:
        player_y = screen_height - player_height

    variablesBullet()
 
    #Shooting Bullets
    mouse_click = pygame.mouse.get_pressed()
    if mouse_click != (0, 0, 0):
        #Finding Mouse X,Y
        mouse_x, mouse_y = pygame.mouse.get_pos()
        bullet_shot()
        #print(mouse_click)
        #print(mouse_x, mouse_y)
        ##SLOPE of BULLET

    #Refreshing Screen
    pygame.display.update()

    #Frames Per Second
    clock.tick(60)

pygame.quit()
