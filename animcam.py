from manim import *

class animcam(Scene):
    def construct(self):
        self.camera.background_colo=LOGO_WHITE
        m1=Square().move_to([2,0,0])
        m2=Circle().move_to([-2,0,0])
        
        self.play(Create(m1),Create(m2),run_time=5)
        self.wait(1)
        self.play(m1.animate.set_fill(PINK,opacity=0.5))
        self.wait(1)
        self.play(m2.animate.set_fill(LOGO_BLUE,opacity=1))
        
        self.wait(1)
        
        self.camera.background_color=LOGO_BLACK
        
        self.play(Transform(m1,m2))
        self.wait(3)

        
        c1=Circle(radius=0.2,color=WHITE).move_to([-2.5,0.3,0])
        c2=Circle(radius=0.2,color=WHITE).move_to([-1.5,0.3,0])
        c11=Circle(radius=0.04,color=BLUE,fill_opacity=1).move_to([-2.5,0.3,0])
        c12=Circle(radius=0.04,color=BLUE,fill_opacity=1).move_to([-1.5,0.3,0])
        re=Rectangle(height=0.2,width=0.4).move_to([-2,-0.5,0])
        tri= Triangle(radius=0.1,color=RED).move_to([-2,0,0])
        

        self.play(Create(c1),Create(c2),Create(c11),Create(c12),Create(re),
                    Create(tri),run_time=10)        

        self.play(FadeOut(m1),FadeOut(c1),FadeOut(c2),FadeOut(re),FadeOut(c11),
                    FadeOut(c12),FadeOut(tri))