import numpy as np
import matplotlib.pyplot as plt

## 矩形波を三角多項式で近似する関数を定義
def square_wave(n):
    x = np.arange(-8, 8, 0.001)
    y = [0 for z in x]  # リスト内包記法
    for k in range(n+1):
        if k % 2 == 1:
            y += (4 / (np.pi * k)) * np.sin(x * k)
    plt.plot(x, y, label = "n = " + str(n))
        # plt.show()されるまでグラフは表示されない


## 上で定義した関数を、引数を変えつつ呼び出す
square_wave(1)
square_wave(5)
square_wave(11)
square_wave(101)
square_wave(10001)

plt.legend()  # グラフに凡例を表示させるように設定
plt.show()  # これまでにplotしたグラフを表示
