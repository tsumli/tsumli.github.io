---
title: "Optimal Transport 03. pythonライブラリ"
date: 2021-02-14T13:55:54Z
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
近年のGPUの普及により、効率的に最適輸送理論を求められるライブラリが開発されています。
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
いちいちTENSOR.numpy() みたいなことをしなくて良いのと、GPUを効率良く使えるのが良いですね。


