import pygame as pg
inf = 'inf'
clock = pg.time.Clock()
class Timer:
    def __init__(self):
        self.time = 0
        self.process = False
        self.stopper = 0

    def start(self, stopper):
        if type(stopper) != str:
            self.stopper = stopper*1000            
        else:
            self.stopper = stopper
        self.time = 0
        self.process = True

    def mainflow(self):
        
        self.time += 1000/FPS
        if type(self.stopper) != str:
            if self.process == True and int(self.time//1000) == self.stopper//1000:
                print(f"{self.stopper//1000} seconds ran out!")
                self.process = False

    def timenow(self):
        return(self.stopper//1000)







timer1 = Timer()


########
timer1.start(inf)   #вместо inf впишите количество секунд

FPS = 1
########



while 1:        
    timer1.mainflow()
    clock.tick(FPS)

    #print(timer1.timenow())
    








































