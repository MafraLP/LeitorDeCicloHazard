from instruction import Instruction 

def identificar_instrucao(binario):
    opcode = binario[25:32]
    if opcode == '0010111':
        return Instruction(rd=binario[20:25])
    elif opcode == '0010011':
        funct3 = binario[17:20]
        if funct3 == '000':
            return Instruction( rd=binario[20:25], rs1=binario[12:17])
        elif funct3 == '001':
            return Instruction(rd=binario[20:25], rs1=binario[12:17])
    elif opcode == '0100011':
        return Instruction(rs2=binario[7:12], rs1=binario[12:17])
    elif opcode == '0110011':
        funct3 = binario[17:20]
        if funct3 == '000':
            return Instruction(rd=binario[20:25], rs2=binario[7:12], rs1=binario[12:17])
    elif opcode == '1100011':
        funct3 = binario[17:20]
        if funct3 == '000':
            return Instruction(rs2=binario[7:12], rs1=binario[12:17])
    elif opcode == '1110011':
        return Instruction(rd=binario[20:25])

    return None

