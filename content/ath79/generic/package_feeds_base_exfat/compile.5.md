---
title: "compile.5"
date: 2021-07-01 17:03:43.053329
hidden: false
draft: false
weight: -5
---

build number: `5`

#### re-implement command 

```bash
docker pull immortalwrt/opde:sdk
docker run -it --rm immortalwrt/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/exfat/compile -j$(nproc) || make package/feeds/base/exfat/compile V=s
```

#### Compile.txt

``` bash
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.128'
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-exfat-oot-5.11.1/inode.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-exfat-oot-5.11.1/namei.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-exfat-oot-5.11.1/dir.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-exfat-oot-5.11.1/super.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-exfat-oot-5.11.1/fatent.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-exfat-oot-5.11.1/cache.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-exfat-oot-5.11.1/nls.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-exfat-oot-5.11.1/misc.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-exfat-oot-5.11.1/file.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-exfat-oot-5.11.1/balloc.o
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-exfat-oot-5.11.1/exfat.o
  Building modules, stage 2.
  MODPOST 1 modules
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-exfat-oot-5.11.1/exfat.mod.o
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-exfat-oot-5.11.1/exfat.ko
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-5.4.128'
Package kmod-fs-exfat0 is missing dependencies for the following libraries:
nls_base.ko
make[3]: *** [Makefile:57: /openwrt/bin/targets/ath79/generic/packages/kmod-fs-exfat0_5.4.128+5.11.1-1_mips_24kc.ipk] Error 1
```
