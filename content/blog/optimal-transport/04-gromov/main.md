---
title: "Optimal Transport 04. Gromov Wasserstein Distance"
date: 2021-03-12T13:55:54Z
slug: "optimal-transport"
description: ""
keywords: ["optimal-transport", "gromov-wasserstein-distance", "最適輸送理論", "最適輸送問題", "Gromov Wasserstein Dsitance"]
draft: true
tags: ["optimal-transport"]
url: "blog/optimal-transport/04-gromov/"
math: true
toc: false
---
[01. はじめ]({{< ref"/blog/optimal-transport/01-introduction/main.md">}})  
[02. エントロピー正則化]({{< ref"/blog/optimal-transport/02-entropy/main.md">}})  
[03. Unbalanced Optimal Transport]({{< ref"/blog/optimal-transport/03-unbalanced/main.md">}})  
[04. Gromov Wasserstein Distance]({{< ref"/blog/optimal-transport/04-gromov/main.md">}})  
## Gromov Wasserstein Distance
普通のOptimal Transportは，例えば集合 $A$ と集合 $B$ があったとして，データポイント間の距離（コスト）をもとに最終的な距離 (Wasserstein Distance) が計算できました．それとは異なり，Gromov Wasserstein Distance (GW) は，その集合の中のデータポイント間の距離をもとにして比較します．
つまり，異なる距離空間をもつ集合の間の距離を計算したいときに，その間の距離を定義することなく実行できるというメリットがあります．
比較したい２つの集合の，その集合の中での距離行列をそれぞれ $\mathbf{D} \in \mathbb{R}^{n\times n}, \mathbf{D}' \in \mathbb{R}^{m\times m}$
とすると，GWは次のように定義されます．
$$
\mathrm{GW} ((\mathbf{a}, \mathbf{D}), (\mathbf{b}, \mathbf{D}'))^2\triangleq 
\min_{\mathbf{P}\in\mathbf{U}(\mathbf{a}, \mathbf{b})} {\LARGE \varepsilon}_{\mathbf{D}, \mathbf{D}'}(\mathbf{P}) 
$$
ここで，
$$
{\LARGE \varepsilon}_{\mathbf{D}, \mathbf{D}'}(\mathbf{P}) \triangleq \sum_{i, j, i', j'} |\mathbf{D}_{i, i'} - \mathbf{D}_{i', j'}|^2 \mathbf{P}_{i, i'} \mathbf{P}_{j, j'}
$$

## 参考文献  
- [Computational optimal transport](https://arxiv.org/abs/1803.00567)
