#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import *
import time

def calc(nw,a,type=1):
	
	#node数
	N=len(nw)
	
	
	#link数
	K=0
	for i in range(0,len(nw)):
		K+=len(nw[i])+a
	

	#重み付け確率
	plist=[]
	if type==1:
		for i in range(0,len(nw)):
			plist.append((len(nw[i])+a)/float(K))
	else:
		for i in range(0,len(nw)):
			plist.append(1./len(nw))

	
	
	#linkを追加するnodeのindex番号
	index=choice(range(0,N),m,replace=False,p=plist)


	for i in index:
		nw[i].append(N)
		
	nw.append(sorted(list(index)))





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
	b=float(len(nw))
	y=y/b

	x2=x

	y2=2.*m*(m+1)/(x*x*x)

	np.save("x.npy",x)
	np.save("y.npy",y)
	np.save("y2.npy",y2)


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
	Nmax=1000
	a=10.



	#node数mの完全グラフ
	nw=comgra(m)


	#Nmax回m本の枝を持つnodeを追加する
	for j in range(0,Nmax):
		print j
		#重み付け確率でシミュレーション
		calc(nw,a,1)
		#一様確率でシミュレーション
		#calc(nw,a,2)
	
	np.save("nwdata.npy",nw)
		


	#分布を計算する
	dist(nw)
	#print nw

	elapsed_time=time.time()-start
	print "elapsed time",elapsed_time


