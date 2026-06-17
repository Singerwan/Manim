from manim import *

class sqrncir(Scene):
    def construct(self):
        circle = Circle(radius=2, color=GREEN_A,fill_opacity=0.5)
        square = Square(side_length=4, color=RED,fill_opacity=0.5)
        
        self.play(Create(circle),RUN_TIME=2)
        self.play(Create(square),RUN_TIME=2)
        self.wait(2)
        self.play(square.animate.next_to(circle,RIGHT, buff=0.5),RUN_TIME=2)