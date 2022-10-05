# "Bird" refers to the circle
# "Gap" refers to the space between the top and bottom pillar

def setup(): 
    size(1000,1000)
    frameRate(30)

pillar1X = 1100
pillar1Y = random(200,650)
pillar2X = -200
pillar2Y = 0

playerX = 300
playerY = 500

playerVel = 0
playerAcc = .5 #0.5 by default

pillarSpeed = 10 #Changing this may make the playerScore not change. 10 by default

isAlive = 1 #My sorry excuse for a boolean

#allows text to be removed
hasStarted = False

#Gap is 175 by default
gap = 175 #Gap between bottom and top of pillars. You can safely edit this value as it is procedural
d = 50 #Diameter of bird

playerScore = 0

def draw():
    
    global pillar1X, pillar1Y, pillar2X, pillar2Y, gap, pillarSpeed, playerX, playerY, d, playerVel, playerAcc, isAlive, hasStarted, playerScore
    background (0,175,255)
    
    playerX = 200-d/2
    
    #isAlive is 1 or 0
    pillar1X -= pillarSpeed * isAlive
    pillar2X -= pillarSpeed * isAlive
    
    
    #Draws the bottom pillar and top pillar 1 respectivly
    #The top left of the bottom pillar is the X,Y coordinates
    
    fill(0,255,0)
    rect(pillar1X,pillar1Y, 100,1000)
    rect (pillar1X, -10, 100, pillar1Y-gap)
    
    #Draws the secondary pillars before pillar 1 reaches the player. 
    #These are used for collision detection
    rect(pillar2X,pillar2Y, 100,1000)
    rect (pillar2X, -10, 100, pillar2Y-gap)
    
    
    #Draws the player and calculates player velocity (y axis)
    #Sets colour of player
    if(isAlive == 1):
        fill(230, 213, 70)
    else:
        fill(255,0,0)
        
    #Detects if a player leaves vertical bounds of screen
    if(playerY < 0 + d/2): # Hit ceiling?
        playerY = 0 + d/2
        isAlive = 0
    #Hit floor? Doesn't work.... Kind of?
    #I have no idea why 1,000 - d/2 isnt perfect... It should work. 
    #I just used 900 because its close
    #I have spent the last 30 minutes trying to fix this. I am beyond confused...
    if(playerY > 900 - d/2): 
        playerY = 900 - d/2
        isAlive = 0
    
    #If the user presses a key, this applies the velocity
    circle(playerX, playerY, d)
    if(keyPressed == True and isAlive == 1):
        playerVel -= 2 # This is the positive vertical force applied to the player
        if(playerVel < -10): playerVel = -10
        
        
    playerVel += playerAcc
    playerY += playerVel
    
    #This block detects if the player hit a pillar
    #Detects if a player is within the vertical boundries of a pillar
    #Uses pillar 2 because it has been converted to pillar2 by the time it reaches the player
    if (pillar2X > 100 and pillar2X < 200):
        #Detects if a player is in the gap
        if(playerY - d/2 > pillar2Y - gap and playerY + d/2 < pillar2Y):
            #Player is within a pillar and is in the gap
            print("Not Hit")
        else:
            #Player is within a pillar but has collided with a pillar
            isAlive = 0 #Setting this to zero and multiplying pillar speed by it makes the pillars stop

        
    
    #Detects when the pillar is behind the player
    if(pillar1X < 220):
        #Swaps positions between pillar1 and pillar2
        #Positions now swap in front of the player
        pillar2X = pillar1X
        pillar2Y = pillar1Y
        hasStarted = True
        pillar1X = 1100
        pillar1Y = random(150+gap,650)
        
    #Tests if a player has passed a pillar to increase score
    if pillar2X == 100:
        playerScore += 1
    
    #Shows and hides the score text and the title text
    if hasStarted == False:
        #Title text
        fill(255,255,0)
        textSize(100)
        text("FLOPPY BIRB!", 175, 100)
    else:
        #Score text
        fill(255)
        textSize(90)
        text(playerScore, 800, 100)
        
    #Tests if the player is alive
    if isAlive == 0:
        #If the player presses R to restart, the game restarts here
        if key == 'r':
            isAlive = 1
            playerY = 500
            playerVel = 0
            pillar1X = 1100
            pillar2X = -200
            hasStarted = False
            playerScore = 0
            
        #This controls the text that tells players to restart
        color(255, 0, 0)
        text("Press R to Restart", 175, 800)
