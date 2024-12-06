from manim import *

class Variables(Scene):
    def construct(self):
        all_variables = VGroup(
            MathTex(
                r"P_{installe}\ de\ la\ technologie\ 1 \ en\ MW",
                tex_to_color_map={
                    r"P_{installe}": GREEN,
                }

            ),
            MathTex(
                r"P_{installe}\ de\ la\ technologie\ 2 \ en\ MW",
                tex_to_color_map={
                    r"P_{installe}": GREEN,
                }
            ),
            MathTex(
                r"P_{installe}\ de\ la\ technologie\ 3 \ en\ MW",
                tex_to_color_map={
                    r"P_{installe}": GREEN,
                }
            ),
            MathTex(
                r"P_{installe}\ de\ la\ technologie\ 4 \ en\ MW",
                tex_to_color_map={
                    r"P_{installe}": GREEN,
                }
            ),
            MathTex(
                r"\vdots",
                tex_to_color_map={
                    r"P_{installe}": GREEN,
                }
            ),
        ).arrange(DOWN, buff=0.5).move_to(ORIGIN)

        variables = MathTex(
                r"P_{i}\ en\ MW",
                tex_to_color_map={
                    r"P_{i}": GREEN,
                }
            )
        self.play(Write(all_variables, run_time=3))
        self.wait()
        self.play(Transform(all_variables, variables))
        
        