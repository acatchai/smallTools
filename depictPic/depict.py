import matplotlib.pyplot as plt

# 可选绘图风格
style = ["seaborn-v0_8-colorblind",
         "fivethirtyeight",
         "dark_background",
         "grayscale",]

config = {
    "font.family" : 'serif',        # 全局字体家族
    "mathtext.fontset" : 'stix',    # 数字公式字体集
    "font.serif" : ['SimSun'],      # serif家族的候选字体列表 (宋体)
    "axes.unicode_minus" : False,   # 使用ASCII里的负号代替Unicode 防止不支持
    "savefig.dpi" : 1000,           # 图片像素
    "figure.dpi"  : 1000,           # 分辨率
    "figure.figsize" : (6,6)        # 图形大小 英寸
}



plt.style.use(style[0])     # 设置图像风格
plt.figure(6,6)
