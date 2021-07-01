---
title: "compile.5"
date: 2021-07-01 17:06:21.018964
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
make package/feeds/base/mac80211/compile -j$(nproc) || make package/feeds/base/mac80211/compile V=s
```

#### Compile.txt

``` bash
Applying ./patches/build/000-fix_kconfig.patch using plaintext: 
patching file kconf/Makefile

Applying ./patches/build/001-fix_build.patch using plaintext: 
patching file Makefile
patching file Makefile.real

Applying ./patches/build/002-change_allconfig.patch using plaintext: 
patching file kconf/conf.c
patching file kconf/confdata.c

Applying ./patches/build/003-remove_bogus_modparams.patch using plaintext: 
patching file compat/main.c

Applying ./patches/build/004-kconfig_backport_fix.patch using plaintext: 
patching file backport-include/linux/kconfig.h

Applying ./patches/build/010-disable_rfkill.patch using plaintext: 
patching file backport-include/linux/rfkill.h

Applying ./patches/build/012-kernel_build_check.patch using plaintext: 
patching file Makefile

Applying ./patches/build/015-ipw200-mtu.patch using plaintext: 
patching file drivers/net/wireless/intel/ipw2x00/ipw2200.c

Applying ./patches/build/050-lib80211_option.patch using plaintext: 
patching file net/wireless/Kconfig

Applying ./patches/build/060-no_local_ssb_bcma.patch using plaintext: 
patching file local-symbols
patching file drivers/net/wireless/broadcom/b43/Kconfig
patching file drivers/net/wireless/broadcom/b43/main.c
patching file drivers/net/wireless/broadcom/b43legacy/Kconfig
patching file drivers/net/wireless/broadcom/b43legacy/main.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmsmac/led.h
patching file drivers/net/wireless/broadcom/brcm80211/brcmsmac/Makefile
patching file drivers/net/wireless/broadcom/brcm80211/Kconfig
patching file Kconfig.local
patching file Kconfig.sources
patching file Makefile.kernel

Applying ./patches/subsys/010-sync-nl80211_h.patch using plaintext: 
patching file include/uapi/linux/nl80211.h

Applying ./patches/subsys/110-mac80211_keep_keys_on_stop_ap.patch using plaintext: 
patching file net/mac80211/cfg.c

Applying ./patches/subsys/120-cfg80211_allow_perm_addr_change.patch using plaintext: 
patching file net/wireless/sysfs.c

Applying ./patches/subsys/150-disable_addr_notifier.patch using plaintext: 
patching file net/mac80211/main.c

Applying ./patches/subsys/210-ap_scan.patch using plaintext: 
patching file net/mac80211/cfg.c

Applying ./patches/subsys/300-cfg80211-support-immediate-reconnect-request-hint.patch using plaintext: 
patching file include/net/cfg80211.h
patching file net/mac80211/mlme.c
patching file net/wireless/mlme.c
patching file net/wireless/nl80211.c
patching file net/wireless/nl80211.h
patching file net/wireless/trace.h

Applying ./patches/subsys/301-mac80211-support-driver-based-disconnect-with-reconn.patch using plaintext: 
patching file include/net/mac80211.h
patching file net/mac80211/ieee80211_i.h
patching file net/mac80211/mlme.c
patching file net/mac80211/trace.h

Applying ./patches/subsys/302-cfg80211-Add-support-to-configure-SAE-PWE-value-to-d.patch using plaintext: 
patching file include/net/cfg80211.h
patching file net/wireless/nl80211.c

Applying ./patches/subsys/304-mac80211-sta-randomize-BA-session-dialog-token-alloc.patch using plaintext: 
patching file net/mac80211/sta_info.c

Applying ./patches/subsys/310-net-fq_impl-bulk-free-packets-from-a-flow-on-overmem.patch using plaintext: 
patching file include/net/fq_impl.h

Applying ./patches/subsys/311-net-fq_impl-drop-get_default_func-move-default-flow-.patch using plaintext: 
patching file include/net/fq.h
patching file include/net/fq_impl.h
patching file net/mac80211/ieee80211_i.h
patching file net/mac80211/tx.c

Applying ./patches/subsys/312-net-fq_impl-do-not-maintain-a-backlog-sorted-list-of.patch using plaintext: 
patching file include/net/fq.h
patching file include/net/fq_impl.h
patching file net/mac80211/tx.c

