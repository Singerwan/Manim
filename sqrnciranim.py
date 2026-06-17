from manim import *
class sqrnciranim(Scene):
    def construct(self):
        circle = Circle(radius=1, color=GREEN_A,fill_opacity=0.8)
        square = Square(side_length=2, color=RED,fill_opacity=0.8)
        
        self.play(Create(circle),RUN_TIME=2)
        self.wait(2)        
        self.play(Create(square),RUN_TIME=2)
        self.wait(2)
        self.play(square.animate.next_to(circle,RIGHT, buff=1.5),RUN_TIME=2)
        self.wait(2)        
        self.play(square.animate.set_fill(color=YELLOW_A, opacity=0.5),RUN_TIME=2)
        self.play(square.animate.rotate(PI/2),RUN_TIME=5)
        self.wait(2)
        self.play(square.animate.next_to(circle,RIGHT, buff=0.5),RUN_TIME=2)
        self.play(Transform(square, circle),RUN_TIME=2)
        self.wait(2)