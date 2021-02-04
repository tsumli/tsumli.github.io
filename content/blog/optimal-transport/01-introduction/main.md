---
title: "Optimal Transport 01. はじめ"
date: 2021-02-02T13:55:54Z
slug: "optimal-transport"
description: ""
keywords: ["optimal-transport", "最適輸送理論", "最適輸送問題"]
draft: false
tags: ["optimal-transport"]
url: "blog/optimal-transport/01-introduction/"
math: true
toc: true
---
## Optimal Transport とは
**Optimal Transport**は、日本語で**最適輸送** (問題) と訳されます。
和訳が表しているように、ある物体をある地点から別の地点に移したときの最小コスト、そしてその輸送方法を求めるという問題です。そこから、確率分布の比較に使われるようになりました。

## 歴史
歴史は古く、1781年にGaspard Mongeが提案しました[^fn1]。問題の発想は簡単で、
**ある場所から別の場所に土砂を運ぶとき、どのように運べばよいのか**
というものです。  
もっと具体的に考えてみましょう。ある場所 (場所Aとします) には $n$ 地点に土砂があったとします。そして、移動先の場所 (場所Bとします) の $n$ 地点に土砂を移したいとします。
Aの $i$ 地点とBの $j$ 地点の間の距離=コストが $\mathbf C_{i,j}$ と表されるとき、
平均の輸送コストはどのようになるか。という問題です。  
これを数式で表すと次のようになります。
$$
\min_{\sigma \in \mathrm{Perm}(n)} \frac{1}{n} \sum_{i=1}^{n} \mathbf{C}_{i, \sigma(i)}
$$
ここで、$\mathrm{Perm}(n)$は$n$の順列の集合。  
では、これを貪欲に解こうと思うと、$O(n!)$ 回計算しなければなりません ($n\geq 10$ だとつらいというイメージ) 。
そこで、この問題をもとに現在に至るまで様々なアルゴリズムが開発されてきました。

## Kantorovichの一般化
Kantorovichはこの輸送問題を確率分布間に適用しました[^fn2]。
距離を求めたい確率分布を $\mathbf{a}\in \mathbb{R}^n, \mathbf{b}\in \mathbb{R}^m$ とします。
ここで、$\mathbf{a}$ と $\mathbf{b}$ の同時分布 $\mathbf{U}$ を考えます。
$$
\mathbf{U}(\mathbf{a}, \mathbf{b}) \triangleq \lbrace \mathbf{P}\in\mathbb{R}^{n\times m}_+: \mathbf{P}\mathbf{1}_m = \mathbf{a} \mathrm{\ and\ } \mathbf{P}^\mathsf{T}\mathbf{1}_n = \mathbf{b} \rbrace
$$
このとき、$\mathbf{1}_n$は$1$が$n$個並んだベクトル。また、$\mathbf{P}$を輸送計画行列と呼び、$(i, j)$ 要素は $i$ 地点から $j$ 地点まで移動させる量を表します。  
この集合の制約条件 ( $\mathbf{P}\mathbf{1}_m = \mathbf{a}$ ) について考えます。
$\mathbf{P}\mathbf{1}_m$ は、行列 $\mathbf{P}$ に対しdim=0でsumを取ったときと同等の結果になります (shapeが違うという意味です) 。
つまり、$\mathbf{P}$ の $i$ 行の要素の合計が $\mathbf{a}_i$ と一致するということです。
同様に、$\mathbf{P}^\mathsf{T} \mathbf{1}_n = \mathbf{b}$ とは、$\mathbf{P}$ の $j$ 列の要素の合計が $\mathbf{b}_j$ と一致するという意味です。

すると、輸送問題はこの制約付きの同時分布を考えた上での、次のような最小化問題になります。
$$
\mathrm{L_{\mathbf{C}}} (\mathbf{a}, \mathbf{b})\triangleq \min_{\mathbf{P}\in\mathbf{U}(\mathbf{a}, \mathbf{b})} \langle \mathbf{C}, \mathbf{P} \rangle \triangleq \min \sum_{i, j} \mathbf{C}_{i,j} \mathbf{P}_{i, j}
$$
ここで、$\langle \cdot, \cdot \rangle$はフロベニウス積。

つづく

## 参考文献  
- [Computational optimal transport](https://arxiv.org/abs/1803.00567).


[^fn1]: Gaspard Monge. Mémoire sur la théorie des déblais et des remblais. De l’Imprimerie Royale, 1781.
[^fn2]: Leonid Vitalievich Kantorovich. On the translocation of masses. In Dokl. Akad. Nauk. USSR (NS), volume 37, pages 199–201, 1942.
