---
title: "First Order Motion Model for Image Animationを読む"
date: 2021-09-25T13:55:54Z
slug: "animation"
description: ""
keywords: ["animation"]
draft: false
tags: ["video", "paper"]
url: "blog/paper/first-order-motion-model/"
math: true
toc: true
---

[**First Order Motion Model for Image Animation**](https://arxiv.org/abs/2003.00196)という論文を読んでいきます。
## Motivation

## Method
source image $\mathbf{S}$ に存在する物体を driving video $\mathcal{D}$ に存在する似た物体をもとに動かすということをやっていきます。
Self-Supervisedな設定で、訓練には同じカテゴリーの物体を含む大量のビデオが必要となります。

フレームワークは大きく2つのモジュールに分かれています: motion estimation moduleとimage generation moduleです。


motion estimation modelはdriving videoの中の1つのフレーム $\mathbf{D} \in \mathbb{R}^{3\times H\times W}$
からsource videoのフレーム $\mathbf{S} \in \mathbb{R}^{3\times H\times W}$ へのdense motionを 推測します。

このdense motionは $\mathcal{T}_{\mathbf{S}\leftarrow\mathbf{D}}: \mathbb{R}^2 \leftarrow \mathbb{R}^2$ と書くことができて、 $\mathbf{D}$ の中のそれぞれのピクセルを $\mathbf{S}$ の対応するピクセルに移動させます。

また、 $\mathcal{T}_{\mathbf{S}\leftarrow\mathbf{D}}$ をbackword optical flowと呼びます。

ここで、abstract reference frame $\mathbf{R}$ が存在すると仮定しましょう。そうすると、次のふたつのマッピングを独立して推測することができます。
- $\mathcal{T}_{\mathbf{S}\leftarrow\mathbf{R}}$ 
- $\mathcal{T}_{\mathbf{S}\leftarrow\mathbf{D}}$



## Result


## Memo
