"""
切割线定理 - 切线长定理的延伸
九上·圆
"""

from manim import *
import numpy as np

CHINESE_FONT = "Heiti SC"


class TangentSecant(Scene):
    def construct(self):
        self.setup_scene()
        self.show_problem()
        self.draw_tangent()
        self.draw_secant()
        self.show_conclusion()

    def setup_scene(self):
        """设置场景"""
        # 圆O
        self.O = Dot(color=YELLOW, radius=0.1).move_to(ORIGIN)
        self.O_label = Text("O", font=CHINESE_FONT, font_size=24, color=YELLOW).next_to(self.O, LEFT + UP)

        radius = 1.8
        self.circle = Circle(radius=radius, color=WHITE, stroke_width=2)

        # 圆外一点P
        P = RIGHT * 3.8
        self.P = Dot(color=RED, radius=0.15).move_to(P)
        self.P_label = Text("P", font=CHINESE_FONT, font_size=28, color=RED).next_to(self.P, RIGHT)

        self.add(self.circle, self.O, self.O_label, self.P, self.P_label)

    def show_problem(self):
        """展示问题"""
        problem = Text("从圆外一点P作圆的切线PA和割线PBC", font=CHINESE_FONT, font_size=22, color=WHITE)
        problem.move_to(UP * 3.2)

        hint = Text("证明：PA² = PB · PC", font=CHINESE_FONT, font_size=22, color=YELLOW)
        hint.move_to(UP * 3.2 + DOWN * 0.5)

        self.play(Write(problem))
        self.wait(1)
        self.play(Write(hint))
        self.wait(2)

        self.problem = problem
        self.hint = hint

    def draw_tangent(self):
        """画切线"""
        self.play(FadeOut(self.problem), FadeOut(self.hint))

        # 切点A
        O = self.O.get_center()
        P = self.P.get_center()
        r = 1.8

        # 计算切点A的位置（在OP连线的上方）
        OP = np.linalg.norm(P - O)
        dir = (P - O) / OP
        perp = np.array([-dir[1], dir[0], 0])

        # A在圆上，且PA是切线
        angle = np.arccos(r / OP)
        A_pos = O + r * (dir * np.cos(angle) + perp * np.sin(angle))

        self.A = Dot(color=GREEN, radius=0.12).move_to(A_pos)
        self.A_label = Text("A", font=CHINESE_FONT, font_size=24, color=GREEN).next_to(self.A, LEFT + UP)

        # 切线PA
        PA = Line(P, A_pos, color=BLUE, stroke_width=3)

        # 标注直角符号
        right_angle = RightAngle(
            Line(A_pos, P, color=BLUE),
            Line(A_pos, O, color=YELLOW),
            length=0.2,
            color=GREEN
        )

        tangent_hint = Text("PA为切线", font=CHINESE_FONT, font_size=20, color=BLUE)
        tangent_hint.move_to(UP * 3.2)

        self.play(Write(tangent_hint))
        self.wait(0.5)

        self.play(Create(PA))
        self.play(Create(self.A), Write(self.A_label))
        self.play(Create(right_angle))
        self.wait(2)

        self.tangent_hint = tangent_hint

    def draw_secant(self):
        """画割线"""
        self.play(FadeOut(self.tangent_hint))

        O = self.O.get_center()
        P = self.P.get_center()
        r = 1.8

        # 计算割线与圆的交点B和C
        OP = np.linalg.norm(P - O)
        dir = (P - O) / OP
        perp = np.array([-dir[1], dir[0], 0])

        # B在上方，C在下方
        angle = np.arccos(r / OP)
        B_pos = O + r * (dir * np.cos(angle) - perp * np.sin(angle))
        C_pos = O + r * (dir * np.cos(angle) + perp * np.sin(angle))

        self.B = Dot(color=ORANGE, radius=0.12).move_to(B_pos)
        self.C = Dot(color=ORANGE, radius=0.12).move_to(C_pos)
        self.B_label = Text("B", font=CHINESE_FONT, font_size=24, color=ORANGE).next_to(self.B, UP)
        self.C_label = Text("C", font=CHINESE_FONT, font_size=24, color=ORANGE).next_to(self.C, DOWN)

        # 割线PBC
        PB = Line(P, B_pos, color=ORANGE, stroke_width=3)
        PC = Line(P, C_pos, color=ORANGE, stroke_width=3)

        secant_hint = Text("PBC为割线", font=CHINESE_FONT, font_size=20, color=ORANGE)
        secant_hint.move_to(UP * 3.2)

        self.play(Write(secant_hint))
        self.wait(0.5)

        self.play(Create(self.B), Write(self.B_label))
        self.play(Create(self.C), Write(self.C_label))
        self.play(Create(PB), Create(PC))
        self.wait(2)

        self.secant_hint = secant_hint

    def show_conclusion(self):
        """展示结论"""
        conclusion = Text("PA² = PB · PC", font=CHINESE_FONT, font_size=36, color=YELLOW)
        conclusion.move_to(UP * 3.2)

        theorem = Text("切割线定理", font=CHINESE_FONT, font_size=24, color=GREEN)
        theorem.next_to(conclusion, DOWN, buff=0.3)

        self.play(FadeOut(self.secant_hint))
        self.play(Write(conclusion), Write(theorem))
        self.wait(3)
