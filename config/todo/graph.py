import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import base64
from io import BytesIO
import numpy as np


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        if height != 0:
            # matplotlib.pyplot.annotate(text, xy, *args, **kwargs)    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html
            plt.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width()/2, height),
                        xytext=(0, 1),
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=10, fontname="Yu Gothic")


def Output_Graph():
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    img = buffer.getvalue()
    graph = base64.b64encode(img)
    graph = graph.decode("utf-8")
    buffer.close()
    return graph

def Plot_Graph(x,y):
    plt.switch_backend("AGG")
    plt.figure(figsize=(10,4.5))
    rects = plt.bar(x,y, width=0.8, color='skyblue')
    plt.xticks(rotation=60, fontname="Yu Gothic")
    # y軸の目盛りを指定（yにタスク数が入っているため、最大のタスク数+1をY軸で表示した）
    plt.yticks([i+1 for i in range(max(y)+1)], fontname="Yu Gothic", color='white')
    plt.title("完了済タスク数の推移", fontsize=15, fontname="Yu Gothic")
    # labelpad 軸からのラベルの距離 0：デフォルト位置,  正の値：軸から離して表示,  負の値：軸に近づけて表示
#    plt.ylabel("タスク数", fontname="Yu Gothic", fontsize=14, labelpad=0)
    # 図の枠線を消す
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    # 軸の目盛りを消す(ちょこっと出ている線)
    plt.gca().yaxis.set_ticks_position('none')
    plt.gca().xaxis.set_ticks_position('none')
    # x軸の日付フォーマットを変更している。Macなら「%-m/%-d」だが、windowsなら
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%#m/%#d"))

    autolabel(rects)

    plt.tight_layout()

    graph = Output_Graph()
    return graph
