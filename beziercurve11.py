from manim import *

class beziercurve11(Scene):
    def construct(self):
        plane = NumberPlane(background_line_style={
                "stroke_color": BLACK,
                "stroke_width": 4,
                "stroke_opacity": 0.5
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
        
        my_vmobject2 = VMobject(color=RED)
        my_vmobject2.points = [
        
            np.array([-1.5, -0.5, 0]),  # ||||start of first curve
            np.array([-2.5, 0.5, 0]),   # ---first curve's first handle
            np.array([0, 2.5, 0]),    # ---first curve's second handle
            np.array([0.5, 2.5, 0]),    # ||||end of first curve
            np.array([0.5, 2.5, 0]),    # >>>>start of second curve
            np.array([0, 0.5, 0]),    # ---second curve's first handle
            np.array([3.5, 2.5, 0]),    # ---second curve's second handle
            np.array([3.5, -1.5, 0]) ]  # >>>> end of second curve
        
        self.add(my_vmobject2)        
        
        line1 = Line(start=np.array([-2, -1, 0]), end=np.array([-1.5, -0.5, 0]) ,path_arc=PI,color=YELLOW)
        line2 = Line(start=np.array([4, -2, 0]), end=np.array([3.5, -1.5, 0]), path_arc=PI,color=YELLOW)
        
        self.play(Create(line1),  Create(line2), run_time=3  )
        
        eye1=Dot(color=WHITE).move_to([-0.5,0.5,0])
        eye2=Dot(color=WHITE).move_to([1.5,0.5,0])
        
        brw1=Line(start=np.array([-1, 0.8, 0]), end=np.array([0, 0.8, 0]) ,path_arc=PI/2,color=RED)
        brw2=Line(start=np.array([1, 0.8, 0]), end=np.array([2, 0.8, 0]) ,path_arc=PI/2,color=RED)

        mouth=Line(start=np.array([0, -1.4, 0]), end=np.array([1, -1.4, 0]) ,path_arc=PI/2,color=PINK)

        tri=Triangle(color=TEAL,fill_opacity=1).scale(0.3).move_to([0.5,-0.6,0])
        
        
        self.play(brw1.animate.rotate(PI))
        self.play(brw2.animate.rotate(PI))
        self.play(mouth.animate.rotate(PI))      

        self.play(FadeOut(plane))       
        self.play(Create(eye1),Create(eye2),Create(tri),run_time=5)
        
        self.play(FadeOut(handle_linesall),  FadeOut(Tex11h),FadeOut(Tex12h),FadeOut(Tex21h),FadeOut(Tex22h),run_time=6)
        self.play(FadeOut(handleall),run_time=2)
        self.play(FadeOut(dot11),FadeOut(dot12),FadeOut(dot21),FadeOut(dot22),run_time=3)
        
        self.wait(5)