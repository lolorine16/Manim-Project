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

class Equation(Scene):
    def construct(self):
        t1 = Tex(r"$y = $", r"$2x + x^2 - 3x + 5$", font_size=96)
        t2 = Tex(r"$y = $", r"$x^2 - x + 5$", font_size=96)

        g = VGroup(t1, t2).arrange(DOWN, aligned_edge= LEFT, buff = 1)

        self.play(Write(t1))
        self.wait(1)

        self.play(TransformFromCopy(t1[0], t2[0]))
        self.play(TransformFromCopy(t1[1], t2[1]))

        self.wait(2)
