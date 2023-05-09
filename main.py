from instruction import Instruction
from functions import identificar_instrucao,quantidade_bolhas, contar_ciclos, swap_instrucoes

with open('dump', 'r') as f:
    instrucoes = f.read().splitlines()

binarios = []
nomes_instrucoes = []


for instrucao in instrucoes:
    binario = bin(int(instrucao, 16))[2:].zfill(32)
    binarios.append(binario)

instrucoes = []
for binario in binarios:
    inst = identificar_instrucao(binario)
    if inst is not None:
        instrucoes.append(inst)
    else:
        print("Instrução nao encontrada")
        print("")

rd_anterior = None
instrucoesComNop = []
for inst in instrucoes:
    quantidade = quantidade_bolhas(rd_anterior= rd_anterior, rs1= inst.rs1, rs2= inst.rs2, forwardHabilitado=False)
    instrucoesComNop.append(['IF', 'ID', 'EXE', 'MEM', 'WB'])
    # print("rd_anterior: " + str(rd_anterior))
    # print("rd: " + str(inst.rd))
    # print("rs1: " + str(inst.rs1))
    # print("rs2: " + str(inst.rs2))

    if quantidade > 0:
        for i in range(quantidade):
            instrucoesComNop.append(['NOP', 'NOP', 'NOP', 'NOP', 'NOP'])
    rd_anterior = inst.rd

print("Ciclos Totais com NOPS: " + str(contar_ciclos(instrucoesComNop)))

print("")

rd_anterior = None
instrucoesComForward = []
for inst in instrucoes:
    quantidade = quantidade_bolhas(rd_anterior= rd_anterior, rs1= inst.rs1, rs2= inst.rs2, forwardHabilitado=True)
    instrucoesComForward.append(['IF', 'ID', 'EXE', 'MEM', 'WB'])
    if quantidade > 0:
            for i in range(quantidade):
                instrucoesComForward.append(['NOP', 'NOP', 'NOP', 'NOP', 'NOP'])
    rd_anterior = inst.rd
print("Ciclos Totais com Forward + NOP: " + str(contar_ciclos(instrucoesComForward)))

rd_anterior = None
instrucoesComSwap = []
for i in range(len(instrucoes)-1):
    instAtual = instrucoes[i]
    instProx = instrucoes[i+1]
    if instProx is not None:
        if swap_instrucoes(rd_anterior= rd_anterior, rs1=instAtual.rs1, rs2=instAtual.rs2, rs1_prox=instProx.rs1, rs2_prox=instProx.rs2, prox_tipo=instProx.instType):
            instrucoes[i] = instProx
            instrucoes[i+1] = instAtual
            instrucoesComSwap.append(['IF', 'ID', 'EXE', 'MEM', 'WB'])
        else:
            quantidade = quantidade_bolhas(rd_anterior= rd_anterior, rs1= inst.rs1, rs2= inst.rs2, forwardHabilitado=True)
            instrucoesComSwap.append(['IF', 'ID', 'EXE', 'MEM', 'WB'])
            if quantidade > 0:
                    for i in range(quantidade):
                        instrucoesComSwap.append(['NOP', 'NOP', 'NOP', 'NOP', 'NOP'])
    rd_anterior = instAtual.rd
print("Ciclos Totais com Swap + Forward + NOP: " + str(contar_ciclos(instrucoesComSwap)))
