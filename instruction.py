from instOrder import instOrder

class Instruction:

    instructionsOrder = ['IF', 'ID', 'EXE', 'MEM', 'WB']

    def __init__(self, rs1=None, rs2=None, rd=None):
        self.rs1=rs1 
        self.rs2=rs2
        self.rd=rd
    