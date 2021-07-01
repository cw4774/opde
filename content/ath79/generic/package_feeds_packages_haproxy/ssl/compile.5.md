---
title: "compile.5"
date: 2021-07-01 17:03:43.036641
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
make package/feeds/packages/haproxy/compile -j$(nproc) || make package/feeds/packages/haproxy/compile V=s
```

#### Compile.txt

``` bash
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/haproxy-ssl/haproxy-2.4.1'
  CC      src/ssl_sample.o
In file included from include/haproxy/listener-t.h:37,
                 from include/haproxy/server-t.h:36,
                 from include/haproxy/lb_map-t.h:26,
                 from include/haproxy/backend-t.h:30,
                 from include/haproxy/proxy-t.h:35,
                 from include/haproxy/hlua-t.h:32,
                 from include/haproxy/applet-t.h:29,
                 from include/haproxy/obj_type.h:26,
                 from src/ssl_sample.c:27:
include/haproxy/openssl-compat.h:5:10: fatal error: openssl/bn.h: No such file or directory
 #include <openssl/bn.h>
          ^~~~~~~~~~~~~~
compilation terminated.
make[4]: *** [Makefile:945: src/ssl_sample.o] Error 1
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/haproxy-ssl/haproxy-2.4.1'
make[3]: *** [Makefile:154: /openwrt/build_dir/target-mips_24kc_musl/haproxy-ssl/haproxy-2.4.1/.built] Error 2
```
