a = [
    ("addiu", 0x09), ("andi", 0x0c), ("ori", 0x0d),
    ("lui", 0x0f), ("lb", 0x20), ("lbu", 0x24),
    ("lw", 0x23), ("sw", 0x2b), ("beq", 0x04), ("bnq", 0x05),
    ("j", 0x02), ("jal", 0x03),
    ("R-Type", 0x0)
]


for d in a:
    print("{}: {:0>6b}".format(d[0], d[1]))
