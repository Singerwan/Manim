from manim import *

class transfrepl(Scene):
    def construct(self):
        a=Tex("a",color=RED,font_size=100).shift(LEFT)
        b=Tex("b",color=GREEN,font_size=100).shift(RIGHT)
        c=Tex("c",color=BLUE,font_size=100).shift(UP)
        self.play(Write(a),Write(b),Write(c))
        self.wait(2)
        self.play(Transform(a,b))
        self.wait(2)
        self.play(FadeOut(a))    
        self.wait(2)    
        arrow=Arrow(start=LEFT,end=RIGHT,color=YELLOW).shift(DOWN)  
        self.play(arrow.animate.next_to(b,LEFT,buff=0))
        self.play(ReplacementTransform(a,c))
        self.wait(2)     
        self.play(FadeOut(c))