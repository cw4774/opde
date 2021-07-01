---
title: "compile.5"
date: 2021-07-01 17:06:20.977641
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
make package/feeds/packages/ffmpeg/compile -j$(nproc) || make package/feeds/packages/ffmpeg/compile V=s
```

#### Compile.txt

``` bash
ERROR: openssl not found

If you think configure made a mistake, make sure you are using the latest
version from Git.  If the latest version fails, report the problem to the
ffmpeg-user@ffmpeg.org mailing list or IRC #ffmpeg on irc.freenode.net.
Include the log file "ffbuild/config.log" produced by configure as this will help
solve the problem.
make[3]: *** [Makefile:754: /openwrt/build_dir/target-mips_24kc_musl/ffmpeg-full/ffmpeg-4.3.2/.configured_e78145485e6b0d78ca0a7ad0e57c975b] Error 1
```
