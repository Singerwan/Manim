from manim import *

class t2g(Scene):
    def construct(self):
        t2ghellow=Text("Hello", font="Comic Sans MS",
                        t2g={"[1:-1]":(RED,GREEN,BLUE)}).move_to(LEFT)
        
        t2gworld=Text("World", font="Comic Sans MS",
                        t2g={"World":(WHITE,YELLOW,TEAL,PINK)}).move_to(RIGHT)
        
        self.play(Write(t2ghellow),Write(t2gworld))