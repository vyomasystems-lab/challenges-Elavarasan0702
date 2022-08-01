# challenges-Elavarasan0702
challenges-Elavarasan0702 created by GitHub Classroom
<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a>
    <img src=https://github.com/vyomasystems-lab/challenges-Elavarasan0702/blob/master/images/boothmultiplier.JPG>
  </a>
  
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#Level1-Design1">Level1-Design</a>
    </li>
    <li><a href="#Level2-Design">Level2-Design</a></li>
    <li><a href="#Level3-Design">Level3-design</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
In this project, design verification of RTL is done using cocotb library in python. Design verification is a important step to check our design in industry in order to avoid failure cases in the design. Multiplexer ,Sequence detector ,Bit manipulation processor and Booth multiplier design's verification  are done with the help of cocotb packages in python












<!-- Level1-Design-->
## Level1-Design

The Multiplexer and Sequence detector designed and verified using cocotb library with the help of python language

### Multiplexer

<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://github.com/vyomasystems-lab/challenges-Elavarasan0702/blob/master/mux_fail.JPG" >
  </a>
</div>
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://github.com/vyomasystems-lab/challenges-Elavarasan0702/blob/master/images/bug1.JPG" >
  </a>

  
</div>

<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://github.com/vyomasystems-lab/challenges-Elavarasan0702/blob/master/images/bug2_mux.JPG" >
  </a>

  
</div>

The line given below are the errored one which was found out using verification process
* Design Bug 
  ```sh
        5'b01101: out = inp12; 
        5'b01101: out = inp13;
  ```
5'b01100 select line only direct the inp12 to out.But bugged code direct the inp12 line to output for the 5'b01101 select line

### Sequence Detector

In our example the sequence detector is designed to find 1011 sequence

<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://github.com/vyomasystems-lab/challenges-Elavarasan0702/blob/master/demo/seq_det_bug1.JPG" >
  </a>

 
</div>

<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://github.com/vyomasystems-lab/challenges-Elavarasan0702/blob/master/demo/seq_det_bug2.JPG" >
  </a>

  
</div>

<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://github.com/vyomasystems-lab/challenges-Elavarasan0702/blob/master/demo/seq_det_nonbug.JPG" >
  </a>
</div>

 ```sh
      49.next_state = SEQ_10;
      65.next_state = SEQ_10;
 ```
   
<!-- Level2-Design-->
## Level2-Design

The Level2 design is Bit manipulation multiplier
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://github.com/vyomasystems-lab/challenges-Elavarasan0702/blob/master/images/bit_manipulate_bug1.JPG">
  </a>
</div>

 The AND function has the bug which has the opcode 0x40007033
 
 <!-- Level3-Design-->
## Level3-Design

 Booth's algorithm is a multiplication algorithm that multiplies two signed binary numbers in 2's complement notation. Booth used desk calculators that were faster at shifting than adding and created the algorithm to increase their speed. Booth's algorithm is of interest in the study of computer architecture
 
 ## Acknowlegdements
- FOSSEE, IIT Bombay
- Kunal Ghosh, Co-founder, VSD Corp. Pvt. Ltd. - kunalpghosh@gmail.com



## Reference
https://github.com/anand873/DigitalVLSI/tree/master/Assignment%202

https://www.google.com/search?q=booth+multiplier+circui 

























