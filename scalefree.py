#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import *
import time

def calc(nw,a,m,type=1): #ネットワーク配列nwにm本のlinkを持つnodeを1個追加する関数type::1:重み付け確率,2:一様確率
	
	#node数
	N=len(nw)
	
	
	#link数
	K=0
	for i in range(0,len(nw)):
		K+=len(nw[i])+a
	

	#重み付け確率を決める
	plist=[]
	if type==1:
		for i in range(0,len(nw)):
			plist.append((len(nw[i])+a)/float(K))
	else:
		for i in range(0,len(nw)):
			plist.append(1./len(nw))

	
	
	#linkを追加するnodeのindex番号を決める
	index=choice(range(0,N),m,replace=False,p=plist)


	#ネットワークに新しいnodeを1個追加する
	for i in index:
		nw[i].append(N)
		
	nw.append(sorted(list(index)))





def dist(nw):  #ネットワーク配列nwから次数分布の配列を作る関数
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

	y2=theofunc(m,a,x)

	np.save("x.npy",x)
	np.save("y.npy",y)
	np.save("y2.npy",y2)


def comgra(m): #次数mの完全グラフを作る関数
	nw=[]

	for i in range(0,m):
		nwdum=[]
		for j in range(0,m):
			if i!=j:
				nwdum.append(j)
		nw.append(nwdum)
	return nw




def theofunc(m,a,x):
	func=2.*m*(m+1)/(x*x*x)    #<========手で計算した理論値の関数を入れてみる,変えて良い
	return func




if __name__=='__main__':
	start=time.time()


	####################
	#シミュレーションの設定(次数mの完全グラフを初期状態にとる)
	###################
	m=4  #追加するnodeの持つlinkの本数   <=============変えて良い
	Nmax=10000 #nodeの最大値				<=============変えて良い
	a=0. #重み付け確率を計算する時のパラメータ<=========変えて良い



	#node数mの完全グラフを作成
	nw=comgra(m)
	######################
	#####################



	
	
	
	#####################
	#ネットワークを成長させる
	####################

	#Nmax回m本の枝を持つnodeを追加する
	for j in range(0,Nmax):
		print j

		#関数calcでネットワークnwにnodeを追加していく
		#3個目の引数(重み付け確率でシミュレーション:1,一様確率でシミュレーション:2)
		calc(nw,a,m,1) #<===============3個目の引数だけ変えて良い
	
	np.save("nwdata.npy",nw)
		


	#分布を計算する
	dist(nw)
	#print nw
	flag=["scalefree"]
	np.save("flag.npy",flag)

	elapsed_time=time.time()-start
	print "elapsed time",elapsed_time


