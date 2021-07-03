---
title: "compile.7"
date: 2021-07-03 03:36:31.721878
hidden: false
draft: false
weight: -7
---

build number: `7`

#### re-implement command 

```bash
docker pull immortalwrt/opde:sdk
docker run -it --rm immortalwrt/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/button-hotplug/compile -j$(nproc) || make package/feeds/base/button-hotplug/compile V=s
```

#### Compile.txt

``` bash
make[4]: Entering directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/linux-5.4.128'
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/button-hotplug/button-hotplug.o
  Building modules, stage 2.
  MODPOST 1 modules
  CC [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/button-hotplug/button-hotplug.mod.o
  LD [M]  /openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/button-hotplug/button-hotplug.ko
make[4]: Leaving directory '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/linux-5.4.128'
Package kmod-button-hotplug is missing dependencies for the following libraries:
input-core.ko
make[3]: *** [Makefile:60: /openwrt/bin/targets/ipq40xx/generic/packages/kmod-button-hotplug_5.4.128-3_arm_cortex-a7_neon-vfpv4.ipk] Error 1
```
