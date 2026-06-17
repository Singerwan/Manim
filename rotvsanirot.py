from manim import *

class RotVsAniRot(Scene):
    def construct(self):
        left_square = Square(color=RED, fill_opacity=0.5).shift(LEFT*2)
        right_square = Square(color=BLUE, fill_opacity=0.5).shift(RIGHT*2)
        self.play(Create(left_square))
        self.play(Create(right_square))
        self.wait(1)

        self.play(Rotate(left_square, angle=PI/4),right_square.animate.rotate(-PI/4),run_time=8)
        self.play(Rotate(left_square, angle=PI/4,run_time=2))
        self.play(right_square.animate.rotate(-PI/4),run_time=2)
        self.wait()