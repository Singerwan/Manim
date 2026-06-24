from manim import *

class heart(Scene):
    def construct(self):
        ax = Axes()
        # self.play(Create(ax), run_time=2)
        cardioid = ax.plot_parametric_curve(
            lambda t: np.array(
                [
                    np.exp(1) * np.cos(t) * (1 - np.cos(t)),
                    np.exp(1) * np.sin(t) * (1 - np.cos(t)),
                    0,
                ]
            ),
            t_range=[0, 2 * PI],
            color="#F10F5A",
        )
        self.play(Create(cardioid), run_time=5)
        self.play(cardioid.animate.set_fill(color=RED,opacity=1))
        self.play(cardioid.animate.rotate(PI/2),run_time=5)
        self.play(FadeOut(cardioid))
        
        car90L=cardioid.copy().rotate(-PI/4).scale(0.4).move_to(LEFT*2.5).set_color(WHITE).set_fill(color=WHITE,opacity=1)
        car90=cardioid.copy().rotate(-PI/4).scale(0.4).move_to(RIGHT*0.1).set_color("#F10F5A").set_fill(color="#F10F5A",opacity=1)
        car90R=cardioid.copy().rotate(-PI/4).scale(0.4).move_to(RIGHT*3).set_color("#22F10F").set_fill(color="#22F10F",opacity=1)   
        car90LU=cardioid.copy().rotate(-PI/4).scale(0.4).move_to(LEFT*3+UP*2.5).set_color("#0F80F1").set_fill(color="#0F80F1",opacity=1)
        car90U=cardioid.copy().rotate(-PI/4).scale(0.4).move_to(UP*2.5).set_color("#3C0FF1").set_fill(color="#3C0FF1",opacity=1)
        car90RU=cardioid.copy().rotate(-PI/4).scale(0.4).move_to(RIGHT*3+UP*2.5).set_color("#E2F10F").set_fill(color="#E2F10F",opacity=1)   
        car90LD=cardioid.copy().rotate(-PI/4).scale(0.4).move_to(LEFT*3+DOWN*2.5).set_color("#2F2B2C",).set_fill(color="#2F2B2C",opacity=1)
        car90D=cardioid.copy().rotate(-PI/4).scale(0.4).move_to(DOWN*2.5).set_color("#238B2C").set_fill(color="#238B2C",opacity=1)
        car90RD=cardioid.copy().rotate(-PI/4).scale(0.4).move_to(RIGHT*3+DOWN*2.5).set_color("#19192E").set_fill(color="#19192E",opacity=1)               
        
        self.play(Create(car90L),run_time=2)
        self.play(Create(car90),run_time=2)
        self.play(Create(car90R),run_time=2)
        self.play(Create(car90LU),run_time=2)
        self.play(Create(car90RU),run_time=2)
        self.play(Create(car90U),run_time=2)
        self.play(Create(car90LD),run_time=2)
        self.play(Create(car90D),run_time=2)
        self.play(Create(car90RD),run_time=2)