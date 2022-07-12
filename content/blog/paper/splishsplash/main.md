---
title: "Lagrangian Fluid Simulation
With Continuous Convolutions を読む"
date: 2022-07-08T15:55:54Z
slug: "simulation"
description: ""
keywords: ["fluid", "simulation"]
draft: false
tags: ["simulation", "paper"]
url: "blog/paper/splishsplash/"
math: true
toc: true
---

[**Lagrangian Fluid Simulation
With Continuous Convolutions**](https://openreview.net/pdf?id=B1lDoJSYDH) という論文を読んでいきます (本文中の図は論文より引用) 。
この論文では液体をグラフとして扱う...のではなくspatial convolutionを使って近傍の粒子との関係を計算します。

## Basics
$$
A(x) = \int A(x') \delta(\|x - x'\|_2) dV (x') 
$$

## Method
{{<figure src="images/spherical.png" caption="Spherical filter.">}}

input: $(x_i^n, [1, v_i^n, \nu_i])$
ここで、$x_i^n$は$v$はベロシティ、$\nu$は粘度を表す。
ホイン法をつかって中間時 (timestep=n) の位置とベロシティを計算できる。
$$
v_i^{n*} = v_i^n + \Delta t a_{\text{ext}}
$$
$$
x_i^{n*} = x_i^n + \Delta t \frac{v_i^n + v_i^{n*}}{2}
$$
ここで、$a_{\text{ext}}$ は加速度を表す係数である。

ConvNetを使うことで近傍の粒子間やオブジェクトとの関係性を考えることができる。
$$
[\Delta x_1, \ldots, \Delta x_N] = \text{ConvNet}
(\lbrace p_1^{n*}, \ldots p_N^{n*}\rbrace, \lbrace s_1, \ldots, s_M \rbrace)
$$

最終的にtimestep=n+1のときの位置とベロシティは次のように計算される
$$
x_i^{n+1} = x_i^{n*} + \Delta x_i
$$
$$
v_i^{n+1} = \frac{x_i^{n+1} - x_i^n}{\Delta t}
$$
## Network Architecture
ネットワークは4層の簡単な畳み込み層で形成されている。以下にネットワークの概要を示す。
{{<figure src="images/schematic.png" caption="Schematic of our network with a depth of four.">}}
$G$ をフィルター、$R$ を半径とすると、
$$
[f_1, \ldots, f_N] = \text{CConv}(\lbrace s_1, \ldots, s_M \rbrace, [x_1^{n*}, \ldots, x_N^{n*}], G, R)
$$
ここで、$f_i$ はそれぞれの $x_i^{n*}$ の特徴量である。

## Training Procedure
$$
\mathcal{L}^{n+1} = \sum^N_{i=1}\phi_i \| x_i^{n+1} - \hat{x}_i^{n+1}\|^\gamma_2
$$
ここで、$\phi_i$ はそれぞれの重みを表していて、$\phi_i = \exp(-\frac{1}{c}|\mathcal{N}(x_i^{n*})|)$ と表される (今回の実験では $c=40, \gamma=0.5$ としている) 。
このtimestep=n+1, n+2のときの損失を合わせて最終的な損失とする。
$$
\mathcal{L} = \mathcal{L}^{n+1} + \mathcal{L}^{n+2}
$$

{{<figure src="images/comp.png" caption="Comparison to ground-truth physics simulation.">}}
[DFSPH](https://animation.rwth-aachen.de/media/papers/2015-SCA-DFSPH.pdf)と比べても匹敵する精度の結果が得られていることがわかる。