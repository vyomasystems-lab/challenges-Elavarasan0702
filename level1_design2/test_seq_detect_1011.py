# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)


    

    IN=[1,0,1,0,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1,0,1,0,1,1,1,0,1,0,1,1]
    OUT=[0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1]
    #IN=[1,0,1,0,1,1]
    #OUT=[0,0,0,0,0,1]
    for i in range(len(IN)):
        dut.inp_bit.value=IN[i]
        await FallingEdge(dut.clk)
        dut._log.info(f'INPUT={IN[i]:05} model={OUT[i]:05} OUT={int(dut.seq_seen .value):05}')
        #assert dut.seq_seen.value==OUT[i],"Incorrect operation {}!={}".format(dut.seq_seen.value,OUT[i])
        if OUT[i]!=dut.seq_seen .value:
            print("Errored place:",i)
            print("DUT.CURRENT STATE:",dut.current_state)
            assert dut.seq_seen.value==OUT[i],"Incorrect operation {}!={}".format(dut.seq_seen.value,OUT[i])


    #cocotb.log.info('#### CTB: Develop your test here! #####

    


   
