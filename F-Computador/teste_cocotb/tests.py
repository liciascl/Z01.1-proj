# Adapted from https://github.com/cocotb/cocotb/blob/master/examples/doc_examples/quickstart/test_my_design.py

import cocotb
from cocotb.triggers import Timer, FallingEdge
from cocotb.clock import Clock
import os
from termcolor import colored
        
        
@cocotb.test()
async def tb_ControlUnit(dut):

    ininstruction= [0b000111111111111111, 0b100000000000010000, 0b100000000000100000, 0b100001000000000000, 0b0000000000000101, 0b100001010100010000, 0b100011100000010000, 0b100001010100100000, 0b100010000100010000, 0b100010100110010000, 0b100000000000000111, 0b100000011000000101, 0b100000011000000101, 0b100000011000000001]
    inng         = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    inzr         = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    
    outzx        = [0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
    outnx        = [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]
    outzy        = [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1]
    outny        = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
    outf         = [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0]
    outno        = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    outmuxALUI_A = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    outmuxAM     = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0]
    outloadA     = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    outloadD     = [0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0]
    outloadM     = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    outloadPC    = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0]   


    for i in range(len(ininstruction)):
        dut.instruction.value = ininstruction[i]
        dut.ng.value = inng[i]
        dut.zr.value = inzr[i]

        await Timer(1, units="ns")
        condition = (dut.zx.value == outzx[i] and dut.nx.value == outnx[i] and dut.zy.value == outzy[i] and
                     dut.ny.value == outny[i] and dut.f.value == outf[i] and dut.no.value == outno[i] and
                     dut.muxALUI_A.value == outmuxALUI_A[i] and dut.muxAM.value == outmuxAM[i] and dut.loadA.value == outloadA[i] and 
                     dut.loadD.value == outloadD[i] and dut.loadM.value == outloadM[i] and dut.loadPC.value == outloadPC[i])
        if not condition:
            if not (dut.zx.value == outzx[i]):
                dut._log.error("Expected value zx: " + "{0:b}".format(outzx[i]) + " Obtained value zx: " + str(dut.zx.value) )
            if not (dut.nx.value == outnx[i]):
                dut._log.error("Expected value nx: " + "{0:b}".format(outnx[i]) + " Obtained value nx: " + str(dut.nx.value) )
            if not (dut.zy.value == outzy[i]):
                dut._log.error("Expected value zy: " + "{0:b}".format(outzy[i]) + " Obtained value zy: " + str(dut.zy.value) )
            if not (dut.ny.value == outny[i]):
                dut._log.error("Expected value ny: " + "{0:b}".format(outny[i]) + " Obtained value ny: " + str(dut.ny.value) )
            if not (dut.f.value == outf[i]):
                dut._log.error("Expected value f: " + "{0:b}".format(outf[i]) + " Obtained value f: " + str(dut.f.value) )
            if not (dut.no.value == outno[i]):
                dut._log.error("Expected value no: " + "{0:b}".format(outno[i]) + " Obtained value no: " + str(dut.no.value) )
            if not (dut.muxALUI_A.value == outmuxALUI_A[i]):
                dut._log.error("Expected value muxALUI_A: " + "{0:b}".format(outmuxALUI_A[i]) + " Obtained value muxALUI_A: " + str(dut.muxALUI_A.value) )
            if not (dut.muxAM.value == outmuxAM[i]):
                dut._log.error("Expected value muxAM: " + "{0:b}".format(outmuxAM[i]) + " Obtained value muxAM: " + str(dut.muxAM.value) )
            if not (dut.loadA.value == outloadA[i]):
                dut._log.error("Expected value loadA: " + "{0:b}".format(outloadA[i]) + " Obtained value loadA: " + str(dut.loadA.value) )
            if not (dut.loadD.value == outloadD[i]):
                dut._log.error("Expected value loadD: " + "{0:b}".format(outloadD[i]) + " Obtained value loadD: " + str(dut.loadD.value) )
            if not (dut.loadM.value == outloadM[i]):
                dut._log.error("Expected value loadM: " + "{0:b}".format(outloadM[i]) + " Obtained value loadM: " + str(dut.loadM.value) )
            if not (dut.loadPC.value == outloadPC[i]):
                dut._log.error("Expected value loadPC: " + "{0:b}".format(outloadPC[i]) + " Obtained value loadPC: " + str(dut.loadPC.value) )
            assert condition, "Error in test {0}!".format(i)
        await Timer(1, units="ns")
        

