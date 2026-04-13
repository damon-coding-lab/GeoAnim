# GeoAnim - AI 数学动画生成器

> 用自然语言描述几何问题，AI 自动生成专业数学动画

[English](README_en.md) | 简体中文

---

## 功能特点

- **自然语言输入**：用中文描述几何问题，即可生成动画
- **AI 智能匹配**：DeepSeek AI 理解几何描述，匹配最佳模型
- **Manim 动画引擎**：基于 3Blue1Brown 的 Manim 渲染高质量动画
- **11+ 预置模型**：涵盖初中几何核心模型
- **开源可扩展**：轻松添加新的几何模型

---

## 效果演示

输入描述：
```
正方形ABCD，对角线AC上有一动点P，连接BP使BP垂直于AC
```

AI 自动分析并生成对应的几何动画。

---

## 预置模型

| 模型 | 章节 | 描述 |
|------|------|------|
| 手拉手模型 | 七下·全等三角形 | 两个三角形通过旋转重合 |
| 将军饮马 | 八上·轴对称 | 河边饮马最短路径问题 |
| 半角模型 | 九上·旋转 | 正方形中的半角旋转全等 |
| 隐圆模型 | 九上·圆 | 到定点距离等于定长的点的轨迹 |
| 一线三等角 | 八下·四边形 | 同位角相等推出平行线 |
| 倍长中线 | 八上·全等三角形 | 倍长中线构造全等三角形 |
| 费马点 | 九下·锐角三角函数 | 使PA+PB+PC最小的点 |
| 弦图模型 | 八下·勾股定理 | 弦图证明勾股定理 |
| 脚拉脚模型 | 九上·圆 | 圆外一点的切线长定理 |
| 胡不归模型 | 中考压轴 | 加权最短路径问题 |
| 切割线定理 | 九上·圆 | 切线长与割线的乘积关系 |

---

## 快速开始

### 环境要求

- Python 3.9+
- FFmpeg
- DeepSeek API Key（免费获取）

### 安装

```bash
# 克隆项目
git clone https://github.com/YOUR_USERNAME/geoanim.git
cd geoanim

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 配置 API Key
export DEEPSEEK_API_KEY="your-api-key-here"

# 运行
python app.py
```

### 使用

1. 打开浏览器访问 `http://localhost:5001`
2. 在输入框中输入几何描述
3. 点击"生成动画"，AI 将分析并匹配最佳模型
4. 点击推荐模型卡片播放视频

---

## 开发指南

### 添加新模型

1. 在 `scenes/` 目录创建新的 Manim 场景文件

```python
from manim import *

class MyModel(Scene):
    def construct(self):
        # 你的几何动画代码
        pass
```

2. 在 `app.py` 的 `PRESET_MODELS` 中注册

```python
"my_model": {
    "name": "我的模型",
    "chapter": "年级·章节",
    "description": "模型描述",
    "video": "my_model/720p30/MyModel.mp4"
}
```

3. 在 `AVAILABLE_MODELS` 中添加关键词映射

```python
"我的模型关键词": "my_model",
```

4. 渲染视频

```bash
python -m manim render scenes/my_model.py MyModel -qm
```

### API 调用

```python
import requests

response = requests.post(
    "http://localhost:5001/api/generate",
    json={"description": "你的几何描述"}
)
print(response.json())
```

---

## 技术栈

| 组件 | 技术 |
|------|------|
| 动画引擎 | Manim Community v0.19+ |
| AI 模型 | DeepSeek Chat API |
| Web 框架 | Flask |
| 视频渲染 | FFmpeg |
| 编程语言 | Python 3.9+ |

---

## 项目结构

```
geoanim/
├── scenes/              # Manim 动画场景
│   ├── hand_in_hand.py
│   ├── general_drink_horse.py
│   └── ...
├── media/               # 渲染输出的视频
├── templates/           # Flask 模板
├── static/              # 静态资源
├── app.py               # Web 应用主文件
└── README.md
```

---

## 贡献

欢迎提交 Issue 和 Pull Request！

---

## 许可证

MIT License

---

## 联系方式

- GitHub Issues: https://github.com/YOUR_USERNAME/geoanim/issues

---

*Built with ❤️ using Manim + DeepSeek AI*
