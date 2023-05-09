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

def quantidade_bolhas(rd_anterior, rs1, rs2, forwardHabilitado = False):
    quantidade = 0

    if rd_anterior is None or (rs1 is None and rs2 is None):
        return 0
    
    if forwardHabilitado:
        if rd_anterior == rs2 or rd_anterior == rs1:
            return 1
        else:
            return 0
  
    if rd_anterior == rs2 or rd_anterior == rs1:
        quantidade = 2
    
    return quantidade

def swap_instrucoes(rd_anterior, rs1, rs2, rs1_prox, rs2_prox, prox_tipo):
    
    if rd_anterior is None or ((rs1 is None and rs2 is None) or (rs1_prox is None and rs2_prox is None)):
        return False
    
    if (rd_anterior == rs1 or rd_anterior == rs2) and (rd_anterior != rs1_prox and rd_anterior !=  rs2_prox and (prox_tipo != "jal" and prox_tipo != "beq")):
        return True
    
    return False

def contar_ciclos(array_instructions):
    contador = 0
    arrayLoop = []
    arrayLoop.append(array_instructions[0])
    array_instructions.pop(0)
    while array_instructions:
        contador+=1
        for ciclo in arrayLoop:
            ciclo.pop(0)
            if not any(ciclo):
                arrayLoop.remove(ciclo)
        if(array_instructions is not None):
            arrayLoop.append(array_instructions[0])
            array_instructions.pop(0)
    return contador
