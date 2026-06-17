from manim import *

class linspacing(Scene):
    def construct(self):
        
        t1=Text("Hello\nWorld",line_spacing=1,color=PURE_RED)
        t2=Text("Hello\nWorld",line_spacing=5)
        self.play(Write(t1),run_time=5)
        an1=Text("Line_space=1",color=PURE_RED).move_to(UP*3).scale(0.6)
        self.add(an1)
        self.wait(3)
        self.play(FadeOut(t1),FadeOut(an1))
        
        self.play(Write(t2),run_time=5)
        an2=Text("Line_space=5",color=WHITE).scale(0.6)
        self.add(an2)
        self.wait(3)
        self.play(FadeOut(t2),FadeOut(an2))    
        
        t12v=Group(t1,t2)
        self.play(FadeIn(t12v),run_time=5)    
        an3=Text("Group(t1,t2)",color=PURE_RED).move_to(RIGHT*4.5).scale(0.6)
        self.add(an3)
        self.wait(3)
        self.play(FadeOut(t12v),FadeOut(an3))
        
        t12h=Group(t1,t2)
        self.play(t12h.animate.arrange(LEFT,buff=5),run_time=5)   
        an4=Text("Group(t1,t2).arrange(LEF,buff=5)",color=PURE_RED).move_to(UP*3).scale(0.6)
        self.add(an4) 
        self.wait(3)
        self.play(FadeOut(t12h),FadeOut(an4))
        
