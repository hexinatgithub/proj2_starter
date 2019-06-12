LfsrPalindrome:
    add $t0, $zero, $a0 # 44020
Loop:
    bitpal $t1, $t0 # 100483e
    bne $t1, $zero, Return # 15200003
    lfsr $t0, $t0 # 100403f
    beq $t0, $a0, Return # 11040001
    j Loop # 8100002
Return:
    add $v0, $zero, $t0 # 81020
    jr $ra # 3e00008