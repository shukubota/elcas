import numpy as np
import matplotlib.pyplot as plt
from numpy import log10

#グラフ描画用関数の定義
def plot_graph(grad_predict,segment_predict,Nmax,show_estimation_line=True,show_theory_line=False,show_cumulative_graph=False):
    x= np.loadtxt("x.dat")
    y= np.loadtxt("y.dat")
    y2=np.loadtxt("y2.dat")
    y_c= np.cumsum(y[::-1])[::-1]
    coef = np.polyfit(log10(x),log10(y_c),1) #最小二乗法による係数の決定
    print('Computed results are below:')
    print('  gamma = '+str(1-coef[0]))
    print('  y-segment = '+str(log10(-coef[0])+coef[1]))
    
    fig1 = plt.figure(1)
    ax1 = fig1.add_subplot(111)
    ax1.plot(log10(x[y>0]),log10(y[y>0]),"ro",color="red",label="simulation") # シミュレーション結果のplot
    if show_theory_line==True:
        ax1.plot(log10(x[y2>0]),log10(y2[y2>0]),"b-",color="blue",label="theory") #理論値のplot
    if  show_estimation_line==True:
        ax1.plot(log10(x),-grad_predict*log10(x)+segment_predict,"b-",color="black",label='estimation') #estimationのplot
    ax1.set_xlabel(r"$x=\log_{10}{k}$")
    ax1.set_ylabel(r"$y=\log_{10}{P(k)}$")
    ax1.set_xlim([log10(1),log10(x[y>0].max())])
    ax1.set_ylim([log10(1/Nmax),log10(y.max())])
    ax1.grid(which='major',color='black',linestyle='-')
    ax1.legend()
    if show_cumulative_graph==True:
        fig2 = plt.figure(2)
        ax2 = fig2.add_subplot(111)
        ax2.loglog(x,y_c,"ro",color="red",label="simulation",basex=10,basey=10)
        ax2.loglog(x,10**(coef[1])*x**(coef[0]),color="black",label='fitting',basex=10,basey=10)
        ax2.set_xlabel(r"degree $k$")
        ax2.set_ylabel(r"cumulative $\Sigma P(k)$")
        #ax2.set_xlim([1,x[y>0].max()])
        ax2.legend()
    plt.show()
    return