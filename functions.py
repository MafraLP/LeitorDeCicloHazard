from instruction import Instruction 

def identificar_instrucao(binario):
    opcode = binario[25:32]
    if opcode == '0010111':
        return Instruction('auipc', rd=binario[20:25])
    elif opcode == '0010011':
        funct3 = binario[17:20]
        if funct3 == '000':
            return Instruction('addi', rd=binario[20:25], rs1=binario[12:17])
        elif funct3 == '001':
            return Instruction('slli', rd=binario[20:25], rs1=binario[12:17])
    elif opcode == '0100011':
        return Instruction('sw', rs2=binario[7:12], rs1=binario[12:17])
    elif opcode == '0110011':
        funct3 = binario[17:20]
        if funct3 == '000':
            return Instruction('add',rd=binario[20:25], rs2=binario[7:12], rs1=binario[12:17])
    elif opcode == '1100011':
        funct3 = binario[17:20]
        if funct3 == '000':
            return Instruction('beq', rs2=binario[7:12], rs1=binario[12:17])
    elif opcode == '1110011':
        return Instruction('jal', rd=binario[20:25])

    return None

