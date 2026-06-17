from manim import *

class animationbasic(Scene):
    def construct(self):
        squ=Square().move_to([0,0,0])
        cir=Circle(color=GREEN,fill_opacity=0.5).move_to([2,0.5,0])
        sta=Star(color=YELLOW,fill_opacity=1).move_to([1,-0.5,0])
        
        self.play(Create(squ),run_time=3)
        self.play(squ.animate.set_fill(RED,opacity=0.5),run_time=3)
        self.play(squ.animate.rotate(PI/3),run_time=6)
        self.play(squ.animate.set_fill(LOGO_WHITE,opacity=0.4),run_time=3)
        self.play(ReplacementTransform(squ,cir),run_time=5)
        self.play(ReplacementTransform(cir,sta),run_time=5)
        
        self.play(ApplyPointwiseFunction (  lambda point : complex_to_R3(  np.exp(R3_to_complex( point ))), 
        sta, run_time=5))

        self.play(FadeOut(sta))
        
        un=Union(squ,cir,sta,squ).move_to([0,0,0])
        grid=NumberPlane()
        cir21=Circle(radius=0.1,color=LOGO_WHITE).move_to([-2,0.8,0])

        self.play(Create(un),Create(cir21),run_time=15)
        self.wait(5)
