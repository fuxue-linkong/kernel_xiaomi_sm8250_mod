# FuXue Kernel for Xiaomi SM8250

[![Build Kernel](https://github.com/fuxue-linkong/kernel_xiaomi_sm8250_mod/actions/workflows/build.yml/badge.svg)](https://github.com/fuxue-linkong/kernel_xiaomi_sm8250_mod/actions/workflows/build.yml)

基于 LineageOS 22.1 内核源码，集成 [ReSukiSU](https://github.com/ReSukiSU/ReSukiSU)，内核版本 **4.19.325-FuXue1.0**

[English](#english) | [中文](#中文)

---

## English

### About this Kernel

This kernel is based on [LineageOS 22.1 xiaomi sm8250 kernel source](https://github.com/LineageOS/android_kernel_xiaomi_sm8250), with MIUI features and drivers ported from [UtsavBalar1231's kernel](https://github.com/UtsavBalar1231/kernel_xiaomi_sm8250).

Thanks to [@UtsavBalar1231](https://github.com/UtsavBalar1231/) and [@liyafe1997](https://github.com/liyafe1997) for the original work!

The main purpose of this kernel is to fix the [battery stuck at 1% problem](https://github.com/liyafe1997/Xiaomi-fix-battery-one-percent) on devices using PM8150 (Qualcomm fuel gauge GEN4), and provide [ReSukiSU](https://github.com/ReSukiSU/ReSukiSU) integrated pre-built images.

For using ReSukiSU, install the [ReSukiSU Manager](https://github.com/ReSukiSU/ReSukiSU/releases) APK.

Affected devices by the "1% battery bug": alioth, apollo, lmi, thyme, umi, pipa. For other devices, you can use this kernel as a KernelSU-enabled stock kernel replacement. The NoKernelSU version is also compatible with [APatch](https://github.com/bmax121/APatch).

Pre-built images are built from the `android15-lineage22-mod` branch. Works on stock MIUI/HyperOS and third-party AOSP Android 11-15 ROMs.

> **Note:** The zip does not include `dtbo.img`. Keep your stock `dtbo` or the one from your ROM. If you use MIUI/HyperOS, flash the **MIUI** variant — AOSP variant will cause black screen due to different display drivers.

### Supported Devices

| Code Name | Device Name                     |
|-----------|---------------------------------|
| psyche    | Xiaomi Mi 12X                   |
| thyme     | Xiaomi Mi 10S                   |
| umi       | Xiaomi Mi 10                    |
| munch     | Poco F4 / Redmi K40S            |
| lmi       | Redmi K30 Pro                   |
| cmi       | Xiaomi Mi 10 Pro                |
| cas       | Xiaomi Mi 10 Ultra              |
| apollo    | Xiaomi Mi 10T / Redmi K30S Ultra|
| alioth    | Xiaomi Mi 11X / POCO F3 / Redmi K40 |
| elish     | Xiaomi Pad 5 Pro                |
| enuma     | Xiaomi Pad 5 Pro 5G             |
| dagu      | Xiaomi Pad 5 Pro 12.4           |
| pipa      | Xiaomi Pad 6                    |

### Features

1. USB Serial support (CH340/FTDI/PL2303/CP210X and more)
2. EROFS support
3. F2FS realtime discard enabled
4. CANBus and USB CAN adapter support (e.g. CANable)
5. LZ4, LZ4HC, ZSTD compression for ZRAM
6. ReSukiSU integration (latest main branch)
7. LTO + ThinLTO optimization

### How to Build

1. **Prepare environment** (Debian/Ubuntu):
   ```bash
   sudo apt install build-essential git curl wget bison flex zip bc cpio libssl-dev ccache python-is-python3
   ```

2. **Download proton-clang toolchain**:
   ```bash
   mkdir -p ~/proton-clang
   cd ~/proton-clang
   wget https://github.com/kdrag0n/proton-clang/archive/refs/tags/20210522.zip
   unzip 20210522.zip
   cd -
   ```

3. **Build**:
   ```bash
   # Without KernelSU
   bash build.sh <device>

   # With ReSukiSU
   bash build.sh <device> ksu

   # Example: build for elish with ReSukiSU
   bash build.sh elish ksu
   ```

---

## 中文

### 关于本内核

该内核基于 [LineageOS 22.1 xiaomi sm8250 内核源码](https://github.com/LineageOS/android_kernel_xiaomi_sm8250)，MIUI 特性代码及部分驱动移植自 [UtsavBalar1231 的内核](https://github.com/UtsavBalar1231/kernel_xiaomi_sm8250)。

感谢 [@UtsavBalar1231](https://github.com/UtsavBalar1231/) 和 [@liyafe1997](https://github.com/liyafe1997) 的原始工作！

维护和编译该内核的主要目的是修复[电量卡在 1% 的问题](https://github.com/liyafe1997/Xiaomi-fix-battery-one-percent)，以及提供集成 [ReSukiSU](https://github.com/ReSukiSU/ReSukiSU) 的预编译内核。

使用 ReSukiSU 请安装 [ReSukiSU 管理器](https://github.com/ReSukiSU/ReSukiSU/releases) APK。

受"1% 电量 bug"影响的设备：alioth, apollo, lmi, thyme, umi, pipa（均使用 PM8150 高通 GEN4 电量计）。其他设备可当作带 KernelSU 的官核平替。不带 KernelSU 版本也可用于 [APatch](https://github.com/bmax121/APatch)。

Release 由 `android15-lineage22-mod` 分支编译，支持原版 MIUI/HyperOS 及第三方 AOSP Android 11-15 ROM。

> **注意：** zip 包不包含 `dtbo.img`。MIUI/HyperOS 用户请刷 **MIUI 版本**，AOSP 版本因 display 驱动不同会导致黑屏。

### 支持设备

| 设备代号 | 设备名称                        |
|----------|--------------------------------|
| psyche   | 小米 12X                        |
| thyme    | 小米 10S                        |
| umi      | 小米 10                         |
| munch    | 红米 K40S                       |
| lmi      | 红米 K30 Pro                    |
| cmi      | 小米 10 Pro                     |
| cas      | 小米 10 Ultra                   |
| apollo   | 小米 10T / 红米 K30S Ultra      |
| alioth   | 小米 11X / POCO F3 / 红米 K40   |
| elish    | 小米平板 5 Pro                  |
| enuma   | 小米平板 5 Pro 5G               |
| dagu     | 小米平板 5 Pro 12.4             |
| pipa     | 小米平板 6                      |

### 特性

1. 支持 USB 串口驱动（CH340/FTDI/PL2303/CP210X 等）
2. 支持 EROFS
3. F2FS 开启 realtime discard
4. 支持 CANBus 及 USB CAN 适配器（如 CANable）
5. ZRAM 支持 LZ4、LZ4HC、ZSTD 压缩算法
6. 集成 ReSukiSU（最新 main 分支）
7. LTO + ThinLTO 优化

### 构建指南

1. **准备环境**（Debian/Ubuntu）：
   ```bash
   sudo apt install build-essential git curl wget bison flex zip bc cpio libssl-dev ccache python-is-python3
   ```

2. **下载 proton-clang 工具链**：
   ```bash
   mkdir -p ~/proton-clang
   cd ~/proton-clang
   wget https://github.com/kdrag0n/proton-clang/archive/refs/tags/20210522.zip
   unzip 20210522.zip
   cd -
   ```

3. **编译**：
   ```bash
   # 不带 KernelSU
   bash build.sh <设备代号>

   # 带 ReSukiSU
   bash build.sh <设备代号> ksu

   # 示例：为 elish 编译带 ReSukiSU 的版本
   bash build.sh elish ksu
   ```

---

## CI 构建

本仓库使用 GitHub Actions 自动构建，每次 push 自动编译 elish 设备带 ReSukiSU 的内核。Workflow dispatch 支持手动选择设备和是否启用 KSU。

构建状态：[![Build Kernel](https://github.com/fuxue-linkong/kernel_xiaomi_sm8250_mod/actions/workflows/build.yml/badge.svg)](https://github.com/fuxue-linkong/kernel_xiaomi_sm8250_mod/actions/workflows/build.yml)