---
title: "First Order Motion Model for Image Animation (FOMM) を読む"
date: 2021-10-24T19:58:16Z
slug: "FOMM"
description: ""
keywords: ["GAN"]
draft: false
tags: ["GAN", "paper"]
url: "blog/paper/fomm/"
math: true
toc: true
---

[**First Order Motion Model for Image Animation**](https://proceedings.neurips.cc/paper/2019/file/31c0b36aef265d9221af80872ceb62f9-Paper.pdf)   
[A. Siarohin et al. NeurIPS 2019] という論文を読んでいきます (本文中の図は論文より引用)。
FOMMという名前で知られている手法です。

{{<figure src="images/result.png" caption="example animation">}}


## Method
### 目的
**source image $\mathbf{S}$ と deiving video $\mathcal{D}$ の動きを表す潜在表現を組み合わせて、 driving video を再構成する**

このとき、driving videoを同じような物体が写っている映像とすることで、教師なし訓練ができる。
### 概観
{{<figure src="images/overview.png" caption="Overview of the method.">}}

上図に本手法のoverviewを示す。inputは source image $\mathbf{S}$ と deiving video のフレーム $\mathbf{D}$ である。
それぞれに対し Keypoint Detector が 疎なキーポイント (sparse keypoints) と 局所的なアフィン変換 (local affine transformation) を抽出する。
そして、dense motionネットワークが動き (motion) の表現をつかって、以下の2つの特徴量を持ってくる
1) dense optical flow: $\hat{\mathcal{T}}_{\mathbf{S} \leftarrow \mathbf{D}}$
2) occlusion map: $\hat{\mathcal{O}}_{\mathbf{S} \leftarrow \mathbf{D}}$

そして、最後にGeneration moduleに通して最終的な画像が生成される。

### 具体的な手法
この手法は主に2つのモジュール: Motion estimation module と image generation module からなる 

motion estimation module の役割は、driving videoから取ってきたフレーム $\mathbf{D} \in \mathbb{R}^{3\times H \times W}$ から source image $\mathbf{S}\in \mathbb{R}^{3\times H \times W}$ への
dense motion field を予測することである。

この motion field は $\mathcal{T}_{\mathbf{S} \leftarrow \mathbf{D}}: \mathbb{R}^2 \leftarrow \mathbb{R}^2$ と定式化される。これを一般的に backward optical flow という。

ここで、抽象的なreference image $\mathbf{R}$ を仮定する。その仮定、
reference image $\rightarrow$ source image と reference image $\rightarrow$ driving image の変換を独立に予測することで、$\mathbf{D}$ と $\mathbf{S}$ に対して独立に処理することができる。

FIRST

そして、dense motion network では
motion field $\hat{\mathcal{T}}_{\mathbf{S} \leftarrow \mathbf{D}}$に加え、

occlusion mask: $\hat{\mathcal{O}}_{\mathbf{S} \leftarrow \mathbf{D}}$ も抽出する。この特徴量は、$\mathbf{D}$ のどの部分が補完 (inpaint) されるべきかをあらわしている。

最後に、image generation moduleで source objectに動きを与える (occlusionで指定された部分をinpaintする) 。


### a
$\mathcal{T}_{\mathbf{X} \leftarrow \mathbf{R}}$ を得る方法について

変換 $\mathcal{T}_{\mathbf{X} \leftarrow \mathbf{R}}$ が与えられた時、一次のテイラー展開を考えることができる

{{<figure src="images/tx_r.png">}}

この定式化では $\mathcal{T}_{\mathbf{X} \leftarrow \mathbf{R}}$ はそれぞれのkeypoint $p_k$ 値とその Jacobian で表すことができる。
{{<figure src="images/tx_r_sim.png">}}

<!-- $$
\mathcal{T}_{\mathbf{X} \leftarrow \mathbf{R}} (p) \sim
\bigl\{ \lbrace
\mathcal{T}_{\mathbf{X} \leftarrow \mathbf{R}} (p_1), \frac{d}{dp} \mathcal{T}_{\mathbf{X} \leftarrow \mathbf{R}} (p) \bigm|_{p=p_1} \rbrace, \ldots,  
\lbrace
\mathcal{T}_{\mathbf{X} \leftarrow \mathbf{R}} (p_k), \frac{d}{dp} \mathcal{T}_{\mathbf{X} \leftarrow \mathbf{R}} (p) \bigm|_{p=p_K} \rbrace
\bigr\} 
$$ -->
****

さらに、$\mathcal{T}_{\mathbf{R} \leftarrow \mathbf{X}}$ ($\mathbf{X}$ から $\mathbf{R}$ への変換の逆変換) を求めるために、

$\mathcal{T}_{\mathbf{X} \leftarrow \mathbf{R}}$がkeypointの近傍に対し局所的に全単射であることを仮定している。

