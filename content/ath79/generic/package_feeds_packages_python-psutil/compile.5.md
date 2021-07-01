---
title: "compile.5"
date: 2021-07-01 16:51:03.348501
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
make package/feeds/packages/python-psutil/compile -j$(nproc) || make package/feeds/packages/python-psutil/compile V=s
```

#### Compile.txt

``` bash
Collecting setuptools-scm==4.1.2
  Downloading setuptools_scm-4.1.2.tar.gz (48 kB)
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
    Preparing wheel metadata: started
    Preparing wheel metadata: finished with status 'done'
Requirement already satisfied: setuptools in /openwrt/staging_dir/hostpkg/lib/python3.9/site-packages (from setuptools-scm==4.1.2->-r ../host-pip-requirements/setuptools-scm.txt (line 1)) (56.0.0)
Building wheels for collected packages: setuptools-scm
  Building wheel for setuptools-scm (PEP 517): started
  Building wheel for setuptools-scm (PEP 517): finished with status 'done'
  Created wheel for setuptools-scm: filename=setuptools_scm-4.1.2-py2.py3-none-any.whl size=27609 sha256=b799013aac06d72fa711c110677283147105b9334ae8522c34f3bba04608b954
  Stored in directory: /openwrt/dl/pip-cache/wheels/2c/84/a2/2ce84b03a15eafdce02eeae7cbd9870d7a40af09f076b2acda
Successfully built setuptools-scm
Installing collected packages: setuptools-scm
Successfully installed setuptools-scm-4.1.2
cc1: note: someone does not honour COPTS correctly, passed 0 times
running install
running build
running build_py
creating build
creating build/lib.-3.9
creating build/lib.-3.9/psutil
copying psutil/_psosx.py -> build/lib.-3.9/psutil
copying psutil/_pssunos.py -> build/lib.-3.9/psutil
copying psutil/__init__.py -> build/lib.-3.9/psutil
copying psutil/_common.py -> build/lib.-3.9/psutil
copying psutil/_compat.py -> build/lib.-3.9/psutil
copying psutil/_pslinux.py -> build/lib.-3.9/psutil
copying psutil/_psaix.py -> build/lib.-3.9/psutil
copying psutil/_pswindows.py -> build/lib.-3.9/psutil
copying psutil/_psposix.py -> build/lib.-3.9/psutil
copying psutil/_psbsd.py -> build/lib.-3.9/psutil
creating build/lib.-3.9/psutil/tests
copying psutil/tests/test_connections.py -> build/lib.-3.9/psutil/tests
copying psutil/tests/test_aix.py -> build/lib.-3.9/psutil/tests
copying psutil/tests/test_posix.py -> build/lib.-3.9/psutil/tests
copying psutil/tests/test_unicode.py -> build/lib.-3.9/psutil/tests
copying psutil/tests/test_bsd.py -> build/lib.-3.9/psutil/tests
copying psutil/tests/test_osx.py -> build/lib.-3.9/psutil/tests
copying psutil/tests/__init__.py -> build/lib.-3.9/psutil/tests
copying psutil/tests/__main__.py -> build/lib.-3.9/psutil/tests
copying psutil/tests/test_contracts.py -> build/lib.-3.9/psutil/tests
copying psutil/tests/test_linux.py -> build/lib.-3.9/psutil/tests
copying psutil/tests/runner.py -> build/lib.-3.9/psutil/tests
copying psutil/tests/test_process.py -> build/lib.-3.9/psutil/tests
copying psutil/tests/test_sunos.py -> build/lib.-3.9/psutil/tests
copying psutil/tests/test_memleaks.py -> build/lib.-3.9/psutil/tests
copying psutil/tests/test_misc.py -> build/lib.-3.9/psutil/tests
copying psutil/tests/test_testutils.py -> build/lib.-3.9/psutil/tests
copying psutil/tests/test_windows.py -> build/lib.-3.9/psutil/tests
copying psutil/tests/test_system.py -> build/lib.-3.9/psutil/tests
warning: build_py: byte-compiling is disabled, skipping.

running build_ext
building 'psutil._psutil_linux' extension
creating build/temp.-3.9
creating build/temp.-3.9/psutil
ccache_cc -Wno-unused-result -Wsign-compare -DNDEBUG -g -O3 -Wall -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -O2 -I/openwrt/staging_dir/host/include -I/openwrt/staging_dir/hostpkg/include -I/openwrt/staging_dir/target-mips_24kc_musl/host/include -Os -pipe -mno-branch-likely -mips32r2 -mtune=24kc -fno-caller-saves -fno-plt -fhonour-copts -Wno-error=unused-but-set-variable -Wno-error=unused-result -msoft-float -mips16 -minterlink-mips16 -fmacro-prefix-map=/openwrt/build_dir/target-mips_24kc_musl/pypi/psutil-5.8.0=psutil-5.8.0 -Wformat -Werror=format-security -fstack-protector -D_FORTIFY_SOURCE=1 -Wl,-z,now -Wl,-z,relro -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/usr/include -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include/fortify -I/openwrt/staging_dir/toolchain-mips_24kc_gcc-8.4.0_musl/include -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -fPIC -DPSUTIL_POSIX=1 -DPSUTIL_SIZEOF_PID_T=4 -DPSUTIL_VERSION=580 -DPSUTIL_LINUX=1 -I/openwrt/staging_dir/target-mips_24kc_musl/usr/include/python3.9 -c psutil/_psutil_common.c -o build/temp.-3.9/psutil/_psutil_common.o
psutil/_psutil_common.c:9:10: fatal error: Python.h: No such file or directory
 #include <Python.h>
          ^~~~~~~~~~
compilation terminated.
error: command '/openwrt/staging_dir/host/bin/ccache_cc' failed with exit code 1
make[3]: *** [Makefile:47: /openwrt/build_dir/target-mips_24kc_musl/pypi/psutil-5.8.0/.built] Error 1
```
