def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2) # Somando os valores (5, 2) temos 7
soma(2, 9, 4) # Somando os valores (2, 9, 4) temos 15