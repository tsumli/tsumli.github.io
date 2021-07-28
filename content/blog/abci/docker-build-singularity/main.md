---
title: "DockerでSingularityのImageをbuildする"
date: 2021-04-16T18:01:52Z
slug: "singularity"
description: ""
keywords: ["singularity", "abci", "docker"]
draft: false
tags: ["singularity", "abci", "docker"]
url: "blog/abci/docker-build-singularity"
math: true
toc: true
---

dockerでsingularityのimage file (.sif) を作成したときのメモ書きです．
## Motivation
ローカルPCでsingularity buildしたい (docker image to singularity image) けど，ローカルPCの環境を汚したくない，という状況です．

## Method
まず，もととなるdocker imageを用意します．例えばこれをfoo:latestとします．
一般的な方法 (コンテナ内でsingularityをインストールし，そこからfoo:latestを変換する) でbuildしようとしても，
コンテナ内からdocker imageを見ることができないため不可能です．

そこで，Docker out of Docker (DooD) という方法でbuildしていきます 
(実際にはコンテナからコンテナを操作しているわけではないので，この用語は適切でないかもしれません)．
やり方としては簡単で，ホストのdocker.sockをマウントして実行することで，ホストのdocker imageをコンテナに共有することができます．
以下のようなshellscriptを作成し，保存します．
今回はquay.ioからimageを持ってきました．[Tags](https://quay.io/repository/singularity/singularity?tab=tags)を見ることで，
他のsingularityのバージョンなどに適宜変更できます．

```shell
# build_singularity.sh
docker run --rm -v "$PWD":/src/ -w="/src/" -v /var/run/docker.sock:/var/run/docker.sock quay.io/singularity/singularity:v3.7.2 build /src/${NAME}.sif docker-daemon://${IMAGE}
```

このshellscriptを次のように実行します．
```shell
IMAGE=foo:latest NAME=foo sh build_singularity.sh 
```

結果として，カレントディレクトリに${NAME}.sifが生成されます．
あとはGPUサーバに上げるなりして使うことができます．
______
感想として，.sifファイルは.defファイルから作成するよりもdocker imageから作成する方が簡単でした (単に慣れの問題かもしれません).
セキュリティの問題でremoteサーバでdockerが使えず，singularityが推奨されることが多いので，
このように簡単にimageファイルが作成できるのはうれしいです．

## 追記（2021/07/28）
公式のgithubレポジトリに同様のものを発見しました （https://github.com/singularityhub/docker2singularity）
こっちのほうが使うときに楽でいいかもしれません

