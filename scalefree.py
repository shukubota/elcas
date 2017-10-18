#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import *
import time

def calc(nw):
	
	#node数
	N=len(nw)
	
	
	#link数
	K=0
	for i in range(0,len(nw)):
		K+=len(nw[i])
	

	#重み付け確率
	plist=[]
	for i in range(0,len(nw)):
		plist.append(len(nw[i])/float(K))
	
	#print 	plist

	
	#linkを追加するnodeのindex番号
	index=choice(range(0,N),m,replace=False,p=plist)
	#print index			


	for i in index:
		nw[i].append(N)
		
	nw.append(sorted(list(index)))

	#print nw


def plot(x,y):	
	plt.xscale("log")
	plt.yscale("log")
	plt.plot(x,y,"o",ms=2)



def dist(nw):
	x=range(m,Nmax)
	x=np.array(x)
	y=[]
	for i in x:
		count=0
		for j in range(0,len(nw)):
			if len(nw[j])==i:
				count+=1
		y.append(count)
	y=np.array(y)
	a=float(len(nw))
	y=y/a

	x2=x

	y2=2.*m*(m+1)/(x*x*x)

	plt.xlabel("k")
	plt.ylabel("P(k)")
	plot(x,y,)
	plot(x,y2)
	#plt.show()
	plt.xlim(0,10000)
	plt.savefig("fig.eps")


def testfunc():
	x=np.arange(0,100,0.1)
	y=x*x*x
	plot(x,y)
	plt.show()

	return x,y




def comgra(m):
	nw=[]

	for i in range(0,m):
		nwdum=[]
		for j in range(0,m):
			if i!=j:
				nwdum.append(j)
		nw.append(nwdum)
	return nw





if __name__=='__main__':
	start=time.time()


	
	#Initial Condition
	m=4
	K0=m*(m-1)
	N0=m
	Nmax=20000

	#node数mの完全グラフ
	nw=comgra(m)


	#Nmax回m本の枝を持つnodeを追加する
	for j in range(0,Nmax):
		print j
		calc(nw)

	#分布をかく
	dist(nw)

	elapsed_time=time.time()-start
	print "elapsed time",elapsed_time


