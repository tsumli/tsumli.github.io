---
title: "FNet: Mixing Tokens with Fourier Transforms を読む"
date: 2021-06-03T07:11:44Z
slug: "FNet"
description: ""
keywords: ["FNet", "Fourier"]
draft: false
tags: ["Fourier", "paper"]
url: "blog/paper/FNet/"
math: true
toc: true
---

[**FNet: Mixing Tokens with Fourier Transforms**](https://arxiv.org/abs/2105.03824)   
[Thorp et al. arXiv 2020] という論文を読んでいきます. (本文中の図は論文より引用).

## Model
### Background: discrete Fourier Transforms
シークエンス $\lbrace x_n \rbrace$ $\left( n \in [0, N-1] \right)$ が与えられたとき, 
discrete Fourier Transform (DFT) は次のように表される.

\begin{align*}
X_k &= \sum_{n=0}^{N-1} x_n \exp(-\frac{2\pi i}{N}nk), & 0\leq k \leq N-1 
\end{align*}

DFTを計算する方法は主に2つ
1. FFT  
[Cooley-Tukeyアルゴリズム](https://ja.wikipedia.org/wiki/%E9%AB%98%E9%80%9F%E3%83%95%E3%83%BC%E3%83%AA%E3%82%A8%E5%A4%89%E6%8F%9B)
2. DFT matrixを入力シークエンスに掛ける  
[Vandermonde matrix](https://ja.wikipedia.org/wiki/%E3%83%B4%E3%82%A1%E3%83%B3%E3%83%87%E3%83%AB%E3%83%A2%E3%83%B3%E3%83%89%E3%81%AE%E8%A1%8C%E5%88%97%E5%BC%8F)  
TPUでの, 相対的に短いシークエンスに対するDFTだとFFTより早い (基本的にはFFTのほうが早いみたいです) .

### FNet architecture
アーキテクチャを下図に示す. 正規化されたResNetのレイヤーを用いる. 
それぞれFourier mixingレイヤーのあとにfeed-forwardレイヤーが続く構成となっている.
{{<figure src="images/architecture.png" caption="FNet encoder architecture">}}

\begin{align*}
y = \mathfrak{R}(\mathcal{F}_\mathrm{seq} (\mathcal{F}_{\mathrm{hidden}}(x)))
\end{align*}
ここで, 実部だけ考慮する (虚部は無視する)

Fourier Transformを利用する意味としては, token を mixing するのに有効なメカニズムであることがあげられる.



