from manim import *

class textgradient(Scene):
    def construct(self):
        t1=Text("Hello",font="Cooper", gradient=(RED,BLUE,GREEN),font_size=96).move_to(LEFT*2)
        t2=Text("World",
                font="Cooper",
                gradient=(YELLOW,WHITE,BLUE),font_size=96).move_to(RIGHT*3)
        t3=Text("Hello World",font="GothicE",font_size=96,
                gradient=(RED,BLUE,GREEN,TEAL,YELLOW,PINK,MAROON,WHITE)).move_to(DOWN*2)
        t4=Text("Hello World",font="Jokerman",font_size=96,
                gradient=(RED,BLUE,GREEN,TEAL,YELLOW,PINK,MAROON,WHITE)).move_to(UP*2)
        self.play(Write(t1),run_time=5)
        self.play(Write(t2),run_time=5)
        self.play(Write(t3),run_time=10)
        self.play(Write(t4),run_time=10)