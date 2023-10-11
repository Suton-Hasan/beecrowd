A,B,C=map(float,input().split())
if (A+B>C and B+C>A and A+C>B):
 perimeter=A+B+C
 print("Perimetro = %.1f"%perimeter)
else:
 trapezium=(A+B)/2*C
 print("Area = %.1f"%trapezium)