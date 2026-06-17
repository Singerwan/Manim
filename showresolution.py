from manim import *

class ShowScreenResolution(Scene):
    def construct(self):
        pixel_height = config["pixel_height"]  #  1080 is default
        pixel_width = config["pixel_width"]    # 1920 is default
        frame_width = config["frame_width"]
        frame_height = config["frame_height"]
        
        d1 = Line(frame_width * LEFT / 2, frame_width * RIGHT / 2).to_edge(DOWN)
        self.add(d1)
        self.play(Text(str(pixel_width),color=PURE_RED).animate.move_to([0,2,0]).scale(0.8).next_to(d1,UP),run_time=5)
        
        
        d2 = Line(frame_height * UP / 2, frame_height * DOWN / 2).to_edge(LEFT)
        self.add(d2)
        self.play(Text(str(pixel_height),color=PURE_GREEN).animate.move_to([0,-2,0]).scale(0.8).next_to(d2,RIGHT*10),run_time=5)
        
        arr=Arrow(buff=0,start=LEFT, end=RIGHT, color=BLUE, tip_shape=ArrowTriangleTip,
                    max_stroke_width_to_length_ratio=0.5,
                    max_tip_length_to_length_ratio=0.1).next_to(d2,RIGHT*16)
        ar1=Arrow(buff=0,start=DOWN, end=UP, color=LOGO_WHITE, tip_shape=ArrowCircleTip,
                    max_stroke_width_to_length_ratio=0.5,
                    max_tip_length_to_length_ratio=0.1).next_to(d1,UP*4)
        self.play(Create(Dot(color=YELLOW,fill_opacity=1)),Create(arr),Create(ar1),run_time=5)
        
        self.wait(2)