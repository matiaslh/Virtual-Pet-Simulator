import pygame,sys,random,math
from pygame.locals import *
from time import sleep

class Pet():
    def __init__(self):
        self.hunger=.7
        self.happy=.5
        self.happyBoost=0
        self.toilet=0
        self.dirty=0
        self.sprite=pygame.image.load('idle.png')
        self.runsAway=0
    
    def update(self):
        self.hunger-=.01
        self.happy+=self.happyBoost
        self.happyBoost-=.05
        self.toilet+=self.hunger/30
        
        
        self.happy+=(self.hunger-0.5)/10
            
        
                
        if self.hunger==0:
            #DIES
            pass
        if self.happy<=.1:
            self.runsAway+=50

            
            pass
        if self.happy>=.6 and self.runsAway>0:
            self.runsAway-=20
        if self.dirty>=.6:
            self.happy-=(self.dirty-0.6)/2
        
        
        if(self.happyBoost<0):
            self.happyBoost=0
        if(self.happy<0):
            self.happy=0
        if(self.hunger<0):
            self.hunger=0
        if(self.dirty<0):
            self.dirty=0
        if(self.toilet<0):
            self.toilet=0
        if(self.happyBoost>1):
            self.happyBoost=1
        if(self.happy>1):
            self.happy=1
        if(self.hunger>1):
            self.hunger=1
        if(self.dirty>1):
            self.dirty=1
        if(self.toilet>1):
            self.toilet=1
        
        
        
        
        
    
    
    
class Game():
    def __init__(self):
        self.pet=Pet()
        self.screen=Home(self.pet)
    def render(self):
        self.screen.render()
    
      
    def update(self):
        self.screen.update()
    
    
class Screen():
    def render(self,pet):
        pass
    def update(self):
        pass
    
class Home(Screen):
    def __init__(self,pet):
        pet.update()
        self.happyText=font.render("Happiness", 1, blue)
        self.hungerText=font.render("Hunger", 1, blue)
        self.dirtyText=font.render("Dirty", 1, blue)
        self.toiletText=font.render("Toilet", 1, blue)
        self.sprite=pet.sprite
        self.pet=pet
        self.hud=(0,h/4.0*3,w,h/4.0)
        self.counter=0
        self.petCounter=0
        self.timer=random.random()
        self.hungerImage=pygame.image.load('hungry.png')
        self.happyImage=pygame.image.load('sadface.png')
        self.toiletImage=pygame.image.load('toilet.png')
        self.running=True
        self.ranAway=font.render("Your pet ran away! You lose", 1, black)
    def update(self):
        if self.pet.runsAway>=450:
            self.running=False
        if self.running:
            self.counter+=fps
            self.petCounter+=fps
            
            if (clean):
                game.screen=Clean(self.pet)
            
            if (feed):
                game.screen=Feed(self.pet)
                
            
            if(walk):
                game.screen=Walk(self.pet)
            
            if self.petCounter>=1:
                self.pet.update()
                self.petCounter=0
                
            if self.counter>=self.timer:
                self.timer=random.random()*5
                self.counter=0
                self.sprite=pygame.transform.flip(self.sprite,True,False)
            
    def render(self):
        if not self.running:
            screen.blit(self.ranAway,(w/2-150,h/2-100))
        else:
            screen.blit(self.sprite,(w/2.0-64+self.pet.runsAway,h/3.0-20))
        
            if self.pet.hunger<0.4:
                screen.blit(self.hungerImage,((w/2.0+128-64+self.pet.runsAway,h/3.0-130-20)))
            if self.pet.happy<0.4:
                screen.blit(self.happyImage,((w/2.0-128-64+self.pet.runsAway,h/3.0-110-20)))
            if self.pet.toilet>0.6:
                screen.blit(self.toiletImage,((w/2.0-15-64+self.pet.runsAway,h/3.0-190-20)))
        self.renderBars()
    def renderBars(self):
        pygame.draw.rect(screen,black,self.hud)
        #TL TR BL BR
        pygame.draw.rect(screen,(255,128,0),(self.hud[0]+5,self.hud[1]+10,(self.hud[2]/2.0-10)*self.pet.happy,self.hud[3]/2-10))
        pygame.draw.rect(screen,(255,1,1),(self.hud[0]+5+self.hud[2]/2.0,self.hud[1]+10,(self.hud[2]/2.0-10)*self.pet.hunger,self.hud[3]/2-10))
        pygame.draw.rect(screen,(255,255,0),(self.hud[0]+5,self.hud[1]+5+self.hud[3]/2.0,(self.hud[2]/2.0-10)*self.pet.toilet,self.hud[3]/2-10))
        pygame.draw.rect(screen,(153,76,0),(self.hud[0]+5+self.hud[2]/2.0,self.hud[1]+5+self.hud[3]/2.0,(self.hud[2]/2.0-10)*self.pet.dirty,self.hud[3]/2-10))
        
        screen.blit(self.happyText,(self.hud[0]+10,self.hud[1]+23))
        screen.blit(self.hungerText,(self.hud[0]+10+self.hud[2]/2.0,self.hud[1]+23))
        screen.blit(self.toiletText,(self.hud[0]+10,self.hud[1]+5+self.hud[3]/2.0+15))
        screen.blit(self.dirtyText,(self.hud[0]+10+self.hud[2]/2.0,self.hud[1]+5+self.hud[3]/2.0+15))

