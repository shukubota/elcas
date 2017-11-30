q(k)の形を変化させたときの次数分布の変化 2017.11.30 H. Masui

設定:
    m=4
    N=1000

* q(k) ∝ k (BAモデル)
* q(k) ∝ k**2
* q(k) ∝ k**0.5
* q(k) ∝ 1 (= k**0)
* q(k) ∝ 1/k (=k**-1)
* q(k) ∝ log10(k)
* q(k) ∝ 1.5**k

上の各caseに対して
* k vs p(k)
* k vs log p(k)
* log k vs log p(k)
* log k vs log log p(k)
のplotをpngで描いてます

(※ファイル名接頭辞はalpha->ベキ， log10->log10, 1.5power-> 1.5**kを表しています)

参考までに．