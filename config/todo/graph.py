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

def Plot_BarGraph(x,y):
    plt.switch_backend("AGG")
    plt.figure(figsize=(8,4))
    bar_graph = plt.bar(x,y, width=0.8, color='skyblue')
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
    # 棒グラフの上に値を表示（自作のautolabel関数）
    autolabel(bar_graph)
    plt.tight_layout()

    graph = Output_Graph()
    return graph



def Plot_PieChart(p,l):
    # 日本語を表示する設定
    plt.rcParams['font.family'] = 'Yu Gothic'
    c = ["skyblue", 'powderblue', 'lightcyan', 'cadetblue',"cornflowerblue"]
    plt.switch_backend("AGG")
    plt.figure(figsize=(4,4))
    # 円グラフを描画。デフォルトは3時の方向から開始
    # autopoctで比率を表示するようにしている。小数点第一位まで表示するときはautopct='%.1f%%'。
    # counterclock=Falseで時計回りに、startangle=90で12時の方向から開始、radiusで半径を変更(2で2倍？)
    plt.pie(p, autopct="%d%%", labels = l, colors = c, counterclock=False, startangle=90, radius=0.8, center=(0, 0))
    plt.title('内訳', fontsize=15)
    
    graph = Output_Graph()
    return graph