class Walk(Screen):
    def __init__(self,pet):
        self.poop=pygame.transform.scale(pygame.image.load('poop.png'),(math.floor(h/5),math.floor(h/5)))
        self.poops=[]
        self.playerY=2
        self.petSprite=pygame.transform.scale(pet.sprite,(math.floor(h/5),math.floor(h/5)))
        self.counter=0
        self.alive=True
        self.pet=pet
        self.loseText=font.render("Ew! You fell in poop. Go clean up!", 1, black)
        for i in range(5,75):
            self.poops.append([i,random.randint(0,4)])
    def update(self):
        self.counter+=fps
        for i in self.poops:
            if i[0]==0 and i[1]==self.playerY:
                self.alive=False
       
        if self.alive:
            if len(self.poops)==0:
                self.loseText=font.render("You did it! You successfully went on a walk!",1,black)
                self.alive=False

            if self.counter>=0.2:
                self.counter=0
                for i in range(len(self.poops)):
                    self.poops[i][0]-=1
                for i in self.poops:
                    if i[0]<0:
                        self.poops.remove(i)
                        
            if up and self.playerY>0:
                self.playerY-=1
            if down and self.playerY<4:
                self.playerY+=1
        else:
            if self.counter>=3:
                if(len(self.poops)==0):
                    self.pet.happyBoost=0.07
                    self.pet.toilet=0
                else:
                    self.pet.happy-=.3
                    self.pet.dirty+=.35
                self.pet.hunger-=0.2
                game.screen=Home(self.pet)           
            
            
    def render(self):
        if self.alive:
            for i in range(len(self.poops)):
                screen.blit(self.poop,(self.poops[i][0]*h/5,self.poops[i][1]*h/5))
        else:
            if len(self.poops)>0:
                screen.blit(self.poop,(self.poops[0][0]*h/5,self.poops[0][1]*h/5))
            screen.blit(self.loseText,(w/4-70,h/2))
        screen.blit(self.petSprite,(0,self.playerY*h/5))