Applying ./patches/subsys/315-mac80211-add-rx-decapsulation-offload-support.patch using plaintext: 
patching file include/net/mac80211.h
patching file net/mac80211/debugfs.c
patching file net/mac80211/debugfs_sta.c
patching file net/mac80211/driver-ops.h
patching file net/mac80211/iface.c
patching file net/mac80211/rx.c
patching file net/mac80211/sta_info.h
patching file net/mac80211/trace.h

Applying ./patches/subsys/320-mac80211_hwsim-add-6GHz-channels.patch using plaintext: 
patching file drivers/net/wireless/mac80211_hwsim.c

Applying ./patches/subsys/321-mac80211_hwsim-make-6-GHz-channels-usable.patch using plaintext: 
patching file drivers/net/wireless/mac80211_hwsim.c

Applying ./patches/subsys/337-mac80211-minstrel_ht-clean-up-CCK-code.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht.h

Applying ./patches/subsys/338-mac80211-minstrel_ht-add-support-for-OFDM-rates-on-n.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel.h
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht.h
patching file net/mac80211/rc80211_minstrel_ht_debugfs.c

Applying ./patches/subsys/339-mac80211-remove-legacy-minstrel-rate-control.patch using plaintext: 
patching file net/mac80211/Makefile
patching file net/mac80211/rc80211_minstrel.c
patching file net/mac80211/rc80211_minstrel.h
patching file net/mac80211/rc80211_minstrel_debugfs.c
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht.h
patching file net/mac80211/rc80211_minstrel_ht_debugfs.c

Applying ./patches/subsys/340-mac80211-minstrel_ht-remove-old-ewma-based-rate-aver.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht.h

Applying ./patches/subsys/341-mac80211-minstrel_ht-improve-ampdu-length-estimation.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/342-mac80211-minstrel_ht-improve-sample-rate-selection.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/343-mac80211-minstrel_ht-fix-max-probability-rate-select.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/344-mac80211-minstrel_ht-increase-stats-update-interval.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/345-mac80211-minstrel_ht-fix-rounding-error-in-throughpu.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/346-mac80211-minstrel_ht-use-bitfields-to-encode-rate-in.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht.h
patching file net/mac80211/rc80211_minstrel_ht_debugfs.c

Applying ./patches/subsys/347-mac80211-minstrel_ht-update-total-packets-counter-in.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/348-mac80211-minstrel_ht-reduce-the-need-to-sample-slowe.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht.h

Applying ./patches/subsys/349-mac80211-minstrel_ht-significantly-redesign-the-rate.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht.h

Applying ./patches/subsys/350-mac80211-minstrel_ht-show-sampling-rates-in-debugfs.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht_debugfs.c

Applying ./patches/subsys/351-mac80211-minstrel_ht-remove-sample-rate-switching-co.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c
patching file net/mac80211/rc80211_minstrel_ht.h

Applying ./patches/subsys/352-mac80211-minstrel_ht-fix-regression-in-the-max_prob_.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/353-mac80211-minstrel_ht-fix-MINSTREL_FRAC-macro.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.h

Applying ./patches/subsys/354-mac80211-minstrel_ht-reduce-fluctuations-in-rate-pro.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/355-mac80211-minstrel_ht-rework-rate-downgrade-code-and-.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c

Applying ./patches/subsys/371-mac80211-don-t-apply-flow-control-on-management-fram.patch using plaintext: 
patching file net/mac80211/tx.c

Applying ./patches/subsys/372-mac80211-set-sk_pacing_shift-for-802.3-txpath.patch using plaintext: 
patching file net/mac80211/tx.c

Applying ./patches/subsys/373-mac80211-support-Rx-timestamp-calculation-for-all-pr.patch using plaintext: 
patching file net/mac80211/ieee80211_i.h
patching file net/mac80211/util.c

Applying ./patches/subsys/374-mac80211-move-A-MPDU-session-check-from-minstrel_ht-.patch using plaintext: 
patching file include/net/mac80211.h
patching file net/mac80211/rc80211_minstrel_ht.c
Hunk #1 succeeded at 1144 (offset -9 lines).
Hunk #2 succeeded at 1438 (offset -16 lines).
Hunk #3 succeeded at 1843 (offset -24 lines).
patching file net/mac80211/tx.c

