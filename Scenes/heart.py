from manim import *
import numpy as np 

class MyHeart(Scene):
    def construct(self):

        #template
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        
        #Text d'intro
        t1 = Tex("3 ", "Heart", " Parametric Funtions", font_size=80)
        t1.set_color_by_tex('Heart', RED) #Heart avec couleur rouge

        self.play(Write(t1, run_time=2)) #ecriture de t 
        self.play(FadeOut(t1, run_time=1)) # FadeOut

        self.wait(0.3) # attente avant l'aparition des axes

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

        #====================================

        #Premier Coeur 
        l1 = Tex(
            r"$\mathscr{H} : $",
            tex_template=myTemplate,
            font_size=80,
        ).shift(UP * 10, LEFT * 4)

        #Ecriture de la formule de l'eq para du 1er Coeur
        f1h1 = Tex(r"$x = \sin t \cos t \ln \lvert t \rvert $", font_size=60)
        f2h1 = Tex(r"$y = \lvert t \rvert ^{0.3} (\cos t)^\frac{1}{2} $", font_size=60)
        f1h1[0][0].set_color(RED)
        f2h1[0][0].set_color(RED)

        #groupe
        fh1 = VGroup(f1h1, f2h1).arrange(DOWN, aligned_edge = LEFT, buff=0.5)
        fh1.shift(UP * 10)

        #rectangle pour encadrer la formule 
        rect = SurroundingRectangle(fh1, color=RED, buff=0.5)
        self.add(l1)
        
        #fonction 
        h1 = ParametricFunction(
            lambda t: np.array([
                np.sin(t) * np.cos(t) * np.log(np.abs(t)),
                np.abs(t)**(0.3) * np.cos(t)**(0.5),
                0
            ]) * 9,
            t_range = np.array([-1, 1]) 
        )

        h1.set_color(RED) 
        #animation
        self.play(
            Create(rect, run_time=2),
            Succession(
                Wait(1.0),
                Write(fh1),   
            ),
            Create(h1, run_time=3),
        )

        self.wait(4)
