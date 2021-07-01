---
title: "compile.5"
date: 2021-07-01 16:52:55.106092
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
make package/feeds/packages/python-rcssmin/compile -j$(nproc) || make package/feeds/packages/python-rcssmin/compile V=s
```

#### Compile.txt

``` bash
running install
running build
running build_py
creating build
creating build/lib.-3.9
copying ./rcssmin.py -> build/lib.-3.9
warning: build_py: byte-compiling is disabled, skipping.

running build_ext
building '_rcssmin' extension
creating build/temp.-3.9
ccache_cc -Wno-unused-result -Wsign-compare -DNDEBUG -g -O3 -Wall -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/pypi/rcssmin-1.0.6=rcssmin-1.0.6 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -fPIC -DEXT_MODULE=_rcssmin -UEXT_PACKAGE -I_setup/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -c rcssmin.c -o build/temp.-3.9/rcssmin.o
In file included from rcssmin.c:18:
_setup/include/cext.h:34:10: fatal error: Python.h: No such file or directory
 #include "Python.h"
          ^~~~~~~~~~
compilation terminated.
error: command '/openwrt/staging_dir/host/bin/ccache_cc' failed with exit code 1
make[3]: *** [Makefile:47: /openwrt/build_dir/target-mips_24kc_musl/pypi/rcssmin-1.0.6/.built] Error 1
```
