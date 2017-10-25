#coding:utf-8

import numpy as np

def testfunc():
    x=np.arange(0.01,100,0.1)
    y=pow(x,3)#<======ここでy=x^3としている、変えて良い

    return x,y




if __name__=="__main__":
	x,y=testfunc()
	np.save("x.npy",x)
	np.save("y.npy",y)
	flag=["test"]
	np.save("flag.npy",flag)












