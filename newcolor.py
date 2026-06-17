from manim import *
import inspect


class NewColors(Scene):
    def construct(self):
        self.camera.background_color = '#000000'
        
        xkcd_color_mobjects = VMobject()
        xkcd_colors = [
            color for color_name, color in inspect.getmembers(XKCD, lambda obj: isinstance(obj, ManimColor))
        ]
        
        for color in xkcd_colors:
            col_square = Square()
            col_square.set_fill(color, opacity=1)
            col_square.set_stroke(opacity=0)
            xkcd_color_mobjects.add(col_square)
            
        def color_sort(col):
            h, s, v = col.to_hsv()
            return h, v
            
        xkcd_sorted_ind = sorted(
            range(len(xkcd_colors)),
            key=lambda ind: xkcd_colors[ind].to_hsv()
        ).all()
        
        xkcd_color_mobjects.arrange_in_grid(23, 41)
        xkcd_color_mobjects.width = config.frame_width
        
        for ind, col_square in enumerate(xkcd_color_mobjects):
            col_square.generate_target()
            target_ind = xkcd_sorted_ind.index(ind)
            col_square.target.move_to(xkcd_color_mobjects[target_ind])
        
        
        self.play(FadeIn(xkcd_color_mobjects, lag_ratio=0.001, run_time=5))
        self.wait()
        
        move_squares = AnimationGroup(*[
                MoveToTarget(col_square)
                for col_square in xkcd_color_mobjects
            ],
            lag_ratio=0.001,
            run_time=5,
        )
        self.play(move_squares)
        self.wait(1)
        
        self.play(FadeOut(xkcd_color_mobjects, lag_ratio=0.001, run_time=5))
        
        