System-wide Lean input method
=============================

This repository contains an MIM file for m17n to convert [Lean](https://leanprover.github.io/)-style abbreviations such as `\nat` to `ℕ` in *all* applications.

First you need an input method framework such as [fcitx](https://wiki.archlinux.org/index.php/Fcitx) (with the fcitx-m17n plugin) or [ibus](https://wiki.archlinux.org/index.php/IBus).  Then you only need to install the MIM file, and enable the new input method:
```shell
install -Dm0644 lean.mim ~/.m17n.d/lean.mim
```