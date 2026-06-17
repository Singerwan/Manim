from manim import *

class beziercurve(Scene):
    def construct(self):
        plane = NumberPlane(background_line_style={
                "stroke_color": GOLD_E,
                "stroke_width": 1,
                "stroke_opacity": 0.2
            })
        self.play(Create(plane),run_time=3)
        
        my_vmobject = VMobject(color=GREEN)
        my_vmobject.points = [
        
            np.array([-2, -1, 0]),  # ||||start of first curve
            np.array([-3, 1, 0]),   # ---first curve's first handle
            np.array([0, 3, 0]),    # ---first curve's second handle
            np.array([1, 3, 0]),    # ||||end of first curve
            np.array([1, 3, 0]),    # >>>>start of second curve
            np.array([0, 1, 0]),    # ---second curve's first handle
            np.array([4, 3, 0]),    # ---second curve's second handle
            np.array([4, -2, 0]) ]  # >>>> end of second curve
        
        Tex11h=Text("1st Curve's 1st handle",color=RED).scale(0.4).move_to([-3, 1.3, 0])
        Tex12h=Text("1st Curve's 2nd handle",color=YELLOW).scale(0.4).move_to([0, 3.3, 0])        
        Tex21h=Text("2nd Curve's 1st handle",color=GREEN).scale(0.4).move_to([0, 1.3, 0])
        Tex22h=Text("2nd Curve's 2nd handle",color=WHITE).scale(0.4).move_to([4, 3.3, 0])        
        
        self.play(Create(Tex11h),run_time=3)    
        self.play(Create(Tex12h),run_time=3)
        self.play(Create(Tex21h),run_time=3)    
        self.play(Create(Tex22h),run_time=3)   
        
        handles = [
            Dot(point, color=RED) for point in
            [[-3, 1, 0], [0, 3, 0], [0, 1, 0], [4, 3, 0]]
        ]
        
        handleall=VGroup(*handles)
        self.play(Create(handleall),run_time=4)
        
        dot11=Dot()
        dot12=Dot()
        dot21=Dot()
        dot22=Dot()
        
        self.play(dot11.animate.set_fill(RED,opacity=1).move_to([-3, 1, 0]),run_time=3)
        self.play(dot12.animate.set_fill(YELLOW,opacity=1).move_to([0, 3, 0]),run_time=3)        
        self.play(dot21.animate.set_fill(GREEN,opacity=1).move_to([0, 1, 0]),run_time=3)
        self.play(dot22.animate.set_fill(WHITE,opacity=1).move_to([4, 3, 0]),run_time=3)    
                
        handle_lines = [
            Line(
                my_vmobject.points[ind],
                my_vmobject.points[ind+1],
                color=RED,
                stroke_width=2
            ) for ind in range(0, len(my_vmobject.points), 2)
        ]
        
        handle_linesall=VGroup(*handle_lines)
        self.play(Create(handle_linesall),run_time=5)
        self.add(my_vmobject)
        self.wait(4)