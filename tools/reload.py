import gdb

gdb.execute("monitor reset halt")
gdb.execute("load")
gdb.execute("monitor reset init")
