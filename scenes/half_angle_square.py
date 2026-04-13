"""
半角模型（正方形）- 旋转全等
九上·旋转
"""

from manim import *
import numpy as np

CHINESE_FONT = "Heiti SC"


class HalfAngleSquare(Scene):
    def construct(self):
        self.setup_scene()
        self.show_problem()
        self.demonstrate_rotation()
        self.show_conclusion()

    def setup_scene(self):
        """设置场景"""
        # 正方形 ABCD，边长设为2
        sq = Square(side_length=2, color=WHITE, stroke_width=2)
        self.square = sq

        # 顶点标注
        self.A = Dot(color=YELLOW, radius=0.12).move_to(LEFT * 1 + DOWN * 1)  # 左下
        self.B = Dot(color=YELLOW, radius=0.12).move_to(RIGHT * 1 + DOWN * 1)  # 右下
        self.C = Dot(color=YELLOW, radius=0.12).move_to(RIGHT * 1 + UP * 1)    # 右上
        self.D = Dot(color=YELLOW, radius=0.12).move_to(LEFT * 1 + UP * 1)     # 左上

        self.A_label = Text("A", font=CHINESE_FONT, font_size=24).next_to(self.A, LEFT + DOWN)
        self.B_label = Text("B", font=CHINESE_FONT, font_size=24).next_to(self.B, RIGHT + DOWN)
        self.C_label = Text("C", font=CHINESE_FONT, font_size=24).next_to(self.C, RIGHT + UP)
        self.D_label = Text("D", font=CHINESE_FONT, font_size=24).next_to(self.D, LEFT + UP)

        # 对角线 AC（虚线）
        self.diagonal = DashedLine(self.A.get_center(), self.C.get_center(), color=BLUE, stroke_width=1.5)

    def show_problem(self):
        """展示问题"""
        self.add(self.square, self.A, self.B, self.C, self.D)
        self.add(self.A_label, self.B_label, self.C_label, self.D_label)
        self.add(self.diagonal)

        # 问题描述
        problem = Text("正方形ABCD，对角线AC上有一动点P", font=CHINESE_FONT, font_size=22, color=WHITE)
        problem.move_to(UP * 3.2)

        # 添加P点
        self.P = Dot(color=RED, radius=0.1).move_to(UP * 0.5)
        self.P_label = Text("P", font=CHINESE_FONT, font_size=18, color=RED).next_to(self.P, LEFT)

        # 从B向角DAC作垂线，垂足为P
        hint = Text("连接BP，使BP⊥AC", font=CHINESE_FONT, font_size=20, color=YELLOW)
        hint.move_to(UP * 3.2 + DOWN * 0.4)

        self.play(Write(problem))
        self.wait(1)
        self.play(Create(self.P), Write(self.P_label))
        self.wait(1)
        self.play(Write(hint))
        self.wait(2)

        self.problem = problem
        self.hint = hint

    def demonstrate_rotation(self):
        """演示旋转全等"""
        self.play(FadeOut(self.problem), FadeOut(self.hint))

        # 构造BP线
        B_pos = self.B.get_center()
        P_pos = self.P.get_center()

        bp_line = Line(B_pos, P_pos, color=GREEN, stroke_width=3)
        right_angle = RightAngle(
            Line(P_pos, P_pos + UP * 0.3),
            Line(P_pos, B_pos),
            length=0.15,
            color=GREEN
        )

        # 显示BP⊥AC
        perp_label = Text("BP⊥AC", font=CHINESE_FONT, font_size=16, color=GREEN)
        perp_label.next_to(right_angle, LEFT)

        self.play(Create(bp_line), Create(right_angle), Write(perp_label))
        self.wait(1.5)

        # 旋转提示
        rotate_hint = Text("将△ABP绕A点旋转90°", font=CHINESE_FONT, font_size=20, color=ORANGE)
        rotate_hint.move_to(UP * 3.2)

        self.play(Write(rotate_hint))
        self.wait(1.5)

        # 隐藏原图中的BP，准备显示旋转后的位置
        self.play(FadeOut(bp_line), FadeOut(right_angle), FadeOut(perp_label))

        # 旋转后的B点位置（绕A旋转90°）
        # A在(-1,-1)，B在(1,-1)，旋转90°后B'应在(-1,1)
        A_pos = self.A.get_center()
        B_pos = self.B.get_center()
        B_prime_pos = np.array([2 * A_pos[0] - B_pos[1] + A_pos[1], B_pos[0] - A_pos[0] + A_pos[1], 0])

        # 新位置
        new_B = Dot(color=ORANGE, radius=0.12).move_to(B_prime_pos)
        new_B_label = Text("B'", font=CHINESE_FONT, font_size=20, color=ORANGE).next_to(new_B, LEFT + UP)

        # 旋转后的P'位置
        P_prime_pos = np.array([2 * A_pos[0] - P_pos[1] + A_pos[1], P_pos[0] - A_pos[0] + A_pos[1], 0])
        new_P = Dot(color=ORANGE, radius=0.1).move_to(P_prime_pos)
        new_P_label = Text("P'", font=CHINESE_FONT, font_size=18, color=ORANGE).next_to(new_P, LEFT)

        # 旋转后的三角形
        new_triangle = Polygon(
            A_pos, B_prime_pos, P_prime_pos,
            color=ORANGE, fill_opacity=0.3, stroke_width=2
        )

        # 旋转箭头（弧线）
        arc = Arc(radius=0.5, start_angle=PI/4, angle=PI/2, color=YELLOW)
        arc.move_to(A_pos)

        self.play(Create(arc), run_time=1)
        self.wait(0.5)

        # 显示旋转后的三角形
        self.play(Create(new_triangle), Create(new_B), Write(new_B_label))
        self.play(Create(new_P), Write(new_P_label))
        self.wait(2)

        # 标注对应边相等
        equal1 = Text("AB = AB'", font=CHINESE_FONT, font_size=16, color=YELLOW)
        equal1.next_to(self.A_label, DOWN, buff=0.3)

        equal2 = Text("AP = AP'", font=CHINESE_FONT, font_size=16, color=YELLOW)
        equal2.next_to(equal1, DOWN, buff=0.2)

        self.play(Write(equal1), Write(equal2))
        self.wait(2)

        self.rotate_hint = rotate_hint
        self.new_triangle = new_triangle
        self.new_B = new_B
        self.new_B_label = new_B_label
        self.new_P = new_P
        self.new_P_label = new_P_label
        self.arc = arc
        self.equal1 = equal1
        self.equal2 = equal2

    def show_conclusion(self):
        """展示结论"""
        conclusion = Text("△ABP ≌ △AB'P'（旋转全等）", font=CHINESE_FONT, font_size=24, color=GREEN)
        conclusion.move_to(UP * 3.2)

        self.play(Write(conclusion))
        self.wait(3)
