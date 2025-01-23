A, B, C, D = map(int, input().split())
B += A * 60
D += C * 60
time = D - B

if time <= 0:
    time += 24 * 60

hour = time // 60
minute = time % 60

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hour, minute))