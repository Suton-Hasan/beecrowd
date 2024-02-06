a,b,c,d=map(float,input().split())
X=(a*2+b*3+c*4+d*1)/10.0
print(f'Media: {X:.1f}')
if X>=7.0:
    print("Aluno aprovado.")
elif X<5.0:
    print("Aluno reprovado.")
elif X>=5.0 and X<=6.9:
    print("Aluno em exame.")
    N=float(input())
    print(f'Nota do exame: {N:.1f}')
    N=(X+N)/2
    if N>=5.0:
        print("Aluno aprovado.")
        print(f'Media final: {N:.1f}')
    else:
        print("Aluno reprovado.")
        print(f'Media final: {N:.1f}')
#
# A,B,C,D = map(float,input().split())
# A = (A*2+B*3+C*4+D*1)/10.0
# print(f'Media: {A:.1f}')
# if A>=7.0:
#     print("Aluno aprovado.")
# elif A<5.0:
#     print("Aluno reprovado.")
# elif A>=5.0 and A<7.0:
#     print("Aluno em exame.")
#     N = float(input())
#     print(f'Nota do exame: {N:.1f}')
#     N = (A+N)/2
#     if N>=5.0:
#         print("Aluno aprovado.")
#         print(f'Media final: {N:.1f}')
#     else:
#         print("Aluno reprovado.")
#         print(f'Media final: {N:.1f}')



