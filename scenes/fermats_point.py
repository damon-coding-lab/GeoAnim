"""
费马点模型 - 三角形的费马点
九下·锐角三角函数
"""

from manim import *
import numpy as np

CHINESE_FONT = "Heiti SC"


class FermatsPoint(Scene):
    def construct(self):
        self.setup_scene()
        self.show_problem()
        self.find_fermats_point()
        self.show_conclusion()

    def setup_scene(self):
        """设置场景"""
        # 锐角三角形ABC
        A = LEFT * 2 + DOWN * 1
        B = RIGHT * 2 + DOWN * 1
        C = UP * 1.5 + LEFT * 0.5

        self.A = Dot(color=YELLOW, radius=0.12).move_to(A)
        self.B = Dot(color=YELLOW, radius=0.12).move_to(B)
        self.C = Dot(color=YELLOW, radius=0.12).move_to(C)

        self.A_label = Text("A", font=CHINESE_FONT, font_size=24).next_to(self.A, LEFT + DOWN)
        self.B_label = Text("B", font=CHINESE_FONT, font_size=24).next_to(self.B, RIGHT + DOWN)
        self.C_label = Text("C", font=CHINESE_FONT, font_size=24).next_to(self.C, UP)

        # 三角形
        triangle = Polygon(A, B, C, color=WHITE, stroke_width=2, fill_opacity=0.1)
        self.triangle = triangle

        self.add(triangle, self.A, self.B, self.C)
        self.add(self.A_label, self.B_label, self.C_label)

    def show_problem(self):
        """展示问题"""
        problem = Text("在△ABC内找一点P，使PA+PB+PC最小", font=CHINESE_FONT, font_size=22, color=WHITE)
        problem.move_to(UP * 3.2)

        condition = Text("（∠A、∠B、∠C均<120°）", font=CHINESE_FONT, font_size=18, color=GRAY)
        condition.next_to(problem, DOWN, buff=0.2)

        self.play(Write(problem), Write(condition))
        self.wait(2)

        self.problem = problem
        self.condition = condition

    def find_fermats_point(self):
        """找费马点"""
        self.play(FadeOut(self.problem), FadeOut(self.condition))

        # 费马点P的位置（近似，在三角形中心附近）
        A = self.A.get_center()
        B = self.B.get_center()
        C = self.C.get_center()

        # 费马点大约在三角形内以120度分开的位置
        P = np.array([0.0, 0.3, 0.0])  # 近似位置
        self.P = Dot(color=RED, radius=0.12).move_to(P)
        self.P_label = Text("P", font=CHINESE_FONT, font_size=24, color=RED).next_to(self.P, RIGHT)

        # 费马点的性质：以P为公共顶点，∠APB=∠BPC=∠CPA=120°
        hint = Text("费马点性质：∠APB = ∠BPC = ∠CPA = 120°", font=CHINESE_FONT, font_size=20, color=YELLOW)
        hint.move_to(UP * 3.2)

        # 连接PA, PB, PC
        PA = Line(P, A, color=GREEN, stroke_width=2)
        PB = Line(P, B, color=GREEN, stroke_width=2)
        PC = Line(P, C, color=GREEN, stroke_width=2)

        self.play(Create(self.P), Write(self.P_label), Write(hint))
        self.wait(1)

        self.play(Create(PA), run_time=0.8)
        self.play(Create(PB), run_time=0.8)
        self.play(Create(PC), run_time=0.8)
        self.wait(2)

        self.hint = hint

    def show_conclusion(self):
        """展示结论"""
        conclusion = Text("费马点P使PA+PB+PC最小", font=CHINESE_FONT, font_size=24, color=GREEN)
        conclusion.move_to(UP * 3.2)

        formula = Text("P满足：∠APB=∠BPC=∠CPA=120°", font=CHINESE_FONT, font_size=18, color=WHITE)
        formula.next_to(conclusion, DOWN, buff=0.3)

        self.play(FadeOut(self.hint), Write(conclusion), Write(formula))
        self.wait(3)
