#Name: Yash Raja
#Date: June 11th, 2019
#Filename:  Space_Invaders.py
#Description: A game of space invaders with main menu and allows user to change important settings

import pygame
import random

class Keys:
    #This class allows user to create instances of keys that need to be clicked
    #to do certain tasks, the class has a class variable that allows the code
    #to check if a user has tried to quit the game
    quitGame = False
    def __init__(self,l,click,x,y):
        #Method that checks the name/unicode of the key that is pressed,
        #checks if it is being used by another Key, by holding all keys in a
        #list, instance has 3 attributes a name, a string name of key, a
        #check to see if it is unique, and a key, special number representing
        #what key is pressed
        name, key = keyName(x,y)#Fucntion called keyName that creates a white box
        #on the x,y (which are positions for where the box is supposed to be)
        #returns the name and the key number
        rep = self.keyChange(key,l,click)#calls keyChange Method checks if the key
        #number is unique if it is then sets the attribute to the key number
        if name == None and key == None:
            rep = True
            Keys.quitGame = True
        self.name = name
        self.rep = rep
        
    def keyChange(self,key,l,click):
        #Checks if key number is unique, changes key attribute if it is unique
        repeat = False
        for x in range(len(l)):
            if l[x]!= None:
                if l[x].key == key:
                    repeat= True
        if not(repeat):
            self.key= key
        if not(click) and (key == pygame.MOUSEBUTTONUP or key == pygame.K_RSHIFT or key == pygame.K_LSHIFT):
            return True
        return repeat
class KeysDefault:
    #Used to initialize keys at the start of the game, has 2 attributes, name and key
    def __init__(self,name,key):
        self.name = name
        self.key = key
class GreenAlien:
    #Class of all greenAliens using the worth of the alien decides which
    #alien to display, has attributes such as w, for pygame surface, xval
    #for x of top left of image, y val for y of top left, worth of the alien
    #Has methods that draw the alien, move the alien, check if the alien is hit
    #and that shoot a bullet, creates instance of Alien Bullet
    def __init__(self,worth,w,x,y):
        if worth == 10:
            self.image = [pygame.image.load("10open.png"),pygame.image.load("10closed.png")]
        elif worth == 20:
            self.image = [pygame.image.load("20open.png"),pygame.image.load("20closed.png")]
        elif worth == 40:
            self.image = [pygame.image.load("40open.png"),pygame.image.load("40closed.png")]
        self.image = [pygame.transform.scale(self.image[0], (xAlienSize,yAlienSize)),pygame.transform.scale(self.image[1], (xAlienSize,yAlienSize))]
        self._xval = x
        self._yval = y
        self.w = w
        self.worth = worth
        self.drawAlien()
    @property
    def xval(self):
        return self._xval
    @xval.setter
    def xval(self,x):
        self._xval = x
        self.drawAlien()
    @property
    def yval(self):
        return self._yval
    @yval.setter
    def yval(self,y):
        self._yval = y
        #if y >= (screenY-screenY//7):
         #   self.yval = 100
        self.drawAlien()
    def drawAlien(self):
        if t <= 60:
            self.w.blit(self.image[0],(self.xval, self.yval))
        else:
            self.w.blit(self.image[1],(self.xval, self.yval))
    def checkHit(self, bulletX, bulletY,c,v):
        #Checks if the Ship's Bullet hits an alien, if hit returns True,worth,pos
        #if not hit then returns False,None,None
        if (bulletX>=self.xval and bulletX<=(self.xval+xAlienSize))or ((bulletX+shipBulletX)>=self.xval and (bulletX+shipBulletX)<=(self.xval+xAlienSize)):
            if (bulletY>=self.yval and bulletY<=(self.yval+yAlienSize))or ((bulletY+shipBulletY)>=self.yval and (bulletY+shipBulletY)<=(self.yval+yAlienSize)):
                del aliens[c][v]
                worth = self.worth
                pos = (self.xval,self.yval)
                del self
                return True, worth,pos
                
        return False, None,None
    def shoot(self):
        return AlienBullet(self.xval,self.yval)#Creates instance of a class Alien
        #bullet that has the xval and yval of the alien
class Spaceship:
    #Class of spaceShip, has attributes such as xval
    #for x of top left of image, y val for y of top left, shot, if it is shot
    #Has methods that draw the alien, move the alien, check if the ship is
    #hit and that shoot a bullet, creates a moving a bullet
    #Bullet has attributes of itself such as bulletX, shot, bullet,bullet is the image
    def __init__(self,w):
        self.image = pygame.image.load("ship.png")
        self.image = pygame.transform.scale(self.image, (xShipSize,yShipSize))
        self._xval = shipStartX
        self._yval = shipStartY
        self.shot = False
        self.drawShip()
    @property
    def xval(self):
        return self._xval
    @xval.setter
    def xval(self,x):
        if x > (screenX-xShipSize) or x < 0:
           if x >= (screenX-xShipSize):
               self.xval = (screenX-xShipSize)
           if x <= 0:
               self.xval = 0
        else:
            self._xval = x 
        self.drawShip()
    @property
    def yval(self):
        return self._yval
    @yval.setter
    def yval(self,y):
        self._yval = y
        #if y >= (screenY-screenY//7):
         #   self.yval = 100
        self.drawShip()
    def drawShip(self):
        window.blit(self.image,(self.xval, self.yval))
        if self.shot == True:
            self.drawBullet()
    def drawBullet(self):
        window.blit(self.bullet,(self.bulletX, self.bulletY))
    def shoot(self, hit = None):
        #if a bullet was shot already checks if hit or edge of screen to stop the bullet
        #if not shot then displays the bullet
        if self.shot == False:            
            self.shot = True
            self.bullet = pygame.image.load("shipBullet.png")
            self.bullet = pygame.transform.scale(self.bullet, (shipBulletX,shipBulletY))
            self.bulletX = self.xval+(.5*xShipSize) -(shipBulletX*.5)
            self.bulletY = self.yval
        if hit == True or self.bulletY <= 0:
            self.shot = False
    def checkHit(self, bulletX, bulletY):
        #checks if alienBullet hit the spaceShip
        if (bulletX>=self.xval and bulletX<=(self.xval+xShipSize))or ((bulletX+shipBulletX)>=self.xval and (bulletX+shipBulletX)<=(self.xval+redAlienX)):
            if (bulletY>=self.yval and bulletY<=(self.yval+yShipSize))or ((bulletY+shipBulletY)>=self.yval and (bulletY+shipBulletY)<=(self.yval+redAlienY)):
                return True
        return False
class RedAlien:
    #Attributes: Has worth of random points, xval, yval
    def __init__(self, w,x):
        self.image = pygame.image.load("Red Alien.png")
        self.image = pygame.transform.scale(self.image, (redAlienX,redAlienY))
        self._xval = x
        self.yval = minRedAlienY
        self.worth = random.randrange(200, 400, 5)
        self.drawAlien()
    def drawAlien(self):
        window.blit(self.image,(self.xval, self.yval))
    @property
    def xval(self):
        return self._xval
    @xval.setter
    def xval(self,x):
        self._xval = x
        if x <= (0-redAlienX):
            self.xval = screenX
        self.drawAlien()
    def checkHit(self, bulletX, bulletY):
        #checks if it is hit by a ship bullet using the x and y of the bullet
        if (bulletX>=self.xval and bulletX<=(self.xval+xShipSize))or ((bulletX+shipBulletX)>=self.xval and (bulletX+shipBulletX)<=(self.xval+shipBulletX)):
            if (bulletY>=self.yval and bulletY<=(self.yval+yShipSize))or ((bulletY+shipBulletY)>=self.yval and (bulletY+shipBulletY)<=(self.yval+shipBulletY)):
                pos = (self.xval+(3/16*redAlienX),self.yval+(4/16*redAlienY))
                return True, self.worth,pos
        return False, None, None