@cocotb.test()
async def tb_MemoryIO(dut):

    inINPUT =   [0xA5A5, 0x0000, 0xAAA3, 0xFFFF, 0x5A5A, 0xFFFF, 0xF0F0, 0xFFFF]
    inLOAD  =   [     1,      0,      1,      0,      1,      0,      0,      1]
    inSW    =   [0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x02AA, 0x02AA]
    inADDRESS = [0x0000, 0x0000, 0x2000, 0x2000, 0x3FFF, 0x3FFF, 0x52C1, 0x2000]
    outOUTPUT = [0xA5A5, 0xA5A5, 0xAAA3, 0xAAA3, 0x5A5A, 0x5A5A, 0x02AA, 0xFFFF]
    
    
    clock = Clock(dut.CLK_FAST, len(inINPUT), units="ns")
    await cocotb.start(clock.start())    

    await FallingEdge(dut.CLK_FAST)
    for i in range(len(inINPUT)):
        dut.INPUT.value = inINPUT[i]
        dut.LOAD.value = inLOAD[i]
        dut.SW.value = inSW[i]
        dut.ADDRESS.value = inADDRESS[i]

        await FallingEdge(dut.CLK_FAST)

        condition = (dut.OUTPUT.value == outOUTPUT[i])
        if not condition:
            dut._log.error("Expected value OUTPUT: " + "{0:016b}".format(outOUTPUT[i]) + " Obtained value OUTPUT: " + str(dut.OUTPUT.value) )
            assert condition, "Error in test {0}!".format(i)


@cocotb.test()
async def tb_CPU(dut):

    file_test = open("../../E-Assembly/config_testes_nasm.txt","r")
    lines_test = file_test.readlines() 
    file_test.close()

    print("\n\n===================================================")
    for line in lines_test:
        if len(line.strip()):
            if ((line.strip()[0] != '#') and ( line.strip().find('.nasm') > 0 )):
                # pega parametros e atribui caminhos globais
                # par[0] : Nome do teste (subpasta)
                # par[1] : quantidade de testes a serem executados
                # par[2] : tempo de simulação em ns
                par = line.rstrip().split()
                name = par[0][:-5]
                sTime = int(par[2])
                mif = "../../E-Assembly/bin/hack/"+name+".mif"

                # verifica se arquivo existe
                if os.path.isfile(mif):
                    # simulate
                    for test in range(0, int(par[1])):
                        ramIn = "../../E-Assembly/tests/" + name + "/" + name +"{}".format(test)+ "_in.mif"
                        ramTest = "../../E-Assembly/tests/" + name + "/" + name +"{}".format(test)+ "_tst.mif"

                        RAM = [0] * (16*1024+4800+2)
                        ROM = [0] * 32*1024
                        #Import initial conditions from file
                        file_in = open(mif,"r")
                        Lines_in = file_in.readlines() 
                        file_in.close()
                        
                        for l in Lines_in:
                            if ":" in l:
                                no_line = int( l.split(":")[0].strip() )
                                value = int( l.split(":")[1].replace(";", "").strip(),2 )
                                ROM[no_line] = value 

                        file_in = open(ramIn,"r")
                        Lines_in = file_in.readlines() 
                        file_in.close()
                        
                        for l in Lines_in:
                            if ":" in l:
                                no_line = int( l.split(":")[0].strip() )
                                value = int( l.split(":")[1].replace(";", "").strip(),2 )
                                RAM[no_line] = value  
                            
                        clock = Clock(dut.clock, 2, units="ns")
                        await cocotb.start(clock.start())   

                        dut.reset.value = 1
                        await FallingEdge(dut.clock)
                        await FallingEdge(dut.clock)
                        dut.reset.value = 0

                        for i in range( sTime ):
                            try:
                                if dut.writeM.value == 1:
                                    RAM[dut.addressM.value] = dut.outM.value
                                else:
                                    if int(dut.addressM.value) <= 21185:
                                        dut.inM.value = RAM[dut.addressM.value]
                            except:
                                pass
                            dut.instruction.value = ROM[dut.pcout.value]
                            await FallingEdge(dut.clock) 

                        #Verification final results
                        file_in = open(ramTest,"r")
                        Lines_in = file_in.readlines() 
                        file_in.close()

                        for l in Lines_in:
                            if ":" in l:
                                no_line = int( l.split(":")[0].strip() )
                                value = int( l.split(":")[1].replace(";", "").strip(),2 )

                                condition = (RAM[no_line] == value)
                                if not condition:
                                    dut._log.error("Expected value " + str(no_line) + ": " + "{0:016b}".format(value) + " Obtained value " + str(no_line) + ": " + "{0:016b}".format(int(RAM[no_line])) )
                                    print( 'Test {:15s}: '.format(name + "{}".format(test)) + colored('Failed', 'red'))
                                    assert condition, "Error in test " + name + "{}".format(test)
                                else:
                                    print( 'Test {:15s}: '.format(name + "{}".format(test)) + colored('Passed', 'green'))
    print("===================================================")
