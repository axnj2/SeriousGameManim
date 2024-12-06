from manim import *

class MovingFrameBox(Scene):
    def construct(self):
        constraint_elec = Text(
            "pas d'accumulation d'électricité",
            t2c={"pas d'accumulation d'":YELLOW,
                 "électricité": YELLOW}
        )

        constraint_elec_math = MathTex(
            r"\sum_{i} Pe_{i} - Consommation = 0"
        )

        self.play(Write(constraint_elec))
        self.play(Transform(constraint_elec, constraint_elec_math))
        self.play(constraint_elec.animate.shift(UP))

        self.wait()

        constraint_carburant = Text(
            "Pas d'accumultation de carburants",
        )

        constraint_carburant_math = MathTex(
            r"\sum_{i} Mc_{i} - Consommation = 0"
        )

        self.play(Write(constraint_carburant))
        self.play(Transform(constraint_carburant, constraint_carburant_math))
        self.play(constraint_carburant.animate.shift(DOWN*2))

        constraint_carbon_negative = Text(
            "négatif en CO2",
        )

        constraint_carbon_negative_math = MathTex(
            r"\sum_{i} CO2_{i} - Import \leq 0"
        )

        self.play(Write(constraint_carbon_negative))
        self.play(Transform(constraint_carbon_negative, constraint_carbon_negative_math))
        self.play(constraint_carbon_negative.animate.shift(DOWN))

        objective = MathTex(
            r"Objectif\ :\ ", "minimiser\ ", "le\ cout",
            tex_to_color_map={
                r"Objectif\ :\ ": YELLOW,
                r"minimiser": BLUE,
                r"le\ cout": GREEN,
            }
        )
        
        objective_math = MathTex(
            r"Objectif\ :\ "," minimiser\ ", "\sum_i  C_{i}",
            tex_to_color_map={
                r"Objectif\ :\ ": YELLOW,
                r"minimiser": BLUE,
                r"\sum_i  C_{i}": GREEN,
            }        
        )


        self.play(Write(objective))
        self.play(Transform(objective, objective_math))
        
        self.wait()
        
        self.play(objective.animate.shift(UP*2))

        constraint_heat = Text(
            "assez de production de chaleur",
        )

        constraint_heat_math = MathTex(
            r"\sum_{i} Q_{i} - Consommation \geq 0"
        )




        