Applying ./patches/subsys/375-mac80211-call-ieee80211_tx_h_rate_ctrl-when-dequeue.patch using plaintext: 
patching file net/mac80211/tx.c

Applying ./patches/subsys/376-mac80211-add-rate-control-support-for-encap-offload.patch using plaintext: 
patching file net/mac80211/ieee80211_i.h
patching file net/mac80211/rate.c
patching file net/mac80211/tx.c

Applying ./patches/subsys/377-mac80211-minstrel_ht-fix-sample-time-check.patch using plaintext: 
patching file net/mac80211/rc80211_minstrel_ht.c
Hunk #1 succeeded at 1450 (offset -16 lines).

Applying ./patches/subsys/378-mac80211-remove-iwlwifi-specific-workaround-that-bro.patch using plaintext: 
patching file drivers/net/wireless/intel/iwlwifi/mvm/tx.c
patching file net/mac80211/mlme.c

Applying ./patches/subsys/379-mac80211-fix-starting-aggregation-sessions-on-mesh-i.patch using plaintext: 
patching file net/mac80211/tx.c

Applying ./patches/subsys/400-allow-ibss-mixed.patch using plaintext: 
patching file net/wireless/core.c

Applying ./patches/subsys/500-mac80211_configure_antenna_gain.patch using plaintext: 
patching file include/net/cfg80211.h
patching file include/net/mac80211.h
patching file include/uapi/linux/nl80211.h
patching file net/mac80211/cfg.c
patching file net/mac80211/ieee80211_i.h
patching file net/mac80211/main.c
patching file net/wireless/nl80211.c

Applying ./patches/subsys/600-mac80211-allow-vht-on-2g.patch using plaintext: 
patching file net/mac80211/vht.c
patching file net/mac80211/util.c
Hunk #1 succeeded at 1906 (offset 137 lines).
patching file net/mac80211/mlme.c
Hunk #1 succeeded at 5067 (offset 243 lines).

Applying ./patches/ath/070-ath_common_config.patch using plaintext: 
patching file drivers/net/wireless/ath/Kconfig

Applying ./patches/ath/120-owl-loader-compat.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/ath9k_pci_owl_loader.c

Applying ./patches/ath/400-ath_move_debug_code.patch using plaintext: 
patching file drivers/net/wireless/ath/Makefile
patching file drivers/net/wireless/ath/ath.h

Applying ./patches/ath/402-ath_regd_optional.patch using plaintext: 
patching file drivers/net/wireless/ath/regd.c
patching file drivers/net/wireless/ath/Kconfig
patching file local-symbols
Hunk #1 succeeded at 85 (offset -1 lines).

Applying ./patches/ath/403-world_regd_fixup.patch using plaintext: 
patching file drivers/net/wireless/ath/regd.c

Applying ./patches/ath/404-regd_no_assoc_hints.patch using plaintext: 
patching file net/wireless/reg.c

Applying ./patches/ath/405-ath_regd_us.patch using plaintext: 
patching file drivers/net/wireless/ath/regd_common.h

Applying ./patches/ath/406-ath_relax_default_regd.patch using plaintext: 
patching file drivers/net/wireless/ath/regd.c

Applying ./patches/ath/431-add_platform_eeprom_support_to_ath5k.patch using plaintext: 
patching file drivers/net/wireless/ath/ath5k/pci.c

Applying ./patches/ath5k/201-ath5k-WAR-for-AR71xx-PCI-bug.patch using plaintext: 
patching file drivers/net/wireless/ath/ath5k/initvals.c
patching file drivers/net/wireless/ath/ath5k/dma.c

Applying ./patches/ath5k/411-ath5k_allow_adhoc_and_ap.patch using plaintext: 
patching file drivers/net/wireless/ath/ath5k/mac80211-ops.c
patching file drivers/net/wireless/ath/ath5k/base.c

Applying ./patches/ath5k/420-ath5k_disable_fast_cc.patch using plaintext: 
patching file drivers/net/wireless/ath/ath5k/reset.c

Applying ./patches/ath5k/430-add_ath5k_platform.patch using plaintext: 
patching file include/linux/ath5k_platform.h

Applying ./patches/ath5k/432-ath5k_add_pciids.patch using plaintext: 
patching file drivers/net/wireless/ath/ath5k/pci.c

