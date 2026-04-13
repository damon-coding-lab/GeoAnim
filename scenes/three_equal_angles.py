"""
一线三等角模型
八下·四边形
"""

from manim import *
import numpy as np

CHINESE_FONT = "Heiti SC"


class ThreeEqualAngles(Scene):
    def construct(self):
        self.setup_scene()
        self.show_equal_angles()
        self.demonstrate_parallel()
        self.show_conclusion()

    def setup_scene(self):
        """设置场景"""
        # 一条水平线（截线）
        self.line_l = Line(LEFT * 5, RIGHT * 5, color=WHITE, stroke_width=2)
        self.line_l.shift(DOWN * 0.5)

        # 三条被截的线
        self.line_a = Line(UP * 3, DOWN * 2, color=BLUE, stroke_width=2)
        self.line_a.shift(LEFT * 2)

        self.line_b = Line(UP * 3, DOWN * 2, color=BLUE, stroke_width=2)

        self.line_c = Line(UP * 3, DOWN * 2, color=BLUE, stroke_width=2)
        self.line_c.shift(RIGHT * 2)

        # 标注
        self.line_a_label = Text("l₁", font=CHINESE_FONT, font_size=20, color=BLUE).next_to(self.line_a, UP)
        self.line_b_label = Text("l₂", font=CHINESE_FONT, font_size=20, color=BLUE).next_to(self.line_b, UP)
        self.line_c_label = Text("l₃", font=CHINESE_FONT, font_size=20, color=BLUE).next_to(self.line_c, UP)

        self.line_l_label = Text("直线l", font=CHINESE_FONT, font_size=20, color=WHITE).next_to(self.line_l, RIGHT)

        self.add(self.line_l, self.line_a, self.line_b, self.line_c)
        self.add(self.line_a_label, self.line_b_label, self.line_c_label, self.line_l_label)

    def show_equal_angles(self):
        """展示三个相等的角"""
        # 计算截线与各线的交点
        l_center = self.line_l.get_center()
        l_angle = self.line_l.get_angle()

        a_pos = self.line_a.get_center()
        b_pos = self.line_b.get_center()
        c_pos = self.line_c.get_center()

        # 标注∠1, ∠2, ∠3
        # 在l和l1的交点处标注∠1
        intersect1 = np.array([l_center[0] + (a_pos[1] - l_center[1]) * np.tan(l_angle + PI/2), a_pos[1], 0])

        angle1 = Text("∠1", font=CHINESE_FONT, font_size=18, color=YELLOW)
        angle1.move_to(LEFT * 1.5 + UP * 0.8)

        angle2 = Text("∠2", font=CHINESE_FONT, font_size=18, color=YELLOW)
        angle2.move_to(UP * 0.8)

        angle3 = Text("∠3", font=CHINESE_FONT, font_size=18, color=YELLOW)
        angle3.move_to(RIGHT * 1.5 + UP * 0.8)

        equal_text = Text("∠1 = ∠2 = ∠3", font=CHINESE_FONT, font_size=24, color=ORANGE)
        equal_text.move_to(UP * 3.2)

        self.play(Write(angle1), Write(angle2), Write(angle3))
        self.wait(1)
        self.play(Write(equal_text))
        self.wait(2)

        self.equal_text = equal_text
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def demonstrate_parallel(self):
        """由同位角相等推出平行"""
        self.play(FadeOut(self.equal_text), FadeOut(self.angle1), FadeOut(self.angle2), FadeOut(self.angle3))

        # 结论
        parallel_text = Text("同位角相等 → 两直线平行", font=CHINESE_FONT, font_size=22, color=GREEN)
        parallel_text.move_to(UP * 3.2)

        # 显示l1 // l2 // l3
        conclusion = Text("l₁ ∥ l₂ ∥ l₃", font=CHINESE_FONT, font_size=28, color=YELLOW)
        conclusion.move_to(UP * 3.2 + DOWN * 0.5)

        self.play(Write(parallel_text))
        self.wait(1.5)
        self.play(Write(conclusion))
        self.wait(2)

        self.parallel_text = parallel_text
        self.conclusion = conclusion

    def show_conclusion(self):
        """总结"""
        final = Text("一线等角 → 平行线", font=CHINESE_FONT, font_size=24, color=YELLOW)
        final.move_to(UP * 3.2)

        self.play(FadeOut(self.parallel_text), FadeOut(self.conclusion))
        self.play(Write(final))
        self.wait(3)
