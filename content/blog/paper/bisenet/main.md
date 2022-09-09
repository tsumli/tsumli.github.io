---
title: "BiSeNet: Bilateral Segmentation Network for Real-time Semantic Segmentation を読む"
date: 2022-09-06T10:33:39Z
slug: "bisenet"
description: ""
keywords: ["BiSeNet", "segmentation"]
draft: false
tags: ["segmentation", "paper"]
url: "blog/paper/bisenet/"
toc: true
mathjax: true
---


[**BiSeNet: Bilateral Segmentation Network for Real-time Semantic Segmentation**](https://arxiv.org/abs/1808.00897)   
[Yu et al. ECCV 2018] という論文を読んでいきます。 (本文中の図は論文より引用) 。
semantic segmentationの課題である、リアルタイム性 (推論速度) と精度のトレードオフ
を解決する新たなネットワークBilateral Segmentation Network (BiSeNet) の提案。


## Introduction
segmentationを高速化する手法は3つのアプローチに分かれる。(下図 (a) 参照)
1) 入力サイズを制限する ... 品質や精度の低下
2) Pruning (枝刈り) を行う ... 大きなサイズに対応できない
3) Spatial Dropoutを適用する (Ref: [ENet](https://arxiv.org/abs/1606.02147)) ... 物を区別する能力の低下

また、一般的にU-shapeのネットワークが使われるが、2つの弱点がある。
1) 高い解像度の特徴量マップの計算コストが過剰であり、スピードが低下する
2) PruningやCroppingによって失われてしまった情報は、浅い層のNNで得ることができない (下図 (b))

{{<figure 
    src="images/arch.png" 
    caption="Illustlation of the architectures to speed up and our proposed approach."
>}}

## Method

{{<figure 
    src="images/bisenet.png" 
    caption="An overview of the Bilateral Segmentation Network."
>}}

### Spatial path
Spatial Pathは十分な空間の情報を得るために必要である。
3つの畳込み層 (stride=2) からなり、そのあとにbatch normalization, ReLUが続く。
最終的に入力の1/8の特徴量マップが出力される。(上図 (a))


### Context path
Context Pathは十分な受容野を得るために必要である。
pyramid poolingや大きなカーネルサイズを使うとメモリを消費し速度の低下につながるため使用しない。

Context Pathは軽量モデル (今回は pre-trained Xception) とglobal average poolingからなる。
軽量モデルでdownsampleを行い、global average poolingを行うことでglobalなcontextを捉えた需要野が得られる。
最終的にup-sampleされたglobal poolingの特徴量と軽量モデルの出力を組み合わせる。

ここで、ARM (Attention Refinement Module) はglobal average poolingを使ってglobalなcontextを得る。
そして、attentionベクトルを計算し、特徴量学習に使用する (上図 (b)) 。

### Feature Fusion Module
それぞれのPathからの出力をまとめるモジュール。
Spatial Pathがローレベルの特徴を捉えているのに対し、Context Pathはハイレベルの特徴を捉えているため、そのまま足し合わせることはできない。
そこで、連結させたものに対してBatch Normalizationをかけ、SENetのように特徴ベクトルと重みベクトルを計算し、最終的な出力を導出する (上図 (c)) 。


### Implementation
論文紹介はここまでで、実装を見ていきます。
pytorchによる実装は[こちら](https://github.com/CoinCheung/BiSeNet/blob/master/lib/models/bisenetv1.py)が分かりやすかったです。
下のコードのように、cp (context path) と sp (spatial path) から出力させた特徴量をffm (feature fusion module) で結合し、conv_out (畳み込み層x2+Upsampling) に入力することで、最終的な特徴量を得ています。

```python
class BiSeNetV1(nn.Module):
    ...
    def forward(self, x):
        H, W = x.size()[2:]
        feat_cp8, feat_cp16 = self.cp(x)
        feat_sp = self.sp(x)
        feat_fuse = self.ffm(feat_sp, feat_cp8)
        feat_out = self.conv_out(feat_fuse)
```

## References
- arXiv  
https://arxiv.org/abs/1808.00897

- Github  
https://github.com/CoinCheung/BiSeNet