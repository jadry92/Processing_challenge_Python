class Julia():
    def __init__(self,n_ite):
        self.pos = [PVector(0,0)]
        self.ite = n_ite
        
    #metho to draw the rectangles
    def show(self):
        for i in range(0,len(self.pos)):
            col =sqrt( (self.pos[i].x*self.pos[i].x) + (self.pos[i].y*self.pos[i].y))
            col = map(col, 0, 2, 0, 225)
            fill(col,col+20,col-20)
            rect(self.pos[i].x,self.pos[i].y,1,1)

       
        

    # metho to generate the poins can be in the fractal
    def generate(self):
        i = 0
        for ix in range(-width/2, width/2):
            for iy in range(-height/2, height/2):
                ix_m = map(ix,-width/2, width/2,-2,2)
                iy_m = map(iy,-height/2, height/2,-2,2)
                nom = 0 
                it = 0
                nom = self.re_julia(ix_m,iy_m,it)
                if nom <= 2:
                    self.pos[i].x = ix
                    self.pos[i].y = iy
                    i += 1
                    self.pos.insert(i,PVector(0,0))
                        
    def re_julia(self,ix_m,iy_m,it):
        real_f = pow(ix_m,2)-pow(iy_m,2)+0.01
        imag_f = 2*ix_m*iy_m + 0.5589
        it += 1
        if self.ite < it:
            return sqrt((real_f*real_f) + (imag_f*imag_f))
        else:    
            return self.re_julia(real_f,imag_f,it)  
        
class Julia_or3():
    def __init__(self,n_ite):
        self.pos = [PVector(0,0)]
        self.ite = n_ite
        
    #metho to draw the rectangles
    def show(self):
        for i in range(0,len(self.pos)):
            rect(self.pos[i].x,self.pos[i].y,1,1)
        

    # metho to generate the poins can be in the fractal
    def generate(self):
        i = 0
        for ix in range(-width/2, width/2):
            for iy in range(-height/2, height/2):
                ix_m = map(ix,-width/2, width/2,-2,2)
                iy_m = map(iy,-height/2, height/2,-2,2)
                nom = 0 
                it = 0
                nom = self.re_julia(ix_m,iy_m,it)
                if nom <= 2:
                    self.pos[i].x = ix
                    self.pos[i].y = iy
                    i += 1
                    self.pos.insert(i,PVector(0,0))
                        
    def re_julia(self,ix_m,iy_m,it):
        real_f = pow(ix_m,3) - 3*ix_m*pow(iy_m,2) - 0.5
        imag_f = 2*pow(ix_m,2)*iy_m + 2*pow(iy_m,2)*ix_m
        it += 1
        if self.ite < it:
            return sqrt((real_f*real_f) + (imag_f*imag_f))
        else:    
            return self.re_julia(real_f,imag_f,it)                                 
                