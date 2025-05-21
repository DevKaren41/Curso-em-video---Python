palavras = ('Amor',
            'Paciencia',
            'Longanimidade',
            'Fe',
            'Mansidao',
            'Temperanca',
            'Alegria',
            'Benignidade',
            'Paz')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end=' ')
    for letra in p:
        if letra in 'AaEeIiOoUu':
            print(letra, end= ' ')