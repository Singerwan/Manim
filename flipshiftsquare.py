from manim import *

class FlipShiftSquare(Scene):
    def construct(self):
        ax=Axes(x_range=[-5, 5], y_range=[-5, 5], axis_config={"color": GREY})
        plane    = NumberPlane()
        self.add(ax,plane)
        left_square = Square(side_length=1, color=BLUE, fill_opacity=0.5).shift(LEFT * 2)
        right_square = Square(side_length=1, color=RED, fill_opacity=0.5).shift(RIGHT * 2)
        self.play(Create(left_square), Create(right_square))
        self.wait(1)

        # Flip the square horizontally
        self.play(left_square.animate.flip(axis=UP))
        self.wait(1)
        self.play(right_square.animate.flip(axis=DOWN))
        self.play(left_square.animate.rotate(PI / 4))
        self.wait(1)
        self.play(right_square.animate.rotate(PI / 4))
        # Shift the square to the right
        self.play(left_square.animate.shift(UP * 2))
        self.play(right_square.animate.shift(DOWN * 2))
        arr=Arrow(start=LEFT * 2, end=RIGHT * 2, color=WHITE)
        self.play(Create(arr))
        self.play(arr.animate.next_to(left_square, ORIGIN, buff=0))
        self.play(FadeOut(left_square), FadeOut(right_square))
        self.wait(1)