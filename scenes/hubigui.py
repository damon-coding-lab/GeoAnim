"""
胡不归模型 - 阿氏圆问题
中考压轴
"""

from manim import *
import numpy as np

CHINESE_FONT = "Heiti SC"


class Hubigui(Scene):
    def construct(self):
        self.setup_scene()
        self.show_problem()
        self.demonstrate_solution()
        self.show_conclusion()

    def setup_scene(self):
        """设置场景"""
        # 地面
        ground = Line(LEFT * 5, RIGHT * 5, color=WHITE, stroke_width=1)
        ground.shift(DOWN * 2)

        # A点（起点）和B点（终点）
        self.A = Dot(color=YELLOW, radius=0.15).move_to(LEFT * 3 + UP * 1)
        self.B = Dot(color=RED, radius=0.15).move_to(RIGHT * 2 + DOWN * 2)

        self.A_label = Text("A", font=CHINESE_FONT, font_size=24).next_to(self.A, LEFT + UP)
        self.B_label = Text("B", font=CHINESE_FONT, font_size=24).color = RED
        self.B_label = Text("B", font=CHINESE_FONT, font_size=24, color=RED).next_to(self.B, RIGHT + DOWN)

        # 标注
        A_anno = Text("起点", font=CHINESE_FONT, font_size=16, color=YELLOW).next_to(self.A, UP)
        B_anno = Text("终点", font=CHINESE_FONT, font_size=16, color=RED).next_to(self.B, UP)

        self.add(ground, self.A, self.B, self.A_label, self.B_label, A_anno, B_anno)

        # 道路AB（普通道路）
        road = Line(self.A.get_center(), self.B.get_center(), color=GRAY, stroke_width=4)
        self.road = road

    def show_problem(self):
        """展示问题"""
        problem = Text("从A到B，有一段沙地（速度慢）和一段普通道路", font=CHINESE_FONT, font_size=22, color=WHITE)
        problem.move_to(UP * 3.2)

        self.play(Write(problem))
        self.wait(2)

        self.problem = problem

    def demonstrate_solution(self):
        """演示解决方案"""
        self.play(FadeOut(self.problem))

        # 沙地区域（用浅黄色表示）
        sand = Rectangle(width=3, height=2, color=YELLOW, fill_opacity=0.2, stroke_width=1)
        sand.move_to(LEFT * 2 + DOWN * 0.5)

        sand_label = Text("沙地（速度0.5倍）", font=CHINESE_FONT, font_size=16, color=YELLOW)
        sand_label.next_to(sand, DOWN, buff=0.1)

        road_label = Text("普通道路", font=CHINESE_FONT, font_size=16, color=GRAY)
        road_label.next_to(self.road, UP, buff=0.1)

        self.play(Create(sand), Write(sand_label), Write(road_label))
        self.wait(1.5)

        # 胡不归技巧：找最优点P
        P = LEFT * 0.5 + DOWN * 1.5
        self.P = Dot(color=GREEN, radius=0.12).move_to(P)
        self.P_label = Text("P", font=CHINESE_FONT, font_size=24, color=GREEN).next_to(self.P, LEFT)

        # 路径 A -> P -> B
        path_AP = Line(self.A.get_center(), P, color=GREEN, stroke_width=3)
        path_PB = Line(P, self.B.get_center(), color=GREEN, stroke_width=3)

        solution = Text("胡不归：构造阿氏圆，找最优点P", font=CHINESE_FONT, font_size=20, color=GREEN)
        solution.move_to(UP * 3.2)

        self.play(Write(solution))
        self.wait(1)

        self.play(Create(path_AP), Create(path_PB))
        self.play(Create(self.P), Write(self.P_label))
        self.wait(2)

        self.solution = solution

    def show_conclusion(self):
        """展示结论"""
        conclusion = Text("走最优路径APB，时间最短", font=CHINESE_FONT, font_size=24, color=YELLOW)
        conclusion.move_to(UP * 3.2)

        formula = Text("原理：加权最短路径 + 阿氏圆", font=CHINESE_FONT, font_size=18, color=WHITE)
        formula.next_to(conclusion, DOWN, buff=0.3)

        self.play(FadeOut(self.solution), Write(conclusion), Write(formula))
        self.wait(3)
