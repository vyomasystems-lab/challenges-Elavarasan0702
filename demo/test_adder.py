import cocotb
from cocotb.triggers import Timer
import random
@cocotb.test()
async def adder_basic_test(dut):
    
    A=5
    B=10
    dut.a.value=A
    dut.b.value=B
    await Timer(2,units="ns")
    #dut.log.info(f'A={A:05} B={B:05} model={A+B:05} OUT={int(dut.sum.value):05}')
    assert dut.sum.value==A+B,f"adder result is incorrect:{dut.sum.value}!=15"



@cocotb.test()
async def adder_randomised_test(dut):
    for i in range(5):
        A=random.randint(0,15)
        B=random.randint(0,15)
        dut.a.value=A
        dut.b.value=B
        await Timer(2,units="ns")
        dut.log.info(f'A={A:05} B={B:05} model={A+B:05} OUT={int(dut.sum.value):05}')
        assert dut.sum.value==A+B,"Randomised test fail with:{A}+{B}={SUM}",format(A=dut.a.value,B=dut.b.value,SUM=dut.sum.value)
