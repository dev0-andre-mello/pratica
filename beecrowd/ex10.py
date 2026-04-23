spt_time = int(input('Digite o tempo gasto em horas: '))
avg_speed = int(input('Digite a velocidade média em km/h: '))

liters = (spt_time * avg_speed) / 12

print(f'The liters needed are: {liters:.3f}')
