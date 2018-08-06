# API without Secrets: Introduction to Vulkan
by Pawel Lapinski

Source code examples for "API without Secrets: Introduction to Vulkan" tutorial which can be found at:

https://software.intel.com/en-us/articles/api-without-secrets-introduction-to-vulkan-preface

Special thanks to Slawomir Cygan for help and for patiently answering my many, many questions!

## Drivers:

Vulkan drivers and other related resources can be found at https://www.khronos.org/vulkan/

## Tutorials:

### [01 - The Beginning](./Project/Tutorials/01/)
<img src="./Document/Images/01 - The Beginning.png" height="96px" align="right">

#### Introduction to a Vulkan world
##### https://software.intel.com/en-us/articles/api-without-secrets-introduction-to-vulkan-part-1

Tutorial presents how to create all resources necessary to use Vulkan inside our application: function pointers loading, Vulkan instance creation, physical device enumeration, logical device creation and queue set up.

<hr>

### [02 - Swap chain](./Project/Tutorials/02/)
<img src="./Document/Images/02 - Swap Chain.png" height="96px" align="right">

#### Integrating Vulkan with OS
##### https://software.intel.com/en-us/articles/api-without-secrets-introduction-to-vulkan-part-2

This lesson focuses on a swap chain creation. Swap chain enables us to display Vulkan-generated image in an application window. To display anything simple command buffers are allocated and recorded.

<hr>

### [03 - First triangle](./Project/Tutorials/03/)
<img src="./Document/Images/03 - First Triangle.png" height="96px" align="right">

#### Graphics pipeline and drawing
##### https://software.intel.com/en-us/articles/api-without-secrets-introduction-to-vulkan-part-3

Here I present render pass, framebuffer and pipeline objects which are necessary to render arbitrary geometry. It is also shown how to convert GLSL shaders into SPIR-V and create shader modules from it.

<hr>

### [04 - Vertex Attributes](./Project/Tutorials/04/)
<img src="./Document/Images/04 - Vertex Attributes.png" height="96px" align="right">

#### Buffers, memory objects and fences
##### https://software.intel.com/en-us/articles/api-without-secrets-introduction-to-vulkan-part-4

This tutorial shows how to set up vertex attributes and bind buffer with a vertex data. Here we also create memory object (which is used by buffer) and fences.

<hr>

### [05 - Staging Resources](./Project/Tutorials/05/)
<img src="./Document/Images/05 - Staging Resources.png" height="96px" align="right">

#### Copying data between buffers
##### https://software.intel.com/en-us/articles/api-without-secrets-introduction-to-vulkan-part-5

In this example staging resources are presented. They are used as an intermediate resources for copying data between CPU and GPU. This way, resources involved in rendering can be bound only to a device local (very fast) memory.

<hr>

### [06 - Descriptor Sets](./Project/Tutorials/06/)
<img src="./Document/Images/06 - Descriptor Sets.png" height="96px" align="right">

#### Using textures in shaders
##### https://software.intel.com/en-us/articles/api-without-secrets-introduction-to-vulkan-part-6

This tutorial shows what resources are needed and how they should be prepared to be able to use textures (or other shader resources) in shader programs.

<hr>

### [07 - Uniform Buffers](./Project/Tutorials/07/)
<img src="./Document/Images/07 - Uniform Buffers.png" height="96px" align="right">

#### Using buffers in shaders
##### https://software.intel.com/en-us/articles/api-without-secrets-introduction-to-vulkan-part-7

Here it is shown how to add uniform buffer to descriptor sets, how to provide data for projection matrix through it and how to use it inside shader.
