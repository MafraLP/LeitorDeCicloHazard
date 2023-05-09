instOrder = {
    "auipc" : ['IF', 'ID', 'EXE', 'MEM', 'WB'],
    "addi" : ['IF', 'ID', 'EXE', 'WB'],
    'beq' : ['IF', 'ID', 'EXE'],
    'slli': ['IF','ID','EXE', 'WB'],
    'add': ['IF', 'ID', 'EXE', 'WB'],
    'sw': ['IF', 'ID', 'EXE', 'MEM'],
    'jal': ['IF', 'ID', 'EXE', 'MEM', 'WB']
}

opcodes = {
    # Load (5 cycles)
    '0000011': 4,# LB, LH, LW, LBU, LHU
    # Store (4 cycles)
    '0100011': 4,  # SB, SH, SW
    # R-type (4 cycles)
    '0110011': 4,  # ADD, SUB, SLL, SLT, SLTU, XOR, SRL, SRA, OR, AND
    # I-type (3 cycles)
    '0010011': 3,  # ADDI, SLTI, SLTIU, XORI, ORI, ANDI, SLLI, SRLI, SRAI
    # Branch (3 cycles)
    '1100011': 3,  # BEQ, BNE, BLT, BGE, BLTU, BGEU
    # Jump (3 cycles)
    '1101111': 3   # JAL
}