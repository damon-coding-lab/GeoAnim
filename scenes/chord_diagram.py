"""
弦图模型 - 勾股定理的几何证明
八下·勾股定理
"""

from manim import *
import numpy as np

CHINESE_FONT = "Heiti SC"


class ChordDiagram(Scene):
    def construct(self):
        self.setup_scene()
        self.show_square()
        self.demonstrate_areas()
        self.show_conclusion()

    def setup_scene(self):
        """设置场景"""
        # 弦图由4个直角三角形组成，中间一个小正方形
        # 外边长为 a+b

        # 直角三角形：直角边为a和b，斜边为c
        self.a = 2
        self.b = 1.5
        self.c = np.sqrt(self.a**2 + self.b**2)

        # 中心位置
        center = ORIGIN

        # 四个三角形的顶点
        # 左下三角形
        A1 = center + LEFT * (self.a/2 + self.b/2) + DOWN * (self.a/2 + self.b/2)
        B1 = center + LEFT * (self.a/2 - self.b/2) + DOWN * (self.a/2 + self.b/2)
        C1 = center + LEFT * (self.a/2 - self.b/2) + DOWN * (self.a/2 - self.b/2)

        # 标注
        self.triangles = []
        colors = [BLUE, RED, GREEN, YELLOW]

        # 创建四个直角三角形
        for i in range(4):
            angle = i * PI / 2
            tri_center = center + RIGHT * (self.b/2) * np.cos(angle) + UP * (self.b/2) * np.sin(angle)

            # 旋转后的三角形顶点
            p1 = center + np.array([self.a/2, -self.a/2, 0]) + RIGHT * self.b * np.cos(angle) * 0.5 + UP * self.b * np.sin(angle) * 0.5
            p2 = center + np.array([self.a/2, -self.a/2, 0]) + RIGHT * self.b * np.cos(angle + PI/2) * 0.5 + UP * self.b * np.sin(angle + PI/2) * 0.5

        # 简化的表示：用四个全等的直角三角形围绕中心
        # 直角边 a 水平，b 垂直
        tri = Polygon(
            LEFT * self.a/2 + DOWN * self.b/2,
            RIGHT * self.a/2 + DOWN * self.b/2,
            RIGHT * self.a/2 + UP * self.b/2,
            color=BLUE, stroke_width=2, fill_opacity=0.3
        )

        self.triangle = tri

        # 标注直角边
        a_label = Text("a", font=CHINESE_FONT, font_size=20, color=YELLOW)
        a_label.next_to(tri, DOWN, buff=0.1)

        b_label = Text("b", font=CHINESE_FONT, font_size=20, color=YELLOW)
        b_label.next_to(tri, LEFT, buff=0.1)

        c_label = Text("c", font=CHINESE_FONT, font_size=20, color=RED)
        c_label.next_to(tri, RIGHT + UP, buff=0.1)

        self.add(tri, a_label, b_label, c_label)
        self.a_label = a_label
        self.b_label = b_label
        self.c_label = c_label

    def show_square(self):
        """展示正方形"""
        problem = Text("用四个全等的直角三角形拼成弦图", font=CHINESE_FONT, font_size=22, color=WHITE)
        problem.move_to(UP * 3.2)

        self.play(Write(problem))
        self.wait(2)

        self.problem = problem

    def demonstrate_areas(self):
        """演示面积关系"""
        self.play(FadeOut(self.problem))

        # 大正方形面积 = (a+b)² = a² + 2ab + b²
        # = 4个三角形面积 + 中间小正方形面积
        # = 4 × (ab/2) + c² = 2ab + c²

        formula1 = Text("(a+b)² = a² + 2ab + b²", font=CHINESE_FONT, font_size=22, color=YELLOW)
        formula1.move_to(UP * 3.2)

        formula2 = Text("= 4×(ab/2) + c² = 2ab + c²", font=CHINESE_FONT, font_size=22, color=ORANGE)
        formula2.next_to(formula1, DOWN, buff=0.3)

        self.play(Write(formula1))
        self.wait(1)
        self.play(Write(formula2))
        self.wait(2)

        self.formula1 = formula1
        self.formula2 = formula2

    def show_conclusion(self):
        """展示勾股定理"""
        self.play(FadeOut(self.formula1), FadeOut(self.formula2))

        conclusion = Text("a² + b² = c²", font=CHINESE_FONT, font_size=36, color=GREEN)
        conclusion.move_to(UP * 3.2)

        theorem = Text("勾股定理：直角三角形的两直角边的平方和等于斜边的平方", font=CHINESE_FONT, font_size=18, color=WHITE)
        theorem.next_to(conclusion, DOWN, buff=0.3)

        self.play(FadeOut(self.formula1), FadeOut(self.formula2), Write(conclusion), Write(theorem))
        self.wait(3)
