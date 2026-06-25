from manim import *

class rosebthem(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        plane = PolarPlane(color=PURE_MAGENTA)
        self.play(Create(plane))
        self.play(FadeOut(plane))
        for i in range(1,20):
            r = lambda theta: 2 * np.sin(theta * i)
            graph = plane.plot_polar_graph(r, [0, 2 * PI], color=random_bright_color())
            self.play(Create(graph),run_time=10)
            self.play(FadeOut(graph))
    