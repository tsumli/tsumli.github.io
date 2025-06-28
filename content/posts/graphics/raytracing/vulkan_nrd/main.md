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
Raytracingを行うときのデノイザーとして、[NRD](https://github.com/NVIDIA-RTX/NRD) (NVIDIA Real-Time Denoisers) というライブラリが知られています。今回はこれをVulkanで使ってみることを目標に実装していきます (各デノイザーの詳細には踏み込みません) 。

### NRDとは
NRDはNVIDIAが開発したdenoiserで、DX12やVulkanなどのAPIに依存しないように設計されています。
使用できるDenoiserは以下の3種類です:
1. REBLUR: 再帰的ブラーを用いたデノイザー
2. RELAX: A-trousベースのデノイザー
3. SIGMA: 影のノイズ除去に使用する

## Build
CMakeのFetchContentを使用して簡単にリンクすることができます. 今回使用するのはversion 4.15.1です。
```cmake
message(STATUS "Setup NRD")
FetchContent_Declare(
  nrd
  GIT_REPOSITORY https://github.com/NVIDIA-RTX/NRD
  GIT_TAG <TAG>)
FetchContent_MakeAvailable(nrd)
target_link_libraries(my-library PUBLIC NRD)
```
ビルド時にシェーダーのコンパイルも行われており、今回はそのSPIRV-V形式のデータを使用します。

## References
- [NRD](https://github.com/NVIDIA-RTX/NRD)
- 
