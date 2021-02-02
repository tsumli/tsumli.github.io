---
title: "自分的Singularityの使い方"
date: 2021-02-02T00:55:54Z
slug: "singularity"
description: ""
keywords: ["abci", "singularity"]
draft: false
tags: ["singularity", "abci"]
url: /blog/singularity/
math: true
toc: true
---

abciを使うときにDockerではなくSingularityを使う必要があったのですが、戸惑う部分が多かったので記録しておきます。
今回扱うバージョンはsingularitypro/3.5です。
imageの作成
imageを作成するためのDefinition fileを作成します (詳細は[公式ドキュメント](https://repo.sylabs.io/c/0f6898986ad0b646b5ce6deba21781ac62cb7e0a86a5153bbb31732ee6593f43/guides/singularitypro35-user-guide/)) 。  
ubuntuのimageをもとにdefinition fileを作成しました (docker-compose.ymlを書くときのイメージですね) 。

```yaml:foo.def
Bootstrap: docker
From: ubuntu

%files
	requirements.txt

%post
	apt update
	apt upgrade -y 
	apt install -y python3
	apt install -y python3-pip
	pip3 install -r requirements.txt

%environment
	export LC_ALL=ja_JP.utf-8
    export LANG=ja_JP.utf-8

```

このファイルをfoo.defとして保存し、buildします。
```sh
singularity build --fakeroot foo.sif foo.def
```

あとは、実行のためのシェルスクリプトを書いて完成です。
```sh
#!/bin/sh
#$ -l rt_G.small=1
#$ -j y
#$ -o fit/output/
#$ -cwd
#$ -l h_rt=12:00:00
source /etc/profile.d/modules.sh
module load singularitypro/3.5
singularity run --nv foo.sif run.sh
```