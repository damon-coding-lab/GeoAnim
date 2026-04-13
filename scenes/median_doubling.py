"""
倍长中线模型 - 构造全等三角形
八上·全等三角形
"""

from manim import *
import numpy as np

CHINESE_FONT = "Heiti SC"


class MedianDoubling(Scene):
    def construct(self):
        self.setup_scene()
        self.show_median()
        self.demonstrate_doubling()
        self.show_conclusion()

    def setup_scene(self):
        """设置场景"""
        # 三角形ABC
        A = LEFT * 2 + DOWN * 1
        B = RIGHT * 2 + DOWN * 1
        C = UP * 2

        self.A = Dot(color=YELLOW, radius=0.12).move_to(A)
        self.B = Dot(color=YELLOW, radius=0.12).move_to(B)
        self.C = Dot(color=YELLOW, radius=0.12).move_to(C)

        self.A_label = Text("A", font=CHINESE_FONT, font_size=24).next_to(self.A, LEFT + DOWN)
        self.B_label = Text("B", font=CHINESE_FONT, font_size=24).next_to(self.B, RIGHT + DOWN)
        self.C_label = Text("C", font=CHINESE_FONT, font_size=24).next_to(self.C, UP)

        # 三角形边
        triangle = Polygon(A, B, C, color=WHITE, stroke_width=2, fill_opacity=0.1)
        self.triangle = triangle

        # BC边上的中点D
        D = (B + C) / 2
        self.D = Dot(color=RED, radius=0.1).move_to(D)
        self.D_label = Text("D", font=CHINESE_FONT, font_size=20, color=RED).next_to(self.D, RIGHT)

        # 中线AD
        self.median = Line(A, D, color=BLUE, stroke_width=3)

        self.add(triangle, self.A, self.B, self.C)
        self.add(self.A_label, self.B_label, self.C_label)
        self.add(self.D, self.D_label, self.median)

    def show_median(self):
        """展示中线"""
        problem = Text("D是BC的中点，AD为△ABC的中线", font=CHINESE_FONT, font_size=22, color=WHITE)
        problem.move_to(UP * 3.2)

        hint = Text("倍长中线：延长AD到E，使DE=AD", font=CHINESE_FONT, font_size=20, color=YELLOW)
        hint.move_to(UP * 3.2 + DOWN * 0.5)

        self.play(Write(problem))
        self.wait(1)
        self.play(Write(hint))
        self.wait(2)

        self.problem = problem
        self.hint = hint

    def demonstrate_doubling(self):
        """演示倍长"""
        self.play(FadeOut(self.problem), FadeOut(self.hint))

        A = self.A.get_center()
        D = self.D.get_center()

        # 延长AD到E，使DE=AD
        E = 2 * D - A
        self.E = Dot(color=GREEN, radius=0.12).move_to(E)
        self.E_label = Text("E", font=CHINESE_FONT, font_size=24, color=GREEN).next_to(self.E, LEFT + DOWN)

        # 连接BE
        BE = Line(self.B.get_center(), E, color=GREEN, stroke_width=2)

        # 显示倍长过程
        extend_hint = Text("延长AD到E，使DE=AD", font=CHINESE_FONT, font_size=20, color=ORANGE)
        extend_hint.move_to(UP * 3.2)

        self.play(Write(extend_hint))
        self.wait(1)

        # 画虚线表示延长
        dashed_extend = DashedLine(A, E, color=ORANGE, stroke_width=2)
        self.play(Create(dashed_extend), run_time=1.5)
        self.play(Create(self.E), Write(self.E_label))
        self.wait(1)

        # 连接BE
        connect_hint = Text("连接BE", font=CHINESE_FONT, font_size=20, color=GREEN)
        connect_hint.move_to(UP * 3.2)

        self.play(FadeOut(extend_hint))
        self.play(Write(connect_hint))
        self.play(Create(BE), run_time=1)
        self.wait(2)

        self.connect_hint = connect_hint
        self.BE = BE

    def show_conclusion(self):
        """展示结论"""
        conclusion = Text("△ABD ≌ △CDE（SAS）", font=CHINESE_FONT, font_size=24, color=YELLOW)
        conclusion.move_to(UP * 3.2)

        meaning = Text("通过倍长中线，构造全等三角形", font=CHINESE_FONT, font_size=18, color=WHITE)
        meaning.next_to(conclusion, DOWN, buff=0.3)

        # 先淡出旧文字
        self.play(FadeOut(self.connect_hint))
        self.wait(0.3)
        # 再显示新文字
        self.play(Write(conclusion), Write(meaning))
        self.wait(3)
