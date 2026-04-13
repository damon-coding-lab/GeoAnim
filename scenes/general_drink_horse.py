"""
将军饮马模型 - 轴对称最短路径
八上·轴对称
"""

from manim import *
import numpy as np

# 使用系统可用的中文字体
CHINESE_FONT = "Heiti SC"


class GeneralDrinkHorse(Scene):
    def construct(self):
        self.setup_scene()
        self.show_problem()
        self.demonstrate_reflection()
        self.show_path_comparison()
        self.conclude()

    def setup_scene(self):
        """设置场景"""
        # 地面线
        ground = Line(LEFT * 6, RIGHT * 6, color=WHITE, stroke_width=1)
        ground.shift(DOWN * 2)
        self.ground = ground

        # 河流（蓝色条带）
        river = Rectangle(width=12, height=0.4, color=BLUE, fill_opacity=0.3, stroke_width=2)
        river.shift(DOWN * 0.5)
        self.river = river

        # A点（将军起点）和B点（军营）
        self.A = Dot(color=YELLOW, radius=0.15).move_to(LEFT * 3 + UP * 1.5)
        self.B = Dot(color=RED, radius=0.15).move_to(RIGHT * 2 + UP * 2)
        self.A_label = Text("A", font=CHINESE_FONT, font_size=24).next_to(self.A, LEFT)
        self.B_label = Text("B", font=CHINESE_FONT, font_size=24).next_to(self.B, RIGHT)

        # 标注
        self.A_annotation = Text("将军", font=CHINESE_FONT, font_size=18, color=YELLOW).next_to(self.A, UP)
        self.B_annotation = Text("军营", font=CHINESE_FONT, font_size=18, color=RED).next_to(self.B, UP)

    def show_problem(self):
        """展示问题"""
        self.add(self.ground, self.river, self.A, self.B, self.A_label, self.B_label)
        self.add(self.A_annotation, self.B_annotation)

        # 问题描述
        problem = Text("将军从A点出发，先去河边饮马，再去B点，怎样走最近？",
                       font=CHINESE_FONT, font_size=22, color=WHITE)
        problem.move_to(UP * 3.2)

        self.play(Write(problem))
        self.wait(2)
        self.problem = problem

    def demonstrate_reflection(self):
        """演示轴对称原理"""
        # 隐藏问题
        self.play(FadeOut(self.problem))

        # 获取河流的y坐标
        river_y = self.river.get_center()[1]

        # 标记河岸（饮马点）
        bank_line = Line(LEFT * 5, RIGHT * 5, color=BLUE_A, stroke_width=2)
        bank_line.shift(DOWN * 0.7)
        bank_label = Text("河岸", font=CHINESE_FONT, font_size=16, color=BLUE_A).next_to(bank_line, RIGHT)

        self.play(Create(bank_line), Write(bank_label))

        # 以河岸为对称轴，构造B的对称点B'
        B = self.B
        river_center = self.river.get_center()
        B_prime_pos = np.array([B.get_center()[0], 2 * river_center[1] - B.get_center()[1], 0])
        self.B_prime = Dot(color=RED, radius=0.12).move_to(B_prime_pos)
        self.B_prime_label = Text("B'", font=CHINESE_FONT, font_size=20, color=RED)
        self.B_prime_label.next_to(self.B_prime, RIGHT)

        # 显示B'构造过程
        show_B_prime = Text("以河岸为对称轴，作B的对称点B'", font=CHINESE_FONT, font_size=20, color=YELLOW)
        show_B_prime.move_to(UP * 3.2)

        self.play(Write(show_B_prime))
        self.wait(1.5)

        # 绘制对称轴虚线
        reflect_line = DashedLine(B.get_center(), B_prime_pos, color=GREEN, stroke_width=1.5)
        self.play(Create(reflect_line))
        self.wait(1)

        self.play(Create(self.B_prime), Write(self.B_prime_label))
        self.wait(1.5)

        self.show_B_prime_text = show_B_prime

    def show_path_comparison(self):
        """展示路径对比"""
        # 连接AB'
        A = self.A.get_center()
        B_prime = self.B_prime.get_center()

        # 新的直线 A -> B'（实际走的路径）
        path = Line(A, B_prime, color=ORANGE, stroke_width=4)
        self.path = path

        # 交点（饮马点P）
        river_y = self.river.get_center()[1]
        t = (river_y - A[1]) / (B_prime[1] - A[1])
        P_x = A[0] + t * (B_prime[0] - A[0])
        self.P = Dot(color=WHITE, radius=0.12).move_to(np.array([P_x, river_y, 0]))
        self.P_label = Text("P", font=CHINESE_FONT, font_size=20, color=WHITE)
        self.P_label.next_to(self.P, DOWN)

        # 画实际路径 A -> P -> B
        path_AP = Line(A, self.P.get_center(), color=ORANGE, stroke_width=4)
        path_PB = Line(self.P.get_center(), self.B.get_center(), color=ORANGE, stroke_width=4)

        conclusion = Text("连接AB'，与河岸的交点P即为最佳饮马位置！",
                          font=CHINESE_FONT, font_size=20, color=GREEN)
        conclusion.move_to(UP * 3.2)

        self.play(FadeOut(self.show_B_prime_text))
        self.play(Write(conclusion))
        self.wait(1)

        self.play(Create(path_AP), Create(path_PB))
        self.play(Create(self.P), Write(self.P_label))
        self.wait(2)

        self.conclusion = conclusion

    def conclude(self):
        """总结"""
        # 隐藏结论
        self.play(FadeOut(self.conclusion))

        # 重新显示完整路径
        summary = Text("原理：轴对称 + 两点之间线段最短",
                       font=CHINESE_FONT, font_size=24, color=YELLOW)
        summary.move_to(UP * 3.2)

        formula = Text("AP + PB = AB'（最短）",
                       font=CHINESE_FONT, font_size=20, color=WHITE)
        formula.next_to(summary, DOWN)

        self.play(Write(summary), Write(formula))
        self.wait(3)
