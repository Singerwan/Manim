from manim import *
import numpy as np
import sympy 

class m(Scene):
    def construct(self):
        sq=Square()
        
        self.play(Create(sq))