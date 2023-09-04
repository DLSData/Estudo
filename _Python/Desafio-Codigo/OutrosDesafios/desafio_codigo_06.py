salario = float(input()) 

if (salario <600.01):
    reajuste = (salario *0.17)
elif (salario > 600.00 and salario < 900.01):
    reajuste = (salario *0.13)
elif (salario > 900.00 and salario < 1500.01):
    reajuste = (salario *0.12)
elif (salario > 1500.00 and salario < 2000.01):
    reajuste = (salario *0.10)
else: 
    reajuste = (salario *0.05)

percentual = round(((reajuste/salario)*100))

print(f'Novo salario:  {salario + reajuste:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual} %')