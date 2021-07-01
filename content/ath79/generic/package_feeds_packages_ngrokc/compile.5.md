---
title: "compile.5"
date: 2021-07-01 16:51:03.339175
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
make package/feeds/packages/ngrokc/compile -j$(nproc) || make package/feeds/packages/ngrokc/compile V=s
```

#### Compile.txt

``` bash
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/ngrokc-1.54'
ccache_cxx -fexceptions -DOPENSSL=1 -O2   -c -o sendmsg.o sendmsg.cpp
In file included from sslbio.h:6,
                 from global.h:7,
                 from config.h:24,
                 from sendmsg.cpp:1:
opensslbio.h:5:9: fatal error: openssl/ssl.h: No such file or directory
 #include<openssl/ssl.h>
         ^~~~~~~~~~~~~~~
compilation terminated.
make[4]: *** [<builtin>: sendmsg.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/ngrokc-1.54'
make[3]: *** [Makefile:42: /openwrt/build_dir/target-mips_24kc_musl/ngrokc-1.54/.built] Error 2
```
