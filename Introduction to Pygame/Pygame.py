from game_objects import *

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change_to = 'Left'
            elif event.key == pygame.K_RIGHT:
                player.change_to = 'Right'
            elif event.key == pygame.K_UP:
                player.change_to = 'Up'
            elif event.key == pygame.K_DOWN:
                player.change_to = 'Down'

    # Direction Change Check
    if player.change_to == 'Left' and player.direction != 'Right':
        player.direction = 'Left'
    elif player.change_to == 'Right' and player.direction != 'Left':
        player.direction = 'Right'
    elif player.change_to == 'Up' and player.direction != 'Down':
        player.direction = 'Up'
    elif player.change_to == 'Down' and player.direction != 'Up':
        player.direction = 'Down'
    
    # Actual Direction Change
    if player.direction == 'Left':
        player.velocityX = -20
        player.velocityY = 0
    if player.direction == 'Right':
        player.velocityX = 20
        player.velocityY = 0
    if player.direction == 'Up':
        player.velocityX = 0
        player.velocityY = -20
    if player.direction == 'Down':
        player.velocityX = 0
        player.velocityY = 20
            
    player.headPositionX += player.velocityX
    player.headPositionY += player.velocityY

    # Check Collisions
    if player.head_collided_in_body() or player.head_collided_in_border():
        running = False
    if player.headPositionX == food.positionX and player.headPositionY == food.positionY:
        player.bodyLength += 1
        food.randomize_position()
        player.bodyPositions.insert(player.bodyLength - 1, player.bodyPositions[-1])
    
    # Game Object Movement and Display
    DISPLAYWINDOW.fill(BLACK)    
    player.move()
    pygame.draw.rect(DISPLAYWINDOW, RED, [food.positionX, food.positionY, food.WIDTH, food.HEIGHT])
    
    pygame.display.update()
    clock.tick(15)

pygame.quit()
quit()