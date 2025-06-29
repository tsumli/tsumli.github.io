---
title: "NRD (Denoiser) をVulkanで使ってみる"
date: 2025-06-22T10:01:52Z
slug: "raytracing"
description: ""
keywords: ["raytracing", "graphics"]
draft: false
tags: ["raytracing", "graphics"]
url: "posts/graphics/raytracing/vulkan_nrd"
math: true
toc: true
---

## はじめに
レイトレーシングを行う際のポストエフェクトとして、[NRD](https://github.com/NVIDIA-RTX/NRD) (NVIDIA Real-Time Denoisers) というライブラリが広く利用されています。ここでは Vulkan で NRD を組み込む方法を解説します (注: この記事では各デノイザーのアルゴリズム詳細には立ち入りません) 

### NRDとは
NRD は NVIDIA が開発したリアルタイム向けデノイザーで、DX12 や Vulkan など API 非依存で設計されています。サポートされる主なデノイザーは次の3種類です。
1. REBLUR: 再帰的ブラーを用いた汎用デノイザー
2. RELAX: A-trous ウェーブレットを利用した高品質デノイザー
3. SIGMA: シャドウ用ノイズ除去

## Build
CMake の FetchContent を使うと簡単に取り込めます。今回は v4.15.1 を使用します。
```cmake
message(STATUS "Setup NRD")
FetchContent_Declare(
  nrd
  GIT_REPOSITORY https://github.com/NVIDIA-RTX/NRD
  GIT_TAG <TAG>)
FetchContent_MakeAvailable(nrd)
target_link_libraries(my-library PUBLIC NRD)
```
NRD の CMake スクリプトはビルド時にシェーダも自動コンパイルし、SPIR-V 形式で生成してくれます。

## Usage
### LibraryDescの取得
`nrd::GetLibraryDesc()`を用いて`LibraryDesc`を取得します。 バージョン・対応フォーマット・バインディングのオフセットなどが含まれます。

```cpp
library_desc_ = nrd::GetLibraryDesc();
spdlog::debug("NRD version: {}.{}.{}", library_desc_.versionMajor, library_desc_.versionMinor,
                library_desc_.versionBuild);
```
実行結果
```bash
[debug] NRD version: 4.15.1
```

### Instanceの作成
利用したいデノイザーを指定してインスタンスを生成します。ここでは`REBLUR_DIFFUSE`を使います。
```cpp
auto denoisers = std::to_array({nrd::DenoiserDesc{
    .identifier = std::to_underlying(NrdIdentifier::kReblurDiffuse),
    .denoiser = nrd::Denoiser::REBLUR_DIFFUSE,
}});
auto instance_creation_desc = nrd::InstanceCreationDesc{
    .denoisers = denoisers.data(),
    .denoisersNum = static_cast<uint32_t>(denoisers.size()),
};
DEBUG_ASSERT(nrd::CreateInstance(instance_creation_desc, instance_) ==  nrd::Result::SUCCESS);
```
返り値は `nrd::Result` なので、適当にチェックしておきましょう. (`[[nodiscard]]` が欲しくはあった)

### InstanceDescの取得
`LibraryDesc`と同様に`InstanceDesc`を取得します。パイプラインや各種リソースの情報が含まれます。

```cpp
instance_desc_ = nrd::GetInstanceDesc(*instance_);
```


### TODO
- Set == Spaceであること

## 注意
- ビルド中に使用されるShaderMakeリポジトリは [FetchContent](https://github.com/NVIDIA-RTX/NRD/blob/b50c3cb575e3dfcc9bfe9933f511da1bf70a4f96/CMakeLists.txt#L126)によって常に最新の`main`ブランチを取得している
  - 古いNRD x 最新のShaderMakeでの互換性のなさによりビルドできないことが起こりうる
  - (一応PRで指摘はしたが対応されず...)

## 感想
- API非依存のライブラリってこうやって作る方法もあるなあと勉強になった
  - SPIR-Vさえあればなんとかなる
- 

## References
- [NVIDIA-RTX/NRD](https://github.com/NVIDIA-RTX/NRD) 
- [nvpro-samples/vk_denoise_nrd](https://github.com/nvpro-samples/vk_denoise_nrd)
  - NVIDIAの公式のintegrationサンプルで、インテグレーション方法として一番参考になる

## References
- [NRD](https://github.com/NVIDIA-RTX/NRD)
