from manim import *

class beziercurvepic1(Scene):
    def construct(self):
        plane = NumberPlane(background_line_style={
                "stroke_color": GOLD_E,
                "stroke_width": 5,
                "stroke_opacity": 0.2})
        
        
        my_vmobject1 = VMobject(color=GREEN)
        my_vmobject1.points = [
        
            np.array([-2, -1, 0]),  # ||||start of first curve
            np.array([-3, 1, 0]),   # ---first curve's first handle
            np.array([0, 3, 0]),    # ---first curve's second handle
            np.array([1, 3, 0]),    # ||||end of first curve
            np.array([1, 3, 0]),    # >>>>start of second curve
            np.array([0, 1, 0]),    # ---second curve's first handle
            np.array([4, 3, 0]),    # ---second curve's second handle
            np.array([4, -2, 0]) ]  # >>>> end of second curve
    
    
            
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
        
        line1 = Line(start=np.array([-2, -1, 0]), end=np.array([-1.5, -0.5, 0]) ,path_arc=PI,color=YELLOW)
        line2 = Line(start=np.array([4, -2, 0]), end=np.array([3.5, -1.5, 0]), path_arc=PI,color=YELLOW)
        
        eye1=Dot(color=WHITE).move_to([-0.5,0.5,0])
        eye2=Dot(color=WHITE).move_to([1.5,0.5,0])
        
        brw1=Line(start=np.array([-1, 0.8, 0]), end=np.array([0, 0.8, 0]) ,path_arc=PI/2,color=RED)
        brw2=Line(start=np.array([1, 0.8, 0]), end=np.array([2, 0.8, 0]) ,path_arc=PI/2,color=RED)

        brw3=Line(start=np.array([0, -1.4, 0]), end=np.array([1, -1.4, 0]) ,path_arc=PI/2,color=PINK)

        tri=Triangle().scale(0.3).move_to([0.5,-0.6,0])
        self.add(plane,my_vmobject1,my_vmobject2,line1,line2,eye1,eye2,brw1,brw2,brw3,tri)