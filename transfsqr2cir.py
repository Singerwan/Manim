from manim import *

class TransfSqr2Cir(Scene):
    def construct(self):
        square = Square(color=BLUE, fill_opacity=0.5)
        circle = Circle(color=WHITE, fill_opacity=0.5)
        
        self.play(Create(square))
        self.wait(1)
        self.play(Transform(square, circle))
        self.wait(1)