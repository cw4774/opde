---
title: "compile.5"
date: 2021-07-01 16:55:36.517837
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
make package/feeds/packages/RPi.GPIO/compile -j$(nproc) || make package/feeds/packages/RPi.GPIO/compile V=s
```

#### Compile.txt

``` bash
running install
running build
running build_py
creating build
creating build/lib.-3.9
creating build/lib.-3.9/RPi
copying RPi/__init__.py -> build/lib.-3.9/RPi
creating build/lib.-3.9/RPi/GPIO
copying RPi/GPIO/__init__.py -> build/lib.-3.9/RPi/GPIO
warning: build_py: byte-compiling is disabled, skipping.

running build_ext
building 'RPi._GPIO' extension
creating build/temp.-3.9
creating build/temp.-3.9/source
ccache_cc -Wno-unused-result -Wsign-compare -DNDEBUG -g -O3 -Wall -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/pypi/RPi.GPIO-0.7.0=RPi.GPIO-0.7.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -fPIC -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -c source/c_gpio.c -o build/temp.-3.9/source/c_gpio.o
ccache_cc -Wno-unused-result -Wsign-compare -DNDEBUG -g -O3 -Wall -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/pypi/RPi.GPIO-0.7.0=RPi.GPIO-0.7.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -fPIC -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -c source/common.c -o build/temp.-3.9/source/common.o
source/common.c:23:10: fatal error: Python.h: No such file or directory
 #include "Python.h"
          ^~~~~~~~~~
compilation terminated.
error: command '/openwrt/staging_dir/host/bin/ccache_cc' failed with exit code 1
make[3]: *** [Makefile:45: /openwrt/build_dir/target-mips_24kc_musl/pypi/RPi.GPIO-0.7.0/.built] Error 1
```
