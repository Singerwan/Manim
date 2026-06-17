from manim import *

class animcoor(Scene):
    def construct(self):
        p1 = [-1,-1, 0]
        p2 = [ 1,-1, 0]
        p3 = [ 1, 1, 0]
        p4 = [-1, 1, 0]
        
        tex1=(Text("P1P2",color=PURE_RED)).move_to( [-0.5,-1.5, 0])
        
        a  = Line(p1,p2,color=PURE_RED)
        tex2=(Text("P2P3",color=PURE_GREEN)).move_to([ 2,0, 0])        
        b  = Line(p2,p3,color=PURE_GREEN)
        tex3=(Text("P3P4",color=PURE_BLUE)).move_to([-0.5, 1.5, 0])        
        c  = Line(p3,p4,color=PURE_BLUE)
        
        self.add(a)
        
        self.wait(2)
        
        self.add(b)
        
        self.wait(2)
        
        self.add(c)
        
        self.wait(2)
        
        self.play(Write(tex1) ,  Write(tex2) , Write(tex3), run_time=5 )