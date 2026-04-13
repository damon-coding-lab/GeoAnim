"""
脚拉脚模型 - 圆的切线长定理
九上·圆
"""

from manim import *
import numpy as np

CHINESE_FONT = "Heiti SC"


class FootPullFoot(Scene):
    def construct(self):
        self.setup_scene()
        self.show_tangents()
        self.demonstrate_equal()
        self.show_conclusion()

    def setup_scene(self):
        """设置场景"""
        # 圆O
        self.O = Dot(color=YELLOW, radius=0.1).move_to(ORIGIN)
        self.O_label = Text("O", font=CHINESE_FONT, font_size=24, color=YELLOW).next_to(self.O, LEFT + UP)

        radius = 1.5
        self.circle = Circle(radius=radius, color=WHITE, stroke_width=2)

        # 圆外一点P
        P = RIGHT * 3.5 + DOWN * 0.5
        self.P = Dot(color=RED, radius=0.12).move_to(P)
        self.P_label = Text("P", font=CHINESE_FONT, font_size=24, color=RED).next_to(self.P, RIGHT)

        self.add(self.circle, self.O, self.O_label, self.P, self.P_label)

    def show_tangents(self):
        """展示两条切线"""
        # 切点A和B
        O = self.O.get_center()
        P = self.P.get_center()

        # 计算切点位置（简化）
        r = 1.5
        OP = np.linalg.norm(P - O)
        d = OP - r

        # A在PO连线的上方
        dir = (P - O) / OP
        perp = np.array([-dir[1], dir[0], 0])
        A = O + r * dir * np.cos(np.arccos(r/OP)) + r * perp * np.sin(np.arccos(r/OP))
        B = O + r * dir * np.cos(np.arccos(r/OP)) - r * perp * np.sin(np.arccos(r/OP))

        # 近似切点
        angle = np.arctan2(P[1] - O[1], P[0] - O[0])
        A_pos = O + np.array([np.cos(angle + 0.5) * r, np.sin(angle + 0.5) * r, 0])
        B_pos = O + np.array([np.cos(angle - 0.5) * r, np.sin(angle - 0.5) * r, 0])

        self.A = Dot(color=GREEN, radius=0.1).move_to(A_pos)
        self.B = Dot(color=GREEN, radius=0.1).move_to(B_pos)
        self.A_label = Text("A", font=CHINESE_FONT, font_size=20, color=GREEN).next_to(self.A, LEFT + UP)
        self.B_label = Text("B", font=CHINESE_FONT, font_size=20, color=GREEN).next_to(self.B, RIGHT + UP)

        # 切线PA和PB
        PA = Line(P, A_pos, color=BLUE, stroke_width=2)
        PB = Line(P, B_pos, color=BLUE, stroke_width=2)

        # 标注直角符号
        right_A = RightAngle(Line(A_pos, P, color=BLUE), Line(A_pos, O, color=YELLOW), length=0.15, color=GREEN)
        right_B = RightAngle(Line(B_pos, P, color=BLUE), Line(B_pos, O, color=YELLOW), length=0.15, color=GREEN)

        self.right_A = right_A
        self.right_B = right_B

        problem = Text("从圆外一点P作圆的两条切线PA、PB", font=CHINESE_FONT, font_size=22, color=WHITE)
        problem.move_to(UP * 3.2)

        self.play(Write(problem))
        self.wait(1)

        self.play(Create(PA), Create(PB))
        self.play(Create(self.A), Write(self.A_label))
        self.play(Create(self.B), Write(self.B_label))
        self.play(Create(right_A), Create(right_B))
        self.wait(2)

        self.problem = problem
        self.PA = PA
        self.PB = PB

    def demonstrate_equal(self):
        """演示切线长相等"""
        self.play(FadeOut(self.problem))

        hint = Text("切线长定理：PA = PB", font=CHINESE_FONT, font_size=24, color=YELLOW)
        hint.move_to(UP * 3.2)

        # 标注PA和PB长度
        PA_label = Text("PA", font=CHINESE_FONT, font_size=18, color=BLUE)
        PA_label.move_to((self.P.get_center() + self.A.get_center()) / 2 + UP * 0.3)

        PB_label = Text("PB", font=CHINESE_FONT, font_size=18, color=BLUE)
        PB_label.move_to((self.P.get_center() + self.B.get_center()) / 2 + DOWN * 0.3)

        self.play(Write(hint))
        self.play(Write(PA_label), Write(PB_label))
        self.wait(2)

        self.hint = hint
        self.PA_label = PA_label
        self.PB_label = PB_label

    def show_conclusion(self):
        """展示结论"""
        conclusion = Text("PA = PB", font=CHINESE_FONT, font_size=32, color=GREEN)
        conclusion.move_to(UP * 3.2)

        reason = Text("由△OPA ≌ △OPB（HL）可得", font=CHINESE_FONT, font_size=18, color=WHITE)
        reason.next_to(conclusion, DOWN, buff=0.3)

        self.play(FadeOut(self.hint), FadeOut(self.PA_label), FadeOut(self.PB_label), Write(conclusion), Write(reason))
        self.wait(3)
