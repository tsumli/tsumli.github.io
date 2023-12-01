---
title: "新しいPCを組んだので構成など"
date: 2023-12-01T0:55:54Z
slug: "desktop"
description: ""
keywords: ["desktop"]
draft: false
tags: ["desktop"]
url: "blog/personal/desktop-20231201/"
math: true
toc: true
---

新しいPCを組んだので構成などのメモです (自分用) 。
セールなど使ってちょこちょこ買ったのですが計50万円は超えました...

|              |                                                       | 
| ------------ | ----------------------------------------------------- | 
| CPU          | intel Core i9-13900KF                                 | 
| CPUクーラー  | MSI MEG CORELIQUID S360                               | 
| GPU          | MSI GeForce RTX 4090 GAMING X TRIO 24G                | 
| SSD          | SAMSUNG 980 PRO 2TB                                   | 
| 電源         | Thermaltake TOUGHPOWER GF3 1200W                      | 
| メモリ       | Crucial CT2K32G4DFD832A x 2                           | 
| マザーボード | MSI MAG Z790 TOMAHAWK WIFI                            | 
| ケース       | Fractal Design Define 7                               | 
| OS           | Ubuntu 22.04                                          | 
| グリス       | ARCTIC MX-4                                           | 
| ケース       | Fractal Design Define 7 Black Solid                   | 
| ファン       | Scythe KAZE FLEX 140 SQUARE PWM 1200rpm KF1425FD12S-P | 
| ファン2      | Noctua NF-A12X25 PWM                                  | 

この構成で良かった所とダメだった所を考えてみます。

## Pros
- 大体のタスクはこなせる
- ケースが大きいので組み立て拡張しやすい
- OS代がかからない！
  - 前回はwindowsで組んだのですが地味に高かったので無料なのはうれしい

## Cons
- CPUがKFなので最小構成での動作チェックがしにくい
  - ややギャンブル
- GPUが空冷
  - ファンを買ってなんとか冷やしています
- wifiなしのマザボで良かった
  - お家に置いとくだけなので有線で十分だった...

## ネットワーク関連
構成には関係ないですがプラスアルファとして、外出先からでも触れるようにネットワーク関連も構築しました。
お家のネットワークの関係で固定IPアドレスが使えないのでVPSからwireguardを使って家のPCにVPN接続できるようにしただけですが...
しかし使ってみるとかなり便利で、この先引っ越してもその場所のネットワークに関係なく (固定IP使えるかどうかに関係なく) 使えるのはとてもうれしいなと感じました。
