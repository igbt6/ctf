
def asm2 (param1, param2):
    loc_var1 = param2
    while  param1 <= 0x1d89:
        loc_var1 += 1
        param1 += 0x64

    return loc_var1


print("Flag: {}".format(hex(asm2(0x4, 0x2d))))
