from manim import *

class styling(Scene):
    def construct(self):
        cir=Circle().shift(LEFT)
        sqr=Square().shift(UP)
        tri=Triangle().shift(RIGHT)
        
    
        cir.set_stroke(color=GREEN,width=20)
        sqr.set_fill(YELLOW,opacity=1)
        tri.set_fill(PINK,opacity=1)
        un=Union(cir , sqr ,  tri).move_to([4,0,0])


        self.play(Create(sqr))
        self.play(Create(tri))  
        self.play(Create(cir))  
        self.play(Create(un),run_time=6)    
        self.play(un.animate.set_fill(GREEN,opacity=0.6))
        self.wait(1)
        self.play(FadeOut(cir), FadeOut(sqr), FadeOut(tri) )