from manim import *

class tsqr2cir(Scene):
    def construct(self):
        circle = Circle(color=RED,fill_opacity=1).shift(LEFT*2)
        square = Square(color=WHITE,fill_opacity=1).shift(RIGHT*2)
        square.rotate(PI/4)
        
        self.play(Create(circle,run_time=3))
        self.play(Create(square,run_time=3))
        self.wait(1)
        self.play(FadeIn(circle,run_time=3))
        self.play(FadeIn(square,run_time=3))
        self.wait(1)
        self.wait(1)
        self.play(Transform(circle, square))  
        self.play(FadeOut(square),run_time=3)

