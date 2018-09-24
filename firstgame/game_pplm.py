import pygame
import time
import random
 
pygame.init()
display_width = 800
display_height = 600
black = (0, 0, 0)
white = (255,255,255)
red = (255,0,0)

player1_width = 89

gameDisplay = pygame.display.set_mode((display_width, display_height)) #window size

pygame.display.set_caption('A little rocky')

clock = pygame.time.Clock() #times thing for us class/class/func?
player1Img = pygame.image.load('madarao2.png')
boulderImg = pygame.image.load('boulder.png')

gameExit= False

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " +str(count), True, black)
    gameDisplay.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, boulderImg):
    #pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    gameDisplay.blit(boulderImg,(thingx,thingy))


def player1(x, y):
    gameDisplay.blit(player1Img,(x,y))
    
def text_objects(text, font):
    textSurface = font.render(text, True, black) # fontrender included with pygame
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 70)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))    
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()
    time.sleep(2)
    
    game_loop()
    
def crash():
    message_display('You Crashed')



def game_loop():
    x =(display_width * .45)
    y = (display_height * 0.8)
    
    x_change = 0
    
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 15
    thing_width = 170
    thing_height = 220
    
    dodged= 0
    
    global gameExit
    
    while not gameExit:
        
        for event in pygame.event.get(): #check what events are happening per frame
            if event.type == pygame.QUIT: #if person x out of window
                gameExit = True
                #pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -7
                elif event.key == pygame.K_RIGHT:
                    x_change = 7
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                
                
                
        x += x_change
        
        gameDisplay.fill(white)  
        #things(thingx, thingy, thingw, thingh, color)
        
        things(thing_startx, thing_starty, thing_width, thing_height, boulderImg)
        thing_starty += thing_speed
        
        things_dodged(dodged)
        
        player1(x, y)
        if x > display_width +20 - player1_width or x < -20:
            crash()
            gameExit = True
            
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed+=1
            
            
        if y < thing_starty+thing_height:
            print('step 1 ')
            if x > thing_startx and  x <= thing_startx + thing_width or\
            x + player1_width > thing_startx and x + player1_width < thing_startx + thing_width:
                print('x crossover')
                crash()
        
        pygame.display.update() # can just update 1 thingwith parameters/ with no parameters updates everything 
        
        clock.tick(30)
    
    

game_loop()
pygame.quit()

        


