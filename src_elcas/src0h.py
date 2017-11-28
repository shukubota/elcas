import numpy as np
import matplotlib.pyplot as plt
from numpy import log10

#グラフ描画用関数の定義
def plot_simulated_data(x,y,graph_style):
    fig1 = plt.figure(0)
    ax = fig1.add_subplot(111)
    if graph_style=="normal":
        ax.plot(x,y,"ro",label="simulation")
        ax.set_xlabel(r"$X=k$")
        ax.set_ylabel(r"$Y=P(k)$")
    elif graph_style=="ylog":
        ax.plot(x[y>0],log10(y[y>0]),"ro",label="simulation")
        ax.set_xlabel(r"$X=k$")
        ax.set_ylabel(r"$Y=\log_{10}{\ P(k)}}$")
    elif graph_style=="xlog-ylog":
        ax.plot(log10(x[y>0]),log10(y[y>0]),"ro",label="simulation")
        ax.set_xlabel(r"$X=\log_{10}{k}$")
        ax.set_ylabel(r"$Y=\log_{10}{\ P(k)}}$")
    elif graph_style=="xlog-yloglog":
        ax.plot(log10(x[y>0]),log10(-log10(y[y>0])),"ro",label="simulation")
        ax.set_xlabel(r"$X=\log_{10}{k}$")
        ax.set_ylabel(r"$Y=\log_{10}{(-\log_{10}{\ P(k)})}$")
    else:
        print("Error! graph_styleが認識できません.")
    ax.legend()        
    plt.show()
    return