import gdb

gdb.execute("gef-remote localhost 3333")
gdb.execute("monitor reset halt")
gdb.execute("load")
gdb.execute("monitor reset init")
gdb.execute("break main")
gdb.execute("c")
