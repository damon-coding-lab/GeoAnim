"""
GeoAnim - AI 数学动画生成器
Flask Web 应用
"""

import os
import json
import re
from pathlib import Path

import requests
from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 配置
VIDEO_DIR = Path("media/videos")
SCENES_DIR = Path("scenes")

# DeepSeek API 配置
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
DEEPSEEK_API_URL = "https://api.deepseek.com/chat/completions"

# 确保目录存在
VIDEO_DIR.mkdir(parents=True, exist_ok=True)

# 预置模型列表
PRESET_MODELS = {
    "hand_in_hand": {
        "name": "手拉手模型",
        "chapter": "七下·全等三角形",
        "description": "两个三角形通过旋转重合",
        "video": "hand_in_hand/1080p60/HandInHand.mp4"
    },
    "tangent_secant": {
        "name": "切割线定理",
        "chapter": "九上·圆",
        "description": "切线长与割线的乘积关系",
        "video": "tangent_secant/720p30/TangentSecant.mp4"
    },
    "general_drink_horse": {
        "name": "将军饮马",
        "chapter": "八上·轴对称",
        "description": "河边饮马最短路径问题",
        "video": "general_drink_horse/1080p60/GeneralDrinkHorse.mp4"
    },
    "half_angle_square": {
        "name": "半角模型（正方形）",
        "chapter": "九上·旋转",
        "description": "正方形中的半角旋转全等",
        "video": "half_angle_square/1080p60/HalfAngleSquare.mp4"
    },
    "hidden_circle": {
        "name": "隐圆模型",
        "chapter": "九上·圆",
        "description": "到定点距离等于定长的点的轨迹",
        "video": "hidden_circle/1080p60/HiddenCircle.mp4"
    },
    "three_equal_angles": {
        "name": "一线三等角",
        "chapter": "八下·四边形",
        "description": "同位角相等推出平行线",
        "video": "three_equal_angles/1080p60/ThreeEqualAngles.mp4"
    },
    "median_doubling": {
        "name": "倍长中线",
        "chapter": "八上·全等三角形",
        "description": "倍长中线构造全等三角形",
        "video": "median_doubling/720p30/MedianDoubling.mp4"
    },
    "fermats_point": {
        "name": "费马点",
        "chapter": "九下·锐角三角函数",
        "description": "使PA+PB+PC最小的费马点",
        "video": "fermats_point/720p30/FermatsPoint.mp4"
    },
    "chord_diagram": {
        "name": "弦图模型",
        "chapter": "八下·勾股定理",
        "description": "弦图证明勾股定理",
        "video": "chord_diagram/720p30/ChordDiagram.mp4"
    },
    "foot_pull_foot": {
        "name": "脚拉脚模型",
        "chapter": "九上·圆",
        "description": "圆外一点的切线长定理",
        "video": "foot_pull_foot/720p30/FootPullFoot.mp4"
    },
    "hubigui": {
        "name": "胡不归模型",
        "chapter": "中考压轴",
        "description": "加权最短路径问题",
        "video": "hubigui/720p30/Hubigui.mp4"
    }
}

# 可生成的模型列表
AVAILABLE_MODELS = {
    "手拉手": "hand_in_hand",
    "将军饮马": "general_drink_horse",
    "半角": "half_angle_square",
    "隐圆": "hidden_circle",
    "一线三等角": "three_equal_angles",
    "倍长中线": "median_doubling",
    "费马": "fermats_point",
    "弦图": "chord_diagram",
    "脚拉脚": "foot_pull_foot",
    "胡不归": "hubigui",
    "切割线": "tangent_secant",
}


@app.route("/")
def index():
    """主页"""
    return render_template("index.html", models=PRESET_MODELS)


@app.route("/api/models")
def get_models():
    """获取所有预置模型"""
    return jsonify(PRESET_MODELS)


