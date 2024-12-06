from manim import *

class Solver_problem_statement(Scene):
    def construct(self):
        math_group = VGroup()
        spoken_group = VGroup()

        objective = MathTex(
            r"Objectif\ :\ ", "minimiser\ ", "le\ cout \n",
            tex_to_color_map={
                r"le\ cout": GREEN,
            }
        )
        spoken_group.add(objective)
        
        objective_math = MathTex(
            r"Objectif\ :\ "," minimiser\ ", "\sum_i  C_{i}",
            tex_to_color_map={
                r"\sum_i  C_{i}": GREEN,
            }        
        )
        math_group.add(objective_math)

        constraint_elec = Text(
            "pas d'accumulation d'électricité\n",
            t2c={"pas d'accumulation d'":YELLOW,
                 "électricité": YELLOW}
        )
        spoken_group.add(constraint_elec)

        constraint_elec_math = MathTex(
            r"\sum_{i} Pe_{i} - Consommation = 0",
            tex_to_color_map={
                r"\sum_{i} Pe_{i}": GREEN,
                r"Consommation": RED,
            }
        )
        math_group.add(constraint_elec_math)


        constraint_carburant = Text(
            "Pas d'accumulation de carburants\n",
            t2c={"Pas d'accumulation de":YELLOW,
                    "carburants": YELLOW}
        )
        spoken_group.add(constraint_carburant)

        constraint_carburant_math = MathTex(
            r"\sum_{i} Mc_{i} - Consommation = 0",
            tex_to_color_map={
                r"\sum_{i} Mc_{i}": GREEN,
                r"Consommation": RED,
            }
        )
        math_group.add(constraint_carburant_math)

        

        constraint_carbon_negative = Text(
            "négatif en CO2",
            t2c={"négatif en":YELLOW,
                    "CO2": YELLOW}
        )
        spoken_group.add(constraint_carbon_negative)

        constraint_carbon_negative_math = MathTex(
            r"\sum_{i} CO2_{i} - Import \leq 0",
            tex_to_color_map={
                r"\sum_{i} CO2_{i}": GREEN,
                r"Import": RED,
            }
        )
        math_group.add(constraint_carbon_negative_math)
        

        constraint_heat = Text(
            "assez de production de chaleur",
            t2c={"assez de production de":YELLOW,
                    "chaleur": YELLOW}
        )
        spoken_group.add(constraint_heat)

        constraint_heat_math = MathTex(
            r"\sum_{i} Q_{i} - Consommation \geq 0",
            tex_to_color_map={
                r"\sum_{i} Q_{i}": GREEN,
                r"Consommation": RED,
            }
        )
        math_group.add(constraint_heat_math)

        math_group.arrange(DOWN, center=False, aligned_edge=LEFT).move_to(ORIGIN)
        for math, spoken in zip(math_group, spoken_group):
            spoken.move_to(math.get_center())
        
        for math, spoken in zip(math_group, spoken_group):
            self.play(Write(spoken))
            self.play(Transform(spoken, math))
            self.wait()

        





        



