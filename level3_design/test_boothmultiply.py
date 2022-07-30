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
  out=dut.c.value
  print(type(out))
  #assert int(str(dut.c.value),2)==A*B,"MODEL:{}  OUT:{}".format(A*B,int(str(dut.c.value),2))