@app.route("/api/models/<model_id>/video")
def get_model_video(model_id):
    """获取模型视频"""
    if model_id not in PRESET_MODELS:
        return jsonify({"error": "模型不存在"}), 404
    
    video_path = VIDEO_DIR / PRESET_MODELS[model_id]["video"]
    if not video_path.exists():
        return jsonify({"error": "视频文件不存在"}), 404
    
    return send_file(video_path, mimetype="video/mp4")


@app.route("/api/generate", methods=["POST"])
def generate():
    """AI生成动画"""
    data = request.json
    description = data.get("description", "")
    
    if not description:
        return jsonify({"error": "请输入几何描述"}), 400
    
    if not DEEPSEEK_API_KEY:
        return jsonify({
            "error": "AI服务未配置",
            "hint": "请设置 DEEPSEEK_API_KEY 环境变量"
        }), 500
    
    # 调用 DeepSeek AI 分析
    try:
        response = call_deepseek_api(description)
        return jsonify({
            "success": True,
            "ai_response": response.get("content", ""),
            "matched_model": response.get("parsed", None)
        })
    except Exception as e:
        return jsonify({
            "error": f"AI调用失败: {str(e)}"
        }), 500


def call_deepseek_api(description: str) -> dict:
    """调用 DeepSeek API"""
    
    system_prompt = """你是一个几何数学助手。用户会输入一个几何问题的描述，你需要分析这个描述，并从以下模型中选择最匹配的一个：

可用模型：
- hand_in_hand: 手拉手模型 - 两个全等三角形通过旋转重合
- general_drink_horse: 将军饮马 - 河边饮马最短路径问题
- half_angle_square: 半角模型 - 正方形或等边三角形中的半角旋转
- hidden_circle: 隐圆模型 - 到定点距离等于定长的点的轨迹
- three_equal_angles: 一线三等角 - 一条线上三个相等角度
- median_doubling: 倍长中线 - 倍长中线构造全等三角形
- fermats_point: 费马点 - 使PA+PB+PC最小的点
- chord_diagram: 弦图模型 - 勾股定理的几何证明
- foot_pull_foot: 脚拉脚模型 - 圆的切线长定理
- hubigui: 胡不归模型 - 加权最短路径问题
- tangent_secant: 切割线定理 - 切线长与割线的乘积关系

请分析用户描述，选择最匹配的模型，返回JSON格式：
{
  "model_id": "模型ID",
  "model_name": "模型名称",
  "matched_keywords": ["匹配的关键词"],
  "explanation": "解释为什么选择这个模型"
}"""

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
    }
    
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"用户描述：{description}"}
        ],
        "max_tokens": 500,
        "temperature": 0.1
    }
    
    resp = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload, timeout=30)
    
    if resp.status_code != 200:
        raise Exception(f"API返回错误: {resp.status_code} - {resp.text}")
    
    result = resp.json()
    content = result["choices"][0]["message"]["content"]
    
    # 解析 JSON
    try:
        # 尝试直接解析
        parsed = json.loads(content)
    except json.JSONDecodeError:
        # 尝试提取 JSON
        json_match = re.search(r'\{[^{}]*\}', content, re.DOTALL)
        if json_match:
            parsed = json.loads(json_match.group())
        else:
            # 备用关键词匹配
            parsed = fallback_keyword_match(description)
    
    return {"content": content, "parsed": parsed}


def fallback_keyword_match(text: str) -> dict:
    """备用关键词匹配"""
    for keyword, model_id in AVAILABLE_MODELS.items():
        if keyword in text:
            return {
                "model_id": model_id,
                "model_name": PRESET_MODELS[model_id]["name"],
                "matched_keywords": [keyword],
                "explanation": f"关键词 '{keyword}' 匹配"
            }
    return None


if __name__ == "__main__":
    ai_status = "✅ DeepSeek 已配置" if DEEPSEEK_API_KEY else "❌ 未配置"
    print(f"""
╔══════════════════════════════════════════════╗
║     GeoAnim - AI 数学动画生成器               ║
║     http://localhost:5001                     ║
║     AI状态: {ai_status:<33}║
╚══════════════════════════════════════════════╝
    """)
    app.run(host="127.0.0.1", port=5001, debug=False)
