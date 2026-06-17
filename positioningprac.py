from manim import *

class pospra(Scene):
    def construct(self):
        sqr=Square(color=RED,fill_opacity=0).move_to([0,0,0])
        cir=Circle(color=BLUE, fill_opacity=0).move_to([-1,0,0])
        ci1=Circle(color=BLUE, fill_opacity=0).move_to([1,0,0])
        sta=Star(color=LOGO_WHITE, fill_opacity=0).move_to([0,-0.6,0])
        st1=Star(color=RED_A, fill_opacity=0).move_to([0,0.6,0])
        ci2=Circle(radius=0.2, color=RED).move_to([4,0,0])
        ci3=Circle(radius=0.2, color=RED).move_to([6,0,0])
                
        un=Union(sqr,cir,ci1,sta,st1, color=LOGO_WHITE, fill_opacity=0.1).move_to([5,0,0])

        self.play(Create(sqr))
        self.play(Create(cir))      
        self.play(Create(ci1))
        self.play(Create(sta),run_time=4)
        self.play(Create(st1),run_time=4)
        self.play(un.animate.rotate(PI),run_time=10)
        self.play(FadeIn(ci2),FadeIn(ci3))
        self.play(FadeOut(sqr)  ,FadeOut(cir)  ,FadeOut(ci1) ,FadeOut(sta),FadeOut(st1))
        self.play(un.animate.move_to([0,0,0]),ci2.animate.move_to([-1,0,0]),ci3.animate.move_to([1,0,0]),run_time=5)
        self.wait()
