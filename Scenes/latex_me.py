from manim import *


class MyText(Scene):
    def construct(self):
        t = Tex(r"$E=mc^2$", font_size = 96)
        self.play(Write(t))
        self.wait(3)

class Fraction(Scene):
    def construct(self):
        t = Tex(r"$(\frac{1}{3})^3 - \frac{5}{3} = -1\frac{17}{27}$", font_size= 96)

        self.play(Write(t))
        self.wait(3)
