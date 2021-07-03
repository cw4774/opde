---
title: "compile.7"
date: 2021-07-03 03:47:14.896790
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
make package/feeds/base/rtl8812au-ac/compile -j$(nproc) || make package/feeds/base/rtl8812au-ac/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/001-use-kernel-byteorder.patch using plaintext: 
patching file include/drv_types.h

Applying ./patches/010-disable-default-build-x86.patch using plaintext: 
patching file Makefile

Applying ./patches/020-change-value-of-vht-enable-and-usb-mode.patch using plaintext: 
patching file os_dep/linux/os_intfs.c

Applying ./patches/030-add-missing-code-for-concurrent-mode.patch using plaintext: 
patching file os_dep/linux/os_intfs.c

Applying ./patches/040-wireless-5.8.patch using plaintext: 
patching file os_dep/linux/ioctl_cfg80211.c
make[3]: *** No rule to make target '/openwrt/staging_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/usr/include/mac80211-backport/backport/autoconf.h', needed by '/openwrt/build_dir/target-arm_cortex-a7+neon-vfpv4_musl_eabi/linux-ipq40xx_generic/rtl8812au-ac-2021-05-22-0b87ed92/.configured_68b329da9893e34099c7d8ad5cb9c940'.  Stop.
```
