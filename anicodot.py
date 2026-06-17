from manim import *

class anicodot(Scene):
    def construct(self):
        p1 = [-1,-1, 0]
        p2 = [ 1,-1, 0]
        p3 = [ 1, 1, 0]
        p4 = [-1, 1, 0]
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
        
        
        dot1t=(Text("dot1",color=YELLOW)).scale(0.4).next_to(dot1,UP)
        self.wait(2)
        self.add(dot1,dot1t)
        
        dot2t=(Text("dot2",color=RED)).scale(0.4).next_to(dot2,UP)
        self.wait(2)
        self.add(dot2,dot2t)
        
        dot3t=(Text("dot3",color=GREEN_A)).scale(0.4).next_to(dot3,UP)        
        self.wait(2)
        self.add(dot3,dot3t)

        dot4t=(Text("dot4",color=GREEN_D)).scale(0.4).next_to(dot4,UP)  
        self.wait(2)
        self.add(dot4,dot4t)

        dot5t=(Text("dot5",color=BLUE)).scale(0.4).next_to(dot5,UP)
        self.wait(2)
        self.add(dot5,dot5t)
        
        dot6t=(Text("dot6",color=ORANGE)).scale(0.4).next_to(dot6,UP)
        self.wait(2)
        self.add(dot6,dot6t)
        self.wait(2)
