from manim import *

class groupcirclesqu(Scene):
    def construct(self):

            mobj1=Square()

            mobj2=Circle()

            self.play(Create(mobj1))
            self.play(Create(mobj2))
            mob_group=Group(mobj1,mobj2)

            self.add(mob_group)
            self.wait(2)
            

