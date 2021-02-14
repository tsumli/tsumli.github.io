---
title: "Optimal Transport 02. エントロピー正則化"
date: 2021-02-13T13:55:54Z
slug: "optimal-transport"
description: ""
keywords: ["optimal-transport", "最適輸送理論", "最適輸送問題"]
draft: true
tags: ["optimal-transport"]
url: "blog/optimal-transport/02-entropy/"
math: true
toc: true
---
[01. はじめ]({{< ref"/blog/optimal-transport/01-introduction/main.md">}})  
[02. エントロピー正則化]({{< ref"/blog/optimal-transport/02-entropy/main.md">}})

[こちら](https://papers.nips.cc/paper/2013/hash/af21d0c97db2e27e13572cbf59eb343d-Abstract.html)の論文をもとに、Optimal Transportのエントロピー正則化について考えていきましょう。

## 計算量
$r$ から $c$ へのOptimal Transportは次のようになります
$$
\large
d_\mathbf{M}(r, c) \triangleq \min_{\mathbf{P}\in\mathbf{U}(r, c)} \langle \mathbf{P}, \mathbf{M} \rangle
$$
ここで、$\mathbf{M} \in \mathbb{R}^{d\times d}$ はcost matrixです  
計算量について考えると、どのような行列$\mathbf{M}$に対しても最悪のケースで $O(d^3 \log d)$となります。

## エントロピー正則化
ここで、Optimal Transportにエントロピー正則化を導入します。  
まず、同時確率分布に対する次の不等式が成り立ちます
$$
\forall r, c \in \Sigma_d, \forall \mathbf{P} \in \mathbf{U} (r, c), h(\mathbf{P}) \leq h(r) + h(c)
$$
また、$h(rc^\mathsf{T}) = h(r) + h(c)$ より次式が成り立ちます  
$$
\begin{eqnarray*}
\mathbf{U}_\alpha (r, c)  &\triangleq& \lbrace \mathbf{P} \in \mathbf{U} (r, c) \mid \mathrm{\bf KL}(\mathbf{P} \Vert rc^\mathsf{T}) \leq \alpha) \rbrace \\\\\\
&=& \lbrace  \mathbf{P} \in \mathbf{U} (r, c) \mid \mid h(\mathbf{P}) \geq h(r) + h(c) - \alpha \rbrace \\\\\\
&\subset& \mathbf{U}(r, c)
\end{eqnarray*}
$$
ここで、$\mathrm{\bf KL}(\mathbf{P} \Vert rc^\mathsf{T}) = h(r) + h(c) - h(\mathbf{P})$

このように定義した同時分布に対して、Optimal Transportを解きます (得られた値を "Sinkhorn Distance" と呼びます) 。
$$
\large
d_{\mathbf{M}, \alpha} (r, c) \triangleq \min_{\mathbf{P}\in \mathbf{U}_{\alpha}(r, c)}\langle \mathbf{P}, \mathbf{M} \rangle
$$

このようにエントロピーを考える理由は2つ
1. 計算量的な問題
2. 解をより"スムーズ"にしたい

1については後で説明するとして、まず2について説明します。[前回]({{< ref"/blog/optimal-transport/01-introduction/main.md">}})説明したように、
輸送計画行列 $\mathbf{P}$ は次の制約条件に従います
$$
\mathbf{P}\mathbf{1}_d = r \mathrm{\quad and\quad } \mathbf{P}^\mathsf{T}\mathbf{1}_d = c
$$
つまり、制約の個数は $2d$ 個となり、$\mathbf{P}$ は $0$ でない要素が $2d-1$ 個だけあって、それ以外は $0$ であるようなスパースな行列で制約を満たせるということです。
そこで、これを防ぐためにエントロピー正則化が必要となってくる。というわけです



## 参考文献  
- [Sinkhorn Distances:
Lightspeed Computation of Optimal Transport](https://papers.nips.cc/paper/2013/hash/af21d0c97db2e27e13572cbf59eb343d-Abstract.html)
- [Computational optimal transport](https://arxiv.org/abs/1803.00567)