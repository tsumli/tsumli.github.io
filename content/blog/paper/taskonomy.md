---
title: "Taskonomyを読む"
date: 2021-02-01T13:55:54Z
slug: "taskonomy"
description: ""
keywords: ["転移学習", "Taskonomy", "transfer-learning"]
draft: false
tags: ["transfer-learning"]
math: true
toc: true
---
[arxiv](https://arxiv.org/abs/1804.08328)

# Method
1. **Task-Specific Modeling**\
全てのSourceのタスクにおいて教師あり学習を行う
ネットワークはエンコーダとデコーダを持つが、**デコーダの構造はタスクによって異なる**。

2. **Transfer Modeling**\
$s\in \mathcal{S}$ と $t\in \mathcal{T}$ が与えられる。
$s$のエンコーダーで変換したものをデコーダーで変換する。
それと正解ラベルとのロスを最小化するようにデコーダーの$\theta$を学習する。
$E_s(I)$が$t$を解くのに役立つかどうかの尺度としてデコーダーのパフォーマンスが使われる。

    - **Accesibility**
転移学習がうまく行くために、Sourceから得られる表現はTargetを解くのに十分な情報をもっていて、かつ情報へのAccesibilityを持ってないといけない。AccesibleなTransferabilityを評価するために少ないデータセットで訓練された小さいアーキテクチャが必要である

    - **High-Order Transfers**
複数のSource taskがTarget taskを解くのに補完的な情報を持っていることがある。しかしすべて実験していると組み合わせ爆発が起こってしまうためTarget taskに良い結果をもたらすであろうSource taskを5つまで選択しすべての組み合わせを検証した

3. **Analytic Hierarchy Process (AHP) による正規化**\
transferabilityのAffinity Matrix(相性の行列)を計算したい。
SourceからTaskへ転移させたときのロスをそのまま$[0, 1]$にスケールさせて用いると、ロスに対しての本当のクオリティが変わるスピードが異なる場合が問題となるため、適切なnormalizationを考えなければいけない。
そこでAHP法を用いる(AHPの中でも固有値を用いる方法[[参考]](https://core.ac.uk/download/pdf/96975029.pdf))。
それぞれのtargetに対してすべての可能なssourceからのtransferabilityのpairwise tornament行列Wtを構成する。
つまり、$(i,j)$は$s_i$が$s_j$よりも優れている確率を表している。これの主固有値に対応する主固有ベクトルを求める。
最終的な$s_i\rightarrow t$ のtransferabilityは主固有ベクトルのi番目の要素と対応する