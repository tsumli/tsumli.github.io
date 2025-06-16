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
SlangとVulkanを用いてRaytracingを触ってみたメモ

### Slangとは
最近では、Sascha Willems 氏の [Vulkan サンプル集](https://github.com/SaschaWillems/Vulkan)でも、[GLSL/HLSL に加えて Slang が採用される](https://www.saschawillems.de/blog/2025/06/03/shaders-for-vulkan-samples-now-also-available-in-slang/)など、使用例が徐々に増えてきている印象です。
少し触ってみて感じたのは、Slang は HLSL や GLSL に比べて書いていてストレスが少ないということです。VSCode 向けの拡張機能によるシンタックスハイライトもサポートされており、開発体験が快適なのも大きなポイントでしょう。
文法的には HLSL に近く、GLSL に慣れていた自分としては最初は戸惑う部分もありましたが、慣れてくると Slang独自の機能や設計がとても魅力的に感じられます。

Slang の特徴的な機能をいくつか紹介していきます。
####  1. Interface
structにinterfaceを持たせることができます。例えば、Light interfaceを定義して、それを実装するPointLight, AreaLightなどを作るという例が紹介されています
 ([Interfaces Design](https://github.com/shader-slang/slang/blob/master/docs/design/interfaces.md).)

```cpp
interface IFoo
{
    int MyMethod(float arg);
}

struct MyType : IFoo
{
    int MyMethod(float arg)
    {
        return (int)arg + 1;
    }
}
```


#### 2. Generics
GLSLには存在しなかった機能のひとつに、Genericsがあります。
HLSLでは[HLSL 2021](https://devblogs.microsoft.com/directx/announcing-hlsl-2021/)でtemplate機能が導入されており、これがそれに近い仕組みと言えるでしょう。

以下はGenericsを用いたコードの例です:
```cpp
T Interpolate<T : IFloat>(T v0, T v1, T v2, float2 uv) {
  let bary_u = T(uv.x);
  let bary_v = T(uv.y);
  let bary_w = T(1.0) - bary_u - bary_v;
  return v0 * bary_w + v1 * bary_u + v2 * bary_v;
}
```

こうして定義された関数は以下のように利用できます:
```cpp
let pos = Interpolate(v0.pos, v1.pos, v2.pos, attr.barycentrics);  // posはfloat3
let uv = Interpolate(v0.uv, v1.uv, v2.uv, attr.barycentrics);      // uvはfloat2
```
ジェネリクスを使うことで、同じロジックを複数の型に対して簡単に記述できて便利ですね

#### 3. Automatic Differentiation
自動微分を行うことができます。今回は深入りしませんが応用先は多そうです。

#### 4. Reflection
Reflectionを使うことによって、Vulkanコードとの整合性チェックやDescriptorSetLayoutなどの自動生成が可能になります。
[SPIRV-Cross](https://github.com/KhronosGroup/SPIRV-Cross)というおなじみのツールがあるので、もし複数のシェーダ言語をSPIR-Vに変換して扱う場合はこちらを使うのも良いでしょう。

## Vulkan Raytracing
今回はC++でコードを書き、[Vulkan-Hpp](https://github.com/KhronosGroup/Vulkan-Hpp)を用いてVulkanのAPIを呼び出します。

raytracingを使うためにはまず対応したdevice extensionを有効にする必要があります。
```cpp
constexpr auto kDeviceExtensions = std::to_array<const char*>({
    vk::KHRPipelineLibraryExtensionName,
    vk::KHRRayTracingPipelineExtensionName,
    vk::KHRAccelerationStructureExtensionName,
    vk::EXTDescriptorIndexingExtensionName,
    // ...
});
```

logical deviceを作成する際に、対応するfeatureを有効にしてあげます。
Vulkan-HppではStructureChainを用いて、以下のように記述することができます (`.sType`や`.pNext`を手動で設定する必要がない)
```cpp
vk::StructureChain<
  /* ... */,
  vk::PhysicalDeviceBufferDeviceAddressFeatures,
  vk::PhysicalDeviceAccelerationStructureFeaturesKHR,
  vk::PhysicalDeviceRayTracingPipelineFeaturesKHR,
  vk::PhysicalDeviceDescriptorIndexingFeatures>
  chain;

chain.get<vk::PhysicalDeviceBufferDeviceAddressFeatures>()
  .setBufferDeviceAddress(VK_TRUE);

chain.get<vk::PhysicalDeviceAccelerationStructureFeaturesKHR>()
  .setAccelerationStructure(VK_TRUE)
  .setAccelerationStructureCaptureReplay(VK_TRUE)
  .setDescriptorBindingAccelerationStructureUpdateAfterBind(VK_TRUE);

chain.get<vk::PhysicalDeviceRayTracingPipelineFeaturesKHR>()
  .setRayTracingPipeline(VK_TRUE)
  .setRayTracingPipelineTraceRaysIndirect(VK_TRUE)
  .setRayTraversalPrimitiveCulling(VK_TRUE);

chain.get<vk::PhysicalDeviceDescriptorIndexingFeatures>()
  .setShaderInputAttachmentArrayDynamicIndexing(VK_TRUE)
  // ...
```



## 感想
- slangは書いててSAN値が削られにくいので良いです
- asan使用するとraytracingのdevice extensionが有効にならないことに気づかず1週間くらい溶かしてしまいました。なぜ...
- imguiがいつの間にかdynamic renderingに対応していて感動した (関係ない)


## References
- [Slang Playground](https://shader-slang.org/slang-playground/)
- [Slang User’s Guide](https://docs.shader-slang.org/en/latest/external/slang/docs/user-guide/)
  - HLSL, GLSLからの移行ガイドなど 
- [shader-slang/slangpy](https://github.com/shader-slang/slangpy)
  - Slangをpythonで扱うためのライブラリ. compute shaderだけではなくgraphicsやhardware raytracingなども行うことができて汎用性が高い
