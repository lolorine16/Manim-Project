from manim import *

class MyHeart(Scene):
    def construct(self):

        axes = Axes(
            x_range=[-4, 4, 2],
            y_range=[-4, 4, 2],
            x_length=12,
            y_length=14,
            axis_config={"tip_shape": StealthTip},
        )
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")

        y_label.move_to(axes.c2p(0.2, 4.2))

        self.play(Create(axes, run_time=2))
        self.play(Write(x_label), Write(y_label))
        self.wait()
