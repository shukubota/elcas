#coding:utf-8

import numpy as np

def testfunc():
    x=np.arange(0,100,0.1)
    y=x*x*x

    return x,y




if __name__=="__main__":
	x,y=testfunc()
	np.save("x.npy",x)
	np.save("y.npy",y)











