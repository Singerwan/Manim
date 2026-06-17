from manim import *
import numpy as np
import sympy 


class warpsquare(Scene):
    def construct(self):
        square=Square()
        self.play(Create(square),run_time=1)
        self.play(square.animate.set_fill(color=RED,opacity=1),run_time=2)
        self.play(ApplyPointwiseFunction (lambda point:complex_to_R3(np.exp(R3_to_complex(point))), square, run_time=5))

        square1=Square().move_to([-2,0,0])
        self.play(Create(square1),run_time=1)
        self.play(square1.animate.set_fill(color=BLUE,opacity=1),run_time=2)
        self.play(ApplyPointwiseFunction (lambda point:complex_to_R3(np.exp(R3_to_complex(point))), square1, run_time=5))

        square2=Square().move_to([0,2,0])
        self.play(Create(square2),run_time=1)
        self.play(square2.animate.set_fill(color=YELLOW,opacity=1),run_time=2)
        self.play(ApplyPointwiseFunction (lambda point:complex_to_R3(np.exp(R3_to_complex(point))), square2, run_time=5))
        
        square3=Square().move_to([0,-2,0])
        self.play(Create(square3),run_time=1)
        self.play(square3.animate.set_fill(color=GREEN,opacity=1),run_time=2)
        self.play(ApplyPointwiseFunction (lambda point:complex_to_R3(np.exp(R3_to_complex(point))), square3, run_time=5))

        self.play(FadeOut(square),FadeOut(square1),FadeOut(square2),FadeOut(square3))