class Barrier:
    def __init__(self, w,x,y):
        self.image = pygame.image.load("greenPixel.png")
        self.image = pygame.transform.scale(self.image, (greenPixelX,greenPixelY))
        self.xval = x
        top1 = []
        self.yval = y
        #initializing all pixels of the image that make the barrier
        #Displaying all pixels of the barrier
        for x in range(int(((219/344)*(barrierSectionX))+((0)*barrierSectionX)+self.xval),int((barrierSectionX)+self.xval),greenPixelX):
            for y in range(self.yval,int(((73/396)*(barrierSectionY))+self.yval),greenPixelY):
                top1.append((x,y))
        for x in range(int(((146/344)*(barrierSectionX))+((0)*barrierSectionX)+self.xval),int((barrierSectionX)+self.xval),greenPixelX):
            for y in range(int(((73/396)*(barrierSectionY))+self.yval),int(((146/396)*(barrierSectionY))+self.yval),greenPixelY):
                top1.append((x,y))
        for x in range(int(((73/344)*(barrierSectionX))+((0)*barrierSectionX)+self.xval),int((barrierSectionX)+self.xval),greenPixelX):
            for y in range(int(((146/396)*(barrierSectionY))+self.yval),int(((219/396)*(barrierSectionY))+self.yval),greenPixelY):
                top1.append((x,y))
        for x in range(self.xval,int(barrierSectionX+self.xval),greenPixelX):
            for y in range(int(((219/396)*barrierSectionY)+self.yval),int(self.yval+barrierSectionY),greenPixelY):
                top1.append((x,y))
        self.top1 = top1
        top2 = []
        for x in range(int(self.xval+barrierSectionX),int((2*barrierSectionX)+self.xval),greenPixelX):
            for y in range(self.yval,int(self.yval+barrierSectionY),greenPixelY):
                top2.append((x,y))
        self.top2 = top2
        top3 = []
        for x in range(int(self.xval+(2*barrierSectionX)),int((3*barrierSectionX)+self.xval),greenPixelX):
            for y in range(self.yval,int(self.yval+barrierSectionY),greenPixelY):
                top3.append((x,y))
        self.top3 = top3
        top4 = []
        for x in range(int((3*barrierSectionX)+self.xval),int((4*barrierSectionX)+self.xval-((219/344)*(barrierSectionX))),greenPixelX):
            for y in range(self.yval,int(((73/396)*(barrierSectionY))+self.yval),greenPixelY):
                top4.append((x,y))
        for x in range(((3)*int(barrierSectionX))+self.xval,int(((4)*barrierSectionX)+self.xval-((146/344)*(barrierSectionX))),greenPixelX):
            for y in range(int(((73/396)*(barrierSectionY))+self.yval),int(((146/396)*(barrierSectionY))+self.yval),greenPixelY):
                top4.append((x,y))
        for x in range(int(((3)*barrierSectionX)+self.xval),int(((4)*barrierSectionX)+self.xval-((73/344)*(barrierSectionX))),greenPixelX):
            for y in range(int(((146/396)*(barrierSectionY))+self.yval),int(((219/396)*(barrierSectionY))+self.yval),greenPixelY):
                top4.append((x,y))
        for x in range(self.xval+((3)*int(barrierSectionX)),(( 4)*int(barrierSectionX))+self.xval,greenPixelX):
            for y in range(int(((219/396)*(barrierSectionY))+self.yval),int(self.yval+(barrierSectionY)),greenPixelY):
                top4.append((x,y))
        self.top4 = top4
        bot1 = []
        for x in range(self.xval,int((barrierSectionX))+self.xval,greenPixelX):
            for y in range(self.yval+int(barrierSectionY),int(((262/406)*(barrierSectionY))+self.yval+(barrierSectionY)),greenPixelY):
                bot1.append((x,y))
        for x in range(self.xval,int(((292/344)*(barrierSectionX))+self.xval),greenPixelX):
            for y in range(int(((262/406)*(barrierSectionY))+self.yval+(barrierSectionY)),self.yval+barrierY,greenPixelY):
                bot1.append((x,y))
        self.bot1 = bot1
        bot2 = []
        for x in range(self.xval+int((barrierSectionX)),((1)*int(barrierSectionX))+self.xval+int(((21/344)*barrierSectionX)),greenPixelX):
            for y in range(self.yval+int(barrierSectionY),int(((262/406)*(barrierSectionY))+self.yval+(barrierSectionY)),greenPixelY):
                bot2.append((x,y))
        for x in range(int((barrierSectionX)+self.xval+((21/344)*barrierSectionX)),self.xval+((2)*int(barrierSectionX)),greenPixelX):
            for y in range(self.yval+int(barrierSectionY),int(((188/406)*(barrierSectionY))+self.yval+(barrierSectionY)),greenPixelY):
                bot2.append((x,y))
        self.bot2 =  bot2
        bot3 = []
        for x in range(int((2*(barrierSectionX))+self.xval),int(((333/344)*barrierSectionX)+self.xval+((2)*int(barrierSectionX))),greenPixelX):
            for y in range(self.yval+int(barrierSectionY),int(((188/406)*(barrierSectionY))+self.yval+int((barrierSectionY))),greenPixelY):
                bot3.append((x,y))
        for x in range(int(((333/344)*barrierSectionX)+(2*(barrierSectionX))+self.xval),int(self.xval+((3)*barrierSectionX)),greenPixelX):
            for y in range(int(self.yval+barrierSectionY),int(((262/406)*(barrierSectionY))+self.yval+(barrierSectionY)),greenPixelY):
                bot3.append((x,y))
        self.bot3 = bot3
        bot4 = []
        for x in range(int((3*(barrierSectionX))+self.xval),int(self.xval+((3)*barrierSectionX)+((63/344)*barrierSectionX)),greenPixelX):
            for y in range(int(self.yval+barrierSectionY),int(((262/406)*(barrierSectionY))+self.yval+int((barrierSectionY))),greenPixelY):
                bot4.append((x,y))
        for x in range(int(self.xval+((3)*barrierSectionX)+((63/344)*barrierSectionX)),self.xval+barrierX,greenPixelX):
            for y in range(int(self.yval+barrierSectionY),self.yval+barrierY,greenPixelY):
                bot4.append((x,y))
        self.bot4 = bot4
        #Uses different lists to hold the pixels and uses them to display them
        #and to see when to destroy the barrier
        self.size = [self.top1,self.top2,self.top3,self.top4,self.bot1,self.bot2,self.bot3,self.bot4]
        size2 = []
        self.size3 = [self.top1,self.top2,self.top3,self.top4,self.bot1,self.bot2,self.bot3,self.bot4]
        for j in range(len(self.size)):
            size2.append((len(self.size[j]))//3)
        self.size2 = size2

        self.drawBarrier()
    def drawBarrier(self):
        for j in self.size:
            for k in j:
                window.blit(self.image,(k[0], k[1]))

    def checkHitVal(self,value):
        #Checks if the alien/ship bullet hit any of the 8 sections of the barrier
        x = value[0]
        y = value[1]
        if self.size[0]!= []:
            if int(((219/344)*(barrierSectionX))+((0)*barrierSectionX)+self.xval)<=x and x<=int((barrierSectionX)+self.xval) and self.yval<= y and y<= int(((73/396)*(barrierSectionY))+self.yval):
                if self.size2[0]>= len(self.size[0]):
                    self.size[0] = []
                else:
                    num = len(self.size[0])//2
                    while num > 0:
                        index = random.randint(0,len(self.size[0])-1)
                        del self.size[0][index]
                        num-=1
                return True

            
            elif int(((146/344)*(barrierSectionX))+((0)*barrierSectionX)+self.xval) <= x and x<=int((barrierSectionX)+self.xval) and int(((73/396)*(barrierSectionY))+self.yval) <= y and y<= int(((146/396)*(barrierSectionY))+self.yval):
                if self.size2[0]>= len(self.size[0]):
                    self.size[0] = []
                else:
                    num = len(self.size[0])//2
                    while num > 0:
                        index = random.randint(0,len(self.size[0])-1)
                        del self.size[0][index]
                        num-=1
                return True
            elif int(((73/344)*(barrierSectionX))+((0)*barrierSectionX)+self.xval)<= x and x<= int((barrierSectionX)+self.xval) and int(((146/396)*(barrierSectionY))+self.yval)<= y and y<= int(((219/396)*(barrierSectionY))+self.yval):
                if self.size2[0]>= len(self.size[0]):
                    self.size[0] = []
                else:
                    num = len(self.size[0])//2
                    while num > 0:
                        index = random.randint(0,len(self.size[0])-1)
                        del self.size[0][index]
                        num-=1
                return True
            elif self.xval<= x and x<= int(barrierSectionX+self.xval) and int(((219/396)*barrierSectionY)+self.yval)<= y and y<=int(self.yval+barrierSectionY):            
                if self.size2[0]>= len(self.size[0]):
                    self.size[0] = []
                else:
                    num = len(self.size[0])//2
                    while num > 0:
                        index = random.randint(0,len(self.size[0])-1)
                        del self.size[0][index]
                        num-=1
                return True
        if self.size[1]!= []:
            if int(self.xval+barrierSectionX)<=x and x<=int((2*barrierSectionX)+self.xval) and self.yval<=y and y<=int(self.yval+barrierSectionY):
                if self.size2[1]>= len(self.size[1]):
                    self.size[1] = []
                else:
                    num = len(self.size[1])//2
                    while num > 0:
                        index = random.randint(1,len(self.size[1])-1)
                        del self.size[1][index]
                        num-=1
                return True
        if self.size[2]!= []:
            if int(self.xval+(2*barrierSectionX))<=x and x<=int((3*barrierSectionX)+self.xval) and self.yval<=y and y<=int(self.yval+barrierSectionY):
                if self.size2[2]>= len(self.size[2]):
                    self.size[2] = []
                else:
                    num = len(self.size[2])//2
                    while num > 0:
                        index = random.randint(0,len(self.size[2])-1)
                        del self.size[2][index]
                        num-=1
                return True
        if self.size[3]!= []:
            if int((3*barrierSectionX)+self.xval)<=x and x<=int((4*barrierSectionX)+self.xval-((219/344)*(barrierSectionX))) and self.yval<=y and y<=int(((73/396)*(barrierSectionY))+self.yval):
                if self.size2[3]>= len(self.size[3]):
                    self.size[3] = []
                else:
                    num = len(self.size[3])//2
                    while num > 0:
                        index = random.randint(0,len(self.size[3])-1)
                        del self.size[3][index]
                        num-=1
                return True
            elif ((3)*int(barrierSectionX))+self.xval<=x and x<=int(((4)*barrierSectionX)+self.xval-((146/344)*(barrierSectionX))) and int(((73/396)*(barrierSectionY))+self.yval)<= y and y<=int(((146/396)*(barrierSectionY))+self.yval):
                if self.size2[3]>= len(self.size[3]):
                    self.size[3] = []
                else:
                    num = len(self.size[3])//2
                    while num > 0:
                        index = random.randint(0,len(self.size[3])-1)
                        del self.size[3][index]
                        num-=1
                return True
            elif int(((3)*barrierSectionX)+self.xval)<=x and x<=int(((4)*barrierSectionX)+self.xval-((73/344)*(barrierSectionX))) and int(((146/396)*(barrierSectionY))+self.yval)<=y and y<=int(((219/396)*(barrierSectionY))+self.yval):
                if self.size2[3]>= len(self.size[3]):
                    self.size[3] = []
                else:
                    num = len(self.size[3])//2
                    while num > 0:
                        index = random.randint(0,len(self.size[3])-1)
                        del self.size[3][index]
                        num-=1
                return True
            elif self.xval+((3)*int(barrierSectionX))<=x and x<=(( 4)*int(barrierSectionX))+self.xval and int(((219/396)*(barrierSectionY))+self.yval) <= y and y<= int(self.yval+(barrierSectionY)):
                if self.size2[3]>= len(self.size[3]):
                    self.size[3] = []
                else:
                    num = len(self.size[3])//2
                    while num > 0:
                        index = random.randint(0,len(self.size[3])-1)
                        del self.size[3][index]
                        num-=1
                return True
        if self.size[4]!= []:
            if self.xval<= x and x<=int((barrierSectionX))+self.xval and self.yval+int(barrierSectionY)<=y and y<=int(((262/406)*(barrierSectionY))+self.yval+(barrierSectionY)):
                if self.size2[4]>= len(self.size[4]):
                    self.size[4] = []
                else:
                    num = len(self.size[4])//2
                    while num > 0:
                        index = random.randint(0,len(self.size[4])-1)
                        del self.size[4][index]
                        num-=1
                return True
            elif self.xval<=x and x<=int(((292/344)*(barrierSectionX))+self.xval) and int(((262/406)*(barrierSectionY))+self.yval+(barrierSectionY))<=y and y<=self.yval+barrierY:
                if self.size2[4]>= len(self.size[4]):
                    self.size[4] = []
                else:
                    num = len(self.size[4])//2
                    while num > 0:
                        index = random.randint(0,len(self.size[4])-1)
                        del self.size[4][index]
                        num-=1
                return True
        if self.size[5]!= []:
            if self.xval+int((barrierSectionX))<=x and x<=((1)*int(barrierSectionX))+self.xval+int(((21/344)*barrierSectionX)) and self.yval+int(barrierSectionY)<=y and y<=int(((262/406)*(barrierSectionY))+self.yval+(barrierSectionY)):
                if self.size2[5]>= len(self.size[5]):
                    self.size[5] = []
                else:
                    num = len(self.size[5])//2
                    while num > 0:
                        index = random.randint(0,len(self.size[5])-1)
                        del self.size[5][index]
                        num-=1
                return True
            elif int((barrierSectionX)+self.xval+((21/344)*barrierSectionX))<=x and x<=self.xval+((2)*int(barrierSectionX)) and self.yval+int(barrierSectionY)<= y and y<=int(((188/406)*(barrierSectionY))+self.yval+(barrierSectionY)):
                if self.size2[5]>= len(self.size[5]):
                    self.size[5] = []
                else:
                    num = len(self.size[5])//2
                    while num > 0:
                        index = random.randint(0,len(self.size[5])-1)
                        del self.size[5][index]
                        num-=1
                return True
        if self.size[6]!= []:
            if int((2*(barrierSectionX))+self.xval)<=x and x<=int(((333/344)*barrierSectionX)+self.xval+((2)*int(barrierSectionX))) and self.yval+int(barrierSectionY)<=y and y<=int(((188/406)*(barrierSectionY))+self.yval+int((barrierSectionY))):
                if self.size2[6]>= len(self.size[6]):
                    self.size[6] = []
                else:
                    num = len(self.size[6])//2
                    while num > 0:
                        index = random.randint(0,len(self.size[6])-1)
                        del self.size[6][index]
                        num-=1
                    return True                                                                                                                                                                                
            elif int(((333/344)*barrierSectionX)+(2*(barrierSectionX))+self.xval)<=x and x<=int(self.xval+((3)*barrierSectionX)) and int(self.yval+barrierSectionY)<=y and y<=int(((262/406)*(barrierSectionY))+self.yval+(barrierSectionY)):
                if self.size2[6]>= len(self.size[6]):
                    self.size[6] = []
                else:                                                                                                                                                                                     
                    num = len(self.size[6])//2
                    while num > 0:
                        index = random.randint(0,len(self.size[6])-1)
                        del self.size[6][index]
                        num-=1
                return True
        if self.size[7]!= []:
            if int((3*(barrierSectionX))+self.xval)<= x and x<=int(self.xval+((3)*barrierSectionX)+((63/344)*barrierSectionX)) and int(self.yval+barrierSectionY)<=y and y<= int(((262/406)*(barrierSectionY))+self.yval+int((barrierSectionY))):
                if self.size2[7]>= len(self.size[7]):
                    self.size[7] = []
                else:
                    num = len(self.size[7])//2
                    while num > 0:
                        index = random.randint(0,len(self.size[7])-1)
                        del self.size[7][index]
                        num-=1
                    return True                                                                                                                                                                                     
            elif int(self.xval+((3)*barrierSectionX)+((63/344)*barrierSectionX))<= x and x<=self.xval+barrierX and int(self.yval+barrierSectionY)<=y and y<=self.yval+barrierY:
                if self.size2[7]>= len(self.size[7]):
                    self.size[7] = []
                else:
                    num = len(self.size[7])//2
                    while num > 0:
                        index = random.randint(0,len(self.size[7])-1)
                        del self.size[7][index]
                        num-=1
                return True
        return False
    def checkHit(self, bulletX, bulletY, typeBullet):
        hit= False
        if typeBullet == "alien":
            val = (bulletX,bulletY)
            hit = self.checkHitVal(val)
            if not(hit):
                val = (bulletX+alienBulletX,bulletY)
                hit = self.checkHitVal(val)
            if not(hit):
                val = (bulletX,bulletY+alienBulletY)
                hit = self.checkHitVal(val)
            if not(hit):
                val = (bulletX+alienBulletX,bulletY+alienBulletY)
                hit = self.checkHitVal(val)

        elif typeBullet == "ship" and not(hit):
            val = (bulletX,bulletY)
            hit = self.checkHitVal(val)
            #uses the checkHitVal method to see if any of the 4 corners of the bullet hit the barrier
            if not(hit):
                val = (bulletX+shipBulletX,bulletY)
                hit = self.checkHitVal(val)
            if not(hit):
                val = (bulletX,bulletY+shipBulletY)
                hit = self.checkHitVal(val)
            if not(hit):
                val = (bulletX+shipBulletX,bulletY+shipBulletY)
                hit = self.checkHitVal(val)
    
        return hit 
        
            

class Explosion:
    #class that displays explosions where the green alien died
    def __init__(self,pos):
        self.image = pygame.image.load("explosiongreen.png")
        self.image = pygame.transform.scale(self.image, (xAlienSize,yAlienSize))        
        self.count = 0
        self.timer = alienExplosionTime
        self.pos = pos
    def checkCount(self,b):
        if self.count>= self.timer:
            del explosion[b]
            del self
            return True
        else:
            self.count+=1
            self.drawExplosion()
            return False
    def drawExplosion(self):
        window.blit(self.image,self.pos)        
class LiveDisplay:
    #displays how many lives the user has
    def __init__(self,w,x,y):
        self.image = pygame.image.load("ship.png")
        self.image = pygame.transform.scale(self.image, (xShipSize,yShipSize))
        self.xval = x
        self.yval = y
        self.drawShip()
    def drawShip(self):
        window.blit(self.image,(self.xval, self.yval))
class AlienBullet:
    #class that allows aliens to have bullets spawn under them and check if they collide with the barrier or ship
    def __init__(self,x,y):
        self.bullet = pygame.image.load("alienBullet.png")
        self.bullet = pygame.transform.scale(self.bullet, (alienBulletX,alienBulletY))
        self.xval = x
        self.yval = y
        self.shot = False
        self.shoot()
    def drawBullet(self):
        window.blit(self.bullet,(self.bulletX, self.bulletY))
    def shoot(self, hit = None):                   
        if self.shot == False:
            self.shot = True
            self.bulletX = self.xval+(.5*xAlienSize)-(alienBulletX*.5)
            self.bulletY = self.yval+yAlienSize- (yAlienSize*3/8)
    def bulletHit(self, c, hit = None):
        if hit == True or self.bulletY >= screenY:
            self.shot = False
            del bullet[c]
            del self
            return True
        return False
class RedScoreText:
    #class that displays the value of the red alien when the red alien dies
    def __init__(self,text,pos,color):
        self.txt = font1.render(text, True, color)        
        self.count = 0
        self.timer = redScoreTime
        self.pos = pos
    def checkCount(self,b):
        if self.count>= self.timer:
            del txt[b]
            del self
        else:
            self.count+=1
            self.displayText()
    def displayText(self):
        window.blit(self.txt,self.pos)
def drawSettings():
    #Used to display all the settings in the settings page
    text1 = font4.render(tempControl[0].name, True, green)
    text2 = font4.render(tempControl[1].name, True, green)
    text3 = font4.render(tempControl[2].name, True, green)
    text4 = font4.render(tempControl[3].name, True, green)
    text5 = font4.render(tempControl[4].name, True, green)
    text6 = font4.render(tempControl[5].name, True, green)
    text7 = font4.render(tempControl[6].name, True, green)
    text8 = font4.render(tempControl[7], True, green)
    text9 = font4.render(tempControl[8], True, green)
    text10 = font4.render(tempControl[9], True, green)
    text11 = font4.render(tempControl[10], True, green)
    text12 = font4.render(tempControl[11], True, green)
    text13 = font6.render(tempControl[12], True, green)
    window.blit(text1,(((11.188/13.333)*screenX),((1.927/7.5)*screenY)))
    window.blit(text2,(((11.188/13.333)*screenX),((2.542/7.5)*screenY)))
    window.blit(text3,(((9.406/13.333)*screenX),((3.135/7.5)*screenY)))
    window.blit(text4,(((11.188/13.333)*screenX),((3.135/7.5)*screenY)))
    window.blit(text5,(((11.188/13.333)*screenX),((4.344/7.5)*screenY)))
    window.blit(text6,(((11.188/13.333)*screenX),((4.969/7.5)*screenY)))
    window.blit(text7,(((11.188/13.333)*screenX),((5.563/7.5)*screenY)))
    window.blit(text8,(((5.094/13.333)*screenX),((3.135/7.5)*screenY)))
    window.blit(text9,(((5.094/13.333)*screenX),((3.740/7.5)*screenY)))
    window.blit(text10,(((5.094/13.333)*screenX),((2.542/7.5)*screenY)))
    window.blit(text11,(((5.094/13.333)*screenX),((4.344/7.5)*screenY)))
    window.blit(text12,(((5.094/13.333)*screenX),((4.969/7.5)*screenY)))
    window.blit(text13,(((5.094/13.333)*screenX),((1.942/7.5)*screenY)))
def keyName(x,y):
    #Fucntion called keyName that creates a white box
    #on the x,y (which are positions for where the box is supposed to be)
    #returns the name and the key number or None,None when it is supposed to quit
    while True:
        pygame.draw.rect(window,white,[x,y ,((1.792/13.333)*screenX),((.283/7.5)*screenY)])
        drawSettings()
        pygame.display.update()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_BACKSPACE]:
            return "Backspace",pygame.K_BACKSPACE
        elif pressed[pygame.K_TAB]:
            return "Tab",pygame.K_TAB
        elif pressed[pygame.K_CLEAR]:
            return "Clear",pygame.K_CLEAR
        elif pressed[pygame.K_RETURN]:
            return "Return",pygame.K_RETURN
        elif pressed[pygame.K_PAUSE]:
            return "Pause",pygame.K_PAUSE
        elif pressed[pygame.K_SPACE]:
            return "Space",pygame.K_SPACE
        elif pressed[pygame.K_EXCLAIM]:
            return "!",pygame.K_EXCLAIM
        elif pressed[pygame.K_QUOTEDBL]:
            return '"',pygame.K_CLEAR
        elif pressed[pygame.K_HASH]:
            return "#",pygame.K_HASH
        elif pressed[pygame.K_DOLLAR]:
            return "$",pygame.K_DOLLAR
        elif pressed[pygame.K_AMPERSAND]:
            return "&",pygame.K_AMPERSAND
        elif pressed[pygame.K_QUOTE]:
            return "'",pygame.K_QUOTE
        elif pressed[pygame.K_LEFTPAREN]:
            return "(",pygame.K_LEFTPAREN
        elif pressed[pygame.K_RIGHTPAREN]:
            return ")",pygame.K_RIGHTPAREN
        elif pressed[pygame.K_ASTERISK]:
            return "*",pygame.K_ASTERISK
        elif pressed[pygame.K_PLUS]:
            return "+",pygame.K_PLUS
        elif pressed[pygame.K_COMMA]:
            return ",",pygame.K_COMMA
        elif pressed[pygame.K_MINUS]:
            return "-",pygame.K_MINUS
        elif pressed[pygame.K_PERIOD]:
            return ".",pygame.K_PERIOD
        elif pressed[pygame.K_SLASH]:
            return "/",pygame.K_SLASH
        elif pressed[pygame.K_COLON]:
            return ":",pygame.K_COLON
        elif pressed[pygame.K_SEMICOLON]:
            return ";",pygame.K_SEMICOLON
        elif pressed[pygame.K_LESS]:
            return "<",pygame.K_LESS
        elif pressed[pygame.K_EQUALS]:
            return "=",pygame.K_EQUALS
        elif pressed[pygame.K_GREATER]:
            return ">",pygame.K_GREATER
        elif pressed[pygame.K_QUESTION]:
            return "?",pygame.K_QUESTION
        elif pressed[pygame.K_AT]:
            return "@",pygame.K_AT
        elif pressed[pygame.K_LEFTBRACKET]:
            return "[",pygame.K_LEFTBRACKET
        elif pressed[pygame.K_BACKSLASH]:
            return "\\",pygame.K_BACKSLASH
        elif pressed[pygame.K_RIGHTBRACKET]:
            return "]",pygame.K_RIGHTBRACKET
        elif pressed[pygame.K_CARET]:
            return "^",pygame.K_CARET
        elif pressed[pygame.K_UNDERSCORE]:
            return "_",pygame.K_UNDERSCORE
        elif pressed[pygame.K_BACKQUOTE]:
            return "`",pygame.K_BACKQUOTE
        elif pressed[pygame.K_a]:
            return "a",pygame.K_a
        elif pressed[pygame.K_b]:
            return "b",pygame.K_b
        elif pressed[pygame.K_c]:
            return "c",pygame.K_c
        elif pressed[pygame.K_d]:
            return "d",pygame.K_d
        elif pressed[pygame.K_e]:
            return "e",pygame.K_e
        elif pressed[pygame.K_f]:
            return "f",pygame.K_f
        elif pressed[pygame.K_g]:
            return "g",pygame.K_g
        elif pressed[pygame.K_h]:
            return "h",pygame.K_h
        elif pressed[pygame.K_i]:
            return "i",pygame.K_i
        elif pressed[pygame.K_j]:
            return "j",pygame.K_j
        elif pressed[pygame.K_k]:
            return "k",pygame.K_k
        elif pressed[pygame.K_l]:
            return "l",pygame.K_l
        elif pressed[pygame.K_m]:
            return "m",pygame.K_m
        elif pressed[pygame.K_n]:
            return "n",pygame.K_n
        elif pressed[pygame.K_o]:
            return "o",pygame.K_o
        elif pressed[pygame.K_p]:
            return "p",pygame.K_p
        elif pressed[pygame.K_q]:
            return "q",pygame.K_q
        elif pressed[pygame.K_r]:
            return "r",pygame.K_r
        elif pressed[pygame.K_s]:
            return "s",pygame.K_s
        elif pressed[pygame.K_t]:
            return "t",pygame.K_t
        elif pressed[pygame.K_u]:
            return "u",pygame.K_u
        elif pressed[pygame.K_v]:
            return "v",pygame.K_v
        elif pressed[pygame.K_w]:
            return "w",pygame.K_w
        elif pressed[pygame.K_x]:
            return "x",pygame.K_x
        elif pressed[pygame.K_y]:
            return "y",pygame.K_y
        elif pressed[pygame.K_z]:
            return "z",pygame.K_z
        elif pressed[pygame.K_0]:
            return "0",pygame.K_0
        elif pressed[pygame.K_1]:
            return "1",pygame.K_1
        elif pressed[pygame.K_2]:
            return "2",pygame.K_2
        elif pressed[pygame.K_3]:
            return "3",pygame.K_3
        elif pressed[pygame.K_4]:
            return "4",pygame.K_4
        elif pressed[pygame.K_5]:
            return "5",pygame.K_5
        elif pressed[pygame.K_6]:
            return "6",pygame.K_6
        elif pressed[pygame.K_7]:
            return "7",pygame.K_7
        elif pressed[pygame.K_8]:
            return "8",pygame.K_8
        elif pressed[pygame.K_9]:
            return "9",pygame.K_9
        elif pressed[pygame.K_RSHIFT]:
            return "RShift",pygame.K_RSHIFT
        elif pressed[pygame.K_LSHIFT]:
            return "LShift",pygame.K_LSHIFT
        elif pressed[pygame.K_RCTRL]:
            return "RCtrl",pygame.K_RCTRL
        elif pressed[pygame.K_LCTRL]:
            return "LCtrl",pygame.K_LCTRL
        elif pressed[pygame.K_RALT]:
            return "RAlt",pygame.K_RALT
        elif pressed[pygame.K_LALT]:
            return "LAlt",pygame.K_LALT
        elif pressed[pygame.K_UP]:
            return "Up",pygame.K_UP
        elif pressed[pygame.K_DOWN]:
            return "Down",pygame.K_DOWN
        elif pressed[pygame.K_RIGHT]:
            return "Right",pygame.K_RIGHT
        elif pressed[pygame.K_LEFT]:
            return "Left",pygame.K_LEFT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None, None
            if event.type == pygame.MOUSEBUTTONUP:
                return "Click", pygame.MOUSEBUTTONUP

        
        
    
    
