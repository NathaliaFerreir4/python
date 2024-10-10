hora : int

hora = int(input('Digite uma hora do dia:'))

if hora < 12:
    input('Bom dia')
elif hora < 18:
    input('Boa tarde')
else:
    input('Boa noite')
