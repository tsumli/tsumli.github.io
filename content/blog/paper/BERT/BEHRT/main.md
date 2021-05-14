---    
title: "BEHRT: Transformer for Electronic Health Records を読む" 
date: 2021-04-16T18:01:52Z 
slug: "bert"
description: "" 
keywords: ["BERT", "Deep Learning"]
draft: true 
tags: ["BERT", "Deep Learning"]
url: "blog/paper/BERT/BEHRT" 
math: true 
toc: true 
---    


電子カルテ (EHR) に対するシーケンシャルな深層学習ネットワーク, [BEHRT](https://www.nature.com/articles/s41598-020-62922-y)を読んでいきます (画像は論文より引用).


## Method
### architecture
$$
V_p = \lbrace \mathbf{v}_p^1, \mathbf{v}_p^2, \ldots, \mathbf{v}_p^{n_p} \rbrace
$$
ここで $n_p$ は $p$ 番目の患者のEHRの数. そして, $\mathbf{v}^j_p$ は $j$ 回目の診療時のdiagnosesを表す.

BERTに入力するために, シーケンシャルな形に変形させる.
$$
V_p = \lbrace CLS, \mathbf{v}_p^1, SEP, \mathbf{v}_p^2, SEP, \ldots, \mathbf{v}_p^{n_p}, SEP \rbrace
$$

{{<figure src="images/behrt_arch_a.png" >}} 

実際の入力には, このembeddingと, age, position, visit segmentの4つを組み合わせたものを使用する. 

positional encoding はEHRのシークエンスの相対的な位置を決める (学習せず, もともと決められた値を用いる).
そして, ageと

visit segmentは$A$または$B$であらわされる学習可能なvectorである. visitごとに $A, B, \ldots, A, B, \ldots$ と交互に現れ, visit間を分けるための情報を示している. 

### pre-training by masked language model (MLM)
diseaseの予測において, 未来の情報を過去の予測に, 過去の情報を未来の予測に使えそうである. 
そこで, BERTと同様なpre-trainingを行う. 
diseaseのうち86.5%は変えない. 12%は[mask]に変える. 1.5%はランダムなdiseaseに置き換える.
{{<figure src="images/behrt_arch_b.jpg"  >}} 


### Disease Prediction
3つのタスクでBEHRTを評価した.
1. 次回訪問時のdiseaseを予測 
2. 6ヶ月後までのdiseaseの予測
3. 12ヶ月後までのdiseaseの予測


## Results
### Disease Embedding
Bayesian Optimizationを用いて最適なハイパーパラメータを見つけ実験したところ, 
$\mathrm{precision\ score} = 0.6597$となった.  
MLMでの訓練結果として, 288次元ベクトルのdisease embeddingが得られる.
これをt-SNEにかけて2次元で表現したものが下図である.
{{<figure src="images/disease_embed_overview.png" >}} 
{{<figure src="images/disease_embed_a.png" >}} 
同時に発症しやすい, またはclinical groupが同じdiseaseに対しては, 同じグループに属する. 
しかし, クラスターの中に医学的には近いと思われないものが存在することがある.  
また, 女性に多い病気は男性に多い病気にたいしてかなり距離が遠いことがわかった. 
このことより, この手法が患者のコンテキストを読み取れていることがわかる.



## thoughts
評価にt-SNEが用いられていたが, t-SNEはハイパーパラメータによってかなり結果が異なることが知られているので, 
他の次元削減手法 (PCAやUMAPなど) の結果も気になった.
