def primitve_inst():
    mips_code = """ 
#ITOB          
.text
root_itob:
.data
.align 2
root_itob_ival: .space 4
.text
    la $t0, root_itob_ival
    sub $sp, $sp, 8
    sw $t0, 0($sp)
    lw $t0, 0($sp)
    lw $t0, 0($t0)
    sw $t0, 0($sp)
    li $t0, 0
    sub $sp, $sp, 8
    sw $t0, 0($sp)
    lw $t0, 0($sp)
    lw $t1, 8($sp)
    sne $t2, $t1, $t0
    sw $t2, 8($sp)
    addi $sp, $sp, 8
    l.d   $f30, 0($sp)
    addi $sp, $sp, 8
    addi $sp, $sp, -8
    s.d   $f30, 0($sp)
    jr   $ra

#BTOI
.text
root_btoi:
.data
.align 2
root_btoi_bval: .space 4
.text
start_btoi_stmt_1:
start_btoi_stmt_2:
.text
    la $t0, root_btoi_bval
    sub $sp, $sp, 8
    sw $t0, 0($sp)
    lw $t0, 0($sp)
    lw $t0, 0($t0)
    sw $t0, 0($sp)
    lw $a0, 0($sp)
    addi $sp, $sp, 8
    beq $a0, 0, end_btoi_stmt_3
    j  start_btoi_stmt_3
start_btoi_stmt_3:
start_btoi_stmt_4:
start_btoi_stmt_5:
    li $t0, 1
    sub $sp, $sp, 8
    sw $t0, 0($sp)
    l.d   $f30, 0($sp)
    addi $sp, $sp, 8
    addi $sp, $sp, -8
    s.d   $f30, 0($sp)
    jr   $ra
end_btoi_stmt_5:
end_btoi_stmt_4:
end_btoi_stmt_3:
end_btoi_stmt_2:
start_btoi_stmt_6:
.text
    li $t0, 0
    sub $sp, $sp, 8
    sw $t0, 0($sp)
    l.d   $f30, 0($sp)
    addi $sp, $sp, 8
    addi $sp, $sp, -8
    s.d   $f30, 0($sp)
    jr   $ra
end_btoi_stmt_6:
end_btoi_stmt_1:

# ITOD
.data
.align 2
root_itod_ival: .space 4
.text
    root_itod:
    la $t0, root_itod_ival
    sub $sp, $sp, 8
    sw $t0, 0($sp)
    lw $t0, 0($sp)
    lw $t0, 0($t0)
    sw $t0, 0($sp)
    mtc1.d $t0, $f0
    cvt.d.w $f0, $f0
    sub $sp, $sp, 8
    s.d $f0, 0($sp)
    l.d   $f30, 0($sp)
    addi $sp, $sp, 8
    addi $sp, $sp, 8
    addi $sp, $sp, -8
    s.d   $f30, 0($sp)
    jr   $ra

#DTOI
root_dtoi_:
.data
.align 2
root_dtoi__dval: .space 8
.text
    li $t0, 1
    sub $sp, $sp, 8
    sw $t0, 0($sp)
    la $t0, root_dtoi__dval
    sub $sp, $sp, 8
    sw $t0, 0($sp)
    lw $t0, 0($sp)
    l.d $f0, 0($t0)
    li.d $f6, 0.5 
    add.d $f0, $f0, $f6
    cvt.w.d $f0,$f0
    mfc1.d $a0,$f0
    sw $a0, 0($sp)
    l.d   $f30, 0($sp)
    addi $sp, $sp, 8
    addi $sp, $sp, 8
    addi $sp, $sp, -8
    s.d   $f30, 0($sp)
    jr   $ra
    
.text
root_ReadChar__:
.text
start_rstmt_65:
start_rstmt_66:
.text
    li $v0, 12      
    syscall       
    sub $sp, $sp, 8
    sw $v0, 0($sp)

    lw   $t8, 0($sp)
    addi $sp, $sp, 8
    addi $sp, $sp, -8
    sw   $t8, 0($sp)
    jr   $ra

end_rstmt_66:
start_rstmt_67:
    lw   $t8, 0($sp)
    addi $sp, $sp, 8
    addi $sp, $sp, -8
    sw   $t8, 0($sp)
    jr   $ra

end_rstmt_67:
end_rstmt_65:
"""


    return mips_code

def lib_initialise():
    code = """
int dtoi(double x){
    if(x >= 0.0)
        return dtoi_(x);
    return -dtoi_(-x-0.00000000001);
}
int ReadInteger__(){
    int res;
    int inp;
    int sign;
    bool hex;
    hex = false;
    sign = 1;
    res = 0;
    while(true){
        inp = ReadChar__();
        if (inp == 10){
            break;
        }
        if (inp != 43 && inp != 13){
            if (inp == 45){
                sign = -1;
            }else{
                if (inp == 120 || inp == 88){
                    hex = true;
                }
                else{
                    if(!hex){
                        res = res * 10 + inp - 48;
                    }else{
                        if(inp <= 60){
                            inp = inp - 48;
                        }else{
                            if(inp <= 75){
                                inp = inp - 65 + 10;
                            }else{
                                inp = inp - 97 + 10;
                            }
                        }
                        res = res * 16 + inp;
                    }
                }
            }
        }
    }
return res * sign;
}
    """
    return code