'''Traduza os seguintes laços do seguinte trecho de código, escritos com o comando for, em laços escritos com o comando while equivalentes,
mantendo a mesma sequência

for count in range(1, 55):
   print(count)

for count in range(50):
   print(count)

for count in range(50, 0, -2):
   print(count)'''

i = 1

while i < 55:
    print(i)

    i += 1
    
i = 0

while i < 50:
    print(i)

    i += 1

i = 50

while i > 0:
    print(i)

    i -= 2