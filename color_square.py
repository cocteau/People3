from time import sleep

class color_square(object):
    
    def __init__(self,source,x,y,w,h,i,j):
        
        self.source = source
        
        self.angle = PI
        self.target_angle = 2.0*PI
        
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.i = i
        self.j = j
        
        self.threshold1 = noise(i*1,j*1)
        self.threshold2 = noise(i*1+1000,j*1+1000)
        self.threshold3 = noise(i*1+5000,j*1+5000)
        self.threshold4 = noise(i*1+10000,j*1+10000)
        self.active = 0
        
        self.img = loadImage(self.source)
        
    def update(self,val):

        if self.active==0 and val > self.threshold1: 
            self.active = 1
            self.angle = PI
            self.target_angle = 2.0*PI
            
        if self.active==1 and val > self.threshold2+1:
            self.active = 2
            self.angle = PI
            self.target_angle = 2*PI
            
        if self.active==2 and val > self.threshold3+2:
            self.active = 3
            self.angle = PI
            self.target_angle = 2*PI
            
        if self.active==3 and val > self.threshold4+3:
            self.active = 4
            self.angle = PI
            self.target_angle = 2*PI
            
        if val!=0 and val!=1 and val!=2:
            self.angle = lerp(self.angle,self.target_angle,0.05)
        
    def render(self,i,j,c):

        if self.active == 1:
            
            pushMatrix()
            translate(90-width/2.0+i*(self.w+30)+30+self.w/2.0, 140-height/2.0+30+j*(self.h+30))
            rotateY(self.angle)
    
            fill(c)  
            strokeWeight(0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
            rect(-self.w/2.0,0,self.w,self.h)            
            
            rotateY(PI)
            translate(0,0,1)
        
            fill(51)  
            strokeWeight(0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
            rect(-self.w/2.0,0,self.w,self.h)
                                
            popMatrix()
            
        if self.active == 2:
            
            pushMatrix()
            translate(90-width/2.0+i*(self.w+30)+30+self.w/2.0, 140-height/2.0+30+j*(self.h+30))
            rotateY(self.angle)
            
            tint(unhex("ff"+c[1:]))
            image(self.img,-self.w/2.0,0,self.w,self.h)
            rotateY(PI)
            translate(0,0,1)
        
            fill(c)  
            strokeWeight(0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
            rect(-self.w/2.0,0,self.w,self.h)
                                
            popMatrix()
            
        if self.active == 3:
            
            pushMatrix()
            translate(90-width/2.0+i*(self.w+30)+30+self.w/2.0, 140-height/2.0+30+j*(self.h+30))
            rotateY(self.angle)
    
            fill(c)  
            strokeWeight(0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
            rect(-self.w/2.0,0,self.w,self.h)
            
            rotateY(PI)
            translate(0,0,1)
            tint(unhex("ff"+c[1:]))
            image(self.img,-self.w/2.0,0,self.w,self.h)
            
            popMatrix()
            
        if self.active == 4:
            
            pushMatrix()
            translate(90-width/2.0+i*(self.w+30)+30+self.w/2.0, 140-height/2.0+30+j*(self.h+30))
            rotateY(self.angle)
    
            fill(51)  
            strokeWeight(0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
            rect(-self.w/2.0,0,self.w,self.h)
            
            rotateY(PI)
            translate(0,0,1)
        
            fill(c)  
            strokeWeight(0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
            rect(-self.w/2.0,0,self.w,self.h)

            popMatrix()