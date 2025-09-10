from manim import *
import numpy as np 

class loveu(Scene):
    def construct(self):
        t1 = Text("ILY").scale(1.5)
        t2 = Text("I Love You").scale(1.5)

        self.play(Write(t1))
        self.play(ReplacementTransform(t1[0], t2[0]))
        self.play(ReplacementTransform(t1[1], t2[1:5]), t1[2].animate.shift(RIGHT*0.3))
        self.play(ReplacementTransform(t1[2], t2[5:8]))
        self.wait(1)

        heart = ParametricFunction(
            lambda t: np.array([
                16*np.sin(t)**3,
                13*np.cos(t) - 5*np.cos(t*2) - 2*np.cos(t*3) - np.cos(t*4),
                0
            ]) * 0.2,

            t_range = np.array([0, np.pi**2])
        )
        heart.set_color(RED)
        heart.set_fill(RED, opacity=0.5)
        self.play(Create(heart))
        self.wait(2)
