#!/bin/sh

openocd_config="$HOME/Projects/tiva/ek-lm4f120xl.cfg"
toolchain="arm-none-eabi"
gdb="$toolchain-gdb"

if [ "$#" -ne 1 ];then
	echo "usage: $0 file"
	exit 1
fi

openocd -f "$openocd_config" 1>openocd.out 2>&1 &
"$gdb" "$1"

pid=$(pgrep openocd)
kill -9 "$pid"

