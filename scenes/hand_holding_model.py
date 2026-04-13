"""
手拉手模型 - 动态几何演示
Manim Community v0.19.0
运行命令: /usr/bin/python3 -m manim scenes/hand_holding_model.py HandHoldingModel -ql
"""

from manim import *
import math


class HandHoldingModel(Scene):
    """
    手拉手模型（旋转全等）

    数学原理：
    两个三角形有公共顶点，一个三角形固定，另一个绕公共顶点旋转。
    当旋转角度等于两个三角形的夹角时，两三角形完全重合。

    关键条件：两边及其夹角相等（SAS）
    """

    def construct(self):
        # 颜色配置
        BLUE_TRIPLE = "#4A90D9"    # 固定三角形颜色
        RED_TRIPLE = "#D94A4A"     # 旋转三角形颜色
        YELLOW_POINT = "#F5D742"   # 公共顶点颜色
        GREEN_HIGHLIGHT = "#4AD97A"  # 高亮颜色

        # ========== 第一幕：绘制固定三角形 ABC ==========
        title = Text("手拉手模型", font_size=48, color=WHITE)
        title.to_edge(UP)
        subtitle = Text("两边及其夹角相等 → SAS → 全等", font_size=24, color=GRAY)
        subtitle.next_to(title, DOWN)
        self.play(Write(title), Write(subtitle))
        self.wait(1)

        # 三角形ABC的三个顶点（固定）
        # A是公共顶点，B和C是另外两点
        A = ORIGIN
        B = 3 * LEFT + 1.5 * UP
        C = 3 * RIGHT + 1.5 * UP

        # 创建三角形ABC
        triangle_abc = Polygon(A, B, C, color=BLUE_TRIPLE, fill_opacity=0.2, stroke_width=3)
        label_a = Text("A", font_size=20, color=YELLOW_POINT).next_to(A, DOWN + RIGHT)
        label_b = Text("B", font_size=20, color=BLUE_TRIPLE).next_to(B, UP + LEFT)
        label_c = Text("C", font_size=20, color=BLUE_TRIPLE).next_to(C, UP + RIGHT)

        self.play(Create(triangle_abc), Write(label_a), Write(label_b), Write(label_c))
        self.wait(1)

        # ========== 第二幕：绘制旋转三角形 ADE ==========
        # 三角形ADE与ABC全等，但初始角度不同
        # D点在BC下方，E点在AC下方，形成"手拉手"姿态
        D = 3 * LEFT + 2 * DOWN
        E = 3 * RIGHT + 2 * DOWN

        triangle_ade = Polygon(A, D, E, color=RED_TRIPLE, fill_opacity=0.2, stroke_width=3)
        label_d = Text("D", font_size=20, color=RED_TRIPLE).next_to(D, DOWN + LEFT)
        label_e = Text("E", font_size=20, color=RED_TRIPLE).next_to(E, DOWN + RIGHT)

        self.play(Create(triangle_ade), Write(label_d), Write(label_e))
        self.wait(1)

        # ========== 第三幕：标注公共顶点 ==========
        # 公共顶点A用高亮圆圈标注
        highlight_circle = Circle(color=YELLOW_POINT, radius=0.15).move_to(A)
        public_vertex_label = Text("公共顶点", font_size=16, color=YELLOW_POINT).next_to(highlight_circle, RIGHT, buff=0.3)
        arrow_to_A = Arrow(public_vertex_label.get_bottom(), highlight_circle.get_top(), buff=0.1, color=YELLOW_POINT)

        self.play(Create(highlight_circle), Write(public_vertex_label), Create(arrow_to_A))
        self.wait(1)

        # ========== 第四幕：标注"手拉手"的边 ==========
        # 边AB和边AD形成"手拉手"的"手臂"
        arm_ab = Line(A, B, color=BLUE_TRIPLE, stroke_width=4)
        arm_ad = Line(A, D, color=RED_TRIPLE, stroke_width=4)
        arm_label = Text("相等边AB", font_size=16, color=BLUE_TRIPLE).move_to(2.5 * LEFT + 0.3 * UP)
        arm_label_2 = Text("相等边AD", font_size=16, color=RED_TRIPLE).move_to(2.5 * LEFT + 0.3 * DOWN)

        self.play(Create(arm_ab), Create(arm_ad))
        self.wait(0.5)
        self.play(Write(arm_label), Write(arm_label_2))
        self.wait(1)

        # ========== 第五幕：旋转三角形ADE ==========
        # 旋转120度（演示全等过程）
        rotation_angle = 120 * DEGREES

        # 创建旋转动画
        self.play(
            FadeOut(arm_label),
            FadeOut(arm_label_2),
            FadeOut(public_vertex_label),
            FadeOut(arrow_to_A)
        )
        self.wait(0.5)

        # 旋转组：包含三角形和标签
        rotation_group = VGroup(triangle_ade, label_d, label_e)

        # 文字提示
        rotate_text = Text("绕A点旋转...", font_size=24, color=YELLOW_POINT)
        rotate_text.to_edge(DOWN)
        self.play(Write(rotate_text))

        # 执行旋转
        self.play(
            Rotate(
                rotation_group,
                angle=rotation_angle,
                about_point=A,
                run_time=4,
                rate_func=linear
            )
        )
        self.wait(0.5)
        self.play(FadeOut(rotate_text))

        # ========== 第六幕：显示全等结论 ==========
        # 重合时高亮显示
        self.play(triangle_abc.animate.set_stroke(GREEN_HIGHLIGHT, width=5))
        self.play(triangle_ade.animate.set_stroke(GREEN_HIGHLIGHT, width=5))
        self.wait(0.5)

        # 结论文字
        conclusion = Text("△ADE ≌ △ABC", font_size=36, color=GREEN_HIGHLIGHT)
        conclusion.move_to(3 * RIGHT + 2 * DOWN)
        reason = Text("（SAS：两边及其夹角相等）", font_size=20, color=GRAY)
        reason.next_to(conclusion, DOWN)

        self.play(Write(conclusion), Write(reason))
        self.wait(2)

        # ========== 终幕：总结 ==========
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait(0.5)

        summary_title = Text("手拉手模型", font_size=44, color=WHITE)
        summary_title.to_edge(UP + LEFT)
        self.play(Write(summary_title))

        summary_points = [
            "✓ 有公共顶点",
            "✓ 有两组相等边",
            "✓ 夹角相等 → SAS全等",
            "✓ 旋转后可完全重合"
        ]

        summary_text = VGroup(*[Text(point, font_size=24, color=GREEN_HIGHLIGHT) for point in summary_points])
        summary_text.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        summary_text.next_to(summary_title, DOWN, aligned_edge=LEFT)
        summary_text.shift(RIGHT * 0.5)

        for point in summary_text:
            self.play(Write(point))
            self.wait(0.3)

        self.wait(2)