Applying ./patches/ath5k/440-ath5k_channel_bw_debugfs.patch using plaintext: 
patching file drivers/net/wireless/ath/ath5k/debug.c
patching file drivers/net/wireless/ath/ath5k/ath5k.h
patching file drivers/net/wireless/ath/ath5k/base.c

Applying ./patches/ath9k/350-ath9k_hw-reset-AHB-WMAC-interface-on-AR91xx.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/hw.c

Applying ./patches/ath9k/351-ath9k_hw-issue-external-reset-for-QCA955x.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/hw.c

Applying ./patches/ath9k/354-ath9k-force-rx_clear-when-disabling-rx.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/mac.c

Applying ./patches/ath9k/356-Revert-ath9k-interpret-requested-txpower-in-EIRP-dom.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/hw.c

Applying ./patches/ath9k/365-ath9k-adjust-tx-power-reduction-for-US-regulatory-do.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/hw.c

Applying ./patches/ath9k/401-ath9k_blink_default.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/init.c

Applying ./patches/ath9k/410-ath9k_allow_adhoc_and_ap.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/init.c

Applying ./patches/ath9k/450-ath9k-enabled-MFP-capability-unconditionally.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/init.c

Applying ./patches/ath9k/500-ath9k_eeprom_debugfs.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/debug.c

Applying ./patches/ath9k/501-ath9k_ahb_init.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/init.c

Applying ./patches/ath9k/510-ath9k_intr_mitigation_tweak.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/hw.c

Applying ./patches/ath9k/511-ath9k_reduce_rxbuf.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/ath9k.h

Applying ./patches/ath9k/512-ath9k_channelbw_debugfs.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/debug.c
patching file drivers/net/wireless/ath/ath.h
patching file drivers/net/wireless/ath/ath9k/common.c

Applying ./patches/ath9k/513-ath9k_add_pci_ids.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/hw.c
patching file drivers/net/wireless/ath/ath9k/hw.h
patching file drivers/net/wireless/ath/ath9k/pci.c

Applying ./patches/ath9k/530-ath9k_extra_leds.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/ath9k.h
patching file drivers/net/wireless/ath/ath9k/gpio.c
patching file drivers/net/wireless/ath/ath9k/init.c
patching file drivers/net/wireless/ath/ath9k/debug.c

Applying ./patches/ath9k/531-ath9k_extra_platform_leds.patch using plaintext: 
patching file include/linux/ath9k_platform.h
patching file drivers/net/wireless/ath/ath9k/gpio.c

Applying ./patches/ath9k/540-ath9k_reduce_ani_interval.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/ani.h

Applying ./patches/ath9k/542-ath9k_debugfs_diag.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/debug.c
patching file drivers/net/wireless/ath/ath9k/hw.h
patching file drivers/net/wireless/ath/ath9k/hw.c
patching file drivers/net/wireless/ath/ath9k/main.c

Applying ./patches/ath9k/543-ath9k_entropy_from_adc.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/hw.h
patching file drivers/net/wireless/ath/ath9k/ar9003_phy.c
patching file drivers/net/wireless/ath/ath9k/init.c
patching file drivers/net/wireless/ath/ath9k/hw-ops.h
patching file drivers/net/wireless/ath/ath9k/ar5008_phy.c
patching file drivers/net/wireless/ath/ath9k/ar9002_phy.h

Applying ./patches/ath9k/544-ath9k-ar933x-usb-hang-workaround.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/hw.c
patching file drivers/net/wireless/ath/ath9k/phy.h

Applying ./patches/ath9k/545-ath9k_ani_ws_detect.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/ar5008_phy.c
patching file drivers/net/wireless/ath/ath9k/ar9003_phy.c

Applying ./patches/ath9k/547-ath9k_led_defstate_fix.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/gpio.c

Applying ./patches/ath9k/548-ath9k_enable_gpio_chip.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/ath9k.h
patching file drivers/net/wireless/ath/ath9k/gpio.c

Applying ./patches/ath9k/549-ath9k_enable_gpio_buttons.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/ath9k.h
patching file drivers/net/wireless/ath/ath9k/gpio.c
patching file include/linux/ath9k_platform.h

Applying ./patches/ath9k/550-ath9k-disable-bands-via-dt.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/init.c

