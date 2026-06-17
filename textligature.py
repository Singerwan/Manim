from manim import *

class textligature(Scene):
    def construct(self):
        fl1=Text("fl ligature",color=RED,font_size=96)
        fl2=Text("fl ligature",color=GREEN,disable_ligatures=True,font_size=96)
        
        go2= Group(fl1,fl2).arrange(DOWN,buff=0.8)
        self.play(FadeIn(go2),run_time=10)
        