from manim import *

class onepy(Scene):
    def construct(self):
        
        tx1=Text("AMGDT",font='AMGDT',color=LOGO_WHITE).scale(0.25).move_to([-6.5,3,0])
        tx2=Text("Vivaldi",font='Vivaldi',color=LOGO_WHITE).scale(0.25).move_to([-5.5,3,0])
        self.play(Write(tx1),Write(tx2),run_time=3) 
        
        