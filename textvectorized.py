from manim import *

class textvectorized(Scene):
    def construct(self):
        text=Text("Colors",font_size=96).move_to(UP*1)
        tet1=Text("are bright",font_size=96).move_to(DOWN*1)        
        
        for letter in text:
            letter.set_color(random_bright_color())
            
        for letter in tet1:
            letter.set_color(random_color())
                        
        self.play(Write(text),run_time=10)
        self.play(Write(tet1),run_time=10)
        
        