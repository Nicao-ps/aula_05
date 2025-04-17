# Um sistema para verificar a temperatura de um sistema de refrigeração

print('')
print('** TERMINAL DO SISTEMA **')
print('')
STEMP_LIMIT = 15.0
stemp = float(input('Informe a temperatura do sistema: '))
print('')
if stemp > 15.0:
    print(f'A temperatura não está segura ({stemp:.1f} ºC > 15.0 ºC).')
    print('')
    print('O sistema demanda manutenção corretiva.')
else:
    print(f'A temperatura está segura ({stemp:.1f} ºC <= 15.0 ºC).')
    print('')
    print('O sistema não demanda manutenção corretiva.')
print('')
print('** FIM DA CONSULTA **')
print('')
