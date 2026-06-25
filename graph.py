from manim import *

class graph(Scene):
    def construct(self):
        
            paragraph = Paragraph(
                "this is a awesome",
                "paragraph",
                "With \nNewlines",
                "\tWith Tabs",
                "  With Spaces",
                "With Alignments",
                "center",
                "left",
                "right",
            )


            for line in paragraph:
                line.set_color(random_color())
                self.play(Write(line),run_time=1)
                