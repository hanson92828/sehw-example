import matplotlib.pyplot as plt
from collections import defaultdict

plt.ion()  # 開啟互動模式（允許圖表被重繪）

# 初始化圖表
fig, ax = plt.subplots()

def update_pie_chart(data):
    ax.clear()  # 清除舊圖

    # 分類加總
    category_sum = defaultdict(int)
    for price, category in data:
        category_sum[category] += price

    labels = category_sum.keys()
    sizes = category_sum.values()

    # 畫圓餅圖
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.set_title("Updated Pie Chart")

    plt.draw()
    plt.pause(0.1)  # 小暫停讓重繪生效