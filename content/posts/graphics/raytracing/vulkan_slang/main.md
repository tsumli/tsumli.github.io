---
title: "SlangとVulkanでのRaytracing"
date: 2025-06-16T00:01:52Z
slug: "raytracing"
description: ""
keywords: ["raytracing", "graphics"]
draft: true
tags: ["raytracing", "graphics"]
url: "posts/graphics/raytracing/vulkan_slang"
math: true
toc: true
---

## はじめに
SlangとVulkanを用いてRaytracingを行う記事があまりなかったので書きます

### Slangとは
最近ではSascha Willemsの[Vulkan](https://github.com/SaschaWillems/Vulkan)レポジトリで、[GLSL/HLSLに加えて採用されたり](https://www.saschawillems.de/blog/2025/06/03/shaders-for-vulkan-samples-now-also-available-in-slang/)と、使用例もだんだん増えてきている印象があります。
少し書いてみて感じたのは、SlangはHLSL, GLSLとは違い書いていてストレスが少ないです。また、vscodeの拡張機能でsyntax highlightingもサポートされているのも大きいでしょう。
文法的にはhlslに似ており、glslを書いていることが多かった自分としてはかなり違いがあって戸惑いました。slangの機能の一部を紹介しましょう

####  Interface



#### Generics
#### Variadic Generics
#### Automatic Differentiation
#### Reflection
reflectionがあるとvulkanコードとの整合性チェックやdescriptor set layoutなどの自動生成が可能になります。
spirv-cross

## References
- [Slang Playground](https://shader-slang.org/slang-playground/)
- [Slang User’s Guide](https://docs.shader-slang.org/en/latest/external/slang/docs/user-guide/)
  - HLSL, GLSLからの移行ガイドなど 