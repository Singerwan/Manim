from manim import *

class animcsw(Scene):
    def construct(self):
        p1 = [-1,-1, 0]
        p2 = [ 1,-1, 0]
        p3 = [ 1, 1, 0]
        p4 = [-1, 1, 0]


        tex1=(Text("P1P2",color=PURE_RED)).scale(0.5).move_to( [-0.5,-1.5, 0])
        adot    = Line(p1,p2,color=PURE_RED).append_points(Line(p1,p2,color=PURE_RED).points)  
        ados    = VGroup(*[Dot(x) for x in adot.points]).set_fill(PURE_RED, opacity=1)        

        tex2=(Text("P2P3",color=PURE_GREEN)).scale(0.5).move_to([ 2,0, 0])        
        bdot    = Line(p2,p3,color=PURE_GREEN).append_points(Line(p2,p3,color=PURE_GREEN).points)  
        bdos    = VGroup(*[Dot(x) for x in bdot.points]).set_fill(PURE_GREEN, opacity=1)
        
        tex3=(Text("P3P4",color=PURE_BLUE)).scale(0.5).move_to([-0.5, 1.5, 0])        
        cdot    = Line(p3,p4,color=PURE_BLUE).append_points(Line(p3,p4,color=PURE_BLUE).points)  
        cdos    = VGroup(*[Dot(x) for x in cdot.points]).set_fill(PURE_BLUE, opacity=1)                


        self.play(Create(ados),run_time=5)
        self.play(Create(adot),run_time=2)        

        self.play(Create(bdos),run_time=5)
        self.play(Create(bdot),run_time=2)        
        
        self.play(Create(cdos),run_time=5)
        self.play(Create(cdot),run_time=2)        
        
        self.wait(3)
        
        
        
        tex1=(Text("P1P2",color=PURE_RED)).move_to( [-0.5,-1.5, 0])
        tex2=(Text("P2P3",color=PURE_GREEN)).move_to([ 2,0, 0])        
        tex3=(Text("P3P4",color=PURE_BLUE)).move_to([-0.5, 1.5, 0])        
        
        self.play(Write(tex1) ,  Write(tex2) , Write(tex3), run_time=5 )        
        
        a  = Line(p1,p2).append_points(Line(p2,p3).points).append_points(Line(p3,p4).points)
        point_start  = a.get_start()
        point_end    = a.get_end()
        point_center = a.get_center()
        
        dot1=Dot(a.get_start()).set_color(YELLOW).scale(2)
        dot2=Dot(a.get_end()).set_color(RED).scale(2)
        dot3=Dot(a.get_top()).set_color(GREEN_A).scale(2)
        dot4=Dot(a.get_bottom()).set_color(GREEN_D).scale(2)
        dot5=Dot(a.get_center()).set_color(BLUE).scale(2)
        dot6=Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2)
        
        
        dot1t=(Text("dot1",color=YELLOW)).scale(0.3).next_to(dot1,UP*0.65)
        self.wait(2)
        self.add(dot1,dot1t)
        
        dot2t=(Text("dot2",color=RED)).scale(0.3).next_to(dot2,DOWN*0.65)
        self.wait(2)
        self.add(dot2,dot2t)
        
        dot3t=(Text("dot3",color=GREEN_A)).scale(0.3).next_to(dot3,DOWN*0.65)        
        self.wait(2)
        self.add(dot3,dot3t)

        dot4t=(Text("dot4",color=GREEN_D)).scale(0.3).next_to(dot4,UP*0.65)  
        self.wait(2)
        self.add(dot4,dot4t)

        dot5t=(Text("dot5",color=BLUE)).scale(0.3).next_to(dot5,LEFT*0.65)
        self.wait(2)
        self.add(dot5,dot5t)
        
        dot6t=(Text("dot6",color=ORANGE)).scale(0.3).next_to(dot6,LEFT*0.65)
        self.wait(2)
        self.add(dot6,dot6t)
        self.wait(2)
        
        tex11=(Text("Singer Wan's Rendering of",color=PURE_GREEN)).move_to([0,2.5,0])
        tex21=(Text("Animated Coordinates",color=PURE_GREEN)).move_to([0,-2.5,0])
        self.play(Write(tex11),Write(tex21),run_time=15)
        self.wait(2)