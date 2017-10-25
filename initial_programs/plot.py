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
		ydum=y[y>0]
		print ydum
		ymin=np.min(ydum)/10.
		plt.ylim(ymin,)
	else:
		plt.plot(x,y)



	#plt.xlim()



if __name__=="__main__":

	flag=np.load("flag.npy")
	
	if flag[0]=="scalefree":
		y2=np.load("y2.npy")
	
	x=np.load("x.npy")
	y=np.load("y.npy")
	
	
	plot(x,y,1)
	if flag[0]=="scalefree":
		plot(x,y2,2)

	plt.savefig("fig.eps")









