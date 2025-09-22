from manim import *
import numpy as np 

class MyHeart(Scene):
    def construct(self):

        #template
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        
        #Text d'intro
        t1 = Tex("3 ", "Heart", " Parametric Equations", font_size=80)
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

        self.play(Create(axes, run_time=4)) #creation des axes
        self.play(Write(x_label), Write(y_label)) #ecriture des labels 

        #============================================

        #Premier Coeur 
        l1 = Tex(
            r"$\mathscr{H}1 : $",
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
        self.play(Create(l1))
        
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
            Create(h1, run_time=4, rate_func=linear),
        )

        self.wait(1)
        self.play(FadeOut(fh1, run_time=0.5), FadeOut(l1),FadeOut(rect),FadeOut(h1, run_time=0.5)) #FadeOut
        
        #==================================================

        #Deuxieme Coeur
        l2 = Tex(
            r"$\mathscr{H}2 : $",
            tex_template=myTemplate,
            font_size=80,
        ).shift(UP * 10, LEFT * 5)

        #Ecriture de la formule de l'eq para du 2eme Coeur
        f1h2 = Tex(r"$x = 16\sin ^3 t $", font_size=60).scale(0.8)
        f2h2 = Tex(r"$y = 13\cos t - 5\cos(2t) - 2\cos(3t) - \cos(4t)$", font_size=60).scale(0.8)
        f1h2[0][0].set_color(RED)
        f2h2[0][0].set_color(RED)

        #groupe
        fh2 = VGroup(f1h2, f2h2).arrange(DOWN, aligned_edge = LEFT, buff=0.5)
        fh2.shift(UP * 10, RIGHT * 1.5)

        #rectangle pour encadrer la formule 
        rect = SurroundingRectangle(fh2, color=RED, buff=0.3)
        self.play(Create(l2))

        #fonction 
        h2 = ParametricFunction(
            lambda t: np.array([
                16*np.sin(t)**3,
                13*np.cos(t) - 5*np.cos(t*2) - 2*np.cos(t*3) - np.cos(t*4),
                0
            ]) * 0.3,

            t_range = np.array([0, TAU])
        )

        h2.set_color(RED) 
        #animation
        self.play(
            Create(rect, run_time=2),
            Succession(
                Wait(1.0),
                Write(fh2),   
            ),
            Create(h2, run_time=4, rate_func=linear),
        )

        self.wait(1)
        self.play(FadeOut(fh2, run_time=0.5), FadeOut(l2),FadeOut(rect),FadeOut(h2, run_time=0.5)) #FadeOut
        
        #==================================================

        #Troisieme Coeur
        l3 = Tex(
            r"$\mathscr{H}3 : $",
            tex_template=myTemplate,
            font_size=80,
        ).shift(UP * 10, LEFT * 4)

        #Ecriture de la formule de l'eq para du 2eme Coeur
        f1h3 = Tex(r"$x = -\sqrt{2} \sin^3 t $", font_size=60)
        f2h3 = Tex(r"$y = 2\cos t - \cos^2 t - \cos^3 t$", font_size=60)
        f1h3[0][0].set_color(RED)
        f2h3[0][0].set_color(RED)

        #groupe
        fh3 = VGroup(f1h3, f2h3).arrange(DOWN, aligned_edge = LEFT, buff=0.5)
        fh3.shift(UP * 10, RIGHT * 1.5)

        #rectangle pour encadrer la formule 
        rect = SurroundingRectangle(fh3, color=RED, buff=0.5)
        self.play(Create(l3))

        #fonction 
        h3 = ParametricFunction(
            lambda t: np.array([
                np.negative(np.sqrt(2) * np.sin(t)**3),
                2*np.cos(t) - np.cos(t)**2 - np.cos(t)**3,
                0
            ]) * 3,

            t_range = np.array([0, TAU])
        )

        h3.set_color(RED) 
        #animation
        self.play(
            Create(rect, run_time=2),
            Succession(
                Wait(1.0),
                Write(fh3),   
            ),
            Create(h3, run_time=4, rate_func=linear),
        )

        self.wait(1)
        self.play(FadeOut(fh3, run_time=0.5), FadeOut(l3),FadeOut(rect),FadeOut(h3, run_time=0.5)) #FadeOut
        
        #==================================================
        self.wait(0.5)
        self.play(FadeOut(axes), FadeOut(x_label), FadeOut(y_label))
        #==================================================

        #Mot de fin 
        self.wait(0.5)
        t2 = Tex("Thanks for watchiiiinnnngggg !!!").scale(2)
        self.play(Create(t2))
        self.wait(0.5)
        self.play(FadeOut(t2))

        #=====================================================
        #PROJECT FINISHH !!!!!!!
        #On Tiktok and insta @ikeda.nh10 Go follow and like !
        #Thanks youuuu !!
        #=====================================================
        
        self.wait(2)
