---
title: "StarGAN v2 を読む"
date: 2021-05-21T19:58:16Z
slug: "StarGANv2"
description: ""
keywords: ["StarGAN", "GAN"]
draft: ture
tags: ["GAN", "paper"]
url: "blog/paper/StarGANv2/"
math: true
toc: true
---

[**StarGAN v2: Diverse Image Synthesis for Multiple Domains**](https://arxiv.org/abs/1912.01865)   
[Choi et al. CVPR 2020] という論文を読んでいきます. (本文中の図は論文より引用).


{{<figure src="images/Synth_result.png" caption="Synthesis Result">}}

image-to-image translationのタスクにおいて, 異なるドメイン間のマッピングを学習しなければいけません.
そして, それらは次の要素を満たす必要があります. 
1. 生成した画像のdiversityが広い
2. 様々にドメインに対応できる (scalability)

## introduction
既存手法では, マッピングが2つのドメイン間に限定される (scalabilityがない) という問題点があったが,
[**StarGAN**](https://arxiv.org/abs/1711.09020) は1つのgeneratorで複数のドメインに対応するモデルを提案した.
この手法では, generatorは追加のinputとしてドメインのラベルを持ち, 画像を目的のドメインに変換させる. しかし, 
StarGANはそれぞれのドメイン間のマッピングを学習しているだけで, データ分布のマルチモーダルな特徴を捉えているわけではない.

## Method 
### Framework
{{<figure src="images/overview.png" caption="Overview">}}
ゴールは **様々な**画像を生成できる**1つ**のgenerator $G$ を訓練すること.
#### Generator (Figure 1a)
$\mathbf x \in \mathcal{X}$ を画像, $y \in \mathcal{Y}$ をドメインとする.
$G$ は 画像とstyle code $\mathbf s$ を引数にとり, 新たな画像を生成する (AdaINを用いて $\mathbf s$ を $G$ に与える).
$y$ を $G$ に与えないことで, すべてのドメインに対応する画像が生成できる.

#### Mapping network (Figure 1b)
latent code $\mathbf z$ とドメイン $y$が与えられたとき, 
mapping network $F$ は style code $\mathbf{s}$ を生成する
$$
\mathbf s = F_y (\mathbf z)
$$

#### Style encoder (Figure 1c)
画像 $\mathbf{x}$ と対応するドメイン $y$ が与えられたとき, 
encoder $E$ は $\mathbf x$ に対応するstyle code $\mathbf s$ を生成する
$$
\mathbf s = E_y(\mathbf x)
$$


#### Discriminator (Figure 1d)
discriminator $D$ は複数のoutput branchを持つmulti-task discriminatorである.
それぞれのbranch $D_y$ は$\mathbf x$ が $y$ に属する本当の画像か, それとも偽物の画像か判定する.

### Training Objectives
#### Adversarial objective
訓練するとき, latent code $\mathbf z$ とターゲットドメイン $\tilde y \in \mathcal{Y}$ をランダムにとってくる.
そして, ターゲットstyle code $\tilde{\mathbf s} = F_\tilde{y}(\mathbf{z})$ を求めたあと,
$\mathbf{x}$ と $\tilde{\mathbf{s}}$ を入力として $G$ を学習させる.
このとき, adversarial lossを用いる.
$$
\mathcal{L}_{adv} = \mathbb{E}_{\mathbf x, y}[\log D_y(\mathbf x)] + \mathbb{E}_{\mathbf x, \tilde{y}, \mathbf{z}}[\log (1-D_\tilde{y}(G(\mathbf{x}, \tilde{\mathbf{s}})))]
$$

#### Style reconstruction
\begin{align*}
\mathcal{L}_{sty} &=  \mathbb{E}_{\mathbf{x}, \tilde{y}, \mathbf{z}} [||\tilde{\mathbf{s}} - E_{\tilde{y}}(G(\mathbf{x}, \tilde{\mathbf{s}}))||_1]\\\\\\
\end{align*}

#### Style diversification
\begin{align*}
\mathcal{L}_{ds} &=  \mathbb{E}_{\mathbf{x}, y, \mathbf{z}_1, \mathbf{z}_2} [||G(\mathbf{x}, \tilde{\mathbf{s}}_1) - G(\mathbf{x}, \tilde{\mathbf{s}}_2)||_1]\\\\\\
\end{align*}
where
\begin{align*}
\tilde{\mathbf{s}}_i &= F_{\tilde{y}} (\mathbf{z}_i) & \mathrm{for}\ \ i \in \{1, 2\}\\\\\\
\end{align*}

#### Preserving source characteristics
\begin{align*}
\mathcal{L}_{cyc} = \mathbb{E}_{\mathbf{x}, y, \tilde{y} \mathbf{z}} [||\mathbf{x} - G(G(\mathbf{x}, \tilde{\mathbf{s}}), \hat{\mathbf{s}})||_1]
\end{align*}
where
\begin{align*}
\hat{\mathbf{s}} &= E_y(\mathbf{x}) &\text{(入力画像}\ \mathbf{x}\ \text{に対するstyle codeの予測値)}
\end{align*}
#### Full objective
\begin{align*}
\min_{G, F, E} \max_D \ \  \mathcal{L}_{adv} + \lambda_{sty} \mathcal{L}_{sty} - \lambda_{ds} \mathcal{L}_{ds} + \lambda_{cyc} \mathcal{L}_{cyc}
\end{align*}

## Experiments

## Discussion





