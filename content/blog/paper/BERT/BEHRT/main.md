---    
title: "BEHRT: Transformer for Electronic Health Records を読む" 
date: 2021-04-16T18:01:52Z 
slug: "bert"
description: "" 
keywords: ["BERT", "Deep Learning"]
draft: false 
tags: ["BERT", "Deep Learning"]
url: "blog/paper/BERT/BEHRT" 
math: true 
toc: true 
---    


電子カルテ (EHR) に対するシーケンシャルな深層学習ネットワーク, [BEHRT](https://www.nature.com/articles/s41598-020-62922-y)を読んでいきます(画像は論文より引用).
過去の病気の経歴を知ると未来の病気の予測の精度も高くなるという

## Method
$$
V_p = \lbrace \mathbf{v}_p^1, \mathbf{v}_p^2, \ldots, \mathbf{v}_p^{n_p} \rbrace
$$
ここで $n_p$ は $p$ 番目の患者のEHRの数. そして, $\mathbf{v}^j_p$ は $j$ 回目の診療時のdiagnosesを表す.

BERTに入力するために, シーケンシャルな形に変形させる.
$$
V_p = \lbrace CLS, \mathbf{v}_p^1, SEP, \mathbf{v}_p^2, SEP, \ldots, \mathbf{v}_p^{n_p}, SEP \rbrace
$$

{{<figure src="images/behrt_arch.png" >}} 

実際の入力には, このembeddingと, age, position, visit segmentの4つを組み合わせたものを使用する. 

positional encoding はEHRのシークエンスの相対的な位置を決める (学習せず, もともと決められた値を用いる).
そして, ageと

visit segmentは$A$または$B$であらわされる学習可能なvectorである. visitごとに $A, B, \ldots, A, B, \ldots$ と交互に現れ, visit間を分けるための情報を示している. 



## 感想
BEHRT のアーキテクチャについて, positional encoding が必要なのか分からなかった (直感的にはageの要素または $CLS, SEP$ による分離の情報があれば十分だと思う). 
また, visit segment に関しても, positional encoding や $CLS, SEP$ の情報があれば十分なようにも感じる (ここらへんはAblation studyが必要？).

