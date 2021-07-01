---
title: "compile.5"
date: 2021-07-01 16:56:50.134488
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
make package/feeds/routing/hnetd/compile -j$(nproc) || make package/feeds/routing/hnetd/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/010-openssl-deprecated.patch using plaintext: 
patching file src/dtls.c

Applying ./patches/020-unused.patch using plaintext: 
patching file src/hnetd.h
CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 2.8.12 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- The C compiler identification is GNU 8.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/bin/mips-openwrt-linux-musl-gcc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Found PkgConfig: /openwrt/staging_dir/host/bin/pkg-config (found version "1.7.3") 
-- Checking for module 'json-c'
--   Found json-c, version 0.15
fatal: not a git repository (or any parent up to mount point /)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
CMake Error at /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:230 (message):
  Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the
  system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY
  OPENSSL_INCLUDE_DIR)
Call Stack (most recent call first):
  /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindPackageHandleStandardArgs.cmake:594 (_FPHSA_FAILURE_MESSAGE)
  /openwrt/staging_dir/host/share/cmake-3.20/Modules/FindOpenSSL.cmake:570 (find_package_handle_standard_args)
  CMakeLists.txt:32 (find_package)


-- Configuring incomplete, errors occurred!
See also "/openwrt/build_dir/target-mips_24kc_musl/hnetd-openssl/hnetd-2018-12-21-c4376661/CMakeFiles/CMakeOutput.log".
make[3]: *** [Makefile:165: /openwrt/build_dir/target-mips_24kc_musl/hnetd-openssl/hnetd-2018-12-21-c4376661/.configured_68b329da9893e34099c7d8ad5cb9c940] Error 1
```
