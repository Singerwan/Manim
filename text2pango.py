from manim import *


class text2pango(Scene):
    def construct(self):
        text11=MarkupText(
                            f'all in red  <span fgcolor="{YELLOW}">except this</span>', 
                            color=RED  )
        self.play(Write(text11),run_time=3)
        self.wait(2)
        