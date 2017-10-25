import h5py

## Matlabファイルの読み込み
d = h5py.File("test.mat","r")

## 各フィールドの内容を表示
print(list(map(lambda x : ''.join((map(chr,x))),d["s/label"][:].T)))
print(d["s/samplingrate"][:],"\n")
print(d["s/DATA"][:,:,:],"\n")
print(d["s/average"][:,:],"\n")