def readSettings():
    try:
        settings=[]
        with open("Settings.txt") as file:
            for line in file:
                line = line.split(":")
                temp = line[0]
                line = line[1]
                line = line.rstrip("\n")
                line = line[1:]
                line = line.split(" ")
                if len(line) == 1:
                    line= line[0]
                else:
                    if temp == "Screensize":
                        for x in range(len(line)):
                            line[x] = int(line[x])
                        line = (line[0],line[1])
                        
                    else:
                        line= [line[0],int(line[1])]
                settings.append(line)
    except:
        settings = [(1280,720),"Default","On",60,["Left",276],["Right",275],["Space",32],["Down",274],["i",105],["o",111],["p",112],4,4,3]
    settings[3] = int(settings[3])
    settings[11] = int(settings[11])
    settings[12] = int(settings[12])
    settings[13] = int(settings[13])
    return settings

def saveSettings(settings):
    #saves all settings in a file
    with open("Settings.txt","w") as file:
        screensize = str(settings[0][0])+" "+str(settings[0][1])
        name = settings[1]
        music = settings[2]
        fps = str(settings[3])
        mL = settings[4][0]+" "+str(settings[4][1])
        mR = settings[5][0]+" "+str(settings[5][1])
        shoot = settings[6][0]+" "+str(settings[6][1])
        shoot2 = settings[7][0]+" "+str(settings[7][1])
        pt10 = settings[8][0]+" "+str(settings[8][1])
        pt20 = settings[9][0]+" "+str(settings[9][1])
        pt40 = settings[10][0]+" "+str(settings[10][1])
        bar = str(settings[11])
        mLives = str(settings[12])
        iLives = str(settings[13])
        file.write(("Screensize: "+screensize))
        file.write(("\nName: "+name))
        file.write(("\nMusic: "+music))
        file.write(("\nFPs: "+fps))
        file.write(("\nMLeft: "+mL))
        file.write(("\nMRight: "+mR))
        file.write(("\nShoot: "+shoot))
        file.write(("\nShoot2: "+shoot2))
        file.write(("\nPt10: "+pt10))
        file.write(("\nPt20: "+pt20))
        file.write(("\nPt40: "+pt40))
        file.write(("\nBarriers: "+bar))
        file.write(("\nMaxLives: "+mLives))
        file.write(("\nMinLives: "+iLives))
