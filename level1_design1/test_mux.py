# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    for i in range(5):
        SEL=random.randint(0,31)
        INP=[random.randint(0,3) for i in range(31)]

        #driving inputs
        dut.sel.value=SEL
        dut.inp0.value=INP[0]
        dut.inp1.value=INP[1]
        dut.inp2.value=INP[2]
        dut.inp3.value=INP[3]
        dut.inp4.value=INP[4]
        dut.inp5.value=INP[5]
        dut.inp6.value=INP[6]
        dut.inp7.value=INP[7]
        dut.inp8.value=INP[8]
        dut.inp9.value=INP[9]
        dut.inp10.value=INP[10]
        dut.inp11.value=INP[11]
        dut.inp12.value=INP[12]
        dut.inp13.value=INP[13]
        dut.inp14.value=INP[14]
        dut.inp15.value=INP[15]
        dut.inp16.value=INP[16]
        dut.inp17.value=INP[17]
        dut.inp18.value=INP[18]
        dut.inp19.value=INP[19]
        dut.inp20.value=INP[20]
        dut.inp21.value=INP[21]
        dut.inp22.value=INP[22]
        dut.inp23.value=INP[23]
        dut.inp24.value=INP[24]
        dut.inp25.value=INP[25]
        dut.inp26.value=INP[26]
        dut.inp27.value=INP[27]
        dut.inp28.value=INP[28]
        dut.inp29.value=INP[29]
        dut.inp30.value=INP[30]
        #dut.inp31.value=INP[31]

        for i in range(31):
            if SEL==i:
                OUT=INP[i]


        await Timer(2,units="ns")
        dut.log.info(f'SEL={SEL:05} INPUT={INP[SEL]:05} model={OUT:05} OUT={int(dut.out.value):05}')
        assert dut.out.value==OUT,"Randomised test fail with:{SEL}+{B}={OUT}".format(A=dut.sel.value,B=INP[int(dut.sel.value)],OUT=dut.out.value)
        #cocotb.log.info('##### CTB: Develop your test here ########')
