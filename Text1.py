from manim import *

class text1(Scene):
    def construct(self):
        text1=Text("Hello World",font_size=144,color=LOGO_RED)
        self.play(Write(text1),run_time=3)
        self.play(text1.animate.set_fill(LOGO_GREEN,opacity=0.5),run_time=3)
        self.wait(3)
    