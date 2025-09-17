from manim import *
import numpy as np 

class MyHeart(Scene):
    def construct(self):
        
        #Text d'intro
        t1 = Tex("3 ", "Heart", " Parametric Funtions", font_size=80)
        t1.set_color_by_tex('Heart', RED) #Heart avec couleur rouge

        self.play(Write(t1, run_time=3)) #ecriture de t 
        self.play(FadeOut(t1, shift=DOWN * 2, scale=1.5)) # FadeOut

        self.wait(0.5) # attente avant l'aparition des axes

        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=12,
            y_length=14,
            axis_config={"tip_shape": StealthTip},
        ) # les axes
        x_label = axes.get_x_axis_label("x") #label des axes
        y_label = axes.get_y_axis_label("y")

        y_label.move_to(axes.c2p(0.2, 4.2)) # le y etait trop en bas donc je l'ai mis en haut 

        self.play(Create(axes, run_time=2)) #creation des axes
        self.play(Write(x_label), Write(y_label)) #ecriture des labels 

        #==========================
        #Premier Coeur 
        
        #Ecriture de la formule de l'eq para du 1er Coeur
        f1h1 = Tex(r"$x $", r"$= \sin t \cos t \ln \lvert t \rvert $", font_size=60)
        f2h1 = Tex(r"$ y $", r"$= \lvert t \rvert ^(0.3) (\cos t)^\frac{1}{2} $", font_size=60)
        f1h1.set_color_by_tex('x', RED)
        f2h1.set_color_by_tex('y', RED)

        #groupe
        fh1 = VGroup(f1h1, f2h1).arrange(DOWN, aligned_edge = LEFT, buff=0.5)
        fh1.shift(UP * 10)

        self.play(Write(fh1))

        #rectangle pour encadrer la formule 

        self.wait()