Applying ./patches/ath9k/551-ath9k_ubnt_uap_plus_hsr.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/channel.c
patching file drivers/net/wireless/ath/ath9k/hsr.c
patching file drivers/net/wireless/ath/ath9k/hsr.h
patching file drivers/net/wireless/ath/ath9k/main.c
patching file drivers/net/wireless/ath/ath9k/Makefile
patching file local-symbols
Hunk #1 succeeded at 112 (offset -1 lines).
patching file drivers/net/wireless/ath/ath9k/Kconfig

Applying ./patches/ath9k/552-ath9k-ahb_of.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/ahb.c
patching file drivers/net/wireless/ath/ath9k/ath9k.h

Applying ./patches/ath9k/553-ath9k_of_gpio_mask.patch using plaintext: 
patching file drivers/net/wireless/ath/ath9k/init.c

Applying ./patches/ath10k/080-ath10k_thermal_config.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/Kconfig
patching file drivers/net/wireless/ath/ath10k/Makefile
patching file drivers/net/wireless/ath/ath10k/thermal.h
patching file local-symbols
Hunk #1 succeeded at 144 (offset -1 lines).

Applying ./patches/ath10k/921-ath10k_init_devices_synchronously.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/core.c

Applying ./patches/ath10k/922-ath10k-increase-rx-buffer-size-to-2048.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/htt.h

Applying ./patches/ath10k/930-ath10k_add_tpt_led_trigger.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/mac.c

Applying ./patches/ath10k/974-ath10k_add-LED-and-GPIO-controlling-support-for-various-chipsets.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/Kconfig
patching file drivers/net/wireless/ath/ath10k/Makefile
patching file local-symbols
Hunk #1 succeeded at 145 (offset -1 lines).
patching file drivers/net/wireless/ath/ath10k/core.c
patching file drivers/net/wireless/ath/ath10k/core.h
patching file drivers/net/wireless/ath/ath10k/hw.h
patching file drivers/net/wireless/ath/ath10k/leds.c
patching file drivers/net/wireless/ath/ath10k/leds.h
patching file drivers/net/wireless/ath/ath10k/mac.c
patching file drivers/net/wireless/ath/ath10k/wmi-ops.h
patching file drivers/net/wireless/ath/ath10k/wmi-tlv.c
patching file drivers/net/wireless/ath/ath10k/wmi.c
patching file drivers/net/wireless/ath/ath10k/wmi.h

Applying ./patches/ath10k/975-ath10k-use-tpt-trigger-by-default.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/core.h
patching file drivers/net/wireless/ath/ath10k/leds.c
patching file drivers/net/wireless/ath/ath10k/mac.c

Applying ./patches/ath10k/980-ath10k-fix-max-antenna-gain-unit.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/mac.c

Applying ./patches/ath10k/981-ath10k-adjust-tx-power-reduction-for-US-regulatory-d.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/mac.c

Applying ./patches/ath10k/983-ath10k-allow-vht-on-2g.patch using plaintext: 
patching file drivers/net/wireless/ath/ath10k/mac.c
Hunk #1 succeeded at 4834 (offset 116 lines).

Applying ./patches/rt2x00/002-rt2x00-define-RF5592-in-init_eeprom-routine.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/100-rt2x00_options.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/Kconfig

Applying ./patches/rt2x00/501-rt2x00-allow-to-build-rt2800soc-module-for-RT3883.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/Kconfig

Applying ./patches/rt2x00/601-rt2x00-introduce-rt2x00_platform_h.patch using plaintext: 
patching file include/linux/rt2x00_platform.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h

Applying ./patches/rt2x00/602-rt2x00-introduce-rt2x00eeprom.patch using plaintext: 
patching file local-symbols
Hunk #1 succeeded at 332 (offset -1 lines).
patching file drivers/net/wireless/ralink/rt2x00/Kconfig
patching file drivers/net/wireless/ralink/rt2x00/Makefile
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.h
patching file drivers/net/wireless/ralink/rt2x00/rt2800soc.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00dev.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00eeprom.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00lib.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00soc.c

Applying ./patches/rt2x00/603-rt2x00-of_load_eeprom_filename.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00eeprom.c

Applying ./patches/rt2x00/604-rt2x00-load-eeprom-on-SoC-from-a-mtd-device-defines-.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/Kconfig
patching file drivers/net/wireless/ralink/rt2x00/rt2x00eeprom.c

Applying ./patches/rt2x00/606-rt2x00-allow_disabling_bands_through_platform_data.patch using plaintext: 
patching file include/linux/rt2x00_platform.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00dev.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h

