#!/usr/bin/python
# -*- coding: utf-8 -*-
"""library
    * よく使うものを集めておく。より良いものがあれば更新する。
    * 参考にしたものがあれば必ず引用元を記載する

Todo:

    * LIS
    * BIT
"""

"""nCr mod(prime number)
    nCr mod

    Args:
        n (int) : nCr のn
        r (int) : nCr のr
        modn (int) : 余りをとる

    Returns:
        int: nCr % modの値。

    Examples:
        init_cmbで配列を作った後で使うこと。

    Note:
        N<10**9, r<10**5のときなどは、NMAX＝10**9にしない。TLEする。
    　　（N-r)! * g2(r)として計算すること。分子は手で構築すればO(10**5)ですむ。
"""
def cmb(n, r, modn):
    if (r < 0 or r > n):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % modn

"""init function for nCr mod(prime number)
    nCr mod

    Args:
        Nmax (int) : nとしてありうるMAX値。2*10**5くらいじゃないの想定。

    Returns:
        g1(list(int)): n! mod の値。
        g2(list(int)): 1/n! mod の値。

    Examples:
        init_cmbで配列を作った後で使うこと。
        g1,g2 = init_cmb(100001)

    Note:
        注意事項などを記載
"""

def init_cmb(Nmax):
    #mod = 10**9+7 #出力の制限
    g1 = [1, 1] # 元テーブル
    g2 = [1, 1] # 逆元テーブル
    inverse = [0, 1] #逆元テーブル計算用テーブル

    for i in range(2, Nmax + 1):
        g1.append((g1[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod//i)) % mod)
        g2.append((g2[-1] * inverse[-1]) % mod)
    return g1, g2
