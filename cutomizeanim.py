from manim import *

class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number,  **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (self.rate_func(alpha) * (self.end - self.start))
        self.mobject.set_value(value)


class CountingScene(Scene):
    def construct(self):
        # Create Decimal Number and add it to scene
        number = DecimalNumber().set_color(WHITE).scale(5)
        # Add an updater to keep the DecimalNumber centered as its value changes
        number.add_updater(lambda number: number.move_to(ORIGIN))
        
        squ=Rectangle(height=4,width=10).set_stroke(color=PURE_GREEN,width=10).move_to([0,0,0])

        self.add(number)
        self.play(Create(squ),run_time=3)
        self.wait()

        # Play the Count Animation to count from 0 to 100 in 4 seconds
        # passing arguments to the count function - 
        #   1 parameter mobject -number 
        #    2 parameter start 0
        #     3 parameter end   100
        self.play(Count(number, 0, 100), run_time=4, rate_func=linear)

        self.wait()