Applying ./patches/rt2x00/607-rt2x00-add_platform_data_mac_addr.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00dev.c
patching file include/linux/rt2x00_platform.h

Applying ./patches/rt2x00/608-rt2x00-allow_disabling_bands_through_dts.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00dev.c

Applying ./patches/rt2x00/609-rt2x00-make-wmac-loadable-via-OF-on-rt288x-305x-SoC.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800soc.c

Applying ./patches/rt2x00/610-rt2x00-change-led-polarity-from-OF.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00leds.c

Applying ./patches/rt2x00/611-rt2x00-add-AP+STA-support.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00dev.c

Applying ./patches/rt2x00/612-rt2x00-led-tpt-trigger-support.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2x00dev.c

Applying ./patches/rt2x00/650-rt2x00-add-support-for-external-PA-on-MT7620.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800.h
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/982-rt2x00-add-rf-self-txdc-calibration.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/983-rt2x00-add-r-calibration.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/984-rt2x00-add-rxdcoc-calibration.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/985-rt2x00-add-rxiq-calibration.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/986-rt2x00-add-TX-LOFT-calibration.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.h

Applying ./patches/rt2x00/990-rt2x00-mt7620-introduce-accessors-for-CHIP_VER-register.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.h
patching file drivers/net/wireless/ralink/rt2x00/rt2800pci.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800soc.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800usb.c

Applying ./patches/rt2x00/991-rt2x00-mt7620-differentiate-based-on-SoC-CHIP_VER.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800.h
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c

Applying ./patches/rt2x00/992-rt2x00-save-survey-for-every-channel-visited.patch using plaintext: 
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800lib.h
patching file drivers/net/wireless/ralink/rt2x00/rt2800pci.c
patching file drivers/net/wireless/ralink/rt2x00/rt2800soc.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00.h
patching file drivers/net/wireless/ralink/rt2x00/rt2x00dev.c
patching file drivers/net/wireless/ralink/rt2x00/rt2x00mac.c

Applying ./patches/mwl/700-mwl8k-missing-pci-id-for-WNR854T.patch using plaintext: 
patching file drivers/net/wireless/marvell/mwl8k.c

Applying ./patches/mwl/801-libertas-configure-sysfs-links.patch using plaintext: 
patching file drivers/net/wireless/marvell/libertas/cfg.c
patching file drivers/net/wireless/marvell/libertas/main.c

Applying ./patches/mwl/802-libertas-set-wireless-macaddr.patch using plaintext: 
patching file drivers/net/wireless/marvell/libertas/cfg.c

Applying ./patches/mwl/940-mwl8k_init_devices_synchronously.patch using plaintext: 
patching file drivers/net/wireless/marvell/mwl8k.c

Applying ./patches/brcm/040-brcmutil_option.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/Kconfig

Applying ./patches/brcm/810-b43-gpio-mask-module-option.patch using plaintext: 
patching file drivers/net/wireless/broadcom/b43/b43.h
patching file drivers/net/wireless/broadcom/b43/main.c

Applying ./patches/brcm/811-b43_no_pio.patch using plaintext: 
patching file drivers/net/wireless/broadcom/b43/Makefile
patching file drivers/net/wireless/broadcom/b43/main.c
patching file drivers/net/wireless/broadcom/b43/pio.h
patching file drivers/net/wireless/broadcom/b43/Kconfig

Applying ./patches/brcm/812-b43-add-antenna-control.patch using plaintext: 
patching file drivers/net/wireless/broadcom/b43/main.c
patching file drivers/net/wireless/broadcom/b43/b43.h

Applying ./patches/brcm/813-b43-reduce-number-of-RX-slots.patch using plaintext: 
patching file drivers/net/wireless/broadcom/b43/dma.h

Applying ./patches/brcm/814-b43-only-use-gpio-0-1-for-led.patch using plaintext: 
patching file drivers/net/wireless/broadcom/b43/main.c

Applying ./patches/brcm/815-b43-always-take-overlapping-devs.patch using plaintext: 
patching file drivers/net/wireless/broadcom/b43/main.c

Applying ./patches/brcm/850-brcmsmac-remove-extra-regulation-restriction.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmsmac/channel.c

Applying ./patches/brcm/860-brcmfmac-register-wiphy-s-during-module_init.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/firmware.c

