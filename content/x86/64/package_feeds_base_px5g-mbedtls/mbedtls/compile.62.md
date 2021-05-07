---
title: "compile.62"
date: 2021-05-05 14:26:33.264877
hidden: false
draft: false
weight: -62
---

build number: `62`

#### re-implement command 

```bash
docker pull elonh/opde:sdk
docker run -it --rm elonh/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make package/feeds/base/px5g-mbedtls/compile -j$(nproc) || make package/feeds/base/px5g-mbedtls/compile V=s
```

#### Compile.txt

``` bash
Package px5g-mbedtls is missing dependencies for the following libraries:
libmbedtls.so.9
make[3]: *** [Makefile:77: /openwrt/bin/packages/x86_64/base/px5g-mbedtls_9_x86_64.ipk] Error 1
```