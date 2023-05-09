from instOrder import instOrder

class Instruction:
    def __init__(self, instType, rs1=None, rs2=None, rd=None):
        self.instType = instType
        self.instructionsOrder = instOrder[instType]
        self.rs1=rs1 
        self.rs2=rs2
        self.rd=rd
    