Applying ./patches/brcm/861-brcmfmac-workaround-bug-with-some-inconsistent-BSSes.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c

Applying ./patches/brcm/862-brcmfmac-Disable-power-management.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c

Applying ./patches/brcm/863-brcmfmac-add-in-driver-tables-with-country-codes.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/of.c

Applying ./patches/brcm/864-brcmfmac-do-not-use-internal-roaming-engine-by-default.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/common.c

Applying ./patches/brcm/998-survey.patch using plaintext: 
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/cfg80211.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.c
patching file drivers/net/wireless/broadcom/brcm80211/brcmfmac/core.h

Applying ./patches/rtl/002-v5.13-rtlwifi-implement-set_tim-by-update-beacon-content.patch using plaintext: 
patching file drivers/net/wireless/realtek/rtlwifi/core.c
patching file drivers/net/wireless/realtek/rtlwifi/core.h
patching file drivers/net/wireless/realtek/rtlwifi/usb.c
patching file drivers/net/wireless/realtek/rtlwifi/wifi.h
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1'
Generating local configuration database from kernel ... done.
cc -Wall -Wmissing-prototypes -Wstrict-prototypes -O2 -fomit-frame-pointer -DKBUILD_NO_NLS   -c -o conf.o conf.c
conf.c: In function 'conf_askvalue':
conf.c:89:3: warning: format not a string literal and no format arguments [-Wformat-security]
   89 |   printf(_("(NEW) "));
      |   ^~~~~~
conf.c: In function 'conf_choice':
conf.c:285:5: warning: format not a string literal and no format arguments [-Wformat-security]
  285 |     printf(_(" (NEW)"));
      |     ^~~~~~
conf.c: In function 'check_conf':
conf.c:440:6: warning: format not a string literal and no format arguments [-Wformat-security]
  440 |      printf(_("*\n* Restart config...\n*\n"));
      |      ^~~~~~
conf.c: In function 'main':
conf.c:617:6: warning: format not a string literal and no format arguments [-Wformat-security]
  617 |      _("\n*** The configuration requires explicit update.\n\n"));
      |      ^
conf.c:669:4: warning: format not a string literal and no format arguments [-Wformat-security]
  669 |    fprintf(stderr, _("\n*** Error during writing of the configuration.\n\n"));
      |    ^~~~~~~
conf.c:673:4: warning: format not a string literal and no format arguments [-Wformat-security]
  673 |    fprintf(stderr, _("\n*** Error during update of the configuration.\n\n"));
      |    ^~~~~~~
conf.c:684:4: warning: format not a string literal and no format arguments [-Wformat-security]
  684 |    fprintf(stderr, _("\n*** Error during writing of the configuration.\n\n"));
      |    ^~~~~~~
lex -ozconf.lex.c -L zconf.l
yacc -ozconf.tab.c -t -l zconf.y
zconf.y:34.1-7: warning: POSIX Yacc does not support %expect [-Wyacc]
   34 | %expect 32
      | ^~~~~~~
