from manim import *

class unionobj(Scene):
    def construct(self):
        square=Square(color=RED_A, fill_opacity=1).move_to([-2,0,0])
        self.play(FadeIn(square),run_time=2)
        circle=Circle(color=BLUE_D,fill_opacity=1).move_to([-1.3,0.7,0])
        self.play(FadeIn(circle),run_time=2)
        un=Union(square,circle).move_to([1.5,0.3,0])
        self.play(FadeIn(un),run_time=2)
        self.play(un.animate.set_fill(color=LOGO_WHITE,opacity=0.5),run_time=3)
        text=Tex("Singer Wan's rendering of Union",color=PURE_GREEN).shift(UP*3)
        self.add(square,circle,un)
        self.play(Write(text),color=PURE_GREEN,run_time=6)
        self.play(FadeOut(square),FadeOut(circle),FadeOut(text))
