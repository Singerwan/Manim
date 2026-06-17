from manim import *
import numpy as np 
class OpeningManim(Scene):
    def construct(self):
        title=Text("Singer Wan's Practice on Latex",color=PURE_GREEN).scale(0.75)
        basel=MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2}=\frac{\pi^{2}}{6}",color=LOGO_WHITE)
        VGroup(title,basel).arrange(DOWN)   # Syntax breakdown analysis : VGroup -vertical group of 2 object ,chained 
        # with arrange down means whatever object is being passed in at the last position will be located at the bottom
        # VGroup can also be used to concatenate two section of texts or individual object horizontally be specifying 
        # direction as RIGHT or LEFT . Therefore, the UP and DOWN direction arguments are associated with vertically alignment
        
        self.play(  Write(title),
                    FadeIn(basel,shift=DOWN),run_time=10)       
        
        self.play(FadeOut(title),FadeOut(basel))
        
        transform_title=Tex("That was a transform")
        transform_title.to_corner(UP+LEFT)
        self.play(  Transform(title,transform_title),
                    LaggedStart(*(FadeOut(obj, shift=DOWN) for obj in basel)))
        # LaggedStart 
        self.wait()
        
        grid=NumberPlane()
        grid_title=Tex("This is a grid",font_size=72,color=PURE_BLUE)
        grid_title.move_to(transform_title) #remove original object instead overlapping on top of it
        
        self.add(grid,grid_title) 
        # make sure title is on top of grid
        self.play(  FadeOut(title), FadeIn(grid_title, shift=UP),
                    Create(grid, run_time=3 ,lag_ratio=0.1))
        
        grid_transform_title= Tex(
            r"This was a non-linear function \\ applied to the grid ")
        grid_transform_title.move_to(grid_title,UL)
        grid.prepare_for_nonlinear_transform()
        self.play(grid.animate.apply_function(lambda p: p + np.array([     np.sin(p[1]),
                                                                            np.sin(p[0]),
                                                                            0             ])),run_time=3)
        self.wait()
        self.play(Transform(grid_title, grid_transform_title))
        self.wait()