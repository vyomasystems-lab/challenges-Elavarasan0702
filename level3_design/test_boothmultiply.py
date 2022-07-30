import cocotb
from cocotb.triggers import Timer
import random
@cocotb.test()
async def multiply_test(dut):
  A=7
  B=10
  dut.a.value=A
  dut.b.value=B
  await Timer(2,units="ns")
  assert dut.c.value==A*B,"MODEL:{}  OUT:{}".format(A*B,dut.c.value)
