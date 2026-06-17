from manim import *

class animcoor(Scene):
    def construct(self):
        p1 = [-1,-1, 0]
        p2 = [ 1,-1, 0]
        p3 = [ 1, 1, 0]
        p4 = [-1, 1, 0]
        a  = Line(p1,p2).append_points(Line(p2,p3).points).append_points(Line(p3,p4).points)
        point_start  = a.get_start()
        point_end    = a.get_end()
        point_center = a.get_center()
        
        self.add(Text(f"a.get_start() = {np.round(point_start,2).tolist()}", 
                        font_size=24).to_edge(UR).set_color(YELLOW))
        self.add(Text(f"a.get_end() = {np.round(point_end,2).tolist()}",
                        font_size=24).next_to(self.mobjects[-1],DOWN).set_color(RED))
        self.add(Text(f"a.get_center() = {np.round(point_center,2).tolist()}", 
                        font_size=24).next_to(self.mobjects[-1],DOWN).set_color(BLUE))

        sdos=VGroup(*[Dot(x) for x in a.points])
        dot1=Dot(a.get_start()).set_color(YELLOW).scale(2)
        dot2=Dot(a.get_end()).set_color(RED).scale(2)
        dot3=Dot(a.get_top()).set_color(GREEN_A).scale(2)
        dot4=Dot(a.get_bottom()).set_color(GREEN_D).scale(2)
        dot5=Dot(a.get_center()).set_color(BLUE).scale(2)
        dot6=Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2)
        
        self.play(Create(sdos),run_time=10)
        self.play(sdos.animate.set_fill(LOGO_GREEN,opacity=1),run_time=5)
        self.play(Create(dot1),Create(dot2), Create(dot3), Create(dot4), Create(dot5), Create(dot6), run_time=10)
        self.play(Create(a), run_time=5)        

