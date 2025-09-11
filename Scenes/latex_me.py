from manim import *


class MyText(Scene):
    def construct(self):
        t = Tex(r"$E=mc^2$", font_size = 96)
        self.play(Write(t))
        self.wait(3)
