"""
隐圆模型 - 到定点距离等于定长的点的轨迹
九上·圆
"""

from manim import *
import numpy as np

CHINESE_FONT = "Heiti SC"


class HiddenCircle(Scene):
    def construct(self):
        self.show_definition()
        self.demonstrate_points()
        self.draw_circle()
        self.show_conclusion()

    def show_definition(self):
        """展示圆的定义"""
        # 定点O
        self.O = Dot(color=YELLOW, radius=0.15).move_to(LEFT * 2)
        self.O_label = Text("O", font=CHINESE_FONT, font_size=28).next_to(self.O, LEFT + UP)

        # 半径R的标注
        radius_text = Text("R = 2", font=CHINESE_FONT, font_size=20, color=WHITE)
        radius_text.next_to(self.O, DOWN, buff=0.3)

        # 定义文字
        definition = Text("到定点O的距离等于定长R的点的轨迹", font=CHINESE_FONT, font_size=22, color=WHITE)
        definition.move_to(UP * 3.2)

        self.play(Create(self.O), Write(self.O_label))
        self.play(Write(definition))
        self.play(Write(radius_text))
        self.wait(2)

        self.definition = definition
        self.radius_text = radius_text

    def demonstrate_points(self):
        """演示几个特殊位置的点"""
        self.play(FadeOut(self.definition), FadeOut(self.radius_text))

        # 半径长度
        R = 2
        O_pos = self.O.get_center()

        # 展示几个特殊位置的P点：右、上、左、下
        positions = [
            O_pos + RIGHT * R,      # P1 右
            O_pos + UP * R,        # P2 上
            O_pos + LEFT * R,      # P3 左
            O_pos + DOWN * R,      # P4 下
            O_pos + RIGHT * R * 0.707 + UP * R * 0.707,  # P5 45度
        ]

        self.P_points = []
        labels = ["P₁", "P₂", "P₃", "P₄", "P₅"]

        for i, pos in enumerate(positions):
            P = Dot(color=RED, radius=0.1).move_to(pos)
            P_label = Text(labels[i], font=CHINESE_FONT, font_size=16, color=RED)
            P_label.next_to(P, RIGHT)

            # 连接OP
            op_line = Line(O_pos, pos, color=BLUE_A, stroke_width=1.5)

            self.play(Create(P), Write(P_label), Create(op_line), run_time=0.8)
            self.wait(0.3)

            self.P_points.append((P, P_label, op_line))

    def draw_circle(self):
        """把各点连成圆"""
        R = 2
        O_pos = self.O.get_center()

        # 画圆
        circle = Circle(radius=R, color=GREEN, stroke_width=3)
        circle.move_to(O_pos)

        hint = Text("经过所有满足OP=R的点，连成圆", font=CHINESE_FONT, font_size=20, color=GREEN)
        hint.move_to(UP * 3.2)

        self.play(Write(hint))
        self.wait(0.5)

        # 动画画出圆
        self.play(Create(circle), run_time=2)
        self.wait(1.5)

        self.circle = circle
        self.hint = hint

    def show_conclusion(self):
        """展示结论"""
        conclusion = Text("轨迹是以O为圆心，R为半径的圆", font=CHINESE_FONT, font_size=24, color=YELLOW)
        conclusion.move_to(UP * 3.2)

        formula = Text("P ∈ ⊙O（R）", font=CHINESE_FONT, font_size=20, color=WHITE)
        formula.next_to(conclusion, DOWN, buff=0.3)

        self.play(FadeOut(self.hint))
        self.play(Write(conclusion), Write(formula))
        self.wait(3)
