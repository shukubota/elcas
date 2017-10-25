import scipy.io

## Matlabファイルの読み込み
d = scipy.io.loadmat("test.mat")

## Matlab構造体の取得
s = d["s"][0,0]

## 各フィールドの内容を表示
print(s["label"],"\n")
print(s["samplingrate"],"\n")
print(s["DATA"],"\n")
print(s["average"],"\n")
