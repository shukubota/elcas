#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt



def plot(x,y,type):
	plt.xlabel("k")
	plt.ylabel("P(k)")
	
	plt.xscale("log")
	plt.yscale("log")

	if type==1:
		plt.plot(x,y,"o",ms=2)
		xmax=np.min(np.where(y==np.min(y)))
		plt.xlim(0,xmax*2.)
	else:
		plt.plot(x,y)







if __name__=="__main__":
	x=np.load("x.npy")
	y=np.load("y.npy")
	y2=np.load("y2.npy")
	plot(x,y,2)
	#plot(x,y2,2)
	plt.savefig("fig.eps")










