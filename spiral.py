from manim import *

class spiral(Scene):
    def construct(self):
        iterations=16
        
        angles=[np.arctan(1/np.sqrt(i)) if i > 0 else 0 for i in range(iterations)]

        tr_grp= VGroup(*[Polygon(ORIGIN,
                                    RIGHT*np.sqrt(i),
                                    RIGHT*np.sqrt(i)+UP,
                                    stroke_width=0.3,
                                    fill_opacity=1).rotate(sum(angles[:i]),
                                    about_point=ORIGIN).set_z_index(i+1) for i in range(1,
                                            iterations+1)]).set_color_by_gradient(LOGO_WHITE	
                                                        ,PURE_RED,PURE_GREEN)
        
        self.add(tr_grp[0])
        self.wait()
        
        for i in range(iterations-1):
            self.play(ReplacementTransform(tr_grp[i].copy().set_z_index(i+3), 
                        tr_grp[i+1],path_arc=angles[i+1]))
        
        self.wait()