{{<figure src="images/ts_d.png">}}
<!-- $$
\mathcal{T}_{\mathbf{S} \leftarrow \mathbf{D}} = \mathcal{T}_{\mathbf{S} \leftarrow \mathbf{R}}
\circ \mathcal{T}_{\mathbf{R} \leftarrow \mathbf{D}} = \mathcal{T}_{\mathbf{S} \leftarrow \mathbf{R}} \circ
\mathcal{T}^{-1}_{\mathbf{D} \leftarrow \mathbf{R}}
$$ -->


{{<figure src="images/ts_d_sim.png">}}
<!-- $$
\mathcal{T}_{\mathbf{S} \leftarrow \mathbf{D}} (z) \sim \mathcal{T}_{\mathbf{S} \leftarrow \mathbf{R}} (p_k)
+ J_k (z - \mathcal{T}_{\mathbf{D} \leftarrow \mathbf{R}}(p_k))
$$ -->

ここで、Jacobian $J_k$ は次のように表される

{{<figure src="images/J_k.png">}}

<!-- $$
J_k = \left(\frac{d}{dp} \mathcal{T}_{\mathbf{S} \leftarrow \mathbf{R}} (p) \Bigm|p=p_k\right)
\left(\frac{d}{dp} \mathcal{T}_{\mathbf{D} \leftarrow \mathbf{R}} (p) \Bigm|p=p_k\right)^{-1}
$$ -->


source, driving imageに対してkeypoint predictorは4つchannelを多く出力する。
これらの特徴用を用いて、対応するkeypointのconfidence mapを重みとした重み付き平均を計算することによって上の式 ($J_k$) の中の

$\frac{d}{dp} \mathcal{T}_{\mathbf{S} \leftarrow \mathbf{R}} (p) \Bigm|p=p_k$

$\frac{d}{dp} \mathcal{T}_{\mathbf{D} \leftarrow \mathbf{R}} (p) \Bigm|p=p_k$

の2つの行列の相関を得ることができる。





{{<figure src="images/Hk_z.png">}}
<!-- $$
\mathbf{H}_k(z) = \exp\left( \frac{\{\mathcal{T}_{\mathbf{D} \leftarrow \mathbf{R}}(p_k) - z\}^2}{\sigma}\right)
- \exp\left( \frac{\{\mathcal{T}_{\mathbf{S} \leftarrow \mathbf{R}}(p_k) - z\}^2}{\sigma}\right)
$$ -->

{{<figure src="images/hat_Ts_d.png">}}
<!-- $$
\hat{\mathcal{T}}_{\mathbf{S} \leftarrow \mathbf{D}}(z) = 
\mathbf{M}_0z +
\sum^K_{k=1} \mathbf{M}_k
\left(
\mathcal{T}_{\mathbf{S} \leftarrow \mathbf{R}}(p_k) + J_k(z - \mathcal{T}_{\mathbf{D} \leftarrow \mathbf{R}}(p_k))
\right)
$$ -->
ここで、$M_0z$ は「背景」のような動かない部分として解釈できる。


### Occlusion-aware Image Generation
特徴量マップ $\xi\in \mathbb{R}^{H' \times W'}$ 得て、これを
$\hat{\mathcal{T}}_{\mathbf{S} \leftarrow \mathbf{D}}$ をもとにwarpさせる。

ここで、occlusion mask $\hat{O}_{\mathbf{S} \leftarrow \mathbf{D}} \in [0, 1]^{H' \times W'}$ でinpaintするべき場所を表す。
つまり、"occluded" された部分に対応した特徴量の影響を削減する効果をもつ。

{{<figure src="images/xi.png">}}
<!-- $$
\xi' = \hat{\mathcal{O}}_{\mathbf{S}\leftarrow \mathbf{D}} \odot f_w(\xi, \hat{\mathcal{T}}_{\mathbf{S} \leftarrow \mathbf{D}})
$$ -->

ここで、$f_w (\cdot, \cdot)$ はback-warpingを表し、$\odot$ はアダマール積を表す。
このocclusion maskは次の層に入力され、画像生成に使われる。

### Dataset
- [VoxCeleb](https://www.robots.ox.ac.uk/~vgg/data/voxceleb/)
- [UvA-Nemo](http://www.uva-nemo.org/index.html)
- [BAIR robot pushing dataset](https://www.tensorflow.org/datasets/catalog/bair_robot_pushing_small)
- Tai-chi-HD

### Result
{{<figure src="images/result-table.png">}}
reconstructionした結果を
L1 Loss, Average Keypoint Distance (AKD), Missing Keypoint Rate (MKR), Average Euclidean Distance (AED) の4つの指標を用いて比較した結果を上図に示す。
関連手法に比べ、一貫して良い結果を出していることがわかる。

## References
- official code
[![AliaksandrSiarohin/first-order-model - GitHub](https://gh-card.dev/repos/AliaksandrSiarohin/first-order-model.svg)](https://github.com/AliaksandrSiarohin/first-order-model)