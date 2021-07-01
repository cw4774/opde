---
title: "compile.5"
date: 2021-07-01 16:48:03.269257
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
make package/feeds/packages/syslog-ng/compile -j$(nproc) || make package/feeds/packages/syslog-ng/compile V=s
```

#### Compile.txt

``` bash
configure: WARNING: you should use --build, --host, --target
configure: loading site script /openwrt/include/site/mips
checking whether make supports nested variables... yes
checking for a BSD-compatible install... /openwrt/staging_dir/host/bin/install -c
checking whether build environment is sane... yes
checking for mips-openwrt-linux-strip... mips-openwrt-linux-musl-strip
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether UID '1000' is supported by ustar format... yes
checking whether GID '1000' is supported by ustar format... yes
checking how to create a ustar tar archive... gnutar
checking for mips-openwrt-linux-gcc... ccache_cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... yes
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether ccache_cc accepts -g... yes
checking for ccache_cc option to accept ISO C89... none needed
checking whether ccache_cc understands -c and -o together... yes
checking whether make supports the include directive... yes (GNU style)
checking dependency style of ccache_cc... none
checking for ccache_cc option to accept ISO C99... none needed
checking for bison... bison -y
checking for flex... flex
checking lex output file root... lex.yy
checking lex library... none needed
checking whether yytext is a pointer... no
checking whether make sets $(MAKE)... (cached) yes
checking pkg-config is at least version 0.9.0... yes
checking build system type... x86_64-pc-linux-gnu
checking host system type... mips-openwrt-linux-gnu
checking how to print strings... printf
checking for a sed that does not truncate output... /openwrt/staging_dir/host/bin/sed
checking for grep that handles long lines and -e... /openwrt/staging_dir/host/bin/grep
checking for egrep... /openwrt/staging_dir/host/bin/grep -E
checking for fgrep... /openwrt/staging_dir/host/bin/grep -F
checking for ld used by ccache_cc... mips-openwrt-linux-musl-ld
checking if the linker (mips-openwrt-linux-musl-ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... mips-openwrt-linux-musl-gcc-nm
checking the name lister (mips-openwrt-linux-musl-gcc-nm) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 3145728
checking how to convert x86_64-pc-linux-gnu file names to mips-openwrt-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for mips-openwrt-linux-musl-ld option to reload object files... -r
checking for mips-openwrt-linux-objdump... mips-openwrt-linux-musl-objdump
checking how to recognize dependent libraries... pass_all
checking for mips-openwrt-linux-dlltool... no
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for mips-openwrt-linux-ar... mips-openwrt-linux-musl-gcc-ar
checking for archiver @FILE support... @
checking for mips-openwrt-linux-strip... (cached) mips-openwrt-linux-musl-strip
checking for mips-openwrt-linux-ranlib... mips-openwrt-linux-musl-gcc-ranlib
checking command to parse mips-openwrt-linux-musl-gcc-nm output from ccache_cc object... ok
checking for sysroot... no
checking for a working dd... /usr/bin/dd
checking how to truncate binary pipes... /usr/bin/dd bs=4096 count=1
checking for mips-openwrt-linux-mt... no
checking for mt... no
checking if : is a manifest tool... no
checking how to run the C preprocessor... ccache_cc -E
checking for ANSI C header files... yes
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking for dlfcn.h... yes
checking for objdir... .libs
checking if ccache_cc supports -fno-rtti -fno-exceptions... no
checking for ccache_cc option to produce PIC... -fPIC -DPIC
checking if ccache_cc PIC flag -fPIC -DPIC works... yes
checking if ccache_cc static flag -static works... yes
checking if ccache_cc supports -c -o file.o... yes
checking if ccache_cc supports -c -o file.o... (cached) yes
checking whether the ccache_cc linker (mips-openwrt-linux-musl-ld) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking for shl_load... no
checking for shl_load in -ldld... no
checking for dlopen... yes
checking whether a program can dlopen itself... cross
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... no
checking for python... /openwrt/staging_dir/host/bin/python
checking for python version... 3.8
checking for python platform... linux
checking for python script directory... ${prefix}/lib/python3.8/site-packages
checking for python extension module directory... ${exec_prefix}/lib/python3.8/site-packages
configure: WARNING: bison is found, but your bison version 3.7.4 is not recent enough, at least 3.7.6 is required
configure: WARNING: No proper bison found, you'll not be able to change lib/cfg-grammar.y
checking for C compiler vendor... gnu
checking for C compiler version... 8.4.0
checking CFLAGS_INITIALIZER_OVERRIDES for gcc -Winitializer-overrides... no, unknown
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking how to enable static linking for certain libraries... GNU or Solaris
checking for ANSI C header files... (cached) yes
checking dmalloc.h usability... no
checking dmalloc.h presence... no
checking for dmalloc.h... no
checking for dlfcn.h... (cached) yes
checking for strings.h... (cached) yes
checking getopt.h usability... yes
checking getopt.h presence... yes
checking for getopt.h... yes
checking stropts.h usability... yes
checking stropts.h presence... yes
checking for stropts.h... yes
checking sys/strlog.h usability... no
checking sys/strlog.h presence... no
checking for sys/strlog.h... no
checking door.h usability... no
checking door.h presence... no
checking for door.h... no
checking sys/capability.h usability... yes
checking sys/capability.h presence... yes
checking for sys/capability.h... yes
checking sys/prctl.h usability... yes
checking sys/prctl.h presence... yes
checking for sys/prctl.h... yes
checking utmp.h usability... yes
checking utmp.h presence... yes
checking for utmp.h... yes
checking utmpx.h usability... yes
checking utmpx.h presence... yes
checking for utmpx.h... yes
checking tcpd.h usability... no
checking tcpd.h presence... no
checking for tcpd.h... no
checking for struct ucred... yes
checking for struct cmsgcred... no
checking whether struct tm is in sys/time.h or time.h... time.h
checking for struct tm.tm_gmtoff... yes
checking for struct msghdr.msg_control... yes
checking for I_CONSLOG... yes
checking for O_LARGEFILE... yes
checking for struct sockaddr_storage... yes
checking for struct sockaddr_in6... yes
checking for PR_SET_KEEPCAPS... yes
checking for modern utmp... yes
checking for door_create in -ldoor... no
checking for socket in -lsocket... no
checking for nanosleep in -lrt... yes
checking for gethostbyname... yes
checking for regexec in -lregex... no
checking for res_init in -lresolv... yes
checking for strdup... yes
checking for strtol... yes
checking for strtoll... yes
checking for strtoimax... yes
checking for inet_aton... yes
checking for inet_ntoa... yes
checking for getaddrinfo... (cached) yes
checking for getnameinfo... yes
checking for getutent... yes
checking for getutxent... yes
checking for pread... yes
checking for pwrite... yes
checking for strcasestr... yes
checking for memrchr... yes
checking for localtime_r... yes
checking for getprotobynumber_r... no
checking for gmtime_r... yes
checking for strnlen... yes
checking for strtok_r... yes
checking for clock_gettime... yes
checking for inotify_init... yes
checking for getrandom... yes
checking for TCP wrapper library... 
checking for dlsym in -ldl... yes
checking for glib-2.0 >= 2.28 gmodule-2.0 gthread-2.0... yes
checking for g_list_copy_deep... yes
checking for g_queue_free_full... yes
checking for g_list_free_full... yes
checking for g_ptr_array_find_with_equal_func... yes
checking for g_canonicalize_filename... yes
checking for g_hash_table_contains... yes
checking sanity checking Glib headers... yes
checking for libpcre >= 6.1... yes
checking for openssl >= 0.9.8... no
configure: error: Cannot find OpenSSL libraries with version >= 0.9.8 it is a hard dependency from syslog-ng 3.7 onwards
make[3]: *** [Makefile:118: /openwrt/build_dir/target-mips_24kc_musl/syslog-ng-3.32.1/.configured_a07b4ff79575cde3e49412b959c90b5d] Error 1
```
