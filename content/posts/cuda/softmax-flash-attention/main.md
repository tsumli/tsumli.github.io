---
title: "Online Softmax と Flash Attentionの実装"
date: 2025-09-02T0:55:54Z
slug: "cuda"
description: ""
keywords: ["cuda"]
draft: false
tags: ["cuda"]
url: "posts/cuda/softmax-flash-attention/"
math: true
toc: true
---

flash attention は通常のattentionの効率的な実装ということでよく聞く名前ですが、疑似コードをみてもあんまり何やっているのかわからない...
{{<figure
    src="images/pseudo_code.png"
    caption="Pseudo code of Flash Attention."
>}}

ということで、どのようにして効率的な計算方法を実現しているのかをモチベーションから見ていきたいと思います

## モチベーション
Attention機構の計算は、GPU上での計算コストが大きいことが知られています。それは、主にsoftmax関数の存在のためです。

$$
\text{Attention}(Q, K, V) = \text{softmax}(\frac{QK^\mathsf{T}}{\sqrt{d_k}})V
$$

ここで、softmaxはrow方向に対して計算するものであることに注意してください。 softmaxは一般的には以下のように計算されます

$$
\text{softmax}(x) = \frac{\exp(x)}{\sum_{i=1}^n \exp(x_i)}
$$

しかし、この計算は安定していません。例えば $x_i=12$ のとき、fp16の最大値 65535以上になってしまうため、オーバーフローを起こしてしまいます。そのため、softmaxの計算にはsafeなバージョンが使用されます

$$
\text{softmax}(x) = \frac{\exp(x - \max(x))}{\sum_{i=1}^n \exp(x_i - \max(x))}
$$

この関数を愚直に実装することを考えてみると、$\max(x)$ の計算を行い、分母について計算した後に分子の計算を行う必要があります。この計算は非常に遅く、また、GPUのリソースを上手に使えていません。そこで、flash attentionはこれらの演算を別のアプローチで解くことでタイル化を行い、高速化を実現しています。

## Online Softmax
まずは準備としてonline softmaxの実装を見ていきましょう。


