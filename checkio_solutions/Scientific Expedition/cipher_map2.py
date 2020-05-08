#!/usr/bin/env checkio --domain=py run cipher-map2

# 
# END_DESC

def recall_password(cipher_grille, ciphered_password):
    
    solution = []
    for _ in range(4):
        for rows in zip(cipher_grille, ciphered_password):
            #print(rows)
            for g, p in zip(*rows):
                if g == 'X':
                    solution.append(p)
        #print(solution)
        #print('rotate')
        cipher_grille = list(zip(*cipher_grille[::-1]))
    return ''.join(solution)
    
    #return ""


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'