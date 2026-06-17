from manim import *

class toyexmapletempfig(Scene):
    def construct(self):
        orange_square=Square(color=ORANGE,fill_opacity=0.5)
        blue_circle  =Circle(color=BLUE,  fill_opacity=1)
        
        self.add(orange_square)
        self.add(blue_circle)
        
        small_dot    =Dot()
        small_dot.add_updater(lambda mob: mob.next_to(blue_circle,DOWN))
        
        self.play(Create(small_dot))
        self.play(blue_circle.animate.shift(RIGHT*3),run_time=3)
        
        self.wait()
        self.play(blue_circle.animate.shift(LEFT*3),run_time=3)
        self.play(ReplacementTransform(orange_square,blue_circle),run_time=5)

        self.wait()
        
        tx=Text("Singer Wan's Rendering of Thematic Guides",color=LOGO_WHITE).shift(UP*2)
        
        self.play(Write(tx),run_time=5)
        
        self.play(FadeOut(blue_circle, small_dot,tx))
        
        self.wait()

with tempconfig({"quality":"fourk_quality","preview":True}):
    Scene=toyexmapletempfig()
    Scene.render()