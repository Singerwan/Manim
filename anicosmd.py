from manim import *

class anicosmd(Scene):
    def construct(self):
        p1 = [-1,-1, 0]
        p2 = [ 1,-1, 0]
        p3 = [ 1, 1, 0]
        p4 = [-1, 1, 0]


        tex1=(Text("P1P2",color=PURE_RED)).move_to( [-0.5,-1.5, 0])
        adot    = Line(p1,p2,color=PURE_RED).append_points(Line(p1,p2,color=PURE_RED).points)  
        ados    = VGroup(*[Dot(x) for x in adot.points]).set_fill(PURE_RED, opacity=1)        
 
        tex2=(Text("P2P3",color=PURE_GREEN)).move_to([ 2,0, 0])        
        bdot    = Line(p2,p3,color=PURE_GREEN).append_points(Line(p2,p3,color=PURE_GREEN).points)  
        bdos    = VGroup(*[Dot(x) for x in bdot.points]).set_fill(PURE_GREEN, opacity=1)
        
        tex3=(Text("P3P4",color=PURE_BLUE)).move_to([-0.5, 1.5, 0])        
        cdot    = Line(p3,p4,color=PURE_BLUE).append_points(Line(p3,p4,color=PURE_BLUE).points)  
        cdos    = VGroup(*[Dot(x) for x in cdot.points]).set_fill(PURE_BLUE, opacity=1)                


        self.play(Create(ados),run_time=5)
        self.play(Create(adot),run_time=2)        

        self.play(Create(bdos),run_time=5)
        self.play(Create(bdot),run_time=2)        
        
        self.play(Create(cdos),run_time=5)
        self.play(Create(cdot),run_time=2)        
        
        self.wait(3)