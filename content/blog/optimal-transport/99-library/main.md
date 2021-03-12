---
title: "Optimal Transport 99. pythonライブラリ"
date: 2021-04-14T13:55:54Z
slug: "optimal-transport"
description: ""
keywords: ["optimal-transport", "python", "最適輸送理論", "最適輸送問題"]
draft: true
tags: ["optimal-transport"]
url: "blog/optimal-transport/03-library/"
math: true
toc: true
---

## ライブラリ
効率的に最適輸送問題を解くことのできるライブラリが開発されています。
今回はその中でも **POT** (python optimal transport) と **GeomLoss** について紹介したいと思います。

### POT
[website](https://pythonot.github.io/)  
[github](https://github.com/PythonOT/POT)

```sh
$ pip install POT
```
installにはcythonが必要なようです。


### GeomLoss  
[website](https://www.kernel-operations.io/geomloss/)  
[github](https://github.com/jeanfeydy/geomloss)

```sh
$ pip install geomloss
```
依存するパッケージは多く、
CUDA toolkit (including nvcc), PyTorch, KeOps が必要なようです。
このパッケージが便利なところは、pytorch用のAPIが用意されていることです。
既存のtorchコードにすぐに組み込めるのが嬉しいですね。

SamplesLossについて紹介します (自分も勉強不足のため理解してない部分があります…) 。
SamplesLossのinitには以下の引数が用意されています。

```python
from geomloss import SamplesLoss

Loss = SamplesLoss(
    loss='sinkhorn', 
    p=2, 
    blur=0.05, 
    reach=None, 
    diameter=None, 
    scaling=0.5, 
    truncate=5, 
    cost=None, 
    kernel=None, 
    cluster_scale=None, 
    debias=True, 
    potentials=False, 
    verbose=False, 
    backend='auto'
)
```

このクラスはnn.Moduleを継承しており、lossの値を得るためにforwardする必要があります。
```python
loss = Loss(*args)
```
*argの個数によって3パターンの入力をすることができます
- 入力が2つ
- 入力が4つ
- 入力が6つ
