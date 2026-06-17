from manim import *
class section(Scene):
    def construct(self):
        self.next_section()
        func=lambda pos: np.sin(pos[0] /2 ) *UR + np.cos(pos[1] /2 ) * LEFT
        
        stream_lines=StreamLines(func,  stroke_width=1.5 , max_anchors_per_line=30)
        
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False , flow_speed=0.5, time_width=0.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed + 10)
        
        
        self.next_section()
        circle=Circle().move_to([-2,0,0])
        circle.set_fill(PURE_GREEN,opacity=0.5)
        
        square=Square(color=RED,fill_opacity=0.4).move_to([2,0,0])
        
        trg=Triangle(color=YELLOW,fill_opacity=0.5).move_to([0,-2,0])
        
        star=Star(color=LOGO_WHITE,fill_opacity=0.5).move_to([0,2,0])
        
        self.play(FadeIn(square), FadeIn(trg) , FadeIn(star),run_time=5 )     
        self.play(Create(circle))
        self.play(circle.animate.set_fill(BLACK,opacity=1))
        self.play(Transform(square,circle),Transform(trg,circle),Transform(star,circle),run_time=10)