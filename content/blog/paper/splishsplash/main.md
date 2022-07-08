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