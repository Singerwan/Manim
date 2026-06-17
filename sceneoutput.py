from manim import *

class squaretocircle(Scene):
    def construct(self):
        circle=Circle().move_to([-2,0,0])
        circle.set_fill(PURE_GREEN,opacity=0.5)
        
        square=Square(color=RED,fill_opacity=0.4).move_to([2,0,0])
        
        trg=Triangle(color=YELLOW,fill_opacity=0.5).move_to([0,-2,0])
        
        star=Star(color=LOGO_WHITE,fill_opacity=0.5).move_to([0,2,0])
        
        self.play(FadeIn(square), FadeIn(trg) , FadeIn(star),run_time=5 )     
        self.play(Create(circle))
        self.play(circle.animate.set_fill(BLACK,opacity=1))
        self.play(Transform(square,circle),Transform(trg,circle),Transform(star,circle),run_time=10)