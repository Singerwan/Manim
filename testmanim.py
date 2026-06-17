from manim import *
import numpy as np


class Square(Scene):
    def construct(self) -> None:
        sq=Square()
        self.play(Create(sq), run_time=1)

