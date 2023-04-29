# ALU-sim
This is an abstracted simulation of an ALU. The goal is to read two binary values from a txt doc and then write their sum back into the text doc. The program will also use functional abstractions of the classic logic gates to work through binary addition. 
To run the program you need to give it two eight bit binary values. They need to be typed into the first and second lines of Values.txt. 
Only type the first twwo lines and only give it two 8 bit digits. Like so: 

00000001 <br />
00000010

We are simply using python's built in lineread method. 
Any other things entered into the Values.txt will produce innacurate or nonsensicle results. 
The program will then read those values do its duty and write the results to the Results.txt. 
If you gave it two valid eight bit values it will either give you the eight bit sum, or let you know the sum was 9 bits by writing OVERFLOW ERROR. 
