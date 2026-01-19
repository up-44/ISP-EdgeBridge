Troubleshooting:


Wrong boot mode:
Wrong boot mode detected (0xXX)! The chip needs to be in download mode.
Communication with the chip works (the ROM boot log is detected), but it is not being reset into the download mode automatically.
To resolve this, check the autoreset circuitry (if your board has it), or try resetting into the download mode manually. 
See Manual Bootloader for instructions.

Manual Bootloader: https://docs.espressif.com/projects/esptool/en/latest/esp32/advanced-topics/boot-mode-selection.html#manual-bootloader
Depending on the kind of hardware you have, it may also be possible to manually put your ESP32 board into Firmware Download mode (reset).
For development boards produced by Espressif, this information can be found in the respective getting started guides or user guides. For example, to manually reset a development board, hold down the Boot button (GPIO0) and press the EN button (EN (CHIP_PU)).