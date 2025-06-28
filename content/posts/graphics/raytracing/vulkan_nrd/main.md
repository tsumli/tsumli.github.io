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
Raytracingを行うときのDenoiserとして、[NRD](https://github.com/NVIDIA-RTX/NRD) (NVIDIA Real-Time Denoisers) というライブラリが知られています。今回はこれをVulkanで使ってみることを目標に実装していきます。今回使用するのはversion 4.15.1です。

### NRDとは
NRDはNVIDIAが開発したDenoiserで、DX12やVulkanなどのAPIに依存しないように設計されています。
使用できるDenoiserは以下の3種類です:
1. REBLUR
2. RELAX
3. SIGMA

## References
