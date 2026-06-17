from manim import *

class BezierSplineExample(Scene):
    def construct(self):
        p1 = np.array([-3, 1, 0])
        p1b = p1 + [1, 0, 0]
        d1 = Dot(point=p1).set_color(BLUE)
        
        l1 = Line(p1, p1b,color=BLUE,fill_opacity=0.6)
        
        p2 = np.array([3, -1, 0])
        p2b = p2 - [1, 0, 0]
        d2 = Dot(point=p2).set_color(RED)
        
        l2 = Line(p2, p2b,color=RED,fill_opacity=0.6)
        
        bezier = CubicBezier(p1b, p1b + 3 * RIGHT, p2b - 3 * RIGHT, p2b,color=GREEN)
        
        dot1=Dot(color=WHITE,fill_opacity=1).move_to([1,1,0])
        dot2=Dot(color=WHITE,fill_opacity=1).move_to([-1,-1,0])
                    
                    
        self.play(Create(dot1),Create(dot2),run_time=3)            

        self.play(Create(l1), run_time=1) 
        self.play(Create(d1), run_time=1) 
        self.play(Create(l2), run_time=1)     
        self.play(Create(d2), run_time=1) 
        self.wait(2)    
        self.play(Create(bezier), run_time=5)
        
        syntax1=Text("CubicBezier(start_anchor, start_handle,",color=GREEN).move_to([0,3,0])
        syntax2=Text("end_handle, end_anchor, **kwargs)",color=GREEN).move_to([0,2,0])
        self.play(Write(syntax1),run_time=2)
        self.play(Write(syntax2),run_time=2)
        self.wait(2)