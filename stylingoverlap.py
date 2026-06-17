from manim import *

class styleoverlap(Scene):
    def construct(self):
        cir=Circle().shift(LEFT)
        sqr=Square().shift(UP)
        tri=Triangle().shift(RIGHT)
        
    
        cir.set_stroke(color=GREEN,width=20)
        sqr.set_fill(YELLOW,opacity=0.5)
        tri.set_fill(PINK,opacity=0.5)


        self.add(cir, sqr ,tri) 