class Feed:
    def __init__(self,pet):
        self.endText=font.render("You just gnobbled some chicken!",1,black)
        self.playerX=8
        self.playerY=8
        self.bones=[]
        self.dx=0
        self.dy=0
        self.pet=pet
        self.gridSize=16
        self.counter=0
        self.chicken=(random.randint(0,15),random.randint(0,15))
        self.finalCount=0
        self.gg=False
        self.chickenCollected=0
        self.petImage=pygame.transform.scale(pet.sprite,(math.floor(w/self.gridSize),math.floor(h/self.gridSize)))
        self.chickenImage=pygame.transform.scale(pygame.image.load('chicken.png'),(math.floor(w/self.gridSize),math.floor(h/self.gridSize)))
        self.bonesImage=pygame.transform.scale(pygame.image.load('bones.png'),(math.floor(w/self.gridSize),math.floor(h/self.gridSize)))
    def update(self):
        if up:
            self.dx=0
            self.dy=-1
        if down:
            self.dx=0
            self.dy=1
        if right:
            self.dx=1
            self.dy=0
        if left:
            self.dx=-1
            self.dy=0
        
        self.counter+=fps
        
        
        if self.counter>=0.13 and not self.gg:
            self.playerX+=self.dx
            self.playerY+=self.dy
            self.finalCount+=self.counter
            self.counter=0
            
            
            if self.playerX==-1 or self.playerY==-1 or self.playerX>15 or self.playerY>15:
                self.gg=True
                self.playerX-=self.dx
                self.playerY-=self.dy
                self.endText=font.render("Out of bounds! Foul!",1,black)
                
            for i in self.bones:
                if i[0]==self.playerX and i[1]==self.playerY:
                    self.gg=True
                    self.pet.dirty+=.2
                    self.endText=font.render("You just stepped on a bone!",1,black)
            
            if self.chicken[0]==self.playerX and self.chicken[1]==self.playerY:
                self.chickenCollected+=1
                self.bones.append(self.chicken)
                while (True):
                    self.chicken=(random.randint(0,15),random.randint(0,15))
                    noBones=True
                    for i in self.bones:
                        if i==self.chicken:
                            noBones=False
                    if noBones:
                        break

        if self.finalCount>=30:
            self.gg=True
        
        if self.counter>=3:
            if self.finalCount>=30:
                self.pet.hunger+=self.chickenCollected/13
            else:
                self.pet.hunger+=self.chickenCollected/50.0
                self.pet.happy-=(0.2*2.5)/(self.finalCount)
            game.screen=Home(self.pet)

                
    
    def render(self):
        
        for i in self.bones:
            screen.blit(self.bonesImage,(i[0]*w/self.gridSize,i[1]*h/self.gridSize))
        screen.blit(self.chickenImage,(self.chicken[0]*w/self.gridSize,self.chicken[1]*h/self.gridSize))
        screen.blit(self.petImage,(self.playerX*w/self.gridSize,self.playerY*h/self.gridSize))
        if self.gg:
            screen.blit(self.endText,((w/2.0-100,h/2.0)))
         
class Clean(Screen):
    def __init__(self,pet):
        self.pet=pet
        self.brushX=1
        self.running=True
        self.counter=0
        self.cleanCounter=0
        self.finalCounter=0
        self.brush=pygame.image.load('brush.png')
        self.bathtub=pygame.transform.scale(pygame.image.load('bathtub.png'),(400,200))
        self.sprite=pygame.transform.scale(pet.sprite,(250,250))
        self.endText=font.render("All clean!",1,black)
    def update(self):
        self.finalCounter+=fps
        if self.finalCounter>=7:
            self.running=False
        if self.running:
            if right and self.brushX==-1:
                self.brushX=1
            if left and self.brushX==1:
                self.brushX=-1
                self.cleanCounter+=1
        else:
            self.counter+=fps
        if self.counter>=3:
            self.pet.dirty-=self.cleanCounter/30.0
            game.screen=Home(self.pet)
            

    def render(self):
        screen.blit(self.sprite,(w/2.0-135,h/3.0-20-20))
        screen.blit(self.brush,(w/2-64+self.brushX*50,h/2-160))
        screen.blit(self.bathtub,(0+100,h/2-50))
        if not self.running:
            screen.blit(self.endText,(w/2-75,h/2+75-15))  
pygame.init()
font = pygame.font.Font(None, 36)
w,h=640,480
screen = pygame.display.set_mode((w,h))
white=(250,250,250)
black=(0,0,0)
blue=(204,229,255)
game = Game()
fps=1.0/60
up,down,left,right,walk,feed,clean=False,False,False,False,False,False,False
upP,downP,leftP,rightP=False,False,False,False

while 1:
    sleep(fps)
    screen.fill(white)
    game.update()
    
    up,down,left,right=False,False,False,False
    
    game.render()
    
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if pygame.key.get_pressed()[K_ESCAPE]:
                pygame.quit()
                sys.exit()
        if pygame.key.get_pressed()[K_UP]:
            if not upP:
                up=True
            else:
                up=False
        upP=pygame.key.get_pressed()[K_UP]
        
        if pygame.key.get_pressed()[K_DOWN]:
            if not downP:
                down=True
            else:
                down=False
        downP=pygame.key.get_pressed()[K_DOWN]
        
        if pygame.key.get_pressed()[K_LEFT]:
            if not leftP:
                left=True
            else:
                left=False
        leftP=pygame.key.get_pressed()[K_LEFT]
        
        if pygame.key.get_pressed()[K_RIGHT]:
            if not rightP:
                right=True
            else:
                right=False
        rightP=pygame.key.get_pressed()[K_RIGHT]
        
        
        walk = pygame.key.get_pressed()[K_w]
        feed = pygame.key.get_pressed()[K_f]
        clean = pygame.key.get_pressed()[K_c]
        
    pygame.display.flip()
    
    
    
    