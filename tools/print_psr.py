import gdb

class APSR:
    def __init__(self, val=0):
        self.val = val

        if val == 0:
            self.n = False
            self.z = False
            self.c = False
            self.v = False
            self.q = False
            self.intr = "None"
        else:
            self.n = bool(val & (1 << 31))
            self.z = bool(val & (1 << 30))
            self.c = bool(val & (1 << 29))
            self.v = bool(val & (1 << 28))
            self.q = bool(val & (1 << 27))
            self.intr = self.__stringify_exception(val & 0xff)

    def __stringify_exception(self, n: int) -> str:
        match n:
            case 0:
                return "None"
            case 1:
                return "Reset"
            case 2:
                return "NMI"
            case 3:
                return "Hardfault"
            case 4:
                return "MemManage"
            case 5:
                return "BusFault"
            case 6:
                return "UsageFault"
            case 7 | 8 | 9 | 10:
                return "Resv{}".format(n)
            case 11:
                return "SVCall"
            case 12:
                return "DebugMonior"
            case 13:
                return "Reserved13"
            case 14:
                return "PendSV"
            case 15:
                return "SysTick"
            case 16:
                return "ExternalInt"
            case _:
                return "Unknown Exception: {}".format(n)

    def __repr__(self):
        return """
        val: {}
        N: {}
        Z: {}
        C: {}
        V: {}
        Q: {}
        Interrupt: {}""".format(hex(self.val), self.n, self.z, self.c, self.v, self.q, self.intr)


# output is in the form of $1 = 0x0000000
# split it into a list, and retrieve the last element
# which is the content
val = gdb.execute("print $xPSR", to_string=True)
val = val.split(' ').pop()
val = val.strip('\n')

psr = APSR(int(val, base=16))
print(psr)
