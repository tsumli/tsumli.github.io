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

{{<figure src="images/result.png" caption="example annimation">}}


## Method
source image $\mathbf{S}$ を driving image $\mathcal{D}$ に基づいて動かす。同じ物体が写っているvideoを使うことで、annotationが不必要な訓練ができる。


## References
- official code
[![AliaksandrSiarohin/first-order-model - GitHub](https://gh-card.dev/repos/AliaksandrSiarohin/first-order-model.svg)](https://github.com/AliaksandrSiarohin/first-order-model)