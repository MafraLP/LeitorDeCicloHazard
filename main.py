from instruction import Instruction
from functions import identificar_instrucao

with open('dump', 'r') as f:
    instrucoes = f.read().splitlines()

binarios = []
nomes_instrucoes = []


for instrucao in instrucoes:
    binario = bin(int(instrucao, 16))[2:].zfill(32)
    binarios.append(binario)

instrucoes = []
for binario in binarios:
    print(binario)
    inst = identificar_instrucao(binario)
    if inst is not None:
        instrucoes.append(inst)
    else:
        print("Instrtucao nao encontrada")

i = 0 
for inst in instrucoes:
    print('         ' * i, inst.instructionsOrder)
    i += 1
    # print("RD: " + str(inst.rd))
    # print("RS1: " + str(inst.rs1))
    # print("RS2: " + str(inst.rs2))