zconf.y:97.1-11: warning: POSIX Yacc does not support %destructor [-Wyacc]
   97 | %destructor {
      | ^~~~~~~~~~~
cc -Wall -Wmissing-prototypes -Wstrict-prototypes -O2 -fomit-frame-pointer -DKBUILD_NO_NLS   -c -o zconf.tab.o zconf.tab.c
In file included from zconf.tab.c:2346:
confdata.c: In function 'conf_write':
confdata.c:773:22: warning: '%s' directive writing likely 7 or more bytes into a region of size between 1 and 4097 [-Wformat-overflow=]
  773 |  sprintf(newname, "%s%s", dirname, basename);
      |                      ^~
confdata.c:773:19: note: assuming directive output of 7 bytes
  773 |  sprintf(newname, "%s%s", dirname, basename);
      |                   ^~~~~~
In file included from /usr/include/stdio.h:867,
                 from zconf.tab.c:78:
/usr/include/x86_64-linux-gnu/bits/stdio2.h:36:10: note: '__builtin___sprintf_chk' output 1 or more bytes (assuming 4104) into a destination of size 4097
   36 |   return __builtin___sprintf_chk (__s, __USE_FORTIFY_LEVEL - 1,
      |          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   37 |       __bos (__s), __fmt, __va_arg_pack ());
      |       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from zconf.tab.c:2346:
confdata.c:776:23: warning: '.tmpconfig.' directive writing 11 bytes into a region of size between 1 and 4097 [-Wformat-overflow=]
  776 |   sprintf(tmpname, "%s.tmpconfig.%d", dirname, (int)getpid());
      |                       ^~~~~~~~~~~
In file included from /usr/include/stdio.h:867,
                 from zconf.tab.c:78:
/usr/include/x86_64-linux-gnu/bits/stdio2.h:36:10: note: '__builtin___sprintf_chk' output between 13 and 4119 bytes into a destination of size 4097
   36 |   return __builtin___sprintf_chk (__s, __USE_FORTIFY_LEVEL - 1,
      |          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   37 |       __bos (__s), __fmt, __va_arg_pack ());
      |       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cc   conf.o zconf.tab.o   -o conf
boolean symbol CRYPTO_LIB_ARC4 tested for 'm'? test forced to 'n'
#
# configuration written to .config
#
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1'
make[4]: Entering directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1'
make[5]: 'Kconfig.versions' is up to date.
make[7]: 'Kconfig.versions' is up to date.
make[8]: 'conf' is up to date.
boolean symbol CRYPTO_LIB_ARC4 tested for 'm'? test forced to 'n'
#
# configuration written to .config
#
Building backport-include/backport/autoconf.h ... done.
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/compat/main.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/compat/backport-5.5.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/compat/backport-5.10.o
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/compat/compat.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/drivers/net/wireless/ath/main.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/drivers/net/wireless/ath/regd.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/drivers/net/wireless/ath/hw.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/drivers/net/wireless/ath/key.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/drivers/net/wireless/ath/debug.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/drivers/net/wireless/ath/dfs_pattern_detector.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/drivers/net/wireless/ath/dfs_pri_detector.o
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/drivers/net/wireless/ath/ath.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/main.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/status.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/driver-ops.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/sta_info.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/wep.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/aead_api.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/wpa.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/scan.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/offchannel.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/ht.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/agg-tx.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/agg-rx.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/vht.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/he.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/s1g.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/ibss.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/iface.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/rate.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/michael.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/tkip.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/aes_cmac.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/aes_gmac.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/fils_aead.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/cfg.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/ethtool.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/rx.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/spectmgmt.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/tx.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/key.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/util.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/wme.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/chan.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/trace.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/mlme.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/tdls.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/ocb.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/airtime.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/led.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/debugfs.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/debugfs_sta.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/debugfs_netdev.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/debugfs_key.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/mesh.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/mesh_pathtbl.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/mesh_plink.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/mesh_hwmp.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/mesh_sync.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/mesh_ps.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/rc80211_minstrel_ht.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/rc80211_minstrel_ht_debugfs.o
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/mac80211.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/core.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/sysfs.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/radiotap.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/util.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/reg.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/scan.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/nl80211.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/mlme.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/ibss.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/sme.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/chan.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/ethtool.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/mesh.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/ap.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/trace.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/ocb.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/pmsr.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/of.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/debugfs.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/wext-compat.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/wext-sme.o
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/cfg80211.o
  Building modules, stage 2.
  MODPOST 4 modules
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/compat/compat.mod.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/drivers/net/wireless/ath/ath.mod.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/mac80211.mod.o
  CC [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/cfg80211.mod.o
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/compat/compat.ko
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/drivers/net/wireless/ath/ath.ko
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/mac80211/mac80211.ko
  LD [M]  /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/net/wireless/cfg80211.ko
make[4]: Leaving directory '/openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1'
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/ipkg-mips_24kc/kmod-cfg80211/lib/modules/5.4.128/cfg80211.ko: relocatable
rstrip.sh: /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/ipkg-mips_24kc/kmod-cfg80211/lib/modules/5.4.128/compat.ko: relocatable
Packaged contents of /openwrt/build_dir/target-mips_24kc_musl/linux-ath79_generic/backports-5.10.42-1/ipkg-mips_24kc/kmod-cfg80211 into /openwrt/bin/targets/ath79/generic/packages/kmod-cfg80211_5.4.128+5.10.42-1-1_mips_24kc.ipk
Package kmod-mac80211 is missing dependencies for the following libraries:
aead.ko
crypto_hash.ko
make[3]: *** [Makefile:574: /openwrt/bin/targets/ath79/generic/packages/kmod-mac80211_5.4.128+5.10.42-1-1_mips_24kc.ipk] Error 1
```
