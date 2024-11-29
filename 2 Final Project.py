import pygame, sys
from pygame.locals import *

wood= (200,250,50)
boardwidth= 3
boardheight= 3
spacesize=50
windowwidth = 700 
windowheight = 500 
xmargin = int((windowwidth - boardwidth * spacesize) / 2)
ymargin = int((windowheight - boardheight * spacesize) / 2)
colorboardrings= (0,0,240)#blue
colorplayer1= (250,0,0)#red
colorplayer2= (128,0,128)#purple
blue=(0,240,0)#lime
#board
board=[[[{"size":"L","row":0,"column":0,"player":"1"}],[],[]],
       [[{"size":"S","row":1,"column":0,"player":"0"}],[],[{"size":"M","row":1,"column":0,"player":"1"}]],
       [[],[],[{"size":"L","row":2,"column":2,"player":"0"}]]]

board=[[[],[],[]],
       [[],[],[]],
       [[],[],[]]]


SIZE_RADIUS = {"L":50,
               "M":30,
               "S":6}
SIZES = SIZE_RADIUS.keys()
PLAYER_COLORS={"0":colorplayer1,
       "1":colorplayer2}

CHOSEN_ROW= {0:215,
             1:345,
             2:475}

CHOSEN_COLUMN= {0:90,
                1:220,
                2:350}


def draw():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((windowwidth, windowheight))
    DISPLAYSURF.fill(wood)
    #circles on board
    pygame.font.init()  
    my_font = pygame.font.SysFont('Arial Bold', 30)
    text_surface1 = my_font.render('0', False, (0, 0, 0))
    DISPLAYSURF.blit(text_surface1, (210,10))
    text_surface2 = my_font.render('1', False, (0, 0, 0))
    DISPLAYSURF.blit(text_surface2, (335,10))
    text_surface2 = my_font.render('2', False, (0, 0, 0))
    DISPLAYSURF.blit(text_surface2, (465,10))
    text_surface1 = my_font.render('0', False, (0, 0, 0))
    DISPLAYSURF.blit(text_surface1, (130,90))
    text_surface2 = my_font.render('1', False, (0, 0, 0))
    DISPLAYSURF.blit(text_surface2, (130,220))
    text_surface2 = my_font.render('2', False, (0, 0, 0))
    DISPLAYSURF.blit(text_surface2, (130, 350))
    for i in range(0,3):
        for j in range (0,3):
            values = board[i][j]
            for val in values:
                pygame.draw.circle(DISPLAYSURF, PLAYER_COLORS[val["player"]], (CHOSEN_ROW[val["column"]],CHOSEN_COLUMN[val["row"]]), SIZE_RADIUS[val["size"]], 8)

                

    pygame.font.init()  
    my_font = pygame.font.SysFont('Arial Bold', 30)

    text_surface1 = my_font.render('Player 0', False, (0, 0, 0))
    DISPLAYSURF.blit(text_surface1, (30,15))
    text_surface2 = my_font.render('Player 1', False, (0, 0, 0))
    DISPLAYSURF.blit(text_surface2, (585,15))


    pygame.display.set_caption('Otrio')
    
def display():
    draw()
    player = 0
    while True: # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        res = makemove(str(player))
        while res==False:
            res = makemove(str(player))
        draw()
        pygame.display.update()
        if iswinner(str(player))==True:
            print("Player", player, 'WON!!!')
            break
        player = (player + 1) % 2
    

#check if spot is occupied already
def occupied(size, row, column):
    values= board[row][column]
    result=False
    for val in values:
        if val["size"]==size:
            result=True
            break
    return result
        

#allows player to input size and location of their piece, do a turn
def makemove(player):
    success = False
    print("Player",player,"")
    size= input("Choose size S,M, or L ").upper().strip()
    row= int(input ("Choose row 0, 1, or 2 ").strip())
    column= int(input("Choose column 0, 1, or 2 ").strip())
    if validmove(size,row,column)== True:
        board[row][column].append({"size":size,"row":row,"column":column,"player":player})
        #print('Board ', board)
        success = True
    else:
        print('Invalid move try again')
    return success

#checks if input is valid, correct letter and number input
def validmove(size,row,column):
    result= False
    if size in SIZES and row>=0 and row<=2 and column>=0 and column<=2 and occupied(size, row, column)==False:
        result=True
    return result

#check if there is a winning pattern in one cell (all sizes in one)
def winnercell(row, column):
    result = False
    value = board[row][column]
    if len(value)<3:
        return result
    players = []
    for piece in value:
        players.append(piece['player'])
    if len(set(players))==1:
        result = True
    
    return result


def doesContainPiece(row, column, size, player):
    found = False
    values = board[row][column]
    for val in values:
        if val["player"]==player and val["size"]==size:
            found = True
            break

    return found
        

#check if there is winning pattern in a row
def winnerrow(player):
    result= False
    print('In winner row', player)
    for row in range(3):
        for size in SIZES:
            if all(doesContainPiece(row, j, size, player) for j in range(3)):
                result= True
                print('1 In winner row returns', result)
                return result
    print('2 In winner row returns', result)
    return result
    

#check if there is a winning pattern in a coloumn
def winnercolumn(player):
    pass
    
    
#checks if there is a winner
def iswinner(player):
    winner= False
    print('In iswinner')
    for i in range(0,3):
        for j in range (0,3):
            if winnercell(i, j)==True:
                winner=True
                return winner
    if winnerrow(player)==True:
        winner=True
        return winner

    return winner
            


            
    
display()







