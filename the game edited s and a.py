import pygame
from tkinter import *

start=Tk()

start.configure(bg='purple')
start.geometry("900x380")
def game():

        pygame.init()
        khaush = pygame.display.set_mode((900,380))
        pygame.display.set_caption("First Game")
        wr = [pygame.image.load('R1.png'),
              pygame.image.load('R2.png'),
              pygame.image.load('R3.png'),
              pygame.image.load('R4.png'),
              pygame.image.load('R5.png'),
              pygame.image.load('R6.png'),
              pygame.image.load('R7.png'),
              pygame.image.load('R8.png'),
              pygame.image.load('R9.png')]
        wl = [pygame.image.load('L1.png'),
              pygame.image.load('L2.png'),
              pygame.image.load('L3.png'),
              pygame.image.load('L4.png'),
              pygame.image.load('L5.png'),
              pygame.image.load('L6.png'),
              pygame.image.load('L7.png'),
              pygame.image.load('L8.png'),
              pygame.image.load('L9.png')]
        mwl = [pygame.image.load('R1E.png'),
               pygame.image.load('R2E.png'),
               pygame.image.load('R3E.png'),
               pygame.image.load('R4E.png'),
               pygame.image.load('R5E.png'),
               pygame.image.load('R6E.png'),
               pygame.image.load('R7E.png'),
               pygame.image.load('R8E.png'),
               pygame.image.load('R9E.png')]
        mwr = [pygame.image.load('L1E.png'),
               pygame.image.load('L2E.png'),
               pygame.image.load('L3E.png'),
               pygame.image.load('L4E.png'),
               pygame.image.load('L5E.png'),
               pygame.image.load('L6E.png'),
               pygame.image.load('L7E.png'),
               pygame.image.load('L8E.png'),
               pygame.image.load('L9E.png')]




        bg = pygame.image.load('BG.png')



        font1=pygame.font.SysFont("conicsans",30,True,True)
        font2=pygame.font.SysFont("conicsans",90,True,True)

        score= 0
        v,e=wr,wl
        clock = pygame.time.Clock()


        def game_over():
                game_over = font2.render('GAME OVER!!!', 1, (255, 0, 0))
                scor=font1.render('SCORE:' + str(score) ,1, (0,0,0))
                khaush.blit(game_over, (250, 10))
                khaush.blit(scor, (400,70))
                pygame.display.update()
                i = 0
                while i <300:
                    pygame.time.delay(10)
                    i+=1
                
                
        class player(object):
            def __init__(Kind,x,y,width,height):
                Kind.x = x
                Kind.y = y
                Kind.width = width
                Kind.height = height
                Kind.vel = 5
                Kind.jump = False
                Kind.left = False
                Kind.right = False
                Kind.walkcount = 0
                Kind.jumpcount = 7
                Kind.standing = True
                Kind.hitbox = (Kind.x+280 , Kind.y+190, 18, 40)

            def draw(Kind, khaush):
                if Kind.walkcount + 1 >= 27:
                    Kind.walkcount = 0

                if not(Kind.standing):
                    if Kind.left:
                        khaush.blit(wl[Kind.walkcount//3], (Kind.x,Kind.y))
                        Kind.walkcount += 1
                    elif Kind.right:
                        khaush.blit(wr[Kind.walkcount//3], (Kind.x,Kind.y))
                        Kind.walkcount +=1
                else:
                    if Kind.right and villain1.x!=Kind.x:
                        khaush.blit(wr[0], (Kind.x, Kind.y))
                    elif Kind.left and villain1.x!=Kind.x:
                        khaush.blit(wl[0], (Kind.x, Kind.y))
                    else:
                        if Kind.left:
                            khaush.blit(wl[0], (Kind.x, Kind.y))
                        else:
                            khaush.blit(wr[0], (Kind.x, Kind.y))
                Kind.hitbox = (Kind.x+280 , Kind.y + 190, 18, 40)       
                                
        class enemy(object):
            wl = [pygame.image.load('R1E.png'),
                  pygame.image.load('R2E.png'),
                  pygame.image.load('R3E.png'),
                  pygame.image.load('R4E.png'),
                  pygame.image.load('R5E.png'),
                  pygame.image.load('R6E.png'),
                  pygame.image.load('R7E.png'),
                  pygame.image.load('R8E.png'),
                  pygame.image.load('R9E.png')]
            wr = [pygame.image.load('L1E.png'),
                  pygame.image.load('L2E.png'),
                  pygame.image.load('L3E.png'),
                  pygame.image.load('L4E.png'),
                  pygame.image.load('L5E.png'),
                  pygame.image.load('L6E.png'),
                  pygame.image.load('L7E.png'),
                  pygame.image.load('L8E.png'),
                  pygame.image.load('L9E.png')]
            
            def __init__(Kind, x, y, width, height, end):
                Kind.x = x
                Kind.y = y
                Kind.width = width
                Kind.height = height
                Kind.path = [x, end]
                Kind.walkcount = 0
                Kind.vel = 3
                Kind.hitbox = (Kind.x+280 , Kind.y+190, 18, 40)
            def draw(Kind, khaush):
                Kind.move()
                if Kind.walkcount + 1 >= 27:
                    Kind.walkcount = 0
                if Kind.x==man.x and man.y==0:
                    khaush.blit(go,(100,20))
                elif Kind.vel < 0:
                    khaush.blit(Kind.wr[Kind.walkcount//3], (Kind.x,Kind.y))
                    Kind.walkcount += 1
                else:
                    khaush.blit(Kind.wl[Kind.walkcount//3], (Kind.x,Kind.y))
                    Kind.walkcount += 1
                Kind.hitbox = (Kind.x+280 , Kind.y + 190, 18, 40) 
               
                    
            def move(Kind):
                
                if Kind.vel > 0:
                    if Kind.x > Kind.path[1] + Kind.vel :
                        if Kind.hitbox[0]<man.hitbox[0]+18 and Kind.hitbox[0]>man.hitbox[0]-18 and Kind.hitbox[1]==man.hitbox[1]:
                            game_over()
                        else:
                            Kind.x -= Kind.vel
                    else:
                        Kind.vel = Kind.vel * -1
                        Kind.x += Kind.vel
                        Kind.walkcount = 0
                    
                else:
                    if Kind.x < Kind.path[0] - Kind.vel :
                        if Kind.hitbox[0]<man.hitbox[0]+18 and Kind.hitbox[0]>man.hitbox[0]-18 and Kind.hitbox[1]==man.hitbox[1]:
                            game_over()
                        else:
                            Kind.x -= Kind.vel
                    else:
                        Kind.vel = Kind.vel * -1
                        Kind.x += Kind.vel
                        Kind.walkcount = 0
           

        class enemy2(object):
            wl = [pygame.image.load('R1E.png'),
                  pygame.image.load('R2E.png'),
                  pygame.image.load('R3E.png'),
                  pygame.image.load('R4E.png'),
                  pygame.image.load('R5E.png'),
                  pygame.image.load('R6E.png'),
                  pygame.image.load('R7E.png'),
                  pygame.image.load('R8E.png'),
                  pygame.image.load('R9E.png')]
            wr = [pygame.image.load('L1E.png'),
                  pygame.image.load('L2E.png'),
                  pygame.image.load('L3E.png'),
                  pygame.image.load('L4E.png'),
                  pygame.image.load('L5E.png'),
                  pygame.image.load('L6E.png'),
                  pygame.image.load('L7E.png'),
                  pygame.image.load('L8E.png'),
                  pygame.image.load('L9E.png')]
            
            def __init__(Kind, x, y, width, height, end):
                Kind.x = x
                Kind.y = y
                Kind.width = width
                Kind.height = height
                Kind.path = [x, end]
                Kind.walkcount = 0
                Kind.vel = 4
                Kind.hitbox = (Kind.x+280 , Kind.y+190, 18, 40)

            def draw(Kind, khaush):
                Kind.move()
                if Kind.walkcount + 1 >= 27:
                    Kind.walkcount = 0
                if Kind.x==man.x and man.y==0:
                    khaush.blit(go,(100,20))
                elif Kind.vel < 0:
                    khaush.blit(Kind.wr[Kind.walkcount//3], (Kind.x,Kind.y))
                    Kind.walkcount += 1
                else:
                    khaush.blit(Kind.wl[Kind.walkcount//3], (Kind.x,Kind.y))
                    Kind.walkcount += 1
                Kind.hitbox = (Kind.x+280 , Kind.y + 190, 18, 40) 
                
                    
            def move(Kind):
                
                if Kind.vel > 0:
                    if Kind.x > Kind.path[1] + Kind.vel :
                        if Kind.hitbox[0]<man.hitbox[0]+18 and Kind.hitbox[0]>man.hitbox[0]-18 and Kind.hitbox[1]==man.hitbox[1]:
                            game_over()
                        else:
                            Kind.x -= Kind.vel
                    else:
                        Kind.vel = Kind.vel * -1
                        Kind.x += Kind.vel
                        Kind.walkcount = 0
                    
                else:
                    if Kind.x < Kind.path[0] - Kind.vel:
                        if Kind.hitbox[0]<man.hitbox[0]+18 and Kind.hitbox[0]>man.hitbox[0]-18 and Kind.hitbox[1]==man.hitbox[1]:
                            game_over()
                        else:
                            Kind.x -= Kind.vel
                    else:
                        Kind.vel = Kind.vel * -1
                        Kind.x += Kind.vel
                        Kind.walkcount = 0      

        class enemy3(object):
            wl = [pygame.image.load('R1E.png'),
                  pygame.image.load('R2E.png'),
                  pygame.image.load('R3E.png'),
                  pygame.image.load('R4E.png'),
                  pygame.image.load('R5E.png'),
                  pygame.image.load('R6E.png'),
                  pygame.image.load('R7E.png'),
                  pygame.image.load('R8E.png'),
                  pygame.image.load('R9E.png')]
            wr = [pygame.image.load('L1E.png'),
                  pygame.image.load('L2E.png'),
                  pygame.image.load('L3E.png'),
                  pygame.image.load('L4E.png'),
                  pygame.image.load('L5E.png'),
                  pygame.image.load('L6E.png'),
                  pygame.image.load('L7E.png'),
                  pygame.image.load('L8E.png'),
                  pygame.image.load('L9E.png')]
            
            def __init__(Kind, x, y, width, height, end):
                Kind.x = x
                Kind.y = y
                Kind.width = width
                Kind.height = height
                Kind.path = [x, end]
                Kind.walkcount = 0
                Kind.vel = 5
                Kind.hitbox = (Kind.x+280 , Kind.y+190, 18, 40)

            def draw(Kind, khaush):
                Kind.move()
                if Kind.walkcount + 1 >= 27:
                    Kind.walkcount = 0
                if Kind.x==man.x and man.y==0:
                    khaush.blit(go,(100,20))
                elif Kind.vel < 0:
                    khaush.blit(Kind.wr[Kind.walkcount//3], (Kind.x,Kind.y))
                    Kind.walkcount += 1
                else:
                    khaush.blit(Kind.wl[Kind.walkcount//3], (Kind.x,Kind.y))
                    Kind.walkcount += 1
                Kind.hitbox = (Kind.x+280 , Kind.y + 190, 18, 40) 
                
                    
            def move(Kind):
                
                if Kind.vel > 0:
                    if Kind.x > Kind.path[1] + Kind.vel :
                        if Kind.hitbox[0]<man.hitbox[0]+18 and Kind.hitbox[0]>man.hitbox[0]-18 and Kind.hitbox[1]==man.hitbox[1]:
                            game_over()
                        else:
                            Kind.x -= Kind.vel
                    else:
                        Kind.vel = Kind.vel * -1
                        Kind.x += Kind.vel
                        Kind.walkcount = 0
                    
                else:
                    if Kind.x < Kind.path[0] - Kind.vel:
                        if Kind.hitbox[0]<man.hitbox[0]+18 and Kind.hitbox[0]>man.hitbox[0]-18 and Kind.hitbox[1]==man.hitbox[1]:
                            game_over()
                        else:
                            Kind.x -= Kind.vel
                    else:
                        Kind.vel = Kind.vel * -1
                        Kind.x += Kind.vel
                        Kind.walkcount = 0                

        class enemy4(object):
            wl = [pygame.image.load('R1E.png'),
                  pygame.image.load('R2E.png'),
                  pygame.image.load('R3E.png'),
                  pygame.image.load('R4E.png'),
                  pygame.image.load('R5E.png'),
                  pygame.image.load('R6E.png'),
                  pygame.image.load('R7E.png'),
                  pygame.image.load('R8E.png'),
                  pygame.image.load('R9E.png')]
            wr = [pygame.image.load('L1E.png'),
                  pygame.image.load('L2E.png'),
                  pygame.image.load('L3E.png'),
                  pygame.image.load('L4E.png'),
                  pygame.image.load('L5E.png'),
                  pygame.image.load('L6E.png'),
                  pygame.image.load('L7E.png'),
                  pygame.image.load('L8E.png'),
                  pygame.image.load('L9E.png')]
            
            def __init__(Kind, x, y, width, height, end):
                Kind.x = x
                Kind.y = y
                Kind.width = width
                Kind.height = height
                Kind.path = [x, end]
                Kind.walkcount = 0
                Kind.vel = 6
                Kind.hitbox = (Kind.x+280 , Kind.y+190, 18, 40)

            def draw(Kind, khaush):
                Kind.move()
                if Kind.walkcount + 1 >= 27:
                    Kind.walkcount = 0
                if Kind.x==man.x and man.y==0:
                    khaush.blit(go,(100,20))
                elif Kind.vel < 0:
                    khaush.blit(Kind.wr[Kind.walkcount//3], (Kind.x,Kind.y))
                    Kind.walkcount += 1
                else:
                    khaush.blit(Kind.wl[Kind.walkcount//3], (Kind.x,Kind.y))
                    Kind.walkcount += 1
                Kind.hitbox = (Kind.x+280 , Kind.y + 190, 18, 40) 
                
                    
            def move(Kind):
                
                if Kind.vel > 0:
                    if Kind.x > Kind.path[1] + Kind.vel:
                        if Kind.hitbox[0]<man.hitbox[0]+18 and Kind.hitbox[0]>man.hitbox[0]-18 and Kind.hitbox[1]==man.hitbox[1]:
                            game_over()
                        else:
                            Kind.x -= Kind.vel
                    else:
                        Kind.vel = Kind.vel * -1
                        Kind.x += Kind.vel
                        Kind.walkcount = 0
                    
                else:
                    if Kind.x < Kind.path[0] - Kind.vel:
                        if Kind.hitbox[0]<man.hitbox[0]+18 and Kind.hitbox[0]>man.hitbox[0]-18 and Kind.hitbox[1]==man.hitbox[1]:
                            game_over()
                        else:
                            Kind.x -= Kind.vel
                    else:
                        Kind.vel = Kind.vel * -1
                        Kind.x += Kind.vel
                        Kind.walkcount = 0

        def Gloop():
            khaush.blit(bg, (0,0))
            man.draw(khaush)
            villain1.draw(khaush)
            villain2.draw(khaush)
            villain3.draw(khaush)
            villain4.draw(khaush)
            scor=font1.render('SCORE:' + str(score) ,1, (0,0,0))
            khaush.blit(scor , (700,50))
            pygame.display.update()


        #mainloop
        font = pygame.font.SysFont('comicsans', 30, True)
        man = player(-290, 20, 64,64)
        villain1 = enemy(600, 20, 64, 64, -290)
        villain2 = enemy2(600, 20, 64, 64, -290)
        villain3 = enemy3(600, 20, 64, 64, -290)
        villain4 = enemy4(600, 20, 64, 64, -290)

        bullets = []
        run = True
        while run:
            clock.tick(27)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()

            
            if keys[pygame.K_LEFT] and man.x >-290:
                if man.hitbox[0]<villain1.hitbox[0]+18 and man.hitbox[0]>villain1.hitbox[0]-18 and man.hitbox[1]==villain1.hitbox[1]:
                    standing=True
                    
                elif man.hitbox[0]<villain2.hitbox[0]+18 and man.hitbox[0]>villain2.hitbox[0]-18 and man.hitbox[1]==villain2.hitbox[1]:
                    standing=True
                    
                elif man.hitbox[0]<villain3.hitbox[0]+18 and man.hitbox[0]>villain3.hitbox[0]-18 and man.hitbox[1]==villain3.hitbox[1]:
                    standing=True
                    
                elif man.hitbox[0]<villain4.hitbox[0]+18 and man.hitbox[0]>villain4.hitbox[0]-18 and man.hitbox[1]==villain4.hitbox[1]:
                    standing=True
                else:
                    man.x -= man.vel
                    man.left = True
                    man.right = False
                    man.standing = False
                if man.x == -290 and (score%2)==1:
                    score+=5
                    print("score:",score)

            elif keys[pygame.K_RIGHT] and man.x <600:
                if man.hitbox[0]<villain1.hitbox[0]+18 and man.hitbox[0]>villain1.hitbox[0]-18 and man.hitbox[1]==villain1.hitbox[1]:
                    standing=True
                    
                    
                elif man.hitbox[0]<villain2.hitbox[0]+18 and man.hitbox[0]>villain2.hitbox[0]-18 and man.hitbox[1]==villain2.hitbox[1]:
                    standing=True
                    
                elif man.hitbox[0]<villain3.hitbox[0]+18 and man.hitbox[0]>villain3.hitbox[0]-18 and man.hitbox[1]==villain3.hitbox[1]:
                    standing=True
                    
                elif man.hitbox[0]<villain4.hitbox[0]+18 and man.hitbox[0]>villain4.hitbox[0]-18 and man.hitbox[1]==villain4.hitbox[1]:
                    standing=True

                    
                else:
                    man.x += man.vel
                    man.right = True
                    man.left = False
                    man.standing = False    
                if man.x == 600 and score%2==0:
                    score+=5
                    print("score:", score)
                    
            elif keys[pygame.K_m]: 
                m=wr
                wr=wl
                wl=m
            elif keys[pygame.K_k]:
                wr=mwr
                wl=mwl
                wl=wl
                wr=wr
            elif keys[pygame.K_l]:
                wr=v
                wl=e
            
            else:
                man.standing = True
                man.walkcount = 0
                    
            if not(man.jump):
                if keys[pygame.K_UP]:
                    man.jump = True
                    man.right = False
                    man.left = False
                    man.walkcount = 0
            else:
                if man.jumpcount >= -7:
                    neg = 1
                    if man.jumpcount < 0:
                        neg = -1
                    man.y -= int((man.jumpcount ** 2) * 0.5 * neg)
                    man.jumpcount -= 1
                else:
                    man.jump = False
                    man.jumpcount = 7
                    
            Gloop()
          
        pygame.quit()


def HELP():
        help1=Tk()
        help1.configure(bg='purple')
        help1.geometry("900x380")
        w = Label(help1, text='INSTRUCTIONS',)
        w.config(font=("Courier", 42))
        e = Label(help1, text='UP ARROW KEY = JUMP')
        e.config(font=("Courier", 14))
        e.place(x=20,y=100)
        r = Label(help1, text='RIGHT ARROW KEY = MOVE FORWARD')
        r.config(font=("Courier", 12))
        r.place(x=20,y=140)
        t = Label(help1, text='LEFT ARROW KEY = MOVE BACKWARD')
        t.config(font=("Courier", 12))
        t.place(x=20,y=180)
        t = Label(help1, text='TOUCHING THE WALLS (THE END OF THE SCREEN) WILL FETCH YOU FIVE POINTS(I.E SCORE+5)')
        t.config(font=("Courier", 12))
        t.place(x=20,y=220)
        t = Label(help1, text='TOUCHING OR COLLIDING WITH THE ENIMIES(GAURDS) WILL MAKE YOU LOSE THE GAME')
        t.config(font=("Courier", 12))
        t.place(x=20,y=260)
        
        
        w.pack()
def about():
        ABOUT=Tk()
        ABOUT.configure(bg='purple')
        ABOUT.geometry("900x380")
        x = Label(ABOUT, text='ABOUT',)
        x.config(font=("Courier", 44))
        c = Label(ABOUT, text='THIS GAME WAS CREATED AND DEVELOPED BY')
        c.config(font=("Courier", 14))
        c.place(x=20,y=100)
        O = Label(ABOUT, text='C.VR.KAUSHIK NARAYANAN')
        O.config(font=("Courier", 20))
        O.place(x=450,y=95)
        Z = Label(ABOUT, text='THIS GAME WAS RELEASED ON 19TH FEBRAURY 2020')
        Z.config(font=("Courier", 20))
        Z.place(x=20,y=135)
        x.pack()
        
button=Button(start,text="GAME", bd='5',command=game,font=("Courier", 20))
button2=Button(start,text="HELP", bd='5',command=HELP,font=("Courier", 20))
button3=Button(start,text="ABOUT", bd='5',command=about,font=("Courier", 20))
button.place(x=410,y=120)
button2.place(x=410,y=210)
button3.place(x=403,y=300)
B = Label(start, text='WALL TOUCH')
B.config(font=("Courier", 50))
B.place(x=260,y=10)
start.mainloop()


          
