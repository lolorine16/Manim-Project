from manim import *

class complexe(Scene):
    def construct(self):

        #ajout d'un template pour povoir utiliser un template de LaTex
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        
        t1 = Tex(r"Ensemble $\mathbb{C}$ des nombres complexes",
                #pour que C ai l'apparence d'un Ensemble
                tex_template=myTemplate,
                font_size=80) #aggrandissement de la taille
        
        #Ecrire t1 
        self.play(Write(t1))
        self.wait(1)
        
        #animation vers le haut(de 6 fois)
        self.play(t1.animate.shift(UP * 6), run_time=1)
        self.wait(0.5)

        #Ajout de la description
        t2 = Tex("C'est l'ensemble des nombres de la forme ", font_size=30).scale(2)
        #animation FadeIn
        self.play(Write(t2, shift=DOWN, scale=0.5))
        self.play(t2.animate.shift(UP * 4), run_time=1)

        #ajout de la formule
        formule = MathTex(
            r"a + ib",
            substrings_to_isolate="i",
            font_size=100
        )
        formule.set_color_by_tex("i", RED)

        #encadrement et ecriture de la formule
        rect = SurroundingRectangle(formule, buff=0.5)
        g1 = VGroup(formule, rect) #groupe pour l'animation vers le haut
        self.play(
            Create(rect, run_time=2),
            Succession(
                Write(formule),
                Wait(2),
                g1.animate.shift(UP * 2),
            ),
        )
        self.wait(1)
        
        t3 = Tex("où a et b sont des nombres réels")

        t3[0][3].set_color(RED)
        t3[0][6].set_color(RED)
        self.play(Write(t3))

        self.wait(3)




