---
title: "Vulkanのバリアについて整理"
date: 2025-06-23T10:01:52Z
slug: "vulkan_barrier"
description: ""
keywords: ["vulkan", "graphics"]
draft: false
tags: ["vulkan", "graphics"]
url: "posts/graphics/vulkan/sync_barrier"
math: true
toc: true
---

## はじめに
Vulkanのバリアについて整理. APIは [VK_KHR_synchronization2](https://registry.khronos.org/vulkan/specs/latest/man/html/VK_KHR_synchronization2.html) で導入されたものを見ていきます

## バリアとは?


## バリアの貼り方
最終的に以下のようなコードでバリアを貼ります ([Vulkan-Hpp](https://github.com/KhronosGroup/Vulkan-Hpp)を使用した場合)
```cpp
command_buffer.pipelineBarrier2(
  vk::DependencyInfo().setImageMemoryBarriers(image_memory_barrier));
```

ここで、[`vk::DependencyInfo`](https://registry.khronos.org/vulkan/specs/latest/man/html/VkDependencyInfo.html) は同期に関する情報を集めたような構造体です. 
```cpp
typedef struct VkDependencyInfo {
    VkStructureType                  sType;
    const void*                      pNext;
    VkDependencyFlags                dependencyFlags;
    uint32_t                         memoryBarrierCount;
    const VkMemoryBarrier2*          pMemoryBarriers;
    uint32_t                         bufferMemoryBarrierCount;
    const VkBufferMemoryBarrier2*    pBufferMemoryBarriers;
    uint32_t                         imageMemoryBarrierCount;
    const VkImageMemoryBarrier2*     pImageMemoryBarriers;
} VkDependencyInfo;
```

ここでは3つのバリアに関する構造体を渡しています。
一例として[VkImageMemoryBarrier2](https://registry.khronos.org/vulkan/specs/latest/man/html/VkImageMemoryBarrier2.html) は、
Vulkanにおいて画像（`VkImage`）の状態遷移やアクセス制御を行うための構造体です。以下のように定義されています

```cpp
typedef struct VkImageMemoryBarrier2 {
    VkStructureType            sType;
    const void*                pNext;
    VkPipelineStageFlags2      srcStageMask;
    VkAccessFlags2             srcAccessMask;
    VkPipelineStageFlags2      dstStageMask;
    VkAccessFlags2             dstAccessMask;
    VkImageLayout              oldLayout;
    VkImageLayout              newLayout;
    uint32_t                   srcQueueFamilyIndex;
    uint32_t                   dstQueueFamilyIndex;
    VkImage                    image;
    VkImageSubresourceRange    subresourceRange;
} VkImageMemoryBarrier2;
```
この中でも特に重要な以下の3つのフィールドに注目します：
- oldLayout / newLayout
- srcStageMask / dstStageMask
- srcAccessMask / dstAccessMask


### Layout（レイアウト）
レイアウトは、その画像がどのような用途で使われるかをVulkanに伝えるものです。
- 例えば、画像をカラーアタッチメントとして使用する場合は `VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL`
- シェーダーから読み込む場合は `VK_IMAGE_LAYOUT_SHADER_READ_ONLY_OPTIMAL`

など、その画像の使い道に合わせたレイアウトを指定します。

> [!tip]
> `VK_IMAGE_LAYOUT_GENERAL`は汎用的なレイアウトで、画像がどのような用途か不明な場合に指定しますが、ドライバによる最適化を妨げる可能性があるため出来る限り指定しない方が良いです (validation layerでも怒られたはず...?)


### StageMask
stage maskの指定には、以下のような[bitフラグ](https://registry.khronos.org/vulkan/specs/latest/man/html/VkPipelineStageFlagBits2.html)が用意されています

```cpp
typedef VkFlags64 VkPipelineStageFlagBits2;
static const VkPipelineStageFlagBits2 VK_PIPELINE_STAGE_2_NONE = 0ULL;
static const VkPipelineStageFlagBits2 VK_PIPELINE_STAGE_2_TOP_OF_PIPE_BIT = 0x00000001ULL;
static const VkPipelineStageFlagBits2 VK_PIPELINE_STAGE_2_DRAW_INDIRECT_BIT = 0x00000002ULL;
static const VkPipelineStageFlagBits2 VK_PIPELINE_STAGE_2_VERTEX_INPUT_BIT = 0x00000004ULL;
...
```

### AccessMask
access maskの指定には、以下のような[bitフラグ](https://registry.khronos.org/vulkan/specs/latest/man/html/VkAccessFlagBits2.html)が用意されています

```cpp
typedef VkFlags64 VkAccessFlagBits2;
static const VkAccessFlagBits2 VK_ACCESS_2_NONE = 0ULL;
static const VkAccessFlagBits2 VK_ACCESS_2_INDIRECT_COMMAND_READ_BIT = 0x00000001ULL;
static const VkAccessFlagBits2 VK_ACCESS_2_INDEX_READ_BIT = 0x00000002ULL;
static const VkAccessFlagBits2 VK_ACCESS_2_VERTEX_ATTRIBUTE_READ_BIT = 0x00000004ULL;
```

### 



### 



## 3. VkBufferMemoryBarrier2


## 感想
- [Vulkan-Hpp](https://github.com/KhronosGroup/Vulkan-Hpp) は便利なのでC++でVulkanを使うなら入れたい


## References
- [Yet another blog explaining Vulkan synchronization | Maister's Graphics Adventures](https://themaister.net/blog/2019/08/14/yet-another-blog-explaining-vulkan-synchronization/)
- [Vulkan® Barriers Explained | GPUOpen](https://gpuopen.com/learn/vulkan-barriers-explained/)