def playMusic(music,play=True):
    #plays music, if play is false then pauses immediately
    pygame.mixer.music.load(music+".mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    if not(play):
        pygame.mixer.music.pause()
def readScore():
    #reads the scores and returns a sorted second degree list, which is [[name,score]...]
    scores = []
    try:
        with open("Score.txt","r") as file:
            for line in file:
                line = line.rstrip("\n")
                line = line.split(" ")
                scores.append((line[0],int(line[1]),line[2]))
        scores.sort(key = lambda x: x[1],reverse =True)
    except:
        pass
    return scores

        
def saveScore(name,score,cus):
    if cus:
        cus = "Yes"
    else:
        cus = "No"
    if not(settings[-3:] == [4,4,3]):
        cus = "Yes"
    try:
        with open("Score.txt","a") as file:
            file.write(name +" "+str(score)+" "+str(cus)+"\n")
    except:
        with open("Score.txt","w") as file:
            file.write(name +" "+str(score)+" "+str(cus)+"\n")
def createMapFile(filename,l):
    if not(len(l[0])+len(l[1])+len(l[2]) == 0):
        
        with open(filename+".txt","w") as file:
            file.write(str(screenX)+" "+str(screenY)+"\n")
            file.write("Green10\n")
            for x in l[0]:
                file.write(str(x)+"\n")
            file.write("Green20\n")
            for x in l[1]:
                file.write(str(x)+"\n")
            file.write("Green40\n")
            for x in l[2]:
                file.write(str(x)+"\n")
def mapCreator(control,file):#Allows user to select aliens
    #and then place them, the controls match those set in settings
    #displays the alien while the user is moving around and allows user to move in a set space that will not interfere with other aspects of the game
    mapmaker = pygame.display.set_mode(settings[0])
    pygame.display.set_caption("Space Invaders Map Creator")
    places = [[],[],[]]
    finish = False
    ob= None
    iclick = False
    oclick = False
    pclick = False
    aliens = []
    im = pygame.image.load("MapCreator.png")
    im = pygame.transform.scale(im, (screenX,screenY))
    pt10 = font5.render(settings[8][0], True, white)
    pt20 = font5.render(settings[9][0], True, white)
    pt40 = font5.render(settings[10][0], True, white)
    while not finish:
        window.blit(im,(0,0))
        window.blit(pt10,(((2.667/13.333)*screenX),((6.156/7.5)*screenY)))
        window.blit(pt20,(((7.438/13.333)*screenX),((6.156/7.5)*screenY)))
        window.blit(pt40,(((12.333/13.333)*screenX),((6.156/7.5)*screenY)))
        mouseX, mouseY =pygame.mouse.get_pos()
        trueMouseX, trueMouseY =pygame.mouse.get_pos()
        if mouseY <= (screenY//8):
            mouseY = (screenY//8)
        if mouseX >= (screenX-xAlienSize):
            mouseX = (screenX-xAlienSize)
        if mouseY >= yParameterAlien:
            mouseY = yParameterAlien
        pressed = pygame.key.get_pressed()
        
        if pressed[control[4].key]:
            iclick = True
            oclick = False
            pclick = False
            if iclick == True:
                ob = "Green10"
            else:
                ob = None
        
        if pressed[pygame.K_RSHIFT]:
            mouseX = initialX
        else:
            initialX = mouseX
        if pressed[pygame.K_LSHIFT]:
            mouseY = initialY
        else:
            initialY = mouseY
        
        if pressed[control[5].key]:
            iclick = False
            oclick = True
            pclick = False
            if oclick == True:
                ob = "Green20"
            else:
                ob = None
        if pressed[control[6].key]:
            iclick = False
            oclick = False
            pclick = True
            if pclick == True:
                ob = "Green40"
            else:
                ob = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.MOUSEBUTTONUP:
                if trueMouseX >=((10.292/13.333)*screenX) and trueMouseX <=((13.250/13.333)*screenX) and trueMouseY >= ((0.416/7.5)*screenY) and trueMouseY <=((0.9375/7.5)*screenY):
                    finish = True
                if ob != None:
                    if ob == "Green10":
                        aliens.append(GreenAlien(10,mapmaker,mouseX,mouseY))
                        places[0].append((mouseX,mouseY))
                    elif ob == "Green20":
                        aliens.append(GreenAlien(20,mapmaker,mouseX,mouseY))
                        places[1].append((mouseX,mouseY))
                    elif ob == "Green40":
                        aliens.append(GreenAlien(40,mapmaker,mouseX,mouseY))
                        places[2].append((mouseX,mouseY))
        if ob == "Green10":
            image = "10open.png"
        elif ob == "Green20":
            image = "20open.png"
        elif ob == "Green40":
            image = "40open.png"
        else:
            image = None
        for x in aliens:
            x.drawAlien()
        if image != None:
            pyimage = pygame.image.load(image)
            pyimage = pygame.transform.scale(pyimage, (xAlienSize,yAlienSize))
            mapmaker.blit(pyimage,(mouseX,mouseY))
            
        pygame.display.update()
        mapmaker.fill(black)
        
    pygame.display.set_caption("Space Invaders")    
    createMapFile(file,places)#Creates a map file
    
def readCustom(f):#reads custom map
    with open(f+".txt","r") as file:
        allelems = []
        first = True
        for line in file:
            if "Green" in line:
                first = False
                try:
                    allelems.append(elems)
                except:
                    pass
                elems = []
            elif not(first):
                elems.append(line.rstrip("\n"))
            else:
                l = line.rstrip("\n")
                l = line.split(" ")
                l = [int(l[0]),int(l[1][:-1])]
    allelems.append(elems)
    return allelems, l[0], l[1]
def highScore():#displays all highscores to screen
    highScores = readScore()#reads the scores and returns a list of the scores
    im = pygame.image.load("Highscores.png")
    im = pygame.transform.scale(im, (screenX,screenY))
    numb = 0
    window.blit(im,(0,0))
    for y in range(int((screenY*(0.034))+((1.688/7.5)*screenY)),int((24*screenY)//25),int((screenY*(0.034))+(screenY//25))):
        
        if len(highScores)>= 10:
            if numb == 11:
                break
        else:
            if numb == (len(highScores)-1):
                break
        st = numb +1
        scStr = str(st)+"."+" "*(screenX//150)+highScores[numb][0]+" "*((screenX//275)+(7-len(highScores[numb][0])))+highScores[numb][2]+" "*((screenX//250)+(7-len(highScores[numb][2])))+str(highScores[numb][1])
        if numb == 9:
            scStr = str(st)+"."+" "*((screenX//150)-1)+highScores[numb][0]+" "*((screenX//275)+(7-len(highScores[numb][0])))+highScores[numb][2]+" "*((screenX//250)+(7-len(highScores[numb][2])))+str(highScores[numb][1])
        txt= font3.render(scStr, True, white)
        window.blit(txt,(int(((1.021/13.333)*screenX)),y))
        numb+= 1
    
    pygame.display.update()
    while True:
       
        mouseX, mouseY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONUP:
                if mouseX>=(11.219/13.333)*screenX and mouseX<= (12.51/13.333)*screenX and mouseY>= (0.604/7.5)*screenY and mouseY<=(0.896/7.5)*screenY:
                    return False
        window.blit(im,(0,0))
def settingsControl(control):
    #Functions that allows you to change all settings 
    global tempControl
    #temp control is what is refrenced in drawSettings()
    newControl = control[:]
    mL = newControl[0]
    mR = newControl[1]
    shoot = newControl[2]
    shoot2 = newControl[3]
    pt10 = newControl[4]
    pt20 = newControl[5]
    pt40 = newControl[6]
    string = settings[1]
    fps = str(settings[3])
    bar = str(settings[11])
    mLives = str(settings[12])
    iLives = str(settings[13])
    screenSize = str(settings[0][0])+"x"+str(settings[0][1])
    tempControl = [mL,mR,shoot,shoot2,pt10,pt20,pt40,string,fps,bar,mLives,iLives,screenSize]
    popUp = False
    while True:
        im = pygame.image.load("Settings.png")
        im = pygame.transform.scale(im, (screenX,screenY))
        if Keys.quitGame:
            return control, True
        
        window.blit(im,(0,0))
        mouseX, mouseY =pygame.mouse.get_pos()
        if popUp:#if the user has clicked screensize before and not clicked off
            while True:
                breakLoop = False
                window.blit(im,(0,0))

                tempControl = [mL,mR,shoot,shoot2,pt10,pt20,pt40,string,fps,bar,mLives,iLives, screenSize]
                drawSettings()
                image1 = pygame.image.load("ScreenSize.png")
                image1 = pygame.transform.scale(image1,(screenX,screenY))
                window.blit(image1,(0,0))
                mouseX, mouseY =pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return control, True
                    if event.type == pygame.MOUSEBUTTONUP:
                        if mouseX>= ((5.094/13.333)*screenX) and mouseX<= ((6.906/13.333)*screenX) and mouseY>= ((1.927/7.5)*screenY) and mouseY<=((2.218/7.5)*screenY):
                            screenSize = "1920x1080"
                            popUp = False
                            breakLoop = True
                            break
                        elif mouseX>= ((5.094/13.333)*screenX) and mouseX<= ((6.906/13.333)*screenX) and mouseY>= ((2.218/7.5)*screenY) and mouseY<=((2.594/7.5)*screenY):
                            screenSize = "1280x720"
                            popUp = False
                            breakLoop = True
                            break
                        elif mouseX>= ((5.094/13.333)*screenX) and mouseX<= ((6.906/13.333)*screenX) and mouseY>= ((2.594/7.5)*screenY) and mouseY<=((2.906/7.5)*screenY):
                            screenSize = "1024x576"
                            popUp = False
                            breakLoop = True
                            break
                        elif mouseX>= ((5.094/13.333)*screenX) and mouseX<= ((6.906/13.333)*screenX) and mouseY>= ((2.906/7.5)*screenY) and mouseY<=((3.219/7.5)*screenY):
                            screenSize = "640x360"
                            popUp = False
                            breakLoop = True
                            break
                        elif mouseX>= ((5.094/13.333)*screenX) and mouseX<= ((6.906/13.333)*screenX) and mouseY>= ((3.219/7.5)*screenY) and mouseY<=((3.531/7.5)*screenY):
                            screenSize = "2560x1440"
                            popUp = False
                            breakLoop = True
                            break
                        elif mouseX>= ((5.094/13.333)*screenX) and mouseX<= ((6.906/13.333)*screenX) and mouseY>= ((3.531/7.5)*screenY) and mouseY<=((3.906/7.5)*screenY):
                            
                            screenSize = "3840x2160"
                            popUp = False
                            breakLoop = True
                            break
                        else:
                            popUp = False
                            breakLoop = True
                            break
                if breakLoop:
                    break
                pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return control, True
            if event.type == pygame.MOUSEBUTTONUP:
                if not(popUp):
                    #Allows user to click each settings box and type their own settings into the box,
                    #has restrictions on some of the settings, allows user to input to the screen
                    #saves settings if save or apply settings, and resets settings if needed
                    if mouseX>=(11.219/13.333)*screenX and mouseX<= (12.51/13.333)*screenX and mouseY>= (0.604/7.5)*screenY and mouseY<=(0.896/7.5)*screenY:
                        #if user clicks back, return control, False
                        return control, False
                    elif mouseX>=(0.760/13.333)*screenX and mouseX<= (3.385/13.333)*screenX and mouseY>= (6.427/7.5)*screenY and mouseY<=(7.115/7.5)*screenY:
                        #if user clicks reset settings, resets to default
                        newControl = [KeysDefault("Left",pygame.K_LEFT),KeysDefault("Right",pygame.K_RIGHT),KeysDefault("Space",pygame.K_SPACE),KeysDefault("Down",pygame.K_DOWN),KeysDefault("i",pygame.K_i),KeysDefault("o",pygame.K_o),KeysDefault("p",pygame.K_p)]
                        string = "Default"
                        mL = newControl[0]
                        mR = newControl[1]
                        shoot = newControl[2]
                        shoot2 = newControl[3]
                        pt10 = newControl[4]
                        pt20 = newControl[5]
                        pt40 = newControl[6]
                        fps = "60"
                        bar = "4"
                        mLives = "4"
                        iLives = "3"
                    elif mouseX>=(5.354/13.333)*screenX and mouseX<= (7.979/13.333)*screenX and mouseY>= (6.427/7.5)*screenY and mouseY<=(7.115/7.5)*screenY:
                        #if user clicks save settings
                        control = newControl[:]
                        tempvar = screenSize.split("x")
                        settings[0] = (int(tempvar[0]),int(tempvar[1]))
                        settings[1] = string
                        settings[3] = int(fps)
                        settings[4] = [control[0].name,control[0].key]
                        settings[5] = [control[1].name,control[1].key]
                        settings[6] = [control[2].name,control[2].key]
                        settings[7] = [control[3].name,control[3].key]
                        settings[8] = [control[4].name,control[4].key]
                        settings[9] = [control[5].name,control[5].key]
                        settings[10] = [control[6].name,control[6].key]
                        settings[11] = int(bar)
                        settings[12] = int(mLives)
                        settings[13] = int(iLives)
                        saveSettings(settings)
                    elif mouseX>=(9.990/13.333)*screenX and mouseX<= (12.615/13.333)*screenX and mouseY>= (6.427/7.5)*screenY and mouseY<=(7.115/7.5)*screenY:
                        #if user click apply settings
                        control = newControl[:]
                        tempvar = screenSize.split("x")
                        settings[0] = (int(tempvar[0]),int(tempvar[1]))
                        settings[1] = string
                        settings[3] = int(fps)
                        settings[4] = [control[0].name,control[0].key]
                        settings[5] = [control[1].name,control[1].key]
                        settings[6] = [control[2].name,control[2].key]
                        settings[7] = [control[3].name,control[3].key]
                        settings[8] = [control[4].name,control[4].key]
                        settings[9] = [control[5].name,control[5].key]
                        settings[10] = [control[6].name,control[6].key]
                        settings[11] = int(bar)
                        settings[12] = int(mLives)
                        settings[13] = int(iLives)
                        setVariables(int(tempvar[0]),int(tempvar[1]))
                        #setVariables is to change the graphic varibales, send screenX and screenY
                        saveSettings(settings)
                    elif mouseX>=((5.094/13.333)*screenX) and mouseX<=((6.906/13.323)*screenX):
                        if mouseY>= ((1.927/7.5)*screenY)and mouseY<=(((1.927/7.5)*screenY)+((0.302/7.5)*screenY)):
                            popUp = True
                            #screensize, popUp is used earlier to open a sub screen to get a value
                        elif mouseY>= ((2.542/7.5)*screenY)and mouseY<=(((2.542/7.5)*screenY)+((0.302/7.5)*screenY)):
                            pygame.draw.rect(window,white,[((5.114/13.333)*screenX),((2.562/7.5)*screenY) ,((1.792/13.333)*screenX),((.283/7.5)*screenY)])
                            bar = ""
                            #barriers settings
                            tempControl = [mL,mR,shoot,shoot2,pt10,pt20,pt40,string,fps,bar,mLives,iLives, screenSize]
                            prev = pygame.key.get_pressed()
                            while True:
                                
                                breakLoop = False
                                window.blit(im,(0,0))
                                pygame.draw.rect(window,white,[((5.114/13.333)*screenX),((2.562/7.5)*screenY) ,((1.792/13.333)*screenX),((.283/7.5)*screenY)])
                                tempControl = [mL,mR,shoot,shoot2,pt10,pt20,pt40,string,fps,bar,mLives,iLives, screenSize]
                                drawSettings()
                                pygame.display.update()
                                pressed = pygame.key.get_pressed()
                                if pressed != prev:
                                    prev= pressed
                                    if pressed[pygame.K_BACKSPACE]:
                                        if len(bar)!= 0:
                                            bar = bar[:-1]
                                    if len(bar) == 0:
                                        if pressed[pygame.K_RETURN]:
                                            break
                                        elif pressed[pygame.K_0]:
                                            if len(bar) != 0:
                                                bar = bar +"0"
                                        elif pressed[pygame.K_1]:
                                            bar = bar +"1"
                                        elif pressed[pygame.K_2]:
                                            bar = bar +"2"
                                        elif pressed[pygame.K_3]:
                                            bar = bar +"3"
                                        elif pressed[pygame.K_4]:
                                            bar = bar +"4"
                                        elif pressed[pygame.K_5]:
                                            bar = bar +"5"
                                        elif pressed[pygame.K_6]:
                                            bar = bar +"6"
                                        elif pressed[pygame.K_7]:
                                            bar = bar +"7"
                                        elif pressed[pygame.K_8]:
                                            bar = bar +"8"
                                        elif pressed[pygame.K_9]:
                                            bar = bar +"9"
                                    elif int(bar)> 10:
                                        if pressed[pygame.K_RETURN]:
                                            break
                                        elif pressed[pygame.K_0]:
                                            if len(bar) != 0:
                                                bar = bar +"0"
                                        elif pressed[pygame.K_1]:
                                            bar = bar +"1"
                                        elif pressed[pygame.K_2]:
                                            bar = bar +"2"
                                        elif pressed[pygame.K_3]:
                                            bar = bar +"3"
                                        elif pressed[pygame.K_4]:
                                            bar = bar +"4"
                                        elif pressed[pygame.K_5]:
                                            bar = bar +"5"
                                        elif pressed[pygame.K_6]:
                                            bar = bar +"6"
                                        elif pressed[pygame.K_7]:
                                            bar = bar +"7"
                                        elif pressed[pygame.K_8]:
                                            bar = bar +"8"
                                        elif pressed[pygame.K_9]:
                                            bar = bar +"9"
                                    
             
                                mouseX, mouseY =pygame.mouse.get_pos()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        return control, True
                                    
                                    if event.type == pygame.MOUSEBUTTONUP:
                                        if not(mouseY>= ((3.740/7.5)*screenY)and mouseY<=(((3.740/7.5)*screenY)+((0.302/7.5)*screenY))and mouseX>=(5.094/13.333)*screenX and mouseX<=((6.906/13.323)*screenX)):                                    
                                            breakLoop = True
                                            break
                                if breakLoop:
                                    break
                            if len(bar) == 0:#restrictions must have have more then 0 barriers
                                bar = "4"
                        elif mouseY>= ((3.135/7.5)*screenY)and mouseY<=(((3.135/7.5)*screenY)+((0.302/7.5)*screenY)):
                            string = ""
                            #name settings
                            tempControl = [mL,mR,shoot,shoot2,pt10,pt20,pt40,string,fps,bar,mLives,iLives, screenSize]
                            prev = pygame.key.get_pressed()
                            while True:
                                
                                breakLoop = False
                                window.blit(im,(0,0))
                                pygame.draw.rect(window,white,[((5.114/13.333)*screenX),((3.155/7.5)*screenY) ,((1.792/13.333)*screenX),((.283/7.5)*screenY)])
                                tempControl = [mL,mR,shoot,shoot2,pt10,pt20,pt40,string,fps,bar,mLives,iLives, screenSize]
                                drawSettings()
                                pygame.display.update()
                                pressed = pygame.key.get_pressed()
                                if pressed != prev:
                                    prev= pressed
                                    if pressed[pygame.K_BACKSPACE]:
                                        if len(string)!= 0:
                                            string = string[:-1]
                                    if len(string) < 7:
                                        if pressed[pygame.K_RETURN]:
                                            break
                                        elif pressed[pygame.K_RSHIFT] or pressed[pygame.K_LSHIFT]:
                                            if pressed[pygame.K_1]:
                                                string = string +"!"
                                            elif pressed[pygame.K_2]:
                                                string = string +"@"
                                            elif pressed[pygame.K_3]:
                                                string = string +"#"
                                            elif pressed[pygame.K_4]:
                                                string = string +"$"
                                            elif pressed[pygame.K_5]:
                                                string = string +"%"
                                            elif pressed[pygame.K_6]:
                                                string = string +"^"
                                            elif pressed[pygame.K_7]:
                                                string = string +"&"
                                            elif pressed[pygame.K_8]:
                                                string = string +"*"
                                            elif pressed[pygame.K_9]:
                                                string = string +"("
                                            elif pressed[pygame.K_0]:
                                                string = string +")"
                                            elif pressed[pygame.K_MINUS]:
                                                string = string +"_"
                                            elif pressed[pygame.K_EQUALS]:
                                                string = string +"+"
                                            elif pressed[pygame.K_LEFTBRACKET]:
                                                string = string +"{"
                                            elif pressed[pygame.K_BACKSLASH]:
                                                string = string +"|"
                                            elif pressed[pygame.K_RIGHTBRACKET]:
                                                string = string +"}"
                                            elif pressed[pygame.K_SEMICOLON]:
                                                string = string +":"
                                            elif pressed[pygame.K_QUOTE]:
                                                string = string +"\""
                                            elif pressed[pygame.K_COMMA]:
                                                string = string +"<"
                                            elif pressed[pygame.K_PERIOD]:
                                                string = string +">"
                                            elif pressed[pygame.K_SLASH]:
                                                string = string +"?"
                                        elif pressed[pygame.K_SPACE]:
                                            string = string +" "
                                        elif pressed[pygame.K_QUOTE]:
                                            string = string +"\'"
                                        elif pressed[pygame.K_COMMA]:
                                            string = string +","
                                        elif pressed[pygame.K_MINUS]:
                                            string = string +"-"
                                        elif pressed[pygame.K_PERIOD]:
                                            string = string +"."
                                        elif pressed[pygame.K_SLASH]:
                                            string = string +"/"
                                        elif pressed[pygame.K_SEMICOLON]:
                                            string = string +";"
                                        elif pressed[pygame.K_EQUALS]:
                                            string = string +"="
                                        elif pressed[pygame.K_LEFTBRACKET]:
                                            string = string +"["
                                        elif pressed[pygame.K_BACKSLASH]:
                                            string = string +"\\"
                                        elif pressed[pygame.K_RIGHTBRACKET]:
                                            string = string +"]"
                                        elif pressed[pygame.K_BACKQUOTE]:
                                            string = string +"`"
                                        elif pressed[pygame.K_a]:
                                            string = string +"a"
                                        elif pressed[pygame.K_b]:
                                            string = string +"b"
                                        elif pressed[pygame.K_c]:
                                            string = string +"c"
                                        elif pressed[pygame.K_d]:
                                            string = string +"d"
                                        elif pressed[pygame.K_e]:
                                            string = string +"e"
                                        elif pressed[pygame.K_f]:
                                            string = string +"f"
                                        elif pressed[pygame.K_g]:
                                            string = string +"g"
                                        elif pressed[pygame.K_h]:
                                            string = string +"h"
                                        elif pressed[pygame.K_i]:
                                            string = string +"i"
                                        elif pressed[pygame.K_j]:
                                            string = string +"j"
                                        elif pressed[pygame.K_k]:
                                            string = string +"k"
                                        elif pressed[pygame.K_l]:
                                            string = string +"l"
                                        elif pressed[pygame.K_m]:
                                            string = string +"m"
                                        elif pressed[pygame.K_n]:
                                            string = string +"n"
                                        elif pressed[pygame.K_o]:
                                            string = string +"o"
                                        elif pressed[pygame.K_p]:
                                            string = string +"p"
                                        elif pressed[pygame.K_q]:
                                            string = string +"q"
                                        elif pressed[pygame.K_r]:
                                            string = string +"r"
                                        elif pressed[pygame.K_s]:
                                            string = string +"s"
                                        elif pressed[pygame.K_t]:
                                            string = string +"t"
                                        elif pressed[pygame.K_u]:
                                            string = string +"u"
                                        elif pressed[pygame.K_v]:
                                            string = string +"v"
                                        elif pressed[pygame.K_w]:
                                            string = string +"w"
                                        elif pressed[pygame.K_x]:
                                            string = string +"x"
                                        elif pressed[pygame.K_y]:
                                            string = string +"y"
                                        elif pressed[pygame.K_z]:
                                            string = string +"z"
                                        elif pressed[pygame.K_0]:
                                            string = string +"0"
                                        elif pressed[pygame.K_1]:
                                            string = string +"1"
                                        elif pressed[pygame.K_2]:
                                            string = string +"2"
                                        elif pressed[pygame.K_3]:
                                            string = string +"3"
                                        elif pressed[pygame.K_4]:
                                            string = string +"4"
                                        elif pressed[pygame.K_5]:
                                            string = string +"5"
                                        elif pressed[pygame.K_6]:
                                            string = string +"6"
                                        elif pressed[pygame.K_7]:
                                            string = string +"7"
                                        elif pressed[pygame.K_8]:
                                            string = string +"8"
                                        elif pressed[pygame.K_9]:
                                            string = string +"9"
             
                                mouseX, mouseY =pygame.mouse.get_pos()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        return control, True
                                    
                                    if event.type == pygame.MOUSEBUTTONUP:
                                        if not(mouseY>= ((3.135/7.5)*screenY)and mouseY<=(((3.135/7.5)*screenY)+((0.302/7.5)*screenY))and mouseX>=(5.094/13.333)*screenX and mouseX<=((6.906/13.323)*screenX)):                                    
                                            breakLoop = True
                                            break
                                if breakLoop:
                                    break
                        elif mouseY>= ((3.740/7.5)*screenY)and mouseY<=(((3.740/7.5)*screenY)+((0.302/7.5)*screenY)):
                            pygame.draw.rect(window,white,[((5.114/13.333)*screenX),((3.760/7.5)*screenY),((1.792/13.333)*screenX),((.283/7.5)*screenY)])
                            fps = ""
                            #fps settings
                            tempControl = [mL,mR,shoot,shoot2,pt10,pt20,pt40,string,fps,bar,mLives,iLives, screenSize]
                            prev = pygame.key.get_pressed()
                            while True:
                                
                                breakLoop = False
                                window.blit(im,(0,0))
                                pygame.draw.rect(window,white,[((5.114/13.333)*screenX),((3.760/7.5)*screenY) ,((1.792/13.333)*screenX),((.283/7.5)*screenY)])
                                tempControl = [mL,mR,shoot,shoot2,pt10,pt20,pt40,string,fps,bar,mLives,iLives, screenSize]
                                drawSettings()
                                pygame.display.update()
                                pressed = pygame.key.get_pressed()
                                if pressed != prev:
                                    prev= pressed
                                    if pressed[pygame.K_BACKSPACE]:
                                        if len(fps)!= 0:
                                            fps = fps[:-1]
                                    if len(fps) < 7:
                                        if pressed[pygame.K_RETURN]:
                                            break
                                        elif pressed[pygame.K_0]:
                                            if len(fps) != 0:
                                                fps = fps +"0"
                                        elif pressed[pygame.K_1]:
                                            fps = fps +"1"
                                        elif pressed[pygame.K_2]:
                                            fps = fps +"2"
                                        elif pressed[pygame.K_3]:
                                            fps = fps +"3"
                                        elif pressed[pygame.K_4]:
                                            fps = fps +"4"
                                        elif pressed[pygame.K_5]:
                                            fps = fps +"5"
                                        elif pressed[pygame.K_6]:
                                            fps = fps +"6"
                                        elif pressed[pygame.K_7]:
                                            fps = fps +"7"
                                        elif pressed[pygame.K_8]:
                                            fps = fps +"8"
                                        elif pressed[pygame.K_9]:
                                            fps = fps +"9"
                                 
                                mouseX, mouseY =pygame.mouse.get_pos()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        return control, True
                                    
                                    if event.type == pygame.MOUSEBUTTONUP:
                                        if not(mouseY>= ((3.740/7.5)*screenY)and mouseY<=(((3.740/7.5)*screenY)+((0.302/7.5)*screenY))and mouseX>=(5.094/13.333)*screenX and mouseX<=((6.906/13.323)*screenX)):                                    
                                            breakLoop = True
                                            break
                                if breakLoop:
                                    break
                        
                        if len(fps) == 0:
                            fps = "60"
                        if int(fps) > 60:
                            fps = "60"
                        if int(fps) < 30:
                            fps = "30"
                        elif mouseY>= ((4.344/7.5)*screenY)and mouseY<=(((4.344/7.5)*screenY)+((0.302/7.5)*screenY)):
                            pygame.draw.rect(window,white,[((5.114/13.333)*screenX),((4.364/7.5)*screenY) ,((1.792/13.333)*screenX),((.283/7.5)*screenY)])
                            mLives = ""
                            #maximumLives
                            tempControl = [mL,mR,shoot,shoot2,pt10,pt20,pt40,string,fps,bar,mLives,iLives, screenSize]
                            prev = pygame.key.get_pressed()
                            while True:
                                
                                breakLoop = False
                                window.blit(im,(0,0))
                                pygame.draw.rect(window,white,[((5.114/13.333)*screenX),((4.364/7.5)*screenY) ,((1.792/13.333)*screenX),((.283/7.5)*screenY)])
                                tempControl = [mL,mR,shoot,shoot2,pt10,pt20,pt40,string,fps,bar,mLives,iLives, screenSize]
                                drawSettings()
                                pygame.display.update()
                                pressed = pygame.key.get_pressed()
                                if pressed != prev:
                                    prev= pressed
                                    if pressed[pygame.K_BACKSPACE]:
                                        if len(mLives)!= 0:
                                            mLives = mLives[:-1]
                                    if len(mLives) == 0:
                                        if pressed[pygame.K_RETURN]:
                                            break
                                        elif pressed[pygame.K_0]:
                                            if len(mLives) != 0:
                                                mLives = mLives +"0"
                                        elif pressed[pygame.K_1]:
                                            mLives = mLives +"1"
                                        elif pressed[pygame.K_2]:
                                            mLives = mLives +"2"
                                        elif pressed[pygame.K_3]:
                                            mLives = mLives +"3"
                                        elif pressed[pygame.K_4]:
                                            mLives = mLives +"4"
                                        elif pressed[pygame.K_5]:
                                            mLives = mLives +"5"
                                        elif pressed[pygame.K_6]:
                                            mLives = mLives +"6"
                                        elif pressed[pygame.K_7]:
                                            mLives = mLives +"7"
                                        elif pressed[pygame.K_8]:
                                            mLives = mLives +"8"
                                        elif pressed[pygame.K_9]:
                                            mLives = mLives +"9"
                                    elif int(mLives)> int(iLives):
                                        if pressed[pygame.K_RETURN]:
                                            break
                                        elif pressed[pygame.K_0]:
                                            if len(mLives) != 0:
                                                mLives = mLives +"0"
                                        elif pressed[pygame.K_1]:
                                            mLives = mLives +"1"
                                        elif pressed[pygame.K_2]:
                                            mLives = mLives +"2"
                                        elif pressed[pygame.K_3]:
                                            mLives = mLives +"3"
                                        elif pressed[pygame.K_4]:
                                            mLives = mLives +"4"
                                        elif pressed[pygame.K_5]:
                                            mLives = mLives +"5"
                                        elif pressed[pygame.K_6]:
                                            mLives = mLives +"6"
                                        elif pressed[pygame.K_7]:
                                            mLives = mLives +"7"
                                        elif pressed[pygame.K_8]:
                                            mLives = mLives +"8"
                                        elif pressed[pygame.K_9]:
                                            mLives = mLives +"9"
                                    
             
                                mouseX, mouseY =pygame.mouse.get_pos()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        return control, True
                                    
                                    if event.type == pygame.MOUSEBUTTONUP:
                                        if not(mouseY>= ((4.344/7.5)*screenY)and mouseY<=(((4.344/7.5)*screenY)+((0.302/7.5)*screenY))and mouseX>=(5.094/13.333)*screenX and mouseX<=((6.906/13.323)*screenX)):                                    
                                            breakLoop = True
                                            break
                                if breakLoop:
                                    break
                            if len(mLives) == 0:#restrictions, if maxLives is 
                                mLives = "4"
                            if len(iLives)!= 0:
                                if int(mLives)< int(iLives):
                                    mLives = iLives
                                
                        elif mouseY>= ((4.969/7.5)*screenY)and mouseY<=(((4.969/7.5)*screenY)+((0.302/7.5)*screenY)):
                            pygame.draw.rect(window,white,[((5.114/13.333)*screenX),((4.989/7.5)*screenY) ,((1.792/13.333)*screenX),((.283/7.5)*screenY)])
                            iLives = ""
                            #initial lives
                            tempControl = [mL,mR,shoot,shoot2,pt10,pt20,pt40,string,fps,bar,mLives,iLives, screenSize]
                            prev = pygame.key.get_pressed()
                            while True:#Checking keys inputed by user
                                
                                breakLoop = False
                                window.blit(im,(0,0))
                                pygame.draw.rect(window,white,[((5.114/13.333)*screenX),((4.989/7.5)*screenY) ,((1.792/13.333)*screenX),((.283/7.5)*screenY)])
                                tempControl = [mL,mR,shoot,shoot2,pt10,pt20,pt40,string,fps,bar,mLives,iLives, screenSize]
                                drawSettings()
                                pygame.display.update()
                                pressed = pygame.key.get_pressed()
                                if pressed != prev:
                                    prev= pressed
                                    if pressed[pygame.K_BACKSPACE]:
                                        if len(iLives)!= 0:
                                            iLives = iLives[:-1]
                                    if len(iLives) == 0:
                                        if pressed[pygame.K_RETURN]:
                                            break
                                        elif pressed[pygame.K_0]:
                                            if len(iLives) != 0:
                                                if int(mLives)>= 0:
                                                    iLives = iLives +"0"
                                        elif pressed[pygame.K_1]:
                                            if int(mLives)>= 1:
                                                iLives = iLives +"1"
                                        elif pressed[pygame.K_2]:
                                            if int(mLives)>= 2:
                                                iLives = iLives +"2"
                                        elif pressed[pygame.K_3]:
                                            if int(mLives)>= 3:
                                                iLives = iLives +"3"
                                        elif pressed[pygame.K_4]:
                                            if int(mLives)>= 4:
                                                iLives = iLives +"4"
                                        elif pressed[pygame.K_5]:
                                            if int(mLives)>= 5:
                                                iLives = iLives +"5"
                                        elif pressed[pygame.K_6]:
                                            if int(mLives)>= 6:
                                                iLives = iLives +"6"
                                        elif pressed[pygame.K_7]:
                                            if int(mLives)>= 7:
                                                iLives = iLives +"7"
                                        elif pressed[pygame.K_8]:
                                            if int(mLives)>= 8:
                                                iLives = iLives +"8"
                                        elif pressed[pygame.K_9]:
                                            if int(mLives)>= 9:
                                                iLives = iLives +"9"
                                    elif int(iLives)> 10:
                                        if pressed[pygame.K_RETURN]:
                                            break
                                        elif pressed[pygame.K_0]:
                                            if len(iLives) != 0:
                                                if int(mLives)>= int(iLives +"0"):
                                                    iLives = iLives +"0"
                                        elif pressed[pygame.K_1]:
                                            if int(mLives)>= int(iLives +"1"):
                                                iLives = iLives +"1"
                                        elif pressed[pygame.K_2]:
                                            if int(mLives)>= int(iLives +"2"):
                                                iLives = iLives +"2"
                                        elif pressed[pygame.K_3]:
                                            if int(mLives)> int(iLives +"3"):
                                                iLives = iLives +"3"
                                        elif pressed[pygame.K_4]:
                                            if int(mLives)> int(iLives +"4"):
                                                iLives = iLives +"4"
                                        elif pressed[pygame.K_5]:
                                            if int(mLives)> int(iLives +"5"):
                                                iLives = iLives +"5"
                                        elif pressed[pygame.K_6]:
                                            if int(mLives)> int(iLives +"6"):
                                                iLives = iLives +"6"
                                        elif pressed[pygame.K_7]:
                                            if int(mLives)> int(iLives +"7"):
                                                iLives = iLives +"7"
                                        elif pressed[pygame.K_8]:
                                            if int(mLives)> int(iLives +"8"):
                                                iLives = iLives +"8"
                                        elif pressed[pygame.K_9]:
                                            if int(mLives)> int(iLives +"9"):
                                                iLives = iLives +"9"
                                    
             
                                mouseX, mouseY =pygame.mouse.get_pos()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        return control, True
                                    
                                    if event.type == pygame.MOUSEBUTTONUP:
                                        if not(mouseY>= ((4.969/7.5)*screenY)and mouseY<=(((4.969/7.5)*screenY)+((0.302/7.5)*screenY))and mouseX>=(5.094/13.333)*screenX and mouseX<=((6.906/13.323)*screenX)):                                    
                                            breakLoop = True
                                            break
                                if breakLoop:
                                    break
                            if len(iLives) == 0:#restrictions initial lives need to not be 0, they are always postive because there is not negative input allowed
                                iLives = "3"
                            if int(mLives)< int(iLives):#restriction initial lives must be less than maxLives
                                iLives = mLives
                                
                    elif mouseX>=((11.188/13.333)*screenX) and mouseX<=((13/13.323)*screenX):                    
                        if mouseY>= ((1.927/7.5)*screenY)and mouseY<=(((1.927/7.5)*screenY)+((0.302/7.5)*screenY)):
                            #move left
                            temp = mL
                            tempControl = [mL,mR,shoot,shoot2,pt10,pt20,pt40,string,fps,bar,mLives,iLives, screenSize]
                            mL = Keys(newControl,True,((11.208/13.333)*screenX),((1.947/7.5)*screenY))
                            if mL.rep:
                                mL= temp
                            newControl[0] = mL
                        elif mouseY>= ((2.542/7.5)*screenY)and mouseY<=(((2.542/7.5)*screenY)+((0.302/7.5)*screenY)):
                            #move Right
                            temp = mR
                            tempControl = [mL,mR,shoot,shoot2,pt10,pt20,pt40,string,fps,bar,mLives,iLives, screenSize]
                            mR = Keys(newControl,True,((11.208/13.333)*screenX),((2.562/7.5)*screenY))
                            if mR.rep:
                                mR= temp
                            newControl[1] = mR
                        elif mouseY>= ((3.135/7.5)*screenY)and mouseY<=(((3.135/7.5)*screenY)+((0.302/7.5)*screenY)):
                            #second button to shoot
                            temp = shoot2
                            tempControl = [mL,mR,shoot,shoot2,pt10,pt20,pt40,string,fps,bar,mLives,iLives, screenSize]
                            shoot2 = Keys(newControl,True,((11.208/13.333)*screenX),((3.155/7.5)*screenY))
                            if shoot2.rep:
                                shoot2= temp
                            newControl[3] = shoot2
                        elif mouseY>= ((4.344/7.5)*screenY)and mouseY<=(((4.344/7.5)*screenY)+((0.302/7.5)*screenY)):
                            #10 pt alien select for map creator
                            temp = pt10
                            tempControl = [mL,mR,shoot,shoot2,pt10,pt20,pt40,string,fps,bar,mLives,iLives, screenSize]
                            pt10 = Keys(newControl,False,((11.208/13.333)*screenX),((4.364/7.5)*screenY))
                            if pt10.rep:
                                pt10= temp
                            newControl[4] = pt10
                        elif mouseY>= ((4.969/7.5)*screenY)and mouseY<=(((4.969/7.5)*screenY)+((0.302/7.5)*screenY)):
                            #20 pt alien select for map creator
                            temp = pt20
                            tempControl = [mL,mR,shoot,shoot2,pt10,pt20,pt40,string,fps,bar,mLives,iLives, screenSize]
                            pt20 = Keys(newControl,False,((11.208/13.333)*screenX),((4.989/7.5)*screenY))
                            if pt20.rep:
                                pt20= temp
                            newControl[5] = pt20
                        elif mouseY>= ((5.563/7.5)*screenY)and mouseY<=(((5.563/7.5)*screenY)+((0.302/7.5)*screenY)):
                            #40 pt alien select for map creator
                            temp = pt40
                            tempControl = [mL,mR,shoot,shoot2,pt10,pt20,pt40,string,fps,bar,mLives,iLives, screenSize]
                            pt40 = Keys(newControl,False,((11.208/13.333)*screenX),((5.583/7.5)*screenY))
                            if pt40.rep:
                                pt40= temp
                            newControl[6] = pt40
                    elif mouseY>= ((3.135/7.5)*screenY)and mouseY<=(((3.135/7.5)*screenY)+((0.302/7.5)*screenY)) and mouseX>=((9.406/13.333)*screenX) and mouseX<=((11.224/13.333)*screenX):
                        #button for shooting
                        temp = shoot
                        tempControl = [mL,mR,shoot,shoot2,pt10,pt20,pt40,string,fps,bar,mLives,iLives, screenSize]
                        shoot = Keys(newControl,True,((9.426/13.333)*screenX),((3.155/7.5)*screenY))
                        if shoot.rep:
                                shoot= temp
                        newControl[2] = shoot
                
                
                    
        tempControl = [mL,mR,shoot,shoot2,pt10,pt20,pt40,string,fps,bar,mLives,iLives,screenSize]
        drawSettings()
        
        pygame.display.update()
        window.fill(black)
def instructions():#for instructions page
    im = pygame.image.load("Instructions.png")
    im = pygame.transform.scale(im, (screenX,screenY))
    window.blit(im, (0,0))
    pt10 = font6.render(settings[4][0], True, white)
    pt20 = font6.render(settings[5][0], True, white)
    pt40 = font6.render(settings[6][0]+"/"+settings[7][0], True, white)
    window.blit(pt10,(((16.183/17.777)*screenX),((2.525/10)*screenY)))
    window.blit(pt20,(((16.183/17.777)*screenX),((3.303/10)*screenY)))
    window.blit(pt40,(((14.883/17.777)*screenX),((4.081/10)*screenY)))

    pygame.display.update()
    while True:
        mouseX, mouseY =pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONUP:
                if mouseX>=(15.653/17.778)*screenX and mouseX<=((16.958/17.778)*screenX)and mouseY>=(0.389/10)*screenY and mouseY<=((0.681/10)*screenY):
                    return False
def playGame():#for the menu to play default, create map, load map
    #returns quit,play,custom depending on users actions
    #quit is True to quit game, false to just go back
    #custom if they want custom or not, if not then returns None for custom
    while True:
        im = pygame.image.load("PlaySelect.png")
        im = pygame.transform.scale(im, (screenX,screenY))
        window.blit(im, (0,0))
        pygame.display.update()
        mouseX, mouseY =pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True, False, None
            if event.type == pygame.MOUSEBUTTONUP:
                if mouseX >= ((11.354/13.333)*screenX) and mouseX <= ((12.656/13.333)*screenX) and mouseY >= ((.698/7.5)*screenY) and mouseY <= ((.990/7.5)*screenY):
                    return False, False, None
                if mouseX>=(4.615/13.333)*screenX and mouseX<=((8.719/13.333)*screenX):
                    if mouseY>=(4.188/7.5)*screenY and mouseY<=((4.615/7.5)*screenY):
                        custom = False
                        return False, True, False
                    if mouseY>=(5.010/7.5)*screenY and mouseY<=((5.438/7.5)*screenY):
                        leave = createMap()
                        if leave:
                            return True, False, None
                    if mouseY>=(5.833/7.5)*screenY and mouseY<=((6.240/7.5)*screenY):
                        leave, load = loadMap()
                        if leave:
                            return True, False, None
                        if load:
                            return False, True, True
                        
def loadMap():
    #returns whether the user wants to leave, and whether they want a custom file
    #globally refrences mapName
    global mapName
    while True:
        im = pygame.image.load("CreateMap.png")
        im = pygame.transform.scale(im, (screenX,screenY))
        window.blit(im, (0,0))
        
        empty = font6.render("- Empty", True, white)
        used = font6.render("- Used", True, white)
        try:
            with open("CustomMap1.txt","r") as file:
        
                file1 = True
        except:
            file1 = False
        try:
            with open("CustomMap2.txt","r") as file:
                file2 = True
        except:
            file2 = False
        try:
            with open("CustomMap3.txt","r") as file:
                file3 = True
        except:
            file3 = False
        if not(file1):
            window.blit(empty,(((7.115/13.333)*screenX),((4.288/7.5)*screenY)))
        else:
            window.blit(used,(((7.115/13.333)*screenX),((4.288/7.5)*screenY)))
        if not(file2):
            window.blit(empty,(((7.115/13.333)*screenX),((5.108/7.5)*screenY)))
        else:
            window.blit(used,(((7.115/13.333)*screenX),((5.108/7.5)*screenY)))
        if not(file3):
            window.blit(empty,(((7.115/13.333)*screenX),((5.918/7.5)*screenY)))
        else:
            window.blit(used,(((7.115/13.333)*screenX),((5.918/7.5)*screenY)))

        pygame.display.update()
        mouseX, mouseY =pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True, False
            if event.type == pygame.MOUSEBUTTONUP:
                if mouseX >= ((11.354/13.333)*screenX) and mouseX <= ((12.656/13.333)*screenX) and mouseY >= ((.698/7.5)*screenY) and mouseY <= ((.990/7.5)*screenY):
                    return False, False
                if mouseX>=((4.615/13.333)*screenX) and mouseX<=((8.719/13.333)*screenX):
                    if mouseY>=(4.188/7.5)*screenY and mouseY<=((4.615/7.5)*screenY):
                        if file1:
                            mapName= "CustomMap1"
                            return False, True
                    if mouseY>=(5.010/7.5)*screenY and mouseY<=((5.438/7.5)*screenY):
                        if file2:
                            mapName = "CustomMap2"
                            return False, True
                    if mouseY>=(5.833/7.5)*screenY and mouseY<=((6.240/7.5)*screenY):
                        if file3:
                            mapName = "CustomMap3"
                            return False, True
                            
def createMap():
    #returns whether the user quit(true) or clicked back(false)
    #allows user to create a map
    overwrite1 = False
    overwrite2 = False
    overwrite3 = False
    
    while True:
        im = pygame.image.load("CreateMap.png")
        im = pygame.transform.scale(im, (screenX,screenY))
        window.blit(im, (0,0))
        empty = font6.render("- Empty", True, white)
        used = font6.render("- Used", True, white)
        try:
            with open("CustomMap1.txt","r") as file:
        
                file1 = True
        except:
            file1 = False
        try:
            with open("CustomMap2.txt","r") as file:
                file2 = True
        except:
            file2 = False
        try:
            with open("CustomMap3.txt","r") as file:
                file3 = True
        except:
            file3 = False
        if not(file1):
            window.blit(empty,(((7.115/13.333)*screenX),((4.288/7.5)*screenY)))
        else:
            window.blit(used,(((7.115/13.333)*screenX),((4.288/7.5)*screenY)))
        if not(file2):
            window.blit(empty,(((7.115/13.333)*screenX),((5.108/7.5)*screenY)))
        else:
            window.blit(used,(((7.115/13.333)*screenX),((5.108/7.5)*screenY)))
        if not(file3):
            window.blit(empty,(((7.115/13.333)*screenX),((5.918/7.5)*screenY)))
        else:
            window.blit(used,(((7.115/13.333)*screenX),((5.918/7.5)*screenY)))
        if overwrite1:
            image1 = pygame.image.load("overwrite.png")
            image1 = pygame.transform.scale(image1,(screenX,screenY))
            window.blit(image1,(0,0))
        if overwrite2:
            image1 = pygame.image.load("overwrite.png")
            image1 = pygame.transform.scale(image1,(screenX,screenY))
            window.blit(image1,(0,0))
        if overwrite3:
            
            image1 = pygame.image.load("overwrite.png")
            image1 = pygame.transform.scale(image1,(screenX,screenY))
            window.blit(image1,(0,0))
        pygame.display.update()
        pygame.display.update()
        mouseX, mouseY =pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONUP:
                if mouseX >= ((11.354/13.333)*screenX) and mouseX <= ((12.656/13.333)*screenX) and mouseY >= ((.698/7.5)*screenY) and mouseY <= ((.990/7.5)*screenY):
                    return False
                if not(overwrite1 or overwrite2 or overwrite3):
                    if mouseX>=((4.615/13.333)*screenX) and mouseX<=((8.719/13.333)*screenX):
                        if mouseY>=(4.188/7.5)*screenY and mouseY<=((4.615/7.5)*screenY):
                            
                            if file1:
                                overwrite1 = True
                            else:
                                mapCreator(control,"CustomMap1")
                        if mouseY>=(5.010/7.5)*screenY and mouseY<=((5.438/7.5)*screenY):
                            if file2:
                                overwrite2 = True
                            else:
                                mapCreator(control,"CustomMap2")
                        if mouseY>=(5.833/7.5)*screenY and mouseY<=((6.240/7.5)*screenY):
                            if file3:
                                overwrite3 = True
                            else:
                                mapCreator(control,"CustomMap3")
                elif overwrite1:
                    if mouseX>= ((4.458/13.333)*screenX) and mouseX<= ((6.25/13.333)*screenX) and mouseY>= ((6.167/7.5)*screenY) and mouseY<=((6.531/7.5)*screenY):
                        mapCreator(control,"CustomMap1")
                        overwrite1 = False
                    if mouseX>= ((7.052/13.333)*screenX) and mouseX<= ((8.844/13.333)*screenX) and mouseY>= ((6.167/7.5)*screenY) and mouseY<=((6.531/7.5)*screenY):
                        overwrite1 = False
                elif overwrite2:
                    if mouseX>= ((4.458/13.333)*screenX) and mouseX<= ((6.25/13.333)*screenX) and mouseY>= ((6.167/7.5)*screenY) and mouseY<=((6.531/7.5)*screenY):
                        mapCreator(control,"CustomMap2")
                        overwrite2 = False
                    if mouseX>= ((7.052/13.333)*screenX) and mouseX<= ((8.844/13.333)*screenX) and mouseY>= ((6.167/7.5)*screenY) and mouseY<=((6.531/7.5)*screenY):
                        overwrite2 = False
                elif overwrite3:
                    if mouseX>= ((4.458/13.333)*screenX) and mouseX<= ((6.25/13.333)*screenX) and mouseY>= ((6.167/7.5)*screenY) and mouseY<=((6.531/7.5)*screenY):
                        mapCreator(control,"CustomMap3")
                        overwrite3 = False
                    if mouseX>= ((7.052/13.333)*screenX) and mouseX<= ((8.844/13.333)*screenX) and mouseY>= ((6.167/7.5)*screenY) and mouseY<=((6.531/7.5)*screenY):
                        overwrite3 = False  
def titleScreen(control):
    #returns quit,control, custom, custom is none if quit is True
    play = False
    q =False
    if settings[2] == "On":
        music = True
    else:
        music = False
    change = False
    while True:
        im = pygame.image.load("Space_Invaders.png")
        im = pygame.transform.scale(im, (screenX,screenY))
        im1  = pygame.image.load("Music.png")
        im1 = pygame.transform.scale(im1, (screenX//22,screenY//15))
        im2  = pygame.image.load("Music-stop.png")
        im2 = pygame.transform.scale(im2, (screenX//22,screenY//15))
        mouseX, mouseY =pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                q = True
            if event.type == pygame.MOUSEBUTTONUP:
                if mouseX>=(4.615/13.323)*screenX and mouseX<=((4.615/13.323)*screenX+(4.093/13.323)*screenX):
                    if mouseY>=(4.188/7.5)*screenY and mouseY<=((4.188/7.5)*screenY+(0.427/7.5)*screenY):
                        q,play,custom = playGame()
                        #play
                    elif mouseY>=(4.969/7.5)*screenY and mouseY<=((4.969/7.5)*screenY+(0.427/7.5)*screenY): 
                        q = instructions()
                        #instructions
                    elif mouseY>=(5.729/7.5)*screenY and mouseY<=((5.729/7.5)*screenY+(0.427/7.5)*screenY):
                        control,q = settingsControl(control)
                        #settings
                    elif mouseY>=(6.5/7.5)*screenY and mouseY<=((6.5/7.5)*screenY+(0.427/7.5)*screenY):
                        v=highScore()
                        #highscore
                        if v:
                            return True, control, None
                if mouseX>=(screenX*(13/16)) and mouseX<= (screenX*(13/16)+(screenX//22)) and mouseY>=(screenY*(7/8)) and mouseY<=(screenY*(7/8)+(screenY//15)):
                    #Turn on or off the music
                    music = not(music)
                    change = True
        window.blit(im,(0,0))
        if music:
            window.blit(im1,(screenX*(13/16),screenY*(7/8)))
            if change:
                settings[2]="On"
                pygame.mixer.music.unpause()
            change = False
        else:
            window.blit(im2,(screenX*(13/16),screenY*(7/8)))
            if change:
                settings[2]="Off"
                pygame.mixer.music.pause()
            change = False
        pygame.display.update()
        window.fill(black)
        if play:
            return False, control, custom
        if q:
            return True, control, None
def setVariables(scX,scY):
    #globally sets all the variables that are used to display things
    global screenX
    global screenY
    global window
    global xAlienSize
    global yAlienSize
    global xShipSize
    global yShipSize
    global redAlienX
    global redAlienY
    global shipBulletX
    global shipBulletY
    global alienBulletX
    global alienBulletY
    global shipStartX
    global shipStartY
    global minRedAlienY
    global minAlienY
    global xAlienScreen
    global minAlienX
    global xAlienScreen
    global minAlienX
    global yAlienStep
    global yAlienScreen
    global xParameterAlien
    global yParameterAlien
    global xAlienStep
    global font
    global font1
    global font2
    global font3
    global font4
    global font5
    global font6
    global minDisplayY
    global scorePos
    global scoreTextPos
    global liveTextPos
    global greenPixelX
    global greenPixelY
    global barrierX
    global barrierY
    global barrierSectionX
    global barrierSectionY
    global barrierinitialY
    screenX = scX
    screenY = scY
    window = pygame.display.set_mode((screenX,screenY))
    pygame.display.set_caption("Space Invaders")
    xAlienSize = screenX//25
    yAlienSize = screenY//18
    xShipSize = screenX//18
    yShipSize = screenY//18
    redAlienX = screenX//15
    redAlienY = screenY//9
    shipBulletX = xShipSize//10
    shipBulletY = yShipSize//2
    alienBulletX = xAlienSize//10
    alienBulletY = yAlienSize//3
    shipStartX = screenX//15
    shipStartY = screenY-(1.5*yShipSize)
    minRedAlienY = screenY//16
    minAlienY = minRedAlienY+redAlienY+int((screenY//100)*2)
    xAlienScreen = (9/16)
    minAlienX = int((.5*screenX)-((.5*xAlienScreen)*screenX)//1)
    yAlienStep = int(1.5*(yAlienSize))
    yAlienScreen = (minAlienY +(5*(yAlienStep)))/screenY
    xParameterAlien = int((.5*screenX)+((.5*xAlienScreen)*screenX)//1)
    yParameterAlien = int((screenY*(yAlienScreen))//1)
    xAlienStep =((xAlienSize)+int((settings[0][0]//100)*1.5))
    font = pygame.font.Font('emulogic.ttf', screenY//25)
    font1 = pygame.font.Font('emulogic.ttf', screenY//30)
    font2 = pygame.font.Font('emulogic.ttf', screenY//15)
    font3 = pygame.font.Font('emulogic.ttf', screenY//25)
    font4 = pygame.font.Font('emulogic.ttf', screenY//30)
    font5 = pygame.font.Font('emulogic.ttf', screenY//25)
    font6 = pygame.font.Font('emulogic.ttf', screenY//40)
    minDisplayY = screenY//100
    scorePos = (3/16*screenX, minDisplayY)
    scoreTextPos = (1/16*screenX, minDisplayY)
    liveTextPos = (35/64*screenX,minDisplayY+(1/100*screenY))
    greenPixelX = screenX/1000
    greenPixelX = 2*round(greenPixelX)
    greenPixelY = screenY/1000
    greenPixelY = 2*round(greenPixelY)
    barrierX = screenX//11
    barrierY = int((barrierX/1.385)*.802)
    barrierSectionX = barrierX/4
    barrierSectionY = barrierY/2
    barrierinitialY = int(screenY*3/4)

def quitGame():
    #returns True to quit game
    return True



pygame.init()
white = (255,255,255)
green = (0,255,0)
black = (0,0,0)
direction = "Left"

t = 0
score = 0
settings = readSettings()
control = [KeysDefault(settings[4][0],settings[4][1]),KeysDefault(settings[5][0],settings[5][1]),KeysDefault(settings[6][0],settings[6][1]),KeysDefault(settings[7][0],settings[7][1]),KeysDefault(settings[8][0],settings[8][1]),KeysDefault(settings[9][0],settings[9][1]),KeysDefault(settings[10][0],settings[10][1])]
screenX = settings[0][0]
screenY = settings[0][1]



xAlienSize = screenX//25
yAlienSize = screenY//18
xShipSize = screenX//18
yShipSize = screenY//18
redAlienX = screenX//15
redAlienY = screenY//9
shipBulletX = xShipSize//10
shipBulletY = yShipSize//2
alienBulletX = xAlienSize//10
alienBulletY = yAlienSize//3
shipStartX = screenX//15
shipStartY = screenY-(1.5*yShipSize)
minRedAlienY = screenY//16
minAlienY = minRedAlienY+redAlienY+int((screenY//100)*2)
xAlienScreen = (9/16)
minAlienX = int((.5*screenX)-((.5*xAlienScreen)*screenX)//1)
yAlienStep = int(1.5*(yAlienSize))
yAlienScreen = (minAlienY +(5*(yAlienStep)))/screenY
xParameterAlien = int((.5*screenX)+((.5*xAlienScreen)*screenX)//1)
yParameterAlien = int((screenY*(yAlienScreen))//1)
xAlienStep =((xAlienSize)+int((settings[0][0]//100)*1.5))
font = pygame.font.Font('emulogic.ttf', screenY//25)
font1 = pygame.font.Font('emulogic.ttf', screenY//30)
font2 = pygame.font.Font('emulogic.ttf', screenY//15)
font3 = pygame.font.Font('emulogic.ttf', screenY//25)
font4 = pygame.font.Font('emulogic.ttf', screenY//30)
font5 = pygame.font.Font('emulogic.ttf', screenY//25)
font6 = pygame.font.Font('emulogic.ttf', screenY//40)
minDisplayY = screenY//100
scorePos = (3/16*screenX, minDisplayY)
scoreTextPos = (1/16*screenX, minDisplayY)
liveTextPos = (35/64*screenX,minDisplayY+(1/100*screenY))
greenPixelX = screenX/1000
greenPixelX = 2*round(greenPixelX)
greenPixelY = screenY/1000
greenPixelY = 2*round(greenPixelY)
barrierX = screenX//11
barrierY = int((barrierX/1.385)*.802)
barrierSectionX = barrierX/4
barrierSectionY = barrierY/2
barrierinitialY = int(screenY*3/4)
if settings[2] == "On":
    playMusic("Title Screen")
if settings[2] == "Off":
    playMusic("Title Screen",False)
window = pygame.display.set_mode(settings[0])
repeat = True
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()
done,control,custom = titleScreen(control)
if done:
    repeat = False
redScoreTime = 60
alienExplosionTime = 2
alienBulletMove = (60*screenY//120)/settings[3]
shipBulletMove = (60*screenY//60)/settings[3]
tempControl = []
shipMove = (60*screenX//200)/settings[3]
minNumBullet = 1
maxNumBullet = 3
alienMove = (60*screenX/1500)/settings[3]
constIncrease = (1/7*alienMove)
intervalStart = 120
intervalEnd = 300
intervalStep = 60
saveSettings(settings)

playAgain = True
while repeat:#The Loop which includes the game over screen, allowing the user to restart game
    
    if not(playAgain):#playAgain allows user to go to main menu after the game is over and it restarts
        #playAgain is False when the user goes back from highscore after the game
        #playAgain is True when the user wants to play Again
        done,control,custom = titleScreen(control)
        saveSettings(settings)
    else:#if playAgain then allows user to play the game
       done = False
    #Reinitializing variables   
    t = 0
    score = 0
    R1=RedAlien(window,screenX)
    timer = 0
    change = False
    reset = True
    initial = pygame.key.get_pressed()
    S1 = Spaceship(window)
    lives = settings[13]-1
    killShip = False
    B1= None
    bullet = []
    interval = random.randrange(intervalStart,intervalEnd,intervalStep)
    intervalTime = 0
    liveDisplay = []
    redAlienMove = 1
    barriers = int(settings[11])
    barrier = []
    txt = []
    explosion = []
      

    resetPiece=False
    saved = False
    played = False
    for h in range(barriers):
        #display barriers
        spacing  = (screenX -(barriers*barrierX))//(barriers+1)
        barrier.append(Barrier(window,(h+1)*spacing + h*(barrierX),barrierinitialY))
    for x in range(lives):#Creates a display of how many lives you have
        liveDisplay.append(LiveDisplay(window,(11/16*screenX)+(x*(xShipSize+(1/3*xShipSize))),minDisplayY))
    while not done:#The main game loop
        played = True
        if reset:#If the game is getting reset, after each round or to start the game
            if resetPiece and killShip:#if reseting Aliens(piece) and ship
                resetPiece = True
                killShip = False
                del S1
                S1 = Spaceship(window)
                del liveDisplay[-1]
                bullet = []
                aliens = []
                k = 0
                if not (custom):#if not custom map
                    for y in range(minAlienY, yParameterAlien,yAlienStep):
                        k+= 1
                        val = []
                        for x in range(minAlienX,xParameterAlien,xAlienStep):
                            if not(x >= (screenX-(xAlienSize))) and not(y >= (screenY-(yAlienSize))):
                                if k == (1/5*yParameterAlien)//(yAlienStep):
                                    val.append(GreenAlien(40,window,x,y))
                                elif k >= (1/5*yParameterAlien)//(yAlienStep) and k <= (3/5*yParameterAlien)//(yAlienStep):
                                    val.append(GreenAlien(20,window,x,y))
                                else:
                                    val.append(GreenAlien(10,window,x,y))
                        aliens.append(val)
                if custom:
                    #uses custom file to display the map
                    aliens=[[],[],[]]
                    pieces,screenCustomX,screenCustomY = readCustom(mapName)#the screenCustomX and Y are the screenX and screenY when the custom was made
                    for i in pieces[0]:
                        i = i[1:-1]
                        i = i.split(",")
                        i[1] = i[1][1:]
                        i[0] = int(i[0])
                        i[1] = int(i[1])
                        i[0]= (i[0]/screenCustomX)*screenX
                        i[1]= (i[1]/screenCustomY)*screenY
                        aliens[0].append(GreenAlien(10,window,i[0],i[1]))
                    for i in pieces[1]:
                        i = i[1:-1]
                        i = i.split(",")
                        i[1] = i[1][1:]
                        i[0] = int(i[0])
                        i[1] = int(i[1])
                        i[0]= (i[0]/screenCustomX)*screenX
                        i[1]= (i[1]/screenCustomY)*screenY
                        aliens[0].append(GreenAlien(20,window,i[0],i[1]))
                    for i in pieces[2]:
                        i = i[1:-1]
                        i = i.split(",")
                        i[1] = i[1][1:]
                        i[0] = int(i[0])
                        i[1] = int(i[1])
                        i[0]= (i[0]/screenCustomX)*screenX
                        i[1]= (i[1]/screenCustomY)*screenY
                        aliens[0].append(GreenAlien(40,window,i[0],i[1])) 
            elif killShip:#if the ship was killed, reseting only the ship
                killShip = False
                del S1
                S1 = Spaceship(window)
                del liveDisplay[-1]
                bullet = []
            else:#If all the aliens are killed, resets only the aliens
                if lives <= settings[12]:
                    lives += 1
                    liveDisplay.append(LiveDisplay(window,(11/16*screenX)+(len(liveDisplay)*(xShipSize+(1/3*xShipSize))),minDisplayY))
                alienMove += constIncrease
                bullet = []
                aliens = []
                k = 0
                if not(custom):#If not custom map
                    for y in range(minAlienY, yParameterAlien,yAlienStep):
                        k+= 1
                        val = []
                        for x in range(minAlienX,xParameterAlien,xAlienStep):
                            if not(x >= (screenX-(xAlienSize))) and not(y >= (screenY-(yAlienSize))):
                                if k == (1/5*yParameterAlien)//(yAlienStep):
                                    val.append(GreenAlien(40,window,x,y))
                                elif k >= (1/5*yParameterAlien)//(yAlienStep) and k <= (5/10*yParameterAlien)//(yAlienStep):
                                    val.append(GreenAlien(20,window,x,y))
                                else:
                                    val.append(GreenAlien(10,window,x,y))
                        aliens.append(val)
                if custom:
                    #uses custom file to display the map
                    aliens=[[],[],[]]
                    pieces,screenCustomX,screenCustomY = readCustom(mapName)#the screenCustomX and Y are the screenX and screenY when the custom was made
                    
                    for i in pieces[0]:
                        i = i[1:-1]
                        i = i.split(",")
                        i[1] = i[1][1:]
                        i[0] = int(i[0])
                        i[1] = int(i[1])
                        i[0]= (i[0]/screenCustomX)*screenX
                        i[1]= (i[1]/screenCustomY)*screenY
                        aliens[0].append(GreenAlien(10,window,i[0],i[1]))
                    for i in pieces[1]:
                        i = i[1:-1]
                        i = i.split(",")
                        i[1] = i[1][1:]
                        i[0] = int(i[0])
                        i[1] = int(i[1])
                        i[0]= (i[0]/screenCustomX)*screenX
                        i[1]= (i[1]/screenCustomY)*screenY
                        aliens[0].append(GreenAlien(20,window,i[0],i[1]))
                    for i in pieces[2]:
                        i = i[1:-1]
                        i = i.split(",")
                        i[1] = i[1][1:]
                        i[0] = int(i[0])
                        i[1] = int(i[1])
                        i[0]= (i[0]/screenCustomX)*screenX
                        i[1]= (i[1]/screenCustomY)*screenY
                        aliens[0].append(GreenAlien(40,window,i[0],i[1])) 
            reset = False
            
                    
        if lives == 0:#if you die then saves score, and quits
            saveScore(settings[1],score,custom)
            done = quitGame()
            saved= True
        else:#if you have not died
            for x in range(len(liveDisplay)):#Draws how many lives you have
                liveDisplay[x].drawShip()
            h = len(aliens)
            b = 0
            for x in aliens:#Checking if all the aliens died
                if len(x)==0:
                    b+=1
            if b==h:
                reset = True
                killShip = False
            else:
                killShip = True
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if control[0].name == "Click":
                    if event.type == pygame.MOUSEBUTTONUP:
                        S1.xval -=shipMove
                if control[1].name == "Click":
                    if event.type == pygame.MOUSEBUTTONUP:
                        S1.xval +=shipMove
                if control[2].name == "Click":
                    if event.type == pygame.MOUSEBUTTONUP:
                        S1.shoot()
                if control[3].name == "Click":
                    if event.type == pygame.MOUSEBUTTONUP:
                        S1.shoot()
            pressed = pygame.key.get_pressed()
            if not(control[2].name == "Click"):
                if pressed[control[2].key]:
                    S1.shoot()
            if not(control[3].name == "Click"):
                if pressed[control[3].key]:
                    S1.shoot()
            if not(control[0].name == "Click"):
                if pressed[control[0].key]:
                    S1.xval -=shipMove
            if not(control[1].name == "Click"):
                if pressed[control[1].key]:
                    S1.xval +=shipMove
            
            if R1.xval != screenX:#Moves the red Alien depending on where the alien is
                R1.xval -= redAlienMove
            else:
                if timer == 5*settings[3]:
                    timer = 0
                    R1.xval -=redAlienMove
                timer += 1
                
            if S1.shot == True: #Moves the ship's bullet
                S1.bulletY -= shipBulletMove
                
            if len(bullet)== 0:#Making bullets for the aliens if none exist already
                intervalTime += 1
                if intervalTime == interval:
                    intervalTime = 0
                    interval = random.randrange(intervalStart,intervalEnd,intervalStep)
                    b= 0
                    for x in range(len(aliens)):
                        for y in range(len(aliens[x])):
                            b+= 1
                    if b < maxNumBullet:
                        maxNumBullet = b
                    else:
                        maxNumBullet = 3
                    numofbullet = random.randint(minNumBullet,maxNumBullet)
                    alienShooting= []
                    for g in range(numofbullet):
                        num = 0
                        for x in aliens:
                            for y in x:
                                num += 1
                        num1 = random.randint(0,num)
                        while num1 in alienShooting:
                            num1 = random.randint(0,num)
                        alienShooting.append(num1)
                        num2 = 0
                        for c in range (len(aliens)):
                            for v in range (len(aliens[c])):
                                num2+=1
                                if num2 == num1:
                                    bullet.append(aliens[c][v].shoot())
                                    
            for c in range (len(bullet)):#If the bullets exists then moves them
                if bullet[c].shot == True:
                    bullet[c].bulletY += alienBulletMove
                    bullet[c].drawBullet()
            c = 0
            while c < len(bullet):#Checking if any of the alien bullets hits the ship
                hitTarget = S1.checkHit(bullet[c].bulletX,bullet[c].bulletY)
                bullet[c].bulletHit(c,hitTarget)
                if hitTarget:
                    reset = True
                    killShip= True
                if not(hitTarget):
                    c+=1
            c = 0
            while c < len(bullet):#checking if any of the alien bullets hit the barriers
                for b in range(len(barrier)):
                    hitTarget = barrier[b].checkHit(bullet[c].bulletX,bullet[c].bulletY,"alien")
                    if hitTarget:
                        break
                bullet[c].bulletHit(c,hitTarget)
                if not(hitTarget):
                    c+=1

            S1.drawShip()
            if S1.shot == True:#Checks if the ships bullets hit the red alien
                hit,worth,postion = R1.checkHit(S1.bulletX,S1.bulletY)
                if not(postion == None) and worth!= None:
                    txt.append(RedScoreText(str(worth),postion,white))
                if worth != None:
                    score+= worth
                    worth = None
            for x in range(len(txt)):#displays the red alien value when it dies
                txt[x].checkCount(x)
            if S1.shot and hit:#resets the red alien
                R1 = RedAlien(window,screenX)
            if S1.shot == True:#Checking if the ship's bullets hit the barriers
                for c in range(len(barrier)):
                    hit = barrier[c].checkHit(S1.bulletX,S1.bulletY,"ship")
                    if hit == True:
                        break  
            if S1.shot == True and not(hit):#Checking if the ships's bullets hit the aliens, and how much they are worth
                for c in range(len(aliens)):
                    for v in range(len(aliens[c])):
                        hit,worth,alienPostion = aliens[c][v].checkHit(S1.bulletX,S1.bulletY,c,v)
                        if not(alienPostion == None) and worth!= None:
                            explosion.append(Explosion(alienPostion))
                        if worth != None:
                            score += worth
                            worth = None
                        if hit == True:
                            break
                    if hit == True:
                        break
            x=0
            while x < len(explosion):#returns False if the explosion has lasted less then 2 frames, if more then returns True and deletes itself from the list
                kill = explosion[x].checkCount(x)
                if not(kill):
                    x+= 1
            if S1.shot and hit:
                S1.shoot(True)
            for x in aliens:#if any of the aliens touch the side of the screen changes direction
                for y in x:
                    if y.xval <= 0:
                        direction = "Right"
                        change = True
                    if y.xval>= screenX-xAlienSize:
                        direction = "Left"
                        change= True
            if change:#If any of the aliens has touched the sides of the screen then moves all the aliens down
                for c in range(len(aliens)):
                    for v in range(len(aliens[c])):
                        aliens[c][v].yval +=yAlienSize
                change= False
            for c in range(len(aliens)):
                for v in range(len(aliens[c])):#Moves the alien in the direction that all of them are moving in
                    if direction == "Right":
                        aliens[c][v].xval +=alienMove
                    elif direction == "Left":
                        aliens[c][v].xval -=alienMove
                    aliens[c][v].drawAlien()
            for c in range(len(barrier)):#Draws barriers
                barrier[c].drawBarrier()
            if t == 120:
                t = 0
            t += 1
            for c in range(len(aliens)):#Checking if any of the aliens have reached the same height as the ship
                for v in range(len(aliens[c])):
                    if aliens[c][v].yval>= screenY-yShipSize-(screenY-(S1.yval)):
                        reset = True
                        resetPiece= True

            
            scoreStr = str(score)
            text = font.render(scoreStr, True, white)
            text1 = font.render("SCORE", True, green)
            text2 = font.render("LIVES", True, green)
            window.blit(text,scorePos)
            window.blit(text1,scoreTextPos)
            window.blit(text2,liveTextPos)
            if lives >= 1 and reset == True and killShip == True:
                lives -=1
            if not(reset):
                pygame.display.update()
                window.fill(black)
            clock.tick(settings[3])

         

    
    if lives == 0:#If the game has ended because the user has died rather than for quiting
        
        endScreen = pygame.image.load("EndScreen.png")
        endScreen = pygame.transform.scale(endScreen, (screenX,screenY))
        menu = False
        playAgain = False
        string = settings[1]
        scoreStr = str(score)
        text = font.render(scoreStr, True, white)
        
        
        while True: #Game Over Screen
            window.blit(endScreen,(0,0))
            window.blit(text,((7.33/13.333)*screenX,(2.573/7.5)*screenY))
            name = font.render(string, True, white)
            window.blit(name,((5.65/13.333)*screenX,(4.23/7.5)*screenY))
            pygame.display.update()
            mouseX, mouseY =pygame.mouse.get_pos() #Finds mouse Postion
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    repeat= False
                    break
                
                if event.type == pygame.MOUSEBUTTONUP:
                    if mouseX>= ((4.875/13.333)*screenX) and mouseX<= ((8.469/13.333)*screenX) and mouseY>= ((4.156/7.5)*screenY) and mouseY<=((4.708/7.5)*screenY):
                        
                        #name change
                        prev = pygame.key.get_pressed()
                        while True:
                            write = True
                            window.blit(endScreen,(0,0))
                            window.blit(text,((7.33/13.333)*screenX,(2.573/7.5)*screenY))
                            name = font.render(string, True, white)
                            window.blit(name,((5.65/13.333)*screenX,(4.23/7.5)*screenY))
                            pygame.display.update()
                            pressed = pygame.key.get_pressed()
                            if pressed != prev:#making sure there is a change in the keyboard
                                prev= pressed
                                #Changing the name of the user
                                if pressed[pygame.K_BACKSPACE]:
                                    if len(string)!= 0:
                                        string = string[:-1]
                                if len(string) < 7:
                                    if pressed[pygame.K_RETURN]:
                                        break
                                    elif pressed[pygame.K_RSHIFT] or pressed[pygame.K_LSHIFT]:
                                        if pressed[pygame.K_1]:
                                            string = string +"!"
                                        elif pressed[pygame.K_2]:
                                            string = string +"@"
                                        elif pressed[pygame.K_3]:
                                            string = string +"#"
                                        elif pressed[pygame.K_4]:
                                            string = string +"$"
                                        elif pressed[pygame.K_5]:
                                            string = string +"%"
                                        elif pressed[pygame.K_6]:
                                            string = string +"^"
                                        elif pressed[pygame.K_7]:
                                            string = string +"&"
                                        elif pressed[pygame.K_8]:
                                            string = string +"*"
                                        elif pressed[pygame.K_9]:
                                            string = string +"("
                                        elif pressed[pygame.K_0]:
                                            string = string +")"
                                        elif pressed[pygame.K_MINUS]:
                                            string = string +"_"
                                        elif pressed[pygame.K_EQUALS]:
                                            string = string +"+"
                                        elif pressed[pygame.K_LEFTBRACKET]:
                                            string = string +"{"
                                        elif pressed[pygame.K_BACKSLASH]:
                                            string = string +"|"
                                        elif pressed[pygame.K_RIGHTBRACKET]:
                                            string = string +"}"
                                        elif pressed[pygame.K_SEMICOLON]:
                                            string = string +":"
                                        elif pressed[pygame.K_QUOTE]:
                                            string = string +"\""
                                        elif pressed[pygame.K_COMMA]:
                                            string = string +"<"
                                        elif pressed[pygame.K_PERIOD]:
                                            string = string +">"
                                        elif pressed[pygame.K_SLASH]:
                                            string = string +"?"
                                    elif pressed[pygame.K_SPACE]:
                                        string = string +" "
                                    elif pressed[pygame.K_QUOTE]:
                                        string = string +"\'"
                                    elif pressed[pygame.K_COMMA]:
                                        string = string +","
                                    elif pressed[pygame.K_MINUS]:
                                        string = string +"-"
                                    elif pressed[pygame.K_PERIOD]:
                                        string = string +"."
                                    elif pressed[pygame.K_SLASH]:
                                        string = string +"/"
                                    elif pressed[pygame.K_SEMICOLON]:
                                        string = string +";"
                                    elif pressed[pygame.K_EQUALS]:
                                        string = string +"="
                                    elif pressed[pygame.K_LEFTBRACKET]:
                                        string = string +"["
                                    elif pressed[pygame.K_BACKSLASH]:
                                        string = string +"\\"
                                    elif pressed[pygame.K_RIGHTBRACKET]:
                                        string = string +"]"
                                    elif pressed[pygame.K_BACKQUOTE]:
                                        string = string +"`"
                                    elif pressed[pygame.K_a]:
                                        string = string +"a"
                                    elif pressed[pygame.K_b]:
                                        string = string +"b"
                                    elif pressed[pygame.K_c]:
                                        string = string +"c"
                                    elif pressed[pygame.K_d]:
                                        string = string +"d"
                                    elif pressed[pygame.K_e]:
                                        string = string +"e"
                                    elif pressed[pygame.K_f]:
                                        string = string +"f"
                                    elif pressed[pygame.K_g]:
                                        string = string +"g"
                                    elif pressed[pygame.K_h]:
                                        string = string +"h"
                                    elif pressed[pygame.K_i]:
                                        string = string +"i"
                                    elif pressed[pygame.K_j]:
                                        string = string +"j"
                                    elif pressed[pygame.K_k]:
                                        string = string +"k"
                                    elif pressed[pygame.K_l]:
                                        string = string +"l"
                                    elif pressed[pygame.K_m]:
                                        string = string +"m"
                                    elif pressed[pygame.K_n]:
                                        string = string +"n"
                                    elif pressed[pygame.K_o]:
                                        string = string +"p"
                                    elif pressed[pygame.K_p]:
                                        string = string +"p"
                                    elif pressed[pygame.K_q]:
                                        string = string +"q"
                                    elif pressed[pygame.K_r]:
                                        string = string +"r"
                                    elif pressed[pygame.K_s]:
                                        string = string +"s"
                                    elif pressed[pygame.K_t]:
                                        string = string +"t"
                                    elif pressed[pygame.K_u]:
                                        string = string +"u"
                                    elif pressed[pygame.K_v]:
                                        string = string +"v"
                                    elif pressed[pygame.K_w]:
                                        string = string +"w"
                                    elif pressed[pygame.K_x]:
                                        string = string +"x"
                                    elif pressed[pygame.K_y]:
                                        string = string +"y"
                                    elif pressed[pygame.K_z]:
                                        string = string +"z"
                                    elif pressed[pygame.K_0]:
                                        string = string +"0"
                                    elif pressed[pygame.K_1]:
                                        string = string +"1"
                                    elif pressed[pygame.K_2]:
                                        string = string +"2"
                                    elif pressed[pygame.K_3]:
                                        string = string +"3"
                                    elif pressed[pygame.K_4]:
                                        string = string +"4"
                                    elif pressed[pygame.K_5]:
                                        string = string +"5"
                                    elif pressed[pygame.K_6]:
                                        string = string +"6"
                                    elif pressed[pygame.K_7]:
                                        string = string +"7"
                                    elif pressed[pygame.K_8]:
                                        string = string +"8"
                                    elif pressed[pygame.K_9]:
                                        string = string +"9"
         
                            mouseX, mouseY =pygame.mouse.get_pos()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    repeat = False
                                
                                if event.type == pygame.MOUSEBUTTONUP:
                                    #if user clicks off of the box then checks if the user wants to playagain or go to highscores
                                    if not(mouseX>= ((4.875/13.333)*screenX) and mouseX<= ((8.469/13.333)*screenX) and mouseY>= ((4.156/7.5)*screenY) and mouseY<=((4.708/7.5)*screenY)):                                    
                                        write = False
                                        settings[1]=string
                                        break
                                    
                            if not(repeat):
                                break
                            if not(write):
                                break
                    if mouseX>= ((0.177/13.333)*screenX) and mouseX<= ((2.896/13.333)*screenX) and mouseY>= ((0.188/7.5)*screenY) and mouseY<=((0.406/7.5)*screenY):
                        #In game over screen going to highscore and checking if they want to quit or go to main menu
                        v=highScore()
                        if v:
                            repeat = False
                        else:
                            menu = True
                    elif mouseX>= ((10.708/13.333)*screenX) and mouseX<= ((13.177/13.333)*screenX) and mouseY>= ((0.188/7.5)*screenY) and mouseY<=((0.406/7.5)*screenY):
                        playAgain = True
            if menu:
                break
            if playAgain:
                settings[1]=string
                break
            if not(repeat):
                settings[1]=string
                break
    else:
        repeat = False
    if not(saved)and played: #Making sure the score is saved
        saveScore(settings[1],score,custom)
    saveSettings(settings)
pygame.quit()
