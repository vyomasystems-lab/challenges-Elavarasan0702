module adder(input [3:0] a,b,output reg [4:0] sum);
    always @ (a or b)
    begin
        sum=a+b;
    end
endmodule : adder