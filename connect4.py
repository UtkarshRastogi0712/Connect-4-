from operator import truediv
import sys, pygame, random, copy
pygame.init()
game_state=True

def endgame(player):
    colour=None
    global text,textRect
    win_text="WINS!!!"
    if(player==1):
        win_text="PLAYER "+win_text
        colour=blue
    else:
        win_text="COMPUTER "+win_text
        colour=red
    text=font.render(win_text, True, colour)
    textRect=text.get_rect()
    textRect.center=(width/2, height/9)

def draw():
    screen.fill(black)
    screen.blit(text, textRect)
    pygame.draw.rect(screen, yellow, fieldRect, border_radius=30)
    for i in range(1,8,1):
        for j in range(1,7,1):
            if state[i-1][-j]==0:
                pygame.draw.circle(screen,black,((70*i)+15,65+(70*j)), 30)
            elif state[i-1][-j]==1:
                pygame.draw.circle(screen,blue,((70*i)+15,65+(70*j)), 30)
            elif state[i-1][-j]==2:
                pygame.draw.circle(screen,red,((70*i)+15,65+(70*j)), 30)
                
    pygame.display.flip()


def game_over(player):
    global game_state
    for i in range(len(state)):
        for j in range(len(state[i])):

            count=0
            for k in range(4):
                if(j+k<len(state[i]) and state[i][j+k]==player):
                    count+=1
                else:
                    break
            if count==4:
                print("Player",player,"won(verticle)!!!")
                game_state=False
                endgame(player)
                draw()
    
            count=0
            for k in range(4):
                if(i+k<len(state) and state[i+k][j]==player):
                    count+=1
                else:
                    break
            if count==4:
                print("Player",player,"won(horizontal)!!!")
                game_state=False
                endgame(player)
                draw()
    
            count=0
            for k in range(4):
                if(j+k<len(state[i]) and i+k<len(state) and state[i+k][j+k]==player):
                    count+=1
                else:
                    break
            if count==4:
                print("Player",player,"won(diagonal + )!!!")
                game_state=False
                endgame(player)
                draw()

            count=0
            for k in range(4):
                if(j+k<len(state[i]) and i-k>=0 and state[i-k][j+k]==player):
                    count+=1
                else:
                    break
            if count==4:
                print("Player",player,"won(diagonal - )!!!")
                game_state=False
                endgame(player)
                draw()

def comp_move():
    comp_col=None
    while True:
        comp_col=random.randint(0,6)
        if state[comp_col][5]==0:
            break
    for i in range(len(state[comp_col])):
        if state[comp_col][i]==0:
            state[comp_col][i]=2
            break
            
def move(row):
    for i in range(len(row)):
        if row[i]==0:
            row[i]=1
            game_over(1)
            comp_move()
            game_over(2)
            break

def column(pos):
    col=(pos-50)//70
    move(state[col])

state=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
size=width, height = (590,580)
screen=pygame.display.set_mode(size)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
font=pygame.font.SysFont("Bauhaus 93",40)
text=font.render("CONNECT 4", True, green)
textRect=text.get_rect()
textRect.center=(width/2, height/9)
fieldRect=pygame.Rect(45,95,500,430)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and game_state==True:
            position=pygame.mouse.get_pos()[0]
            column(position)
    if game_state:
